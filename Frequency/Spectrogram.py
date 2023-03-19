import librosa
import matplotlib.pyplot as plt

# Load the audio file
filename = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/AmpLowTests/normal/AmpToLow/LowAudio/(1).wav'
y, sr = librosa.load(filename)

# Compute the Fourier transform of the audio signal
fft = librosa.stft(y)

# Convert the complex Fourier coefficients to magnitudes 
mag = librosa.amplitude_to_db(abs(fft))

# Plot the filtered spectrum
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
librosa.display.specshow(mag, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')

plt.subplot(2, 1, 2)
plt.plot(y)

plt.tight_layout()
plt.show()
