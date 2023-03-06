import numpy as np
import scipy.signal as signal
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])
 
 
trim_wav("C:/Users/Matt/Documents/Project/CS-M/Datasets/normal/test/(2).wav", 0,10)
#C:/Users/Matt/Documents/Project/CS-M/Datasets/murmur/test/(2).wav

# Read in the audio file
frames, sample_rate = sf.read('File.wav')

# Convert the frames to a numpy array
#frames = np.frombuffer(frames, dtype=np.int16)

# Low-pass filter
cutoff_freq = 250 # set cutoff frequency
nyq_freq = 0.5 * sample_rate # Nyquist frequency
Wn = cutoff_freq / nyq_freq # filter cutoff frequency
b, a = signal.cheby1(4, 5, Wn, btype='low', analog=False)
filtered_frames = signal.filtfilt(b, a, frames)


# Export new WAV file
sf.write('Low-Pass_Filter.wav', filtered_frames, sample_rate)


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