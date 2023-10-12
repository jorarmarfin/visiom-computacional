import cv2
import numpy as np
import matplotlib.pyplot as plt

#Imagen Negra
img = np.zeros((10, 10, 1), np.uint8)

#cambiamos algunos pixeles
img[0, 1] = 30

#Mostramos numeros
print(img)

#mostramos imagen
plt.imshow(img, cmap='gray')
plt.show()

