# FILTER COMPARISION 
import matplotlib.pyplot as plt
from skimage import data
from skimage import filters
from scipy import ndimage

coins = data.coins()
gaussian_filter_coins = ndimage.gaussian_filter(coins, sigma=2)
med_filter_coins = ndimage.filters.median_filter(coins,size=2)
tv_filter_coins = filters.denoise_tv_chambolle(coins, weight=0.1)

plt.figure(figsize=(16, 4))
plt.subplot(141)
plt.imshow(coins[10:80, 300:370], cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Image')
plt.subplot(142)
plt.imshow(gaussian_filter_coins[10:80, 300:370], cmap='gray',interpolation='nearest')
plt.axis('off')
plt.title('Gaussian filter')
plt.subplot(143)
plt.imshow(med_filter_coins[10:80, 300:370], cmap='gray',interpolation='nearest')
plt.axis('off')
plt.title('Median filter')
plt.subplot(144)
plt.imshow(tv_filter_coins[10:80, 300:370], cmap='gray',interpolation='nearest')
plt.axis('off')
plt.title('TV filter')
plt.show()