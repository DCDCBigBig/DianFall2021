import numpy as np
from tqdm import tqdm
import copy
import matplotlib.pyplot as plt
import tensorflow as tf

class Knn(object):

    def __init__(self, k=1):
        self.k = k

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X, datasize=60000):
        self.X=self.X.astype(np.int32)
        X=X.astype(np.int32)
        tmp=copy.deepcopy(self.X)
        self.X=self.X[:datasize]
        tot=X.shape[0]
        y_pred=np.ones(tot,np.int32)*10
        for i in range(tot):
            if i%100==0:
                print("#%d finished."%(i))
            cnt=np.zeros(10,np.int32)
            distances=np.sum(np.abs(self.X-X[i]),axis=2)
            distances=np.sum(distances,axis=1)
            for k in range(self.k):
                minn=np.argmin(distances)
                cnt[self.y[minn]]+=1
                distances=np.delete(distances,minn)
            y_pred[i]=np.argmax(cnt)
        self.X=tmp
        return y_pred

if __name__=="__main__":
    mnist = tf.keras.datasets.mnist
    (train_X,train_y),(test_X,test_y)=mnist.load_data()
    """train_X=train_X.astype(np.int32)
    train_y=train_y.astype(np.int32)
    test_X=test_X.astype(np.int32)
    test_y=test_y.astype(np.int32)"""
    knn=Knn()
    knn.fit(train_X,train_y)
    testx=test_X[:1000]
    testy=test_y[:1000]
    res=knn.predict(testx)
    print(res)
    print(testy)
    correct=sum((testy-res)==0)
    print(correct/len(testx))
