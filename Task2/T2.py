import numpy as np
import cv2 as cv
import copy

def init(n):
    global origin,src,dis1,dis2
    src=cv.imread("D:\\TEST\\Dian2021\\gendata\\t2\\%d.jpg"%n,0)
    origin=copy.deepcopy(src)
    src=cv.GaussianBlur(src,(11,11),0)
    ret,src=cv.threshold(src,250,255,cv.THRESH_BINARY)
    contours=cv.findContours(src,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    points=[]
    for i in contours[0]:
        minx,miny,maxx,maxy=114514,114514,0,0
        for j in i:
            minx=min(j[0][0],minx)
            maxx=max(j[0][0],maxx)
            miny=min(j[0][1],miny)
            maxy=max(j[0][1],maxy)
        midx=(int)((minx+maxx)/2)
        midy=(int)((miny+maxy)/2)
        points.append([midx,midy])
    min1,min2=[0,114514],[0,114514]
    for i in points:
        if i[1]<min1[1]:
            min2=min1
            min1=i
        elif i[1]<min2[1]:
            min2=i
    if min2[0]<min1[0]:
        tmp=min2
        min2=min1
        min1=tmp

    dis1=[]
    nowy=min1[1]+70
    nowx=min1[0]
    for i in range(4):
        dis1.append(src[nowy:nowy+560,nowx-40:nowx+40])
        nowx+=80
        nowy-=3
    dis2=[]
    nowy=min2[1]+70
    nowx=min2[0]
    for i in range(4):
        dis2.append(src[nowy:nowy+560,nowx-40:nowx+40])
        nowx+=80
        nowy-=3

def main():
    global dis1,dis2,res1,res2
    res1=[[0]*(12) for _ in range(4)]
    res2=[[0]*(12) for _ in range(4)]
    cnt=0
    for i in dis1:
        total_y=i.shape[0]
        dy=(float)(total_y/12)
        contours=cv.findContours(i,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
        tmp=contours[0]
        for j in tmp:
            miny,maxy=114514,0
            for t in j:
                miny=min(miny,t[0][1])
                maxy=max(maxy,t[0][1])
            midy=(int)((miny+maxy)/2)
            for t in range(12):
                #print(cnt,t,miny,maxy,midy,dy,total_y)
                if t*dy<=midy and midy<=(t+1)*dy:
                    res1[cnt][t]=1
                    break
        cnt+=1
    cnt=0
    for i in dis2:
        total_y=i.shape[0]
        dy=(float)(total_y/12)
        contours=cv.findContours(i,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
        tmp=contours[0]
        for j in tmp:
            miny,maxy=114514,0
            for t in j:
                miny=min(miny,t[0][1])
                maxy=max(maxy,t[0][1])
            midy=(int)((miny+maxy)/2)
            for t in range(12):
                #print(cnt,t,miny,maxy,midy,dy,total_y)
                if t*dy<=midy and midy<=(t+1)*dy:
                    res2[cnt][t]=1
                    break
        cnt+=1

def debug():
    for i in range(4):
        cv.imshow("%d"%i,dis1[i])
        cv.waitKey()
        cv.destroyAllWindows()
    for i in range(4):
        cv.imshow("%d"%i,dis2[i])
        cv.waitKey()
        cv.destroyAllWindows()

def printout(n):
    f=open("D:\\TEST\\Dian2021\\Task2\\result\\result_%d.txt"%n,'w')
    #for i in range(4):
    #    print("%s,"%res1[i],file=f)
    #for i in range(4):
    #    print("%s,"%res2[i],file=f)
    print(res1,file=f)
    print(res2,file=f)
    f.close()

if __name__=="__main__":
    for i in range(1,28):
        init(i)
        main()
        #debug()
        printout(i)