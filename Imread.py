import cv2

fname = "1.jpg"

original = cv2.imread('1.jpg', cv2.IMREAD_COLOR)
gray = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original", original)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
