
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trayectoria de Mirada – Demo", page_icon="👀", layout="wide")
st.title("👀 Demo: Dibujo de la trayectoria de la mirada (WebGazer.js)")

st.markdown(
    """
Este experimento **dibuja tu trayectoria de mirada** en un lienzo y permite **descargar**:
- Una **imagen PNG** con el trazo.
- Un **CSV** con tiempo (ms), x, y.

**Recomendado**: PC/notebook con webcam, buena iluminación frontal y mínima movilidad de cabeza.
    """
)

components.html(open("static/gaze_canvas.html", "r", encoding="utf-8").read(), height=720, scrolling=False)
