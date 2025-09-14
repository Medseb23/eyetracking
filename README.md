# Diagnóstico Boca + Mirada + Brocha (Streamlit + MediaPipe + WebGazer)

## Modos
1. **Test de Boca**: muestra preview de webcam + landmarks + **MAR** con umbral.
2. **Test de Mirada**: cursor movido por WebGazer; (opcional) calibración rápida (4 esquinas + centro).
3. **Brocha**: mira para mover la brocha; **boca abierta** (MAR>umbral) para dibujar.

## Uso local
```bash
pip install -r requirements.txt
streamlit run app.py
