from PIL import Image
from tensorflow.python import keras
import numpy as np
#import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Activation, Conv2D, Dense, Flatten, MaxPool2D, BatchNormalization, Dropout
from tensorflow.keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
import os
import cv2
import random

X0 = [] #image,cat pairs
X = [] #images
Y = [] #cetegories
cat1 = 'cat'
cat2 = 'dog'
folder_cat = 'train/'+cat1
folder_dog = 'train/'+cat2
name_encode = {cat1 : 0, cat2 : 1}
def images_to_array(folder,name):
    for image in os.listdir(folder):
        loaded_image = Image.open(os.path.join(folder,image))
        resized_image = Image.Image.resize(loaded_image,[100,100])
        
        image_array = np.array(resized_image)
        X0.append((image_array,name_encode[name]))
        
        image_flipped = cv2.flip(image_array,1)
        X0.append((image_flipped,name_encode[name]))
        
        image_blurred = cv2.blur(image_array,(2,2))
        X0.append((image_blurred,name_encode[name]))
        
        image_flipped_blurred = cv2.blur(image_flipped,(2,2))
        X0.append((image_flipped_blurred,name_encode[name]))

    
    
images_to_array(folder_cat,cat1)    
images_to_array(folder_dog,cat2)   

random.shuffle(X0)
for x,y in X0:
    X.append(x)
    Y.append(y)


        
def show_image(index):
    plt.imshow(X[index])
    plt.show()
    print(Y[index])
    
 

Y = to_categorical(Y,num_classes=2)
X = (np.array(X)-127.5)/127.5


model = Sequential()
model.add(Conv2D(16,(5,5),padding='same',activation='relu',input_shape=(100,100,3)))

model.add(BatchNormalization())
model.add(Dropout(rate=0.5))


#model.add(MaxPool2D(pool_size=(2,2) ))

model.add(Flatten())

#model.add(Dense(124))

#model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('sigmoid'))
model.summary()


X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.1)

optimizer = Adam(lr=0.001)
model.compile(optimizer=optimizer,loss = 'binary_crossentropy',metrics=['acc'])
h = model.fit(X_train,y_train,batch_size=50,epochs = 30,shuffle=True,validation_data=(X_test,y_test))

model.save('fluff_CNN.h5')

#plt.plot(h.history['acc'],label='train')
#plt.plot(h.history['val_acc'],label='test')
#plt.title('CNN Accuracy')
#plt.xlabel('epoch')
#plt.ylabel('accuracy')
#plt.legend(loc='lower right')
#plt.show()


#model = load_model('fluff_CNN.h5')




# def prediction(index_number):
#     img = (np.array(X[index_number]) - 127.5)/127.5
#     img = img.reshape(1,100,100,3)
    
#     plt.imshow(img)
#     plt.show()
    # prediction= model.predict_classes(img)
    # if prediction ==0:
    #     print(cat1)
    # else:
    #     print(cat2)
    # return prediction

    
