import cv2
import numpy as np

img = cv2.imread("picture/YinYang.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300, 300))
thresh, biimg = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)

thinimg = biimg.copy()

kernel1 = np.array((
        [-1, -1, -1],
        [0, 1, 0],
        [1, 1, 1]), dtype="int")
kernel2 = np.array((
        [-1, 0, 1],
        [-1, 1, 1],
        [-1, 0, 1]), dtype="int")
kernel3 = np.array((
        [1, 1, 1],
        [0, 1, 0],
        [-1, -1, -1]), dtype="int")
kernel4 = np.array((
        [1, 0, -1],
        [1, 1, -1],
        [1, 0, -1]), dtype="int")

for i in range(1,3):
 hm1 = cv2.morphologyEx(thinimg, cv2.MORPH_HITMISS, kernel1)
 hm2 = cv2.morphologyEx(thinimg, cv2.MORPH_HITMISS, kernel2)
 hm3 = cv2.morphologyEx(thinimg, cv2.MORPH_HITMISS, kernel3)
 hm4 = cv2.morphologyEx(thinimg, cv2.MORPH_HITMISS, kernel4)
 hm = hm1 + hm2 + hm3 + hm4
 thinimg = thinimg - hm

cv2.imshow('Original image', biimg)
cv2.imshow('Thinned image', thinimg)

cv2.waitKey(0)
