import streamlit as st
import random

ФУНКЦИИ ДЛЯ ВИЗУАЛА

def add_snowflakes(count=30):
    Добавляет анимированные снежинки
    snowflakes_html = '<style>.snow { position: fixed; top: -10px; z-index: 9999; color: white; animation: fall linear infinite; opacity: 0.7; }'
    snowflakes_html += '@keyframes fall { to { transform: translateY(100vh) rotate(360deg); } }'
    
    for i in range(count):
        left = random.randint(0, 100)
        duration = random.randint(8, 15)
        delay = random.uniform(0, 5)
        size = random.uniform(0.8, 1.5)
        snowflakes_html += f'.snow:nth-child({i+1}) {{ left: {left}%; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}em; }}'
    
    snowflakes_html += '</style>'
    
    for i in range(count):
        snowflake = random.choice(['❄', '❅', '❆'])
        snowflakes_html += f'<div class="snow">{snowflake}</div>'
    
    st.markdown(snowflakes_html, unsafe_allow_html=True)


БИЗНЕС-ЛОГИКА: ВАЛИДАЦИЯ ДАННЫХ


def validate_day(day):
    
    Валидация дня декабря
    Возвращает: (is_valid: bool, error_message: str или None)
    
    if day is None:
        return False, "День не выбран"
    
    if not isinstance(day, int):
        return False, "День должен быть числом"
    
    if day < 1 or day > 31:
        return False, "День должен быть от 1 до 31"
    
    return True, None


def validate_task_done(task_done):
    
    Валидация статуса задания
    Возвращает: (is_valid: bool, error_message: str или None)
    
    if task_done is None:
        return False, "Статус задания не определён"
    
    if not isinstance(task_done, bool):
        return False, "Статус задания должен быть True или False"
    
    return True, None


БИЗНЕС-ЛОГИКА: ОПРЕДЕЛЕНИЕ СЦЕНАРИЯ

def determine_scenario(day, task_done):
    
    Определяет сценарий на основе валидации данных
    
    Возвращает: 
        - "NONE" - недостаточно данных или данные невалидны
        - "FALSE" - day валиден, но task_done = False
        - "TRUE" - day валиден и task_done = True
    
    Шаг 1: Валидация day
    day_valid, day_error = validate_day(day)
    
    Шаг 2: Валидация task_done
    task_valid, task_error = validate_task_done(task_done)
    
    Шаг 3: Определение сценария
    if not day_valid or not task_valid:
        Сценарий NONE: хотя бы одна валидация провалена
        return "NONE", {"day_error": day_error, "task_error": task_error}
    
    day валиден, task_done валиден
    if task_done is False:
        Сценарий FALSE: день ок, но задание не выполнено
        return "FALSE", None
    
    Сценарий TRUE: всё отлично!
    return "TRUE", None


def get_message_by_day(day):
    Возвращает сообщение в зависимости от дня"""
    if day in (1, 10):
        return "🎅 Ты уже начал подготовку к Новому году?"
    elif day == 15:
        return "⏰ Все ли идёт по плану?"
    elif day == 31:
        return "🎆 Новый год уже совсем близко!"
    elif day < 10:
        return "❄️ Самое время составить список желаний!"
    elif day < 20:
        return "🎄 Не забудь украсить ёлку!"
    elif day < 25:
        return "🎁 Пора готовить подарки близким!"
    else:
        return "✨ Волшебство уже в воздухе!"


ВИЗУАЛИЗАЦИЯ ПО СЦЕНАРИЯМ

def show_none_scenario(errors):
    Сценарий NONE: показываем ошибки валидации
    st.error("❌ Недостаточно данных для продолжения")
    
    st.markdown("🔍 Проблемы с данными:")
    
    if errors["day_error"]:
        st.warning(f"**День:** {errors['day_error']}")
    
    if errors["task_error"]:
        st.warning(f"**Задание:** {errors['task_error']}")
    
    st.info("💡 Пожалуйста, проверьте введённые данные и попробуйте снова")


def show_false_scenario(day):
    Сценарий FALSE: день валиден, но задание не выполнено
    st.warning("⚠️ Задание не выполнено")
    
    Показываем ёлку без украшений
    st.markdown("""
        <div style='text-align: center; font-size: 100px;'>
            🌲
        </div>
        <div style='text-align: center; padding: 20px; background: #fff3cd; border-radius: 10px; margin-top: 20px;'>
            <h3>Ёлка ждёт украшений!</h3>
            <p>Выполни задание, чтобы украсить ёлку и получить поздравление 🎁</p>
        </div>
    """, unsafe_allow_html=True)
    
    Показываем сообщение по дню
    message = get_message_by_day(day)
    st.info(message)


def show_true_scenario(day):
    Сценарий TRUE: всё отлично! Показываем полную визуализацию
    
    Снежинки
    add_snowflakes(30)
    
    Украшенная ёлка
    st.markdown("""
        <div style='text-align: center; font-size: 120px; animation: pulse 2s infinite;'>
            🎄
        </div>
        <style>
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
        </style>
    """, unsafe_allow_html=True)
    
    Поздравление
    st.balloons()
    
    st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 30px;
                    border-radius: 15px;
                    text-align: center;
                    color: white;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                    margin: 20px 0;'>
            <h1>🎁 Подарок получен!</h1>
            <h2>Ты большой молодец!</h2>
            <p style='font-size: 20px; margin-top: 15px;'>Продолжай в том же духе! 🌟</p>
        </div>
    """, unsafe_allow_html=True)
    
    Сообщение по дню
    message = get_message_by_day(day)
    st.success(message)
    
    Прогресс до Нового года
    progress = round((day / 31) * 100)
    st.progress(progress / 100)
    st.markdown(f"<p style='text-align: center; color: #666;'>{progress}% пути до Нового года пройдено!</p>", unsafe_allow_html=True)


 ГЛАВНЫЙ КОД ПРИЛОЖЕНИЯ


Стили приложения
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #1e3a8a, #3b82f6, #60a5fa);
    }
    h1 {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

Заголовок
st.title("🎄 Дед Мороз — Cloud Concept")
st.markdown("<p style='text-align: center; color: white; font-size: 18px;'>с валидацией и бизнес-логикой</p>", unsafe_allow_html=True)


ПОЛУЧЕНИЕ ДАННЫХ ОТ ПОЛЬЗОВАТЕЛЯ

st.markdown("📝 Введите данные")

col1, col2 = st.columns(2)

with col1:
    day = st.slider("День декабря", 1, 31, 1, key="day_slider")

with col2:
    task_done = st.checkbox("✅ Задание выполнено", key="task_checkbox")

st.markdown("---")


ВАЛИДАЦИЯ И ОПРЕДЕЛЕНИЕ СЦЕНАРИЯ


if st.button("🎁 Получить сообщение", type="primary", use_container_width=True):
    
    Показываем процесс обработки
    with st.spinner("⚙️ Проверяем данные..."):
        scenario, errors = determine_scenario(day, task_done)
    
    st.markdown("---")
    
    Показываем отладочную информацию (можно убрать в продакшене)
    with st.expander("🔍 Отладочная информация"):
        st.write(f"День:{day} (тип: {type(day).__name__})")
        st.write(fЗадание выполнено:{task_done} (тип: {type(task_done).__name__})")
        st.write(f"Определённый сценарий:{scenario}")
        if errors:
            st.write(f"Ошибки валидации:{errors}")
    
    st.markdown("---")
    
    
    ВЫПОЛНЕНИЕ ВИЗУАЛА ПО СЦЕНАРИЮ
    
    
    if scenario == "NONE":
        Недостаточно данных или невалидные данные
        show_none_scenario(errors)
    
    elif scenario == "FALSE":
        День валиден, но задание не выполнено
        show_false_scenario(day)
    
    elif scenario == "TRUE":
        Всё отлично! Показываем полную визуализацию
        show_true_scenario(day)

Футер
st.markdown("---")
st.markdown("<p style='text-align: center; color: white; opacity: 0.8;'>✨ Волшебство происходит каждый день декабря ✨</p>", unsafe_allow_html=True)




Сценарии:
    
NONE 🚫
Хотя бы один параметр невалиден
Показываем ошибки валидации
Визуал не запускается
    
FALSE ⚠️
`day` валиден
`task_done = False`
Показываем ёлку без украшений
Мотивируем выполнить задание
    
TRUE ✅
`day` валиден
`task_done = True`
Полная визуализация:
Снежинки
Украшенная ёлка
Поздравление
    
    
    st.markdown(Версия: 1.0)
    st.markdown(Дата:01.2026)
