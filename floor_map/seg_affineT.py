# segmentaation: affinetransform

from skimage import data
from skimage import transform
import numpy as np
import matplotlib.pyplot as plt

image = data.chelsea()

shift_y, shift_x = np.array(image.shape[:2]) / 2.
tf_rotate = transform.SimilarityTransform(rotation=np.deg2rad(30))
tf_shift = transform.SimilarityTransform(translation=[-shift_x, -shift_y])
tf_shift_inv = transform.SimilarityTransform(translation=[shift_x, shift_y])

image_rotated = transform.warp(image, (tf_shift + (tf_rotate + tf_shift_inv)).inverse)

plt.imshow(image_rotated)
plt.show()