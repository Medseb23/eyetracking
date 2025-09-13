
# Gaze Brush con calibración (mirada + boca)

- **Mirada** controla la posición del pincel (WebGazer) con **calibración afín** (4 esquinas + centro).
- **Boca** controla el **inicio/paro del trazo** usando **MAR** (MediaPipe FaceMesh) con **calibración** (cerrada/abierta).
- Permite descargar **PNG** del lienzo y **CSV** de datos (t, x, y, mar, drawing).

## Ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Consejos
- Haz la **calibración de mirada** primero (mira cada punto ~2 s).
- Luego **calibra la boca** (2 s cerrada, 2 s abierta). El umbral se fija automáticamente.
- Si el cursor queda desplazado, repite la calibración de mirada. Si dibuja sin abrir la boca, repite la calibración de boca.

## Notas de compatibilidad
- Funciona mejor en **PC/notebook** con buena luz frontal. Mantén la cabeza estable.
- Si usas Streamlit Cloud, asegúrate que el **Main file path** apunte a `app.py` en la raíz del repo (o ajusta la ruta si está en subcarpeta).
