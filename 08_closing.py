import cv2
import numpy as np

im = cv2.imread('figuras_3.bmp', 0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Imagen Original', im)
cv2.imshow('Imagen', closing)
cv2.imwrite('08_closing.jpg', closing)
cv2.waitKey()