import numpy as np
import cv2 as cv
import copy
import pyzbar.pyzbar as zbar

from numpy.core.fromnumeric import shape

def init():
    global src,_origin,origin,grad_x,grad_y
    origin=cv.imread("D:\\TEST\\Dian2021\\gendata\\t1_2\\ok2.jpg")
    src=copy.deepcopy(origin)
    _origin=copy.deepcopy(origin)
    src=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    #src=cv.imread("D:\\TEST\\Dian2021\\testimg\\2.jpg",0)
    src=cv.GaussianBlur(src,(3,3),0)
    grad_x=cv.Sobel(src,-1,1,0,ksize=3)
    grad_y=cv.Sobel(src,-1,0,1,ksize=3)
    src=cv.addWeighted(grad_x,0.5,grad_y,0.5,0)
    #src=grad_y-grad_x
    src=cv.blur(src,(3,3))
    ret,src=cv.threshold(src,80,255,cv.THRESH_BINARY)
    kernel1=cv.getStructuringElement(cv.MORPH_RECT,(1,50))
    src=cv.morphologyEx(src,cv.MORPH_CLOSE,kernel1)
    kernel2=cv.getStructuringElement(cv.MORPH_RECT,(55,55))
    src=cv.erode(src,kernel2)
    src=cv.dilate(src,kernel2)

def main():
    global res,_origin,origin,src,contours,l
    contours=cv.findContours(src,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    l=contours[0]
    res=[]
    for i in l:
        minx,miny,maxx,maxy=114514,114514,0,0
        for j in i:
            minx=min(j[0][0],minx)
            maxx=max(j[0][0],maxx)
            miny=min(j[0][1],miny)
            maxy=max(j[0][1],maxy)
        tmp=origin[miny-20:maxy+20,minx-20:maxx+20]
        h=zbar.decode(tmp)
        if h!=[]:
            res.append(tmp)
            _origin=cv.rectangle(_origin,(minx-20,miny-20),(maxx+20,maxy+20),(255,0,0),8)
    #tmp=np.ones(src.shape,np.uint8)*255
    #cv.drawContours(tmp,contours[0],-1,(0,255,0),3)
    #print(contours)

def debug():
    pass

def printout():
    tmp=0
    f=open("D:\\TEST\\Dian2021\\Task1\\result2\\ok2_result.txt",'w')
    for i in res:
        tmp+=1
        cv.imwrite("D:\\TEST\\Dian2021\\Task1\\result2\\ok2_bar%d.jpg"%tmp,i)
        barcode=zbar.decode(i)
        print("TYPE=%s"%barcode[0].type,"data=%s"%(str)(barcode[0].data),file=f)
    f.close()
    cv.imwrite("D:\\TEST\\Dian2021\\Task1\\result2\\ok2_result.jpg",_origin)

if __name__=="__main__":
    init()
    main()
    debug()
    printout()