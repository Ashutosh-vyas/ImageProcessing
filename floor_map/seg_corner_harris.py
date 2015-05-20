# HARRIS CORNER DETECTION
# corner detection is based upon the change of the position vector with respect 
# to arc length. 
# approximates the autocorrelation function in the direction (u, v). A measure of
# curvature is given by the minimum value  obtained by considering the shifts (u, v)
# in the four main directions. That is, by (1,0), (0,−1), (0,1) and (−1,0). The minimum is chosen
# because it agrees with the following two observations. First, if the pixel is in an edge defining a
# straight line, is small for a shift along the edge and large for a shift perpendicular to
# the edge. In this case, we should choose the small value since the curvature of the edge is small.
# Secondly, if the edge defines a corner, then all the shifts produce a large value. Thus, if we also
# chose the minimum, this value indicates high curvature.

from skimage import data
import matplotlib.pyplot as plt
from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform


tform = AffineTransform(scale=(1.3, 1.1), rotation=0, shear=0,translation=(0,0))#
image = warp(data.coins(), tform.inverse, output_shape=(500, 500))

coords = corner_peaks(corner_harris(image), min_distance=5)
coords_subpix = corner_subpix(image, coords, window_size=13)

plt.gray()
plt.imshow(image, interpolation='nearest')
plt.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15, mew=5)
plt.plot(coords[:, 1], coords[:, 0], '.b', markersize=7)
plt.axis('off')
plt.show()