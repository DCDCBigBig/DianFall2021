import numpy as np
import cv2 as cv
import copy

def init(n):
    global src,dis
    src=cv.imread("D:\\TEST\\Dian2021\\gendata\\t2\\%d.jpg"%n,0)
    src=cv.GaussianBlur(src,(11,11),0)
    #ret,src=cv.threshold(src,250,255,cv.THRESH_BINARY)
    dis=[]
    dis.append(src[1570:2090,843:931])
    dis.append(src[1570:2090,931:1005])
    dis.append(src[1570:2090,1005:1082])
    dis.append(src[1565:2090,1082:1156])
    dis.append(src[1557:2080,1398:1482])
    dis.append(src[1557:2075,1482:1555])
    dis.append(src[1552:2075,1555:1633])
    dis.append(src[1550:2070,1633:1708])

def main():
    global dis,res
    res=[[0]*(12) for _ in range(8)]
    cnt=0
    for i in dis:
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
                    res[cnt][t]=1
                    break
        cnt+=1

def debug():
    for i in range(8):
        cv.imshow("%d"%i,dis[i])
        cv.waitKey()
        cv.destroyAllWindows()

def printout(n):
    f=open("D:\\TEST\\Dian2021\\Task2\\result\\result_%d.txt"%n,'w')
    for i in range(8):
        print("%s,"%res[i],file=f)
    f.close()

if __name__=="__main__":
    for i in range(8,9):
        init(i)
        #main()
        debug()
        #printout(i)