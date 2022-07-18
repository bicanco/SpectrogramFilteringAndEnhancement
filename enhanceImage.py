from enum import IntEnum
import matplotlib.pyplot as plt
import numpy as np

class EnhancementTechniques(IntEnum):
  Logarithmic = 0
  HistogramEqualisation = 1

# Function responsable for applying a logarithmic
# function to the image
def logarithmic(image: np.ndarray) -> np.ndarray:
  const = 255/np.log2(256)
  return const*np.log2(1+image)

# Function responsable for applying a histogram
# equalisation to the image
def histogramEqualisation(image: np.ndarray) -> np.ndarray:
  histogram,_ = np.histogram(image,256)
  cumulativeHistogram = np.empty(256)

  cumulativeHistogram[0] = histogram[0]
  for i in range(1,256):
    cumulativeHistogram[i] = cumulativeHistogram[i-1]+histogram[i]

  N,M = image.shape
  const = 255/(N*M)
  enhancedImage = np.empty(image.shape)
  enhancedImage = const * cumulativeHistogram[image.astype(int)]

  return enhancedImage

# Function resposable for enhancing the image
def enhanceImage(image: np.ndarray, option: EnhancementTechniques) -> np.ndarray:
  enhancementTechniques = [
    lambda: logarithmic(image),
    lambda: histogramEqualisation(image),
  ]

  enhancedImage = enhancementTechniques[option]()

  plt.figure('Enhanced Image')
  plt.imshow(enhancedImage, cmap='gray',vmin=0,vmax=255)

  return enhancedImage
