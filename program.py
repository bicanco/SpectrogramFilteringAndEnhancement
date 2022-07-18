from generateImage import generateImage
from filterImage import Filters, filterImage
from enhanceImage import EnhancementTechniques, enhanceImage
from evaluateImage import evaluateImage
import imageio.v3 as iio
import matplotlib.pyplot as plt

# Script to run the program for all the files at once

files = [
  'LEEC02__0__20161129_054600_ma',
  'LEEC02__0__20161129_072900_ma',
  'LEEC02__0__20161129_080100_ma',
  'LEEC02__0__20161130_063100_ma',
  'LEEC02__0__20161202_050100_ma',
]

images = []
tags = []
for filename in files:
  tags.append(generateImage(filename))
  images.append(iio.imread(f'images/{filename}.png')[:,:,0])

for i in range(len(images)):
  image = images[i]
  filteredImage1 = filterImage(image, Filters.Gaussian)
  filteredImage2 = filterImage(image, Filters.FilterInFrequencyDomain)

  result1 = enhanceImage(filteredImage1, EnhancementTechniques.HistogramEqualisation)
  result2 = enhanceImage(filteredImage2, EnhancementTechniques.HistogramEqualisation)
  result3 = enhanceImage(image, EnhancementTechniques.HistogramEqualisation)

  evaluateImage(image, tags[i])
  evaluateImage(result1, tags[i])
  evaluateImage(result2, tags[i])
  evaluateImage(result3, tags[i])

  plt.show()
