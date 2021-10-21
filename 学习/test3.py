import numpy as np
import cv2 as cv
from copy import *

img=cv.imread("D:\\testimg\\1.jpg",0)


_img=copy(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i,j]>150):
            _img[i,j]=255
        else:
            _img[i,j]=0

cv.imshow("1",img)
cv.imshow("2",_img)

cv.waitKey()
cv.destroyAllWindows()