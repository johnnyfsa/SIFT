import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('broken1.png')
img2 = cv2.imread('broken2.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#sift
sift = cv2.SIFT_create()
kp1, dscp1 = sift.detectAndCompute(img1,None)
kp2, dsp2 = sift.detectAndCompute(img2, None)

print(len(kp1), len(kp2))

