import streamlit as st
import random


def render():
    frases = [
        "No importa la distancia, seguimos contando los mismos días.",
        "Cada segundo que pasa nos acerca un poco más.",
        "La espera también forma parte de nuestra historia.",
        "Volver a verte será mi momento favorito.",
        "Falta menos que ayer, y eso ya me hace feliz."
    ]

    st.subheader("Mensaje de hoy")
    st.write(random.choice(frases))
    