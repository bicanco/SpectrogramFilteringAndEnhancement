from enum import IntEnum
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import scipy.fft as fft
import numpy as np

class Filters(IntEnum):
  Gaussian = 0
  Maximum = 1
  Minimum = 2
  Percentile = 3
  Rank = 4
  Uniform = 5
  FilterInFrequencyDomain = 6
  Laplacian = 7
  GaussianLaplacian = 8
  Prewitt = 9
  Sobel = 10

# Function responsable for filtering in the frequency domain
def filterInFrequencyDomain(image: np.ndarray) -> np.ndarray:
  Spectrum = fft.fft2(image)
  Spectrum[Spectrum > 100000000] = 1000000000
  return np.abs(fft.ifft2(Spectrum))

# Function responsable for applying several filters to the image
def filterImage(image: np.ndarray, option: Filters) -> np.ndarray:
  filterFunctions = [
    lambda: nd.gaussian_filter(image, 4),
    lambda: nd.maximum_filter(image, 10),
    lambda: nd.minimum_filter(image, 10),
    lambda: nd.percentile_filter(image, 50, 10),
    lambda: nd.rank_filter(image, 42, 20),
    lambda: nd.uniform_filter(image),
    lambda: filterInFrequencyDomain(image),
    # Discarded Filters
    lambda: nd.laplace(image),
    lambda: nd.gaussian_laplace(image, 1),
    lambda: nd.prewitt(image),
    lambda: nd.sobel(image),
  ]

  filteredImage = filterFunctions[option]()
  plt.figure('Filtered Image')
  plt.imshow(filteredImage, cmap='gray',vmin=0,vmax=255)

  return filteredImage
