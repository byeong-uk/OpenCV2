import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg', cv2.IMREAD_COLOR)

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
