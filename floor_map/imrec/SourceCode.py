# PATTERN RECOGNITION
############################
### Import libraries
############################
from functools import reduce
import math, operator
import numpy as np
import scipy as sp
import PIL
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt

from skimage import data , io
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_harris,corner_peaks, ORB, plot_matches)
from skimage.color import rgb2gray
from skimage.feature import match_template


#############################
### reading the image 
#############################

#fmap = Image.open('fmap.jpg')
#a1 = Image.open('aa.png')
#a2 = Image.open('fmap.jpg')
#coin = rgb2gray(np.asarray(a1))
#image = rgb2gray(np.asarray(a2))


#print(a2.size)
#print(a1.size)
#ia1 = np.asarray(a1)

#############################
### GRAY SCALING AND
### NORMALIZING THE IMAGES
#############################

#############################
### THRESHOLDING 
#############################

#############################
### code to resize image 
#############################

#basewidth = 20

#wpercent = (basewidth / float(a1.size[0]))
#hsize = int((float(a2.size[1]) * float(wpercent)))
#a1 = a1.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
#a1 = rgb2gray(np.asarray(a1))

#ia2 = np.asarray(a2)
#print(ia2)

##---------------------------------------------------------
########### USE WHEN THE HEIGHT IS FIXED ##############

#baseheight = 560
#hpercent = (baseheight / float(a2.size[1]))
#wsize = int((float(a2.size[0]) * float(hpercent)))
#a2 = a2.resize((wsize, baseheight), PIL.Image.ANTIALIAS)

#a2 = a2.histogram()
##---------------------------------------------------------

##############################
### CROPPING THE IMAGES
##############################

#box=(301,146,318,163)
#coin = rgb2gray(np.asarray(a2.crop(box)))


########################
### calculating RMS error 
########################
#A1 = a1.histogram()
#A2 = a2.histogram()

#rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, A1, A2))/len(A1))



...

####################################################################################
########  	ORB MATCHING --- FEATURE MATCHING
####################################################################################

#descriptor_extractor = ORB(n_keypoints=100)

#descriptor_extractor.detect_and_extract(a1)
#keypoints1 = descriptor_extractor.keypoints
#descriptors1 = descriptor_extractor.descriptors

#descriptor_extractor.detect_and_extract(image)
#keypoints2 = descriptor_extractor.keypoints
#descriptors2 = descriptor_extractor.descriptors

#matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)

#fig, ax = plt.subplots(nrows=2, ncols=1)

#plt.gray()

#plot_matches(ax[0], coin, image, keypoints1, keypoints2, matches12)
#ax[0].axis('off')

#plt.show()

...
###############################################################
####### 	TEMPLATE MATCHING
##############################################################


#image = data.coins()
#coin = image[170:220, 75:130]

#result = match_template(image, coin)
#print(result)
#ij = np.unravel_index(np.argmax(result), result.shape)
#x, y = ij[::-1]

#fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(8, 3))

#ax1.imshow(coin)
#ax1.set_axis_off()
#ax1.set_title('template')

#ax2.imshow(image)
#ax2.set_axis_off()
#ax2.set_title('image')
## highlight matched region
#hcoin, wcoin = coin.shape
#rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
#ax2.add_patch(rect)

#ax3.imshow(result)
#ax3.set_axis_off()
#ax3.set_title('`match_template`\nresult')#
# highlight matched region
#ax3.autoscale(False)
#ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

#plt.show()


###############################################################
### plotting the images
###############################################################

#plt.figure(figsize=(16, 32))
#plt.subplot(121)
#plt.imshow(a1)
#plt.title('Image')
#plt.subplot(122)
#plt.imshow(a2)
#plt.show()
#print(rms)

#########################################################################################################################
################################################################ NEW TEST ###############################################
###############################################################-------------#############################################
#########################################################################################################################

floor_map = Image.open('fmap.jpg')
# //// DICTIONARY ///

box=(301,146,318,163)
Character_B = ((floor_map.crop(box)))

box1 = (572,346,589,363)
b2 = ((floor_map.crop(box1)))

box3 = (517,150,534,167)
b3 = ((floor_map.crop(box3)))

# /// DECARING VARIABLES ///

ImageSize = floor_map.size # dimension of floor map
ImageX = ImageSize[0]      # X length of floor_map
ImageY = ImageSize[1]      # Y length of floor_map

rms_thrushold = .5         # This threshold verifies the possibility of character
window_X = 17              # This is the X-dim length of window we will be looking at
window_Y = 17              # This is the Y-dim length of window we will be looking at  

cord_X = 0				   # This is current location pointer X-axis
cord_Y = 0 				   # This is current location pointer Y-axis

I = 0  
# /// ROOT MEAN SQUARE ERROR CLACULATION FORMULAE TO BE USED ////

def rms_error(character_image,window_image): # Function which calculate rms error...
    A1 = character_image.histogram() 
    A2 = window_image.histogram() 
    rms_r = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, A1, A2))/len(A1)) 
    return rms_r 

# /// COMPARISIONS ///

for cord_Y in range(0,ImageY - window_Y):  
   for cord_X in range(0,ImageX - window_X):
      window_block = (cord_X,cord_Y,cord_X + window_X,cord_Y + window_Y)
      window_img = ((floor_map.crop(window_block)))
      
      # /// CHARACTER B SEARCH /// 	  
      rms_err =  rms_error(Character_B,window_img)
      if rms_err <= rms_thrushold:     
         print(I , window_block)
                  
         I = I + 1
      else:                  
         continue
#print("number of B found are -->  ",I)
#print(floor_map.size)
plt.imshow(floor_map)
plt.show()
