import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('stop2.png')
img2 = cv2.imread('face.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#sift
sift = cv2.SIFT_create()
kp1, dscp1 = sift.detectAndCompute(img1,None)
kp2, dscp2 = sift.detectAndCompute(img2, None)

#print(len(kp1), len(kp2))

#brute force matching

bf = cv2.BFMatcher.create(cv2.NORM_L1,crossCheck=True)

matches = bf.match(dscp1, dscp2)
matches = sorted(matches, key= lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], img2, flags=2)
print(len(matches))
plt.imshow(img3), plt.show()


