
# Gaze Brush con disparo por boca (Streamlit + WebGazer + MediaPipe)

- El **pincel** se posiciona con la **mirada** (WebGazer).
- El **trazo** se dibuja **solo si abres la boca** por sobre un umbral (MAR con MediaPipe FaceMesh).
- Descarga **PNG** del lienzo y **CSV** con puntos (t, x, y, drawing).

## Requisitos
- Python 3.11 recomendado.
- `streamlit==1.37.1` (en `requirements.txt`).
- Permiso de **webcam** en el navegador.

## Ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Notas
- Si en Streamlit Cloud no carga, verifica que el **Main file path** apunte a `app.py` en la **raíz** del repo. Si lo tienes en una subcarpeta, ajusta el valor (p.ej. `main/app.py`) en los *Settings* de la app.
- Ajusta en la UI: **tamaño de brocha**, **suavizado**, **umbral de boca (MAR)** y **depuración** (ver landmarks).
