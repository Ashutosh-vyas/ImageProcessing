# non local filter and equalization 
import matplotlib.pyplot as plt
from skimage import data , filters , exposure

camera = data.camera()
camera_equalized = exposure.equalize_hist(camera)


plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(camera)

plt.subplot(122)
plt.imshow(camera_equalized)
plt.tight_layout()
plt.show()
