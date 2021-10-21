import os
import struct
import numpy as np
import cv2 as cv

def load_mnist(path,kind="train"):
    labels_path = os.path.join(path, '%s-labels.idx1-ubyte'% kind)
    images_path = os.path.join(path, '%s-images.idx3-ubyte'% kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))
        labels = np.fromfile(lbpath, dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
        images = np.fromfile(imgpath, dtype=np.uint8)#.reshape(len(labels), 784)

    return images, labels

if __name__=="__main__":
    train_X,train_y=load_mnist("D:\TEST\Dian2021\Task3\MNIST")
    train_X=train_X.reshape(60000,28,28)
    #print(train_X[0])
    cv.imshow("1",train_X[0])
    cv.waitKey()