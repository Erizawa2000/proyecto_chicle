import streamlit as st
from datetime import datetime
import importlib
import os

from config import APP_TITLE, PARTNER_1, PARTNER_2, REUNION_DATE, MAIN_MESSAGE


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="❤️",
    layout="centered"
)


def calculate_countdown(target_date: datetime):
    now = datetime.now()
    difference = target_date - now

    if difference.total_seconds() <= 0:
        return None

    days = difference.days
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days, hours, minutes, seconds


def load_plugins():
    plugins_folder = "plugins"

    if not os.path.exists(plugins_folder):
        return

    for filename in os.listdir(plugins_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"plugins.{module_name}")

            if hasattr(module, "render"):
                module.render()


st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #fff1f5 0%, #ffffff 100%);
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #c9184a;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #590d22;
        margin-bottom: 30px;
    }

    .counter-box {
        background-color: #fff0f3;
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    .counter-number {
        font-size: 48px;
        font-weight: bold;
        color: #a4133c;
    }

    .counter-label {
        font-size: 16px;
        color: #590d22;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(f"<div class='title'>❤️ {APP_TITLE} ❤️</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{PARTNER_1} & {PARTNER_2}</div>", unsafe_allow_html=True)

st.write("")

countdown = calculate_countdown(REUNION_DATE)

if countdown is None:
    st.success("¡El día llegó! Ya pueden verse de nuevo ❤️")
else:
    days, hours, minutes, seconds = countdown

    st.markdown("<div class='counter-box'>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"<div class='counter-number'>{days}</div>", unsafe_allow_html=True)
        st.markdown("<div class='counter-label'>Días</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div class='counter-number'>{hours}</div>", unsafe_allow_html=True)
        st.markdown("<div class='counter-label'>Horas</div>", unsafe_allow_html=True)

    with col3:
        st.markdown(f"<div class='counter-number'>{minutes}</div>", unsafe_allow_html=True)
        st.markdown("<div class='counter-label'>Minutos</div>", unsafe_allow_html=True)

    with col4:
        st.markdown(f"<div class='counter-number'>{seconds}</div>", unsafe_allow_html=True)
        st.markdown("<div class='counter-label'>Segundos</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.info(MAIN_MESSAGE)

st.divider()

load_plugins()
