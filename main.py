import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, Sequential, models

print(tf.__version__)

pixels = 1024

model = models.Sequential()
model.add(layers.Conv2D(pixels, (3, 3), activation='relu', input_shape=(pixels, pixels, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(2 * pixels, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(2 * pixels, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))