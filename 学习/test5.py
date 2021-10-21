import numpy as np
import cv2 as cv
import pyzbar.pyzbar as zbar

img=cv.imread("D:\\TEST\\Dian2021\\Task1\\result2\\ok_result.jpg")

barcodes=zbar.decode(img)

for i in barcodes:
    print(i.data)