import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, Sequential, models
from os import listdir
from os.path import isfile, join
from PIL import Image as img
import glob

print(tf.__version__)

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
folder_path = "C:/NN/Pneumonia/chest_xray/train/"
for filename in glob.glob(folder_path + "NORMAL"):
    
