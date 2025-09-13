import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Experimento Eyetracking", page_icon="👀", layout="centered")
st.title("👀 Demo Eyetracking con Webcam (WebGazer.js)")

st.markdown(
    "Este es un experimento **demo** que usa la webcam para estimar la posición de la mirada. "
    "Funciona mejor en PC con buena luz y cara estable."
)

# HTML con WebGazer.js (solo demo de coordenadas de mirada)
html_code = """
<!DOCTYPE html>
<html>
  <head>
    <script src="https://webgazer.cs.brown.edu/webgazer.js"></script>
    <style>
      body { margin:0; overflow:hidden; }
      canvas { position:absolute; top:0; left:0; }
      #coords { position:fixed; bottom:10px; left:10px; background:#000; color:#0f0;
                font-family:monospace; padding:6px; border-radius:4px; }
    </style>
  </head>
  <body>
    <div id="coords">Esperando datos...</div>
    <script>
      window.saveDataAcrossSessions = true;
      webgazer.setRegression('ridge')             
              .setGazeListener(function(data, elapsedTime) {
                  if (data == null) return;
                  var x = data.x;
                  var y = data.y;
                  document.getElementById("coords").innerText = "x:" + x.toFixed(0) + " y:" + y.toFixed(0);
              }).begin();
    </script>
  </body>
</html>
"""

components.html(html_code, height=600)
