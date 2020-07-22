# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:58:57 2020

@author: Nikitha
"""

import cv2
import numpy as np



img=cv2.imread( 'C:\\Users\\Nikitha\\Desktop\\spyder\\images.jpg',1)
cv2.namedWindow('oimg',cv2.WINDOW_NORMAL)
cv2.imshow('oimg',img)
cv2.waitKey(0)
h,w,n=img.shape
print(img.shape)

mean=0 
gauss=np.random.normal(mean,1,(h,w,n))
gauss=gauss.reshape(h,w,n)
noisy=img + gauss
cv2.namedWindow('gimage',cv2.WINDOW_NORMAL)
cv2.imshow('gimage',noisy)
cv2.namedWindow('oimg',cv2.WINDOW_NORMAL)
cv2.imshow('oimg',img)

cv2.waitKey(0)

