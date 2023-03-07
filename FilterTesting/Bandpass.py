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
trim_wav("C:/Users/Matt/Documents/Project/CS-M/Datasets/normal/test/(2).wav", 0,10)
frames, sample_rate = sf.read('File.wav')


# Define filter parameters
fmin = 50  # Lower cutoff frequency
fmax = 200  # Upper cutoff frequency

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
# Calculate the SNR (High is good)
signal_power = np.sum(np.square(frames))
noise_power = np.sum(np.square(frames - filtered_frames))
SNR = 10 * np.log10(signal_power / noise_power)

# Calculate the MSE (low is good)
MSE = np.mean(np.square(frames - filtered_frames))

# Calculate the PSNR (High is Good)
max_amp_value = np.finfo(frames.dtype).max
PSNR = 10 * np.log10((max_amp_value ** 2) / MSE)

# Output the value of SNR and MSE
print("SNR: ", SNR)
print("MSE: ", MSE)
print("PSNR: ", PSNR)


# Plot sound graphs
t = np.arange(0, len(frames)/sample_rate, 1/sample_rate)
plt.figure(1)
plt.title("Sound Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.plot(t, frames)
plt.plot(t, filtered_frames)
plt.show()