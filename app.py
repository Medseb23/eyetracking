import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Brocha: ojos o nariz + boca", page_icon="🎨", layout="wide")
st.title("🎨 Brocha controlada por OJOS o NARIZ + Boca como gatillo")

st.markdown(
    """
- **Movimiento**: elige si la brocha se mueve con **OJOS (WebGazer)** o con **NARIZ (FaceMesh)**.  
- **Pintado**: la **BOCA** sigue siendo el gatillo → **abre = pinta / cierra = no pinta**.  
- Sugerencias: buena iluminación, rostro centrado, calibra si hace falta.
    """
)

c0, c1, c2, c3, c4 = st.columns(5)
with c0:
    control = st.selectbox("Mover brocha con", ["Ojos (WebGazer)", "Nariz (FaceMesh)"], index=0)
with c1:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with c2:
    alpha = st.slider("Suavizado movimiento (0–0.9)", 0.0, 0.9, 0.45, 0.05)
with c3:
    mouth_thr = st.slider("Umbral MAR (boca)", 0.10, 0.60, 0.28, 0.01)
with c4:
    debug = st.toggle("Mostrar preview/landmarks", value=True)

html_path = Path(__file__).parent / "static" / "diagnostic_gaze_or_nose_with_mouth.html"
html = html_path.read_text(encoding="utf-8")

cfg = f"""
<script>
window.DIAG_CFG = {{
  brush: {brush},
  alpha: {alpha},
  mouthThr: {mouth_thr},
  debug: {str(debug).lower()},
  controlMode: {{"Ojos (WebGazer)":"eyes","Nariz (FaceMesh)":"nose"}}[{control!r}]
}};
</script>
"""

components.html(cfg + html, height=900, scrolling=False)
