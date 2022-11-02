import cv2
import numpy as np

img = cv2.imread('1.jpg')

rows, cols = img.shape[:2]

#변환 행렬, X축으로 20, Y축으로 20 이동
M = np.float32([[1,0,20],[0,1,20]])

dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
