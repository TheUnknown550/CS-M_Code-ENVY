import numpy as np
import scipy.signal as signal
import wave

# Open the audio file
with wave.open('audio_file.wav', 'rb') as wav_file:
    # Read the audio frames
    frames = wav_file.readframes(-1)
    # Get the sample rate and number of channels
    sample_rate = wav_file.getframerate()
    num_channels = wav_file.getnchannels()

# Apply a low-pass filter
cutoff_freq = 200 # set cutoff frequency
nyq_freq = 0.5 * sample_rate # Nyquist frequency
normal_cutoff = cutoff_freq / nyq_freq
b, a = signal.butter(4, normal_cutoff, btype='low', analog=False)
filtered_frames = signal.filtfilt(b, a, frames)


# Filter Effectiveness Tests
# Calculate the SNR (High is good)
signal_power = np.sum(np.square(frames))
noise_power = np.sum(np.square(frames - filtered_frames))
SNR = 10 * np.log10(signal_power / noise_power)

# Calculate the MSE (low is good)
MSE = np.mean(np.square(frames - filtered_frames))


# Output the value of SNR and MSE
print("SNR: ", SNR)
print("MSE: ", MSE)