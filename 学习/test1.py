import numpy as np
import cv2 as cv
from os import *

rgb_img=cv.imread("D:\\TEST\\Dian2021\\testimg\\1.jpg",1)
grey_img=cv.imread("D:\\TEST\\Dian2021\\testimg\\1.jpg",0)

grey_img=255-grey_img
cv.imshow("Grey_img",grey_img)
cv.imshow("RGB_img",rgb_img)

if cv.waitKey(3000):
    #cv.destroyAllWindows()
    cv.destroyWindow("RGB_img")
#system("pause")