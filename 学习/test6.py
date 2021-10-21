import numpy as np
import cv2 as cv
import pyzbar.pyzbar as zbar

#orb
img=cv.imread("D:\\TEST\\Dian2021\\testimg\\2.jpg",0)
orb=cv.ORB_create()
keypoint,descriptor=orb.detectAndCompute(img,None)
img=cv.drawKeypoints(img,keypoint,None)
cv.imshow("orb",img)
cv.waitKey()
cv.destroyAllWindows()

#sift
img=cv.imread("D:\\TEST\\Dian2021\\testimg\\2.jpg",0)
sift=cv.xfeatures2d.SIFT_create()
keypoint,descriptor=sift.detectAndCompute(img,None)
img=cv.drawKeypoints(img,keypoint,None)
cv.imshow("sift",img)
cv.waitKey()
cv.destroyAllWindows()

#surf
img=cv.imread("D:\\TEST\\Dian2021\\testimg\\2.jpg",0)
surf=cv.xfeatures2d.SURF_create()
keypoint,descriptor=surf.detectAndCompute(img,None)
img=cv.drawKeypoints(img,keypoint,None)
cv.imshow("surf",img)
cv.waitKey()
cv.destroyAllWindows()