import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
img = cv.imread('broken2.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0,255,0),3)
ax.imshow(img)

class Index():

    contour_index =-1

    def next(self, event):
        self.contour_index += 1
        cv.drawContours(img, contours, self.contour_index, (255,0,0),3)
        ax.imshow(img)
        plt.draw()
        
    def previous(self, event):
        self.contour_index -= 1
        cv.drawContours(img, contours, self.contour_index, (0,255,0),3)
        ax.imshow(img)
        plt.draw()

callback = Index();
axNext = plt.axes([0.81, 0.05, 0.1, 0.075])
axPrev = plt.axes([0.7, 0.05, 0.1, 0.075])
bNext = Button(axNext,'Next')
bPrev = Button(axPrev,'Previous')
bNext.on_clicked(callback.next)
bPrev.on_clicked(callback.previous)
plt.show()

