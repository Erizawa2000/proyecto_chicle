import streamlit as st
import random
from datetime import datetime, timedelta


def render():
    frases = [
        "Te amo mucho, tanto....",
        "Te amo, por si las moscas.",
        "Me encanta como tus besos se sintieron tan bien y tan familiares desde el minuto uno.",
        "Me encanta como me amas.",
    ]

    ahora = datetime.now()

    intervalo_cambio = timedelta(hours=24)

    if "frase_actual" not in st.session_state:
        st.session_state.frase_actual = random.choice(frases)
        st.session_state.ultima_actualizacion_frase = ahora

    tiempo_transcurrido = ahora - st.session_state.ultima_actualizacion_frase

    if tiempo_transcurrido >= intervalo_cambio:
        st.session_state.frase_actual = random.choice(frases)
        st.session_state.ultima_actualizacion_frase = ahora

    st.subheader("Mensaje de hoy")
    st.write(st.session_state.frase_actual)
