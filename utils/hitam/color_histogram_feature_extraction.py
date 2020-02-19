from PIL import Image
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq
from utils.hitam import knn_classifier as knn_classifier
current_path = os.getcwd()


def color_histogram_of_test_image(test_src_image):

    # load the image
    image = test_src_image

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter_black = 0
    for (chan, color) in zip(chans, colors):
        counter_black = counter_black + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter_black == 1:
            blue = str(elem)
        elif counter_black == 2:
            green = str(elem)
        elif counter_black == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
    with open(current_path + '/utils/hitam/'
              + 'test.data', 'w') as myfile:
        myfile.write(feature_data)


def color_histogram_of_training_image(img_name):

    # detect image color by using image file name to label training data
    if 'black' in img_name:
        data_source = 'hitam'
        
    # load the image
    image = cv2.imread(img_name)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter_black = 0
    for (chan, color) in zip(chans, colors):
        counter_black = counter_black + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter_black == 1:
            blue = str(elem)
        elif counter_black == 2:
            green = str(elem)
        elif counter_black == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue

    with open('training.data', 'a') as myfile:
        myfile.write(feature_data + ',' + data_source + '\n')


def training():

    # black color training images
    for f in os.listdir('./training_dataset/hitam'):
        color_histogram_of_training_image('./training_dataset/hitam/' + f)
