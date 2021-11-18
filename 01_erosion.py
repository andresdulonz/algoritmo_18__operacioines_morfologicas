import cv2
import numpy as np

im = cv2.imread('nombre_1.bmp', 0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(im,kernel)

cv2.imshow('Imagen Original', im)
cv2.imshow('Imagen', erosion)
cv2.imwrite('01_erosion.jpg', erosion)
cv2.waitKey()