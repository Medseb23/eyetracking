import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Diagnóstico Boca + Mirada + Brocha", page_icon="🧪", layout="wide")
st.title("🧪 Diagnóstico paso a paso: Boca → Mirada → Brocha")

st.markdown(
    """
**Flujo recomendado**  
1) **Probar cámara** (botón) y **Test de Boca**: revisa que el MAR suba al abrir la boca.  
2) **Test de Mirada**: el cursor debe seguir tus ojos; calibra si está corrido.  
3) **Brocha**: mirada mueve el pincel y boca abierta dibuja.

> Recomendado en **PC/notebook** con buena iluminación frontal y cabeza lo más estable posible.
    """
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with c2:
    alpha = st.slider("Suavizado mirada (0–0.9)", 0.0, 0.9, 0.45, 0.05)
with c3:
    mouth_thr = st.slider("Umbral MAR (boca)", 0.10, 0.60, 0.28, 0.01)
with c4:
    debug = st.toggle("Depuración (preview/landmarks)", value=True)

html_path = Path(__file__).parent / "static" / "diagnostic_gaze_brush_getusermedia.html"
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
