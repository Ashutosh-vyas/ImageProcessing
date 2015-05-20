# Differencing horizontally adjacent points will detect vertical 
# changes in intensity and is often called a horizontal edge-detector by virtue 
# of its action
# Similarly for horizantal detection we need vertical edge detector
# The template is convolved with the image to detect edges.
import numpy
import scipy
from scipy import ndimage
from skimage import data
import matplotlib.pyplot as plt
im = data.coins()
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
plt.imshow(mag,cmap='gray')
plt.show()