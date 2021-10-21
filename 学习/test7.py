#from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import tensorflow

mnist = tensorflow.keras.datasets.mnist

(train_X,train_Y),(x_1,y_1)=mnist.load_data()

"""
#load data
train_X = mnist.train.images               
validation_X = mnist.validation.images      
test_X = mnist.test.images                  
#labels
train_Y = mnist.train.labels                
validation_Y = mnist.validation.labels      
test_Y = mnist.test.labels           
"""       

print(train_X.shape,train_Y.shape)          

print(train_X[0])       
print(train_Y[0])

fig, ax = plt.subplots(nrows=4,ncols=5,sharex='all',sharey='all')
ax = ax.flatten()
for i in range(20):
    img = train_X[i].reshape(28, 28)
    ax[i].imshow(img,cmap='Greys')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()

