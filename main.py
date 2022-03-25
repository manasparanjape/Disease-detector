from os import listdir
from os.path import isfile, join
import numpy as np
import tensorflow as tf
from PIL import Image as img
from tensorflow.keras import Sequential, datasets, layers, models

train_data_points = 1000
test_data_points = 100
total_data_points = train_data_points
pixels = 1024
bins = 3
mid_layer = 750
training_iters = 10
learning_rate = 2e-3
num_epochs = 1

train_images = []
train_labels = np.array()
folder_path = "/mnt/c/NN/Pneumonia/chest_xray/train/"

for f in listdir(folder_path + "NORMAL"):
    im = img.open(f)
    train_images.append(im)
    train_labels = np.append(train_labels, 0)

for f in listdir(folder_path + "PNEUMONIA"):
    im = img.open(f)
    train_images.append(im)
    if "bacteria" in f:
        train_labels = np.append(train_labels, 1)
    elif "virus" in f:
        train_labels = np.append(train_labels, 2)

test_images = []
test_labels = np.array()
folder_path = "/mnt/c/NN/Pneumonia/chest_xray/test/"

for f in listdir(folder_path + "NORMAL"):
    im = img.open(f)
    train_images.append(im)
    train_labels = np.append(train_labels, 0)