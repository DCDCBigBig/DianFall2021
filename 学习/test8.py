import numpy as np
import cv2 as cv
import tensorflow as tf

mnist=tf.keras.datasets.mnist

(train_X,train_y),(test_X,test_y)=mnist.load_data()

for i in range(31633,31634):
    cv.imshow("%d"%i,train_X[i])
    cv.imshow("origin",test_X[1])
    cv.waitKey()
    cv.destroyAllWindows()
