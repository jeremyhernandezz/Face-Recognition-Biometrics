# Load imports
#!/usr/bin/python3
#-*- coding: UTF-8 -*-   
import os
from PIL import Image
from PIL import ImageEnhance
import numpy as np
# from IPython.display import display # to display images in the console
'''
function get_images() definition
Parameter, image_directory, is the directory 
holding the images
'''

def get_images(image_directory, x):
    case = x
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
                    image = Image.open('Project Data/' + subfolder + '/' + file)
                    ''' Present different cases, based on selection in main '''               
                    # Create new folder for post brightness enhanced pictures.
                    if case == '1':
                        #Brightness 
                        image = brighten_image(image)
                        directory = 'Group1_FaceData_EnhancedBrightness/' + subfolder
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        image.save(directory + '/' + file, "PNG")
                        image = np.array(image)
                        X.append(image)
                        y.append(subfolder)
                        
                        # pil_im = Image.open(directory + '/' + file)                   # used with IPython
                        # display(pil_im)
                    # Create new folder for Contrast Enhancement
                    if case == '2':
                        #Contrast
                        image = contrast_image(image)
                        directory = 'Group1_FaceData_EnhancedContrast/' + subfolder
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        image.save(directory + '/' + file, "PNG")
                        X.append(image)
                        y.append(subfolder)
                    # Create new folder for Sharpness Enhancement
                    if case == '3':
                        # Sharpness
                        image = sharpen_image(image)
                        directory = 'Group1_FaceData_EnhancedSharpness/' + subfolder
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        image.save(directory + '/' + file, "PNG")
                        X.append(image)
                        y.append(subfolder)
                    # Create new folder for combining all three
                    if case == '4':
                        #Combining all three 
                        image = modify_image(image)
                        directory = 'Group1_FaceData_CombinedEnhanced/' + subfolder
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        image.save(directory + '/' + file, "PNG")
                        X.append(image)
                        y.append(subfolder)
    print("All images are loaded")  
    # return the images and their labels      
    return X, y

def brighten_image(image):
    enh_br = ImageEnhance.Brightness(image)
    brightness = 2.0
    brightened_img = enh_br.enhance(brightness)                    

    return brightened_img
        
def contrast_image(image):
     enh_cont = ImageEnhance.Contrast(image)
     contrast = 0.5
     contrasted_img = enh_cont.enhance(contrast)

     return contrasted_img

def sharpen_image(image):
    #Sharpness                
     enh_sharp = ImageEnhance.Sharpness(image)
     sharpness = 3.0
     sharped_img = enh_sharp.enhance(sharpness)
            
     return sharped_img

def modify_image(image):
    #Brightness
    enh_br = ImageEnhance.Brightness(image)
    brightness = 2.0
    modified_img = enh_br.enhance(brightness)
                    
    #Contrast
    enh_cont = ImageEnhance.Contrast(modified_img)
    contrast = 0.5
    modified_img = enh_cont.enhance(contrast)
                    
    #Sharpness                
    enh_sharp = ImageEnhance.Sharpness(modified_img)
    sharpness = 3.0
    modified_img = enh_sharp.enhance(sharpness)
      
    return modified_img