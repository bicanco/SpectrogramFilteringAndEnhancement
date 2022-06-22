import matplotlib.pyplot as plt
from scipy.io import wavfile

filename = str(input().strip())

samplingRate, audioWave = wavfile.read(f'audios/{filename}.wav')

fig,_ = plt.subplots(1)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
plt.specgram(audioWave, Fs=samplingRate, cmap='gray')
fig.savefig(f'images/{filename}.png', dpi=600)
