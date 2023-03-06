import numpy as np
import soundfile as sf
from scipy import signal

# Load audio file
audio_data, sample_rate = sf.read('File.wav')

db_range = [45,70]
fmin = 100
fmax = 4000

# Generate the noise signal with random dB
db = np.random.uniform(*db_range)
noise = np.random.normal(0, 1, len(audio_data))
noise = 10 ** (db / 20) * noise

# Create a bandpass filter
b, a = signal.butter(10, [fmin, fmax], btype='bandpass', fs=sample_rate)

# Apply the filter to the noise signal
filtered_noise = signal.filtfilt(b, a, noise)

# Add the filtered noise to the audio signal
noisy_audio = audio_data + filtered_noise

# Normalize the audio signal
max_amp_value = np.iinfo(audio_data.dtype).max
norm_factor = max_amp_value / np.max(np.abs(noisy_audio))
noisy_audio_norm = noisy_audio * norm_factor

# Save noisy audio file
sf.write("noisyFile", audio_data, sample_rate)