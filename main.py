import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from os import listdir
from os.path import isfile, join
import numpy as np
import tensorflow as tf
from PIL import Image as img
from tensorflow.python import keras
from keras import Sequential, datasets, layers, models

# train_data_points = 1000
# test_data_points = 100
# total_data_points = train_data_points + test_data_points
pixels = 500
dimensions = (pixels, pixels)
bins = 3
mid_layer = 750
training_iters = 10
learning_rate = 2e-3
num_epochs = 1

train_images = []
train_labels = np.array([])
folder_path = "/mnt/c/NN/Pneumonia/chest_xray/train/"

for f in listdir(folder_path + "NORMAL"):
    im = img.open(folder_path + "NORMAL/" + f)
    im = im.resize(dimensions)
    im = im.convert('L')
    im_array = np.asarray(im)
    train_images.append(im_array)
    im.close()
    train_images.append(im)
    train_labels = np.append(train_labels, 0)

for f in listdir(folder_path + "PNEUMONIA"):
    im = img.open(folder_path + "PNEUMONIA/" + f)
    im = im.resize(dimensions)
    im = im.convert('L')
    im_array = np.asarray(im)
    train_images.append(im_array)
    im.close()    
    if "bacteria" in f:
        train_labels = np.append(train_labels, 1)
    elif "virus" in f:
        train_labels = np.append(train_labels, 2)

test_images = []
test_labels = np.array([])
folder_path = "/mnt/c/NN/Pneumonia/chest_xray/test/"

for f in listdir(folder_path + "NORMAL"):
    im = img.open(folder_path + "NORMAL/" + f)
    im = im.resize(dimensions)
    im = im.convert('L')
    im_array = np.asarray(im)
    test_images.append(im_array)
    im.close()    
    test_labels = np.append(test_labels, 0)

for f in listdir(folder_path + "PNEUMONIA"):
    im = img.open(folder_path + "PNEUMONIA/" + f)
    im = im.resize(dimensions)
    im = im.convert('L')
    im_array = np.asarray(im)
    test_images.append(im_array)
    im.close()    
    if "bacteria" in f:
        test_labels = np.append(test_labels, 1)
    elif "virus" in f:
        test_labels = np.append(test_labels, 2)

# train_images = np.array(train_images)
# test_images = np.array(test_images)
print(type(train_images[0]))
print(type(test_images))

train_images = np.stack(train_images)
test_images = np.stack(test_images)

print(np.shape(train_images))
print(np.shape(test_images))
