import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('60938328.jpeg')
# img = cv2.imread('foto.jpeg')

alto, ancho = img.shape[:2]
margin_y = 0.80
margin_y2 = 0.30
margin_x = 0.1
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
face = face_cascade.detectMultiScale(gray, 1.1, 4)
if len(face) > 0:
    x, y, w, h = face[0]
    delta_y = int(margin_y * y)
    delta_y2 = int(margin_y2 * y)
    delta_x = int(margin_x * x)
    x1, y1 = x - delta_x, y - delta_y
    x2, y2 = x + w + delta_x, y + h + delta_y2
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    img_face = img[y1:y2, x1:x2]
    cv2.imshow('imagen2', img_face)

cv2.imshow('imagen1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
