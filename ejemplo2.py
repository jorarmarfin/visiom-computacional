import cv2

# Carga la imagen del pasaporte
imagen = cv2.imread("foto.jpeg")  # Reemplaza con la ruta de tu imagen

# Carga el clasificador de detección de rostros preentrenado
clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Convierte la imagen a escala de grises (la detección de rostros funciona mejor en imágenes en escala de grises)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detecta rostros en la imagen
rostros = clasificador_rostros.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibuja un cuadro verde centrado en la parte superior de la cabeza
for (x, y, w, h) in rostros:
    x_cabeza = x + w // 2  # Calcula el centro de la cabeza
    y_cabeza = y  # La parte superior de la cabeza
    alto_cabeza = h // 2
    ancho_cabeza = w

    cv2.rectangle(imagen, (x_cabeza, y_cabeza), (x_cabeza + ancho_cabeza, y_cabeza + alto_cabeza), (0, 255, 0), 2)  # Color verde limón

# Muestra la imagen con el cuadro centrado en la cabeza
cv2.imshow("Cabeza Detectada", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
