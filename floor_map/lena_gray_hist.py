# grayscaling lena
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
lena  = data.lena()

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(lena, cmap='gray', interpolation='nearest')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

lena_gry = rgb2gray(lena)
plt.subplot(122)
plt.hist(lena_gry,256,[0,256])
plt.tight_layout()
plt.show()
