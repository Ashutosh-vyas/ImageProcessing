# filter 1: horizontal Sobel filter
import matplotlib.pyplot as plt
from skimage import data , filters

camera = data.camera()
hsobel_camera = filters.hsobel(camera)


plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(camera)

plt.subplot(122)
plt.imshow(hsobel_camera)
plt.tight_layout()
plt.show()

