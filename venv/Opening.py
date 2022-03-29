import cv2
import numpy as np
# Đọc ảnh và xử lý ảnh ( biến ảnh màu thành ảnh nhị phân)
img1 = cv2.imread('picture/city.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img1, (300, 300))
r,img = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
cv2.imshow("Original", img)
cv2.imwrite('result/Original.png', img)

#tạo một kernel là một ma trận 5x5 có tất cả các phần tử là 1
kernel = np.ones((5,5),np.uint8)

#Thực hiện phép toán Opening
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opened)
cv2.imwrite('result/Opening.png', opened)
cv2.waitKey(0)

