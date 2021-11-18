import cv2
import numpy as np

im = cv2.imread('figuras_1.bmp', 0)
kernel = np.ones((5,5),np.uint8)
dilatacion = cv2.dilate(im,kernel)

cv2.imshow('Imagen Original', im)
cv2.imshow('Imagen', dilatacion)
cv2.imwrite('04_dilatacion.jpg', dilatacion)
cv2.waitKey()