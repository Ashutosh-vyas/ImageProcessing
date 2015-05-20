import skimage
from skimage import data, filters  # most functions are in subpackages
import matplotlib.pyplot as plt
camera = data.camera()
plt.figure(figsize=(4, 4))
plt.imshow(camera, cmap='gray', interpolation='nearest')
plt.axis('off')

plt.tight_layout()
plt.show()
