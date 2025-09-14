import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Gaze Brush + Calibración", page_icon="🎯", layout="wide")
st.title("🎯 Gaze Brush: mirada como puntero + boca como gatillo (con calibración y feedback)")

st.markdown(
    """
**Flujo recomendado**  
1) Pulsa **🎯 Calibrar mirada** (4 esquinas + centro).  
2) Pulsa **👄 Calibrar boca** (2 s cerrada → 2 s abierta).  
3) Ajusta **tamaño de brocha**, **suavizado** y activa **Depuración** si quieres ver landmarks/preview.  
4) Pulsa **▶️ Iniciar** y dibuja: la **mirada** mueve la brocha y la **boca** (MAR>umbral) activa el trazo.

> Recomendado en **PC/notebook** con buena iluminación frontal y mínima movilidad de cabeza.
    """
)

# Controles (inyectados como config global en la página embebida)
col = st.columns(4)
with col[0]:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with col[1]:
    alpha = st.slider("Suavizado mirada (0–0.9)", 0.0, 0.9, 0.45, 0.05)
with col[2]:
    mouth_thr = st.slider("Umbral inicial boca (MAR)", 0.10, 0.60, 0.28, 0.01)
with col[3]:
    debug = st.toggle("Depuración (preview/landmarks)", value=False)

html_path = Path(__file__).parent / "static" / "gaze_brush_calibrated.html"
html = html_path.read_text(encoding="utf-8")

cfg = f"""
<script>
window.GAZE_CFG = {{
  brush: {brush},
  alpha: {alpha},
  mouthThr: {mouth_thr},
  debug: {str(debug).lower()}
}};
</script>
"""

components.html(cfg + html, height=860, scrolling=False)
