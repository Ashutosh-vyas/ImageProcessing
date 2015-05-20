from skimage import data
import matplotlib.pyplot as plt

im = data.lena()
fig = plt.figure()
fig.add_subplot(311)
plt.hist(im[...,0].flatten(), 256, range=(0, 250), fc='b')
fig.add_subplot(312)
plt.hist(im[...,1].flatten(), 256, range=(0, 250), fc='g')
fig.add_subplot(313)
plt.hist(im[...,2].flatten(), 256, range=(0, 250), fc='r')
plt.show()
