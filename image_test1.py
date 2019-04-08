# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:03:23 2019

@author: safak
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("box.jpg")

gray0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray0,(7,7),0)

cv2.imshow('image',gray1)

corners0 = cv2.goodFeaturesToTrack(gray1,7,0.01,10)
print(corners0)
corners1 = np.int0(corners0)

for i in corners1:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()