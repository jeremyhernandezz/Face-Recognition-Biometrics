# Load imports
import os 
import cv2
import numpy as np

'''get_images used for lbp and pca, which is why the images are being resized'''
'''reads raw image files with the extensions'''
def get_images(image_directory):
    X = []
    y = []
    extensions = ('jpg','png','gif')
    
    '''
    Each subject has their own folder with their
    images. The following line lists the names
    of the subfolders within image_directory.
    '''
    subfolders = os.listdir(image_directory)
    for subfolder in subfolders:
        print("Loading images in %s" % subfolder)
        if os.path.isdir(os.path.join(image_directory, subfolder)): # only load directories
            subfolder_files = os.listdir(
                    os.path.join(image_directory, subfolder)
                    )
            for file in subfolder_files:
                if file.endswith(extensions): # grab images only
                    # read the image using openCV
                    img = cv2.imread(
                            os.path.join(image_directory, subfolder, file), cv2.IMREAD_GRAYSCALE
                            )
                    # resize the image by half
                    scale_percent = 64 # percent of original size, changed to 64 to get 64x64 was getting an error about the size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
#                    print(width)
                    img = cv2.resize(img, dim)
                    # add the resized image to a list X
                    X.append(img)
                    # add the image's label to a list y
                    y.append(subfolder)
    
    print("All images are loaded")  
    print('\n')
    # return the images and their labels      
    return np.array(X), np.array(y)

'''get_landmarks used for knn and nb match, which will be used for calculating performance'''
'''reads .npy files'''
def get_landmarks(landmark_directory):
    X = []
    y = []
    subfolders = os.listdir(landmark_directory)
    for subfolder in subfolders:
        print("Loading landmarks in %s" % subfolder)
        if os.path.isdir(os.path.join(landmark_directory, subfolder)): # only load directories
            subfolder_files = os.listdir(
                    os.path.join(landmark_directory, subfolder)
                    )
            for file in subfolder_files:
                if file.endswith('5.npy'):                              # getting specific type of file, similar to getting a certain task for additional architecture 
                    landmarks = np.load(os.path.join(landmark_directory, subfolder, file))
                    X.append(landmarks)
                    y.append(subfolder)
    
    print("All landmarks are loaded")
    print('\n')     
    # return the images and their labels      
    return np.array(X), np.array(y)