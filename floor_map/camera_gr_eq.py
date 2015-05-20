from skimage import data, exposure
import matplotlib.pyplot as plt

camera = data.camera()
camera_equalized = exposure.equalize_hist(camera) 

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])


plt.figure(figsize=(8, 4))

plt.subplot(121)
plt.imshow(camera_equalized, cmap='gray', interpolation='nearest')

plt.subplot(122)
plt.hist(camera_equalized,256,[0,256])
plt.tight_layout()
plt.show()