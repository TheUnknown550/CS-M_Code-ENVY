import soundfile as sf
import numpy as np
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('ANC.h5')

file_path = 'MixedAudio.wav'
noise_path = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Noise/(2).wav'

# Load the recorded audio and noise audio files for testing
recorded_audio, sr_recorded = sf.read(file_path, dtype='float32')
noise_audio, sr_noise = sf.read(noise_path, dtype='float32')

# Pad the signals with zeros to make them equal length to the clean signal
max_len = max(len(recorded_audio), len(noise_audio))
recorded_audio = np.pad(recorded_audio, (0, max_len - len(recorded_audio)), 'constant')
noise_audio = np.pad(noise_audio, (0, max_len - len(noise_audio)), 'constant')

# Define the window size and step size for testing data
window_size = 16000 # 1 second
step_size = 8000 # 0.5 seconds

# Split the signals into windows of 1 second each
X_test_windows = []
for i in range(0, len(recorded_audio) - window_size, step_size):
    window = np.stack((recorded_audio[i:i + window_size], noise_audio[i:i + window_size]), axis=-1)
    X_test_windows.append(window)
X_test_windows = np.array(X_test_windows)

# Use the model to clean up the recorded audio
y_pred_windows = model.predict(X_test_windows)
y_pred_windows = np.squeeze(y_pred_windows, axis=-1)

# Remove any padding added earlier
y_pred = np.reshape(y_pred_windows, (-1,))
y_pred = y_pred[:len(recorded_audio)]

# Save the cleaned audio using soundfile
sf.write('CleanedFile.wav', y_pred, sr_recorded)
