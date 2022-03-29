import cv2
import numpy as np

img = cv2.imread("picture/city.jpg", cv2.IMREAD_GRAYSCALE)
thresh, biimg = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)

floodimg = biimg.copy()

y, x = biimg.shape[:2]
kernel = np.zeros((y+2, x+2), np.uint8)

cv2.floodFill(floodimg, kernel, (0,0), 255)
invfloodimg = cv2.bitwise_not(floodimg)
outimg = cv2.bitwise_or(biimg,invfloodimg)

cv2.imshow("Original image", img)
cv2.imshow("Output filled image", outimg)

cv2.waitKey(0)
