import cv2
import numpy as np

im = cv2.imread('nombre_1.bmp', 0)
kernel = np.ones((5,5),np.uint8)
dilatacion = cv2.dilate(im,kernel)

cv2.imshow('Imagen Original', im)
cv2.imshow('Imagen', dilatacion)
cv2.imwrite('03_dilatacion.jpg', dilatacion)
cv2.waitKey()