import cv2
import numpy as np

img = cv2.imread('picture/dog.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300, 300))
thresh,img1 = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)

skelimg = np.zeros(img.shape, np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

while (cv2.countNonZero(img1) != 0):

    white = cv2.morphologyEx(img1, cv2.MORPH_TOPHAT, kernel)
    erodeimg = cv2.erode(img1, kernel)
    skelimg = cv2.bitwise_or(skelimg,white)
    img1 = erodeimg.copy()

cv2.imshow("Original image", img)
cv2.imshow("Skeleton image",skelimg)

cv2.waitKey(0)
