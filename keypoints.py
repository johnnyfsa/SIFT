import cv2
import matplotlib
import matplotlib.pyplot as plt

#reading image
img1 = cv2.imread('broken1.png')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#keypoints
sift = cv2.SIFT_create()
kp = sift.detect(gray1,None)
img1 = cv2.drawKeypoints(gray1, kp, img1)
plt.imshow(img1)
plt.show()
