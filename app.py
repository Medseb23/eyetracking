import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Diagnóstico Boca/Mirada/Brocha", page_icon="🧪", layout="wide")
st.title("🧪 Diagnóstico: Mirada + Gatillo (Boca o Nariz) → Brocha")

st.markdown(
    """
Elige el **gatillo** que activará el dibujo.
- **Boca**: dibuja con **boca abierta** (MAR > umbral).
- **Nariz**: dibuja al **acercar la nariz** a la cámara (profundidad Z cruza umbral).

Consejos: buena iluminación, cabeza estable, calibrar primero.
    """
)

c0, c1, c2, c3, c4 = st.columns(5)
with c0:
    trigger = st.selectbox("Gatillo", ["Boca", "Nariz"], index=0)
with c1:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with c2:
    alpha = st.slider("Suavizado mirada (0–0.9)", 0.0, 0.9, 0.45, 0.05)
with c3:
    mouth_thr = st.slider("Umbral MAR (boca)", 0.10, 0.60, 0.28, 0.01)
with c4:
    debug = st.toggle("Depuración (preview/landmarks)", value=True)

# el HTML depende del gatillo elegido
html_file = "diagnostic_gaze_brush_getusermedia.html" if trigger == "Boca" \
            else "diagnostic_gaze_brush_nose.html"

html_path = Path(__file__).parent / "static" / html_file
html = html_path.read_text(encoding="utf-8")

cfg = f"""
<script>
window.DIAG_CFG = {{
  brush: {brush},
  alpha: {alpha},
  mouthThr: {mouth_thr},
  debug: {str(debug).lower()}
}};
</script>
"""

components.html(cfg + html, height=900, scrolling=False)
