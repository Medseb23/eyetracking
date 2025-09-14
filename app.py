import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Brocha: ojos o nariz + boca", page_icon="🎨", layout="wide")
st.title("🎨 Brocha controlada por OJOS o NARIZ + Boca como gatillo")

st.markdown("""
- **Movimiento**: elige si la brocha se mueve con **OJOS (WebGazer)** o con **NARIZ (FaceMesh)**.  
- **Pintado**: la **BOCA** es el gatillo → **abre = pinta / cierra = no pinta**.  
- Sugerencias: buena iluminación, rostro centrado, calibra si hace falta.
""")

c0, c1, c2, c3, c4 = st.columns(5)
with c0:
    control = st.selectbox("Mover brocha con", ["Ojos (WebGazer)", "Nariz (FaceMesh)"], index=0)
with c1:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with c2:
    alpha = st.slider("Suavizado movimiento (EMA α nuevo)", 0.0, 0.9, 0.20, 0.05)
with c3:
    mouth_thr = st.slider("Umbral MAR (boca)", 0.10, 0.60, 0.28, 0.01)
with c4:
    debug = st.toggle("Mostrar preview/landmarks", value=True)

st.subheader("⚙️ Estabilidad avanzada")
c5, c6, c7, c8 = st.columns(4)
with c5:
    deadzone = st.slider("Deadzone (px)", 0, 20, 8, 1)
with c6:
    maxstep = st.slider("Paso máx. por frame (px)", 5, 60, 24, 1)
with c7:
    medianN = st.slider("Ventana mediana pos (N)", 1, 9, 5, 2)
with c8:
    mouth_hys = st.slider("Histeresis MAR (±)", 0.00, 0.12, 0.05, 0.01)

c9, c10 = st.columns(2)
with c9:
    marMedianN = st.slider("Ventana mediana MAR (N)", 1, 11, 5, 2)
with c10:
    marEmaAlpha = st.slider("EMA MAR α nuevo", 0.00, 0.9, 0.30, 0.05)

st.subheader("🎭 Confianzas FaceMesh")
cc1, cc2 = st.columns(2)
with cc1:
    det_conf = st.slider("minDetectionConfidence", 0.1, 0.9, 0.5, 0.05)
with cc2:
    track_conf = st.slider("minTrackingConfidence", 0.1, 0.9, 0.5, 0.05)

html_path = Path(__file__).parent / "static" / "diagnostic_gaze_or_nose_with_mouth.html"
html = html_path.read_text(encoding="utf-8")

cfg = f"""
<script>
window.DIAG_CFG = {{
  brush: {brush},
  alpha: {alpha},
  mouthThr: {mouth_thr},
  debug: {str(debug).lower()},
  controlMode: {{"Ojos (WebGazer)":"eyes","Nariz (FaceMesh)":"nose"}}[{control!r}],
  deadzonePx: {deadzone},
  maxStepPx: {maxstep},
  medianN: {medianN},
  mouthHys: {mouth_hys},
  marMedianN: {marMedianN},
  marEmaAlpha: {marEmaAlpha},
  detConf: {det_conf},
  trackConf: {track_conf}
}};
</script>
"""

components.html(cfg + html, height=900, scrolling=False)
