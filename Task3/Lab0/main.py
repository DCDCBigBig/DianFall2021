import os
import struct
import numpy as np
import matplotlib.pyplot as plt
#import tensorflow as tf
from tqdm import tqdm
from knn import Knn


"""def _load_mnist(root='./', n_samples=6e4):
    #X: datas
    #y: labels
    mnist = tf.keras.datasets.mnist
    (train_X,train_y),(test_X,test_y)=mnist.load_data()
    return train_X,train_y,test_X,test_y"""

def load_mnist(root='./',n_samples=6e4):
    labels_path=os.path.join(root,'train-labels.idx1-ubyte')
    images_path=os.path.join(root,'train-images.idx3-ubyte')
    with open(labels_path,'rb') as lbpath:
        magic,n=struct.unpack('>II', lbpath.read(8))
        train_lab=np.fromfile(lbpath, dtype=np.uint8)
    with open(images_path,'rb') as imgpath:
        magic,num,rows,cols=struct.unpack('>IIII',imgpath.read(16))
        train_img=np.fromfile(imgpath,dtype=np.uint8).reshape(len(train_lab),28,28)
    labels_path=os.path.join(root,'t10k-labels.idx1-ubyte')
    images_path=os.path.join(root,'t10k-images.idx3-ubyte')
    with open(labels_path,'rb') as lbpath:
        magic,n=struct.unpack('>II', lbpath.read(8))
        test_lab=np.fromfile(lbpath, dtype=np.uint8)
    with open(images_path,'rb') as imgpath:
        magic,num,rows,cols=struct.unpack('>IIII',imgpath.read(16))
        test_img=np.fromfile(imgpath,dtype=np.uint8).reshape(len(test_lab),28,28)
    n_samples=int(n_samples)
    train_img=train_img[:n_samples]
    train_lab=train_lab[:n_samples]
    return train_img,train_lab,test_img,test_lab

def main():
    X_train, y_train, X_test, y_test = load_mnist(root="D:\TEST\Dian2021\Task3\MNIST")
    print("Load over.")

    knn = Knn()
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    correct = sum((y_test - y_pred) == 0)

    print('==> correct:', correct)
    print('==> total:', len(X_test))
    print('==> acc:', correct / len(X_test))

    # plot pred samples
    """fig = plt.subplots(nrows=4, ncols=5, sharex='all',
                       sharey='all')[1].flatten()
    for i in range(20):
        img = X_test[i]
        fig[i].set_title(y_pred[i])
        fig[i].imshow(img, cmap='Greys', interpolation='nearest')
    fig[0].set_xticks([])
    fig[0].set_yticks([])
    plt.tight_layout()
    plt.show()"""


if __name__ == '__main__':
    main()