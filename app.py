import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Diagnóstico Boca + Mirada + Brocha", page_icon="🧪", layout="wide")
st.title("🧪 Diagnóstico paso a paso: Boca → Mirada → Brocha")

st.markdown(
    """
**Flujo recomendado**  
1) **Test de Boca**: verifica que el detector (MAR) cambie al abrir/cerrar la boca.  
2) **Test de Mirada**: comprueba que el cursor siga tus ojos y (opcional) calibra.  
3) **Brocha**: usa la mirada para mover el pincel y la boca (MAR>umbral) para dibujar.

> Recomendado en **PC/notebook** con buena iluminación frontal y cabeza lo más estable posible.
    """
)

# Panel de controles básico
c1, c2, c3, c4 = st.columns(4)
with c1:
    brush = st.slider("Tamaño de brocha", 2, 40, 8, 1)
with c2:
    alpha = st.slider("Suavizado mirada (0–0.9)", 0.0, 0.9, 0.45, 0.05)
with c3:
    mouth_thr = st.slider("Umbral MAR (boca)", 0.10, 0.60, 0.28, 0.01)
with c4:
    debug = st.toggle("Depuración (preview/landmarks)", value=True)

# Cargar HTML
html_path = Path(__file__).parent / "static" / "diagnostic_gaze_brush.html"
html = html_path.read_text(encoding="utf-8")

# Config inicial inyectada
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
