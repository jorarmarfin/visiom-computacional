import cv2
import numpy as np

# Carga la imagen del pasaporte
imagen = cv2.imread("foto.jpeg")  # Reemplaza con la ruta de tu imagen

# Carga el clasificador de detección de rostros preentrenado
clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Convierte la imagen a escala de grises (la detección de rostros funciona mejor en imágenes en escala de grises)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detecta rostros en la imagen
rostros = clasificador_rostros.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibuja un cuadro verde alrededor de cada rostro detectado
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Color verde limón

# Muestra la imagen con los cuadros alrededor de los rostros
cv2.imshow("Rostros Detectados", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
