import numpy as np
import cv2 as cv
import copy

def init(n,m):
    global src,_src,target1,target2,methods
    src=cv.imread("D:\\TEST\\Dian2021\\gendata\\t1_1\\2x%d\\%d.jpg"%(n+2,m))
    _src=copy.deepcopy(src)
    target1=cv.imread("D:\\TEST\\Dian2021\\gendata\\t1_1\\target1.jpg")
    target2=cv.imread("D:\\TEST\\Dian2021\\gendata\\t1_1\\target2.jpg")
    src=cv.GaussianBlur(src,(7,7),0)
    target1=cv.GaussianBlur(target1,(7,7),0)
    target2=cv.GaussianBlur(target2,(7,7),0)
    methods=[cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]

def main():
    global result1,result2,a,b
    #back
    result1=cv.matchTemplate(src,target1,methods[2])
    a=[]
    for i in range(result1.shape[0]):
        for j in range(result1.shape[1]):
            if result1[i,j]>0.45:
                a.append([j,i])
    #front
    result2=cv.matchTemplate(src,target2,methods[2])
    b=[]
    for i in range(result2.shape[0]):
        for j in range(result2.shape[1]):
            if result2[i,j]>0.58:
                b.append([j,i])

def debug():
    print(len(a),len(b))
    mx2=0
    for i in range(3205,3226):
        for j in range(820,841):
            if result2[i,j]>mx2:
                mx2=result2[i,j]
    print(mx2)

def printout(n,m):
    global _src
    for i in a:
        _src=cv.rectangle(_src,(i[0],i[1]),(i[0]+target1.shape[1],i[1]+target1.shape[0]),(0,0,255),2)
    for i in b:
        _src=cv.rectangle(_src,(i[0],i[1]),(i[0]+target2.shape[1],i[1]+target2.shape[0]),(255,0,0),2)
    cv.imwrite("D:\\TEST\\Dian2021\\Task1\\result1\\result_%d_%d.jpg"%(n,m),_src)
    print("#%d finished.\n"%m)

if __name__=="__main__":
    for i in range(1,4):
        if i==1:
            mx=4
        elif i==2:
            mx=8
        else:
            mx=16
        for j in range(1,mx):
            init(i,j)
            main()
            #debug()
            printout(i,j)