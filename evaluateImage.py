from matplotlib.axes import Axes
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function resposable for extracting a segment of the
# image and highlighting it
def extractSegment(image, stime, etime, sfreq, efreq, axes: Axes):
  N,M = image.shape
  # Due to the axis orientation in the image
  # and values of the frequency in the original
  # spectrogram being inverted
  # the coordinates need to be adjusted
  startFrequency = int(N - (sfreq * N))
  endFrequency = int(N - (efreq * N))

  startTime = int(stime * M)
  endTime = int(etime * M)

  plt.imshow(image[
    endFrequency:startFrequency,
    startTime:endTime
  ],cmap='gray',vmin=0,vmax=255)

  width = endTime - startTime
  height = startFrequency - endFrequency
  axes.add_patch(Rectangle((startTime, endFrequency), width, height,fc='none',ec='red'))

# Function responsable for creating the images for evaluation
def evaluateImage(image: np.ndarray, tags: pd.DataFrame) -> None:
  numberOfTags = len(tags)
  plt.figure('Full Image')
  plt.imshow(image,cmap='gray',vmin=0,vmax=255)
  axes = plt.gca()
  for i in range(numberOfTags):
    line = tags.iloc[i]
    plt.figure(f'Tag {i}')
    extractSegment(image, line[0], line[1], line[2], line[3], axes)
