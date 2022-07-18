from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pandas as pd

# Function responsable for generating the images and
# extracting the normalized tag values
def generateImage(filename: str) -> pd.DataFrame:
  samplingRate, audioWave = wavfile.read(f'audios/{filename}.wav')

  fig,_ = plt.subplots(1)
  fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
  _,freq,_,_ = plt.specgram(audioWave, Fs=samplingRate, cmap='gray')
  fig.savefig(f'images/{filename}.png', dpi=600)

  df = pd.read_csv(f'audios/{filename}.Table.1.selections.txt', sep='\t')

  maxFreq = freq[len(freq)-1]
  lines = []
  for line in range(len(df)):
    d = [
      df.iloc[line][3] / 60,
      df.iloc[line][4] / 60,
      df.iloc[line][5] / maxFreq,
      df.iloc[line][6] / maxFreq,
    ]
    lines.append(d)

  newDf = pd.DataFrame(lines,columns=[
    'startTime',
    'endTime',
    'startFrequency',
    'endFrequency',
  ])

  newDf.to_csv(
    f'images/{filename}.csv'
  )

  return newDf
