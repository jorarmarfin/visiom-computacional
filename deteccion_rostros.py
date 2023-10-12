import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('60938328.jpeg')
#img = cv2.imread('foto.jpeg')

alto, ancho = img.shape[:2]
margen_h = int(0.16*alto)
margen_w = int(0.10*ancho)
print(ancho,alto)
print(margen_w,margen_h)
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
face = face_cascade.detectMultiScale(gray, 1.1, 4)
if len(face) > 0:
    x, y, w, h = face[0]
    x1, y1 = x - margen_w, y - margen_h
    x2, y2 = x + w + margen_w, y + h + margen_h
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    img_face = img[y1:y2, x1:x2]
    cv2.imshow('imagen2', img_face)

cv2.imshow('imagen1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

