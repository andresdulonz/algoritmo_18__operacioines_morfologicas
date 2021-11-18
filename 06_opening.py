import cv2
import numpy as np

im = cv2.imread('figuras_2.bmp', 0)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)

cv2.imshow('Imagen Original', im)
cv2.imshow('Imagen', opening)
cv2.imwrite('06_opening.jpg', opening)
cv2.waitKey()