import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf
from scipy.signal import firwin, filtfilt

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
 
# Trim and Load the audio file
trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/murmur/10dB/(2).wav", 0,10)
frames, sample_rate = sf.read('File.wav')

# Band-pass Filter
# Define filter parameters
fmin = 20  # Lower cutoff frequency
fmax = 250  # Upper cutoff frequency

# Calculate the filter order
nyquist_freq = 0.5 * sample_rate
width = 100  # Width of the transition band, in Hz
n = int(np.ceil(4 * nyquist_freq / width))

# Design the bandpass filter
b = firwin(n, [fmin, fmax], pass_zero=False, fs=sample_rate)

# Apply the filter to the audio file
filtered_frames = filtfilt(b, [1], frames)



# Export new WAV file
sf.write('Band-Pass_Filter.wav', filtered_frames, sample_rate)


# Filter Effectiveness Tests
# Calculate the Noise% (High is good)
signal_power = np.sum(np.square(frames))
noise_power = np.sum(np.square(frames - filtered_frames))
Noise = noise_power / signal_power * 100
print('Noise%: ',Noise)
# Calculate the MSE (low is good)
MSE = np.mean(np.square(frames - filtered_frames))
print('MSE: ',MSE)


'''# Plot sound graphs
t = np.arange(0, len(frames)/sample_rate, 1/sample_rate)
plt.figure(1)
plt.title("Sound Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.plot(t, frames)
plt.plot(t, filtered_frames)
plt.show()'''