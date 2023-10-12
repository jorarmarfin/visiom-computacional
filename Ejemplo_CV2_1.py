import cv2

img = cv2.imread('foto.jpeg')
ficha = cv2.imread('D2-151-0001.jpg')
cv2.imshow('Imagen de ejemplo', img)

cv2.imwrite('foto_tmp.jpg', img)

x1, y1 = 0, 0
x2, y2 = 150, 150
roi = img[y1:y2, x1:x2]

cv2.imshow('Recorte', roi)

cv2.imshow('identificacion',ficha)

cv2.waitKey(0)
cv2.destroyAllWindows()

