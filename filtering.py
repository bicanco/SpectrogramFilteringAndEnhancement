import imageio.v3 as iio
import scipy.ndimage as nd
import matplotlib.pyplot as plt

image = iio.imread('images\LEEC02__0__20161129_054600_ma.png')[:,:,0]

plt.figure('Original image')
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.figure('Laplacian filter')
plt.imshow(nd.laplace(image), cmap='gray', vmin=0, vmax=255)
plt.figure('Gaussian filter')
plt.imshow(nd.gaussian_filter(image, 4), cmap='gray', vmin=0, vmax=255)
plt.figure('Gaussian laplacian filter')
plt.imshow(nd.gaussian_laplace(image, 1), cmap='gray', vmin=0, vmax=255)
plt.figure('Maximum filter')
plt.imshow(nd.maximum_filter(image, 10), cmap='gray', vmin=0, vmax=255)
plt.figure('Minimum filter')
plt.imshow(nd.minimum_filter(image, 10), cmap='gray', vmin=0, vmax=255)
plt.figure('Percentile filter')
plt.imshow(nd.percentile_filter(image, 50, 10), cmap='gray', vmin=0, vmax=255)
plt.figure('Prewitt filter')
plt.imshow(nd.prewitt(image), cmap='gray', vmin=0, vmax=255)
plt.figure('Rank filter')
plt.imshow(nd.rank_filter(image, 42, 20), cmap='gray', vmin=0, vmax=255)
plt.figure('Sobel filter')
plt.imshow(nd.sobel(image), cmap='gray', vmin=0, vmax=255)
plt.figure('Uniform filter')
plt.imshow(nd.uniform_filter(image), cmap='gray', vmin=0, vmax=255)
plt.show()
