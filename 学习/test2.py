import numpy as np
import cv2 as cv

img=cv.imread("D:\\testimg\\2.jpg",1)

"""img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("1",img)

cv.waitKey()
cv.destroyAllWindows()"""

#flags=[i for i in dir(cv) if i.startswith("COLOR_")]
#print(flags)

white=np.ones((512,512,3),np.uint8)
white=100*white

Weight=img.shape[1]
Height=img.shape[0]

_img=img
k=10

for i in range(0,Height):
    for j in range(0,Weight):
        for t in range(0,3):
            tot=0
            num=0
            for ii in range(i-k,i+k+1):
                for jj in range(j-k,j+k+1):
                    if(ii<0 or jj<0 or ii>=Height or jj>=Weight):
                        continue
                    tot+=1
                    num+=img[ii,jj,t]
            try:
                _img[i,j,t]=(int)(num/tot)
            except:
                print("%d %d\n"%(i,j))


#_img[Height-1,Weight-1]=[0,0,0]

cv.imshow("2",_img)
cv.imwrite("2_gauss_10.jpg",_img)

cv.waitKey()