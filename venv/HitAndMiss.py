import cv2
import numpy as np

img = cv2.imread('picture/man.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300, 300))

kernel1 = np.array((
        [0, 1, 0],
        [-1, 1, 1],
        [-1, -1, 0]), dtype="int")

kernel2 = np.array((
        [0, 1, 0],
        [1, 1, -1],
        [0, -1, -1]), dtype="int")


kernel3 = np.array((
        [-1, -1, 0],
        [-1, 1, 1],
        [0, 1, 0]), dtype="int")

kernel4 = np.array((
        [0, -1, -1],
        [1, 1, -1],
        [0, 1, 0]), dtype="int")

outimg1 = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel1)
outimg2 = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel2)
outimg3 = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel3)
outimg4 = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel4)

outimg = outimg1 + outimg2 + outimg3 + outimg4

cv2.imshow("Original", img)
cv2.imshow("Hit&Miss1", outimg1)
cv2.imshow("Hit&Miss2", outimg2)
cv2.imshow("Hit&Miss3", outimg3)
cv2.imshow("Hit&Miss4", outimg4)
cv2.imshow("Hit&Miss", outimg)

cv2.waitKey(0)
