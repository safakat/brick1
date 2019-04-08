# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:24:54 2019

@author: safak
"""

#Import packages

from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import cv2

def midpoint(ptA, ptB):
    return ((ptA[0]+ptB[0]) * 0.5,(ptA[1] + ptB[1]) * 0.5)

#Construct the argument parse and parse the arguments

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help= "path to the input image")
#ap.add_argument("-w", "--width", type = float, required=True, help = "width of the left-most object in the image (in inches)")
#args = vars(ap.parse_args())

#load the image, convert it to grayscale, and blur it slightly

image = cv2.imread("rubber-bush-coupling-500x500.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
print(cv2.imshow('image',gray))