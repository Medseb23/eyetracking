
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Gaze Brush + Calibración", page_icon="🎯", layout="wide")
st.title("🎯 Gaze Brush con calibración de mirada y boca (WebGazer + MediaPipe)")

st.markdown(
    """
**Modo de uso sugerido**  
1) Pulsa **Calibrar mirada** y sigue los puntos (4 esquinas + centro).  
2) Pulsa **Calibrar boca**: primero **cerrada**, luego **abierta**.  
3) Ajusta si quieres el tamaño de brocha y el suavizado.  
4) Pulsa **Iniciar** → mueve la brocha con la mirada; **dibuja al abrir la boca**.

> Recomendado en **PC/notebook** con buena iluminación frontal.
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with c2:
    alpha = st.slider("Suavizado de mirada (0–0.9)", 0.0, 0.9, 0.45, 0.05)
with c3:
    debug = st.toggle("Depuración (landmarks/MAR)", value=False)

html_path = Path(__file__).parent / "static" / "gaze_brush_calibrated.html"
html = html_path.read_text(encoding="utf-8")

cfg = f"""
<script>
window.GAZE_CFG = {{
  brush: {brush},
  alpha: {alpha},
  debug: {str(debug).lower()}
}};
</script>
"""

components.html(cfg + html, height=820, scrolling=False)
