
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Gaze Brush (Mouth-Trigger)", page_icon="🎨", layout="wide")
st.title("🎨 Pincel con mirada + disparo por boca abierta (WebGazer + MediaPipe)")

st.markdown(
    """
**Cómo usar**  
1) Permite el acceso a la **webcam**.  
2) Ajusta el **umbral de boca** si es necesario.  
3) Mueve la mirada para posicionar el pincel.  
4) **Abre la boca** para empezar a dibujar (cierra para detener).  

> Recomendado en **PC/notebook** con buena iluminación frontal y mínima movilidad de cabeza.
    """
)

# Controles (se pasan a la página embebida vía query params)
col = st.columns(4)
with col[0]:
    brush = st.slider("Tamaño de brocha", 2, 40, 6, 1)
with col[1]:
    alpha = st.slider("Suavizado mirada (0–0.9)", 0.0, 0.9, 0.4, 0.05)
with col[2]:
    mouth_thr = st.slider("Umbral boca (MAR)", 0.10, 0.60, 0.28, 0.01)
with col[3]:
    show_dbg = st.toggle("Mostrar depuración (landmarks/caja)", value=False)

# Cargar HTML local
html_path = Path(__file__).parent / "static" / "gaze_brush_mouth.html"
html = html_path.read_text(encoding="utf-8")

# Inyectar configuración inicial vía script global
cfg_script = f"""
<script>
  window.GAZE_BRUSH_CONFIG = {{
    brush: {brush},
    alpha: {alpha},
    mouthThr: {mouth_thr},
    debug: {str(show_dbg).lower()}
  }};
</script>
"""

components.html(cfg_script + html, height=780, scrolling=False)
