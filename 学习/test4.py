import numpy as np
import cv2
capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)
capture.set(3,1280)
capture.set(4,960)
while True:
    ret,img =capture.read()
    cv2.imshow('Hi', img)
    k=cv2.waitKey(1)
    if k==27:
        break