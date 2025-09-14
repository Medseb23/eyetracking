# Gaze Brush (mirada + boca) con **calibración** y **feedback**

- La **mirada** controla la posición del pincel (WebGazer) con **calibración afín** (4 esquinas + centro).
- La **boca** (MAR con MediaPipe FaceMesh) **activa** o **detiene** el trazo; incluye **calibración** (cerrada/abierta) para fijar el umbral.
- Panel de **feedback**: valor MAR en vivo, **barra** con umbral, **preview** opcional de cámara + landmarks.
- Descarga **PNG** del lienzo y **CSV** de datos (t, x, y, mar, drawing).

## Ejecutar local
```bash
pip install -r requirements.txt
streamlit run app.py
