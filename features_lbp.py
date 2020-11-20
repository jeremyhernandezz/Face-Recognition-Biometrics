# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:26:32 2019

@author: Tyree
"""

import matplotlib.pyplot as plt
import numpy as np

def get_lbp(image, width):
    image = image.reshape((width, width))
    lbp_image = np.zeros(shape=(width, width))
    num_neighbors = 1
    
    for i in range(num_neighbors, image.shape[0] - num_neighbors):
        for j in range(num_neighbors, image.shape[1] - num_neighbors):
            center_pixel = image[i,j]
            binary_string = ""
            
            for m in range(i-num_neighbors, i+num_neighbors+1):
                for n in range(j-num_neighbors, j+num_neighbors+1):
                    
                    if [i,j] == [m,n]: # same pixel
                        pass
                    else:
                        neighbor_pixel = image[m, n]                                           
                        if center_pixel >= neighbor_pixel:
                            binary_string += '1'
                        else:
                            binary_string += '0'
            
            lbp_image[i,j] = int(binary_string, 2)            
    return lbp_image

def get_features(image, size):
    # compute and concatenate histograms
    histograms = []
    for i in range(0,image.shape[0],size):
        for j in range(0,image.shape[1],size):
            block = image[i:i+size, j:j+size]
            histograms.extend( np.histogram(block, bins=256)[0] )    
    return histograms

#########################################################################
def init_lbp(X):
    
    width = 64

    blockSize = 16

    features = []
    for i in range(len(X)):
        lbp_face = get_lbp(X[i], width)
        lbp_features = get_features(lbp_face, blockSize)
        features.append(lbp_features)
    
#        if i <= 5: # Show first 5 images
#            plt.figure()
#            plt.imshow(X[i].reshape((width,width)), cmap='gray')
#            plt.figure()
#            plt.imshow(lbp_face, cmap='gray')
        
    features = np.array(features)
    
    return features

#image_directory = 'Group1_FaceData'
#X, y = get_data.get_images(image_directory)
#init_lbp(X)