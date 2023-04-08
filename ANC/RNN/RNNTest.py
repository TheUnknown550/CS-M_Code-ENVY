import numpy as np
import librosa
import tensorflow as tf
from sklearn.metrics import confusion_matrix

# Load the clean audio and the noise audio
clean_audio, sr_clean = librosa.load('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Original/All/(1).wav', sr=16000)
noise_audio, sr_noise = librosa.load('C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Noise/(1).wav', sr=16000)

# Pad the shorter signal with zeros to make them equal length
max_len = max(len(clean_audio), len(noise_audio))
clean_audio = np.pad(clean_audio, (0, max_len - len(clean_audio)), 'constant')
noise_audio = np.pad(noise_audio, (0, max_len - len(noise_audio)), 'constant')

# Create training data by adding clean and noise signals together
X_train = np.stack((clean_audio, noise_audio), axis=-1)
y_train = clean_audio

# Define the window size and step size for training data
window_size = 16000 # 1 second
step_size = 8000 # 0.5 seconds

# Split the training data into windows of 1 second each
X_train_windows = []
y_train_windows = []
for i in range(0, len(X_train) - window_size, step_size):
    X_train_windows.append(X_train[i:i + window_size])
    y_train_windows.append(y_train[i:i + window_size])
X_train_windows = np.array(X_train_windows)
y_train_windows = np.array(y_train_windows)

# Define the RNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True, input_shape=(window_size, 2)),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train_windows, y_train_windows[:, :, np.newaxis], epochs=10)

# Save the model
model.save('ANC.h5')