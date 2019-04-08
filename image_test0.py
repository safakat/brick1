# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:13:21 2019

@author: safak
"""

import cv2
import matplotlib.pyplot as plt

#load the image
img = cv2.imread('box.jpg')

#output of the image
#cv2.imshow('image',img)

#Convert the image to grayscale
gray0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#output of the grayscale image
cv2.imshow('image',gray0)

import numpy as np

corners0 = cv2.goodFeaturesToTrack(gray0,7,0.01,10)
print(corners0)
corners1 = np.int0(corners0)

for i in corners1:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()