import cv2
import numpy as np

img = cv2.imread("picture/dog.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300, 300))
thresh, biimg = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)

thickimg = biimg.copy()

kernel1 = np.array((
        [1, 1, 0],
        [1, -1, 0],
        [1, 0, -1]), dtype="int")
kernel2 = np.array((
        [0, 0, -1],
        [1, -1, 0],
        [1, 1, 1]), dtype="int")
kernel3 = np.array((
        [-1, 0, 1],
        [0, -1, 1],
        [0, 1, 1]), dtype="int")
kernel4 = np.array((
        [1, 1, 1],
        [0, -1, 1],
        [-1, 0, 0]), dtype="int")

for i in range(1,40):
 hm1 = cv2.morphologyEx(thickimg, cv2.MORPH_HITMISS, kernel1)
 hm2 = cv2.morphologyEx(thickimg, cv2.MORPH_HITMISS, kernel2)
 hm3 = cv2.morphologyEx(thickimg, cv2.MORPH_HITMISS, kernel3)
 hm4 = cv2.morphologyEx(thickimg, cv2.MORPH_HITMISS, kernel4)
 hm = hm1 + hm2 + hm3 + hm4
 thickimg = cv2.bitwise_or(thickimg, hm)

cv2.imshow('Original image', img)
cv2.imshow('Thickened image', thickimg)

cv2.waitKey(0)
