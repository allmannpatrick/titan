from PIL import Image
from keras.models import load_model
#import matplotlib.pyplot as plt
import numpy as np

model = load_model('fluff_CNN.h5')

def prediction(image_path):
     image_path = image_path[1:]
     img_loaded = Image.open(image_path)
     img_resized = Image.Image.resize(img_loaded,(100,100))
     img = (np.array(img_resized) - 127.5)/127.5
     img = img.reshape(1,100,100,3)
     prediction= model.predict_classes(img)
     #plt.imshow(img_resized)
     #plt.show()
     if prediction ==0:
         prediction = 'cat'
     else:
         prediction = 'dog'
     return prediction
