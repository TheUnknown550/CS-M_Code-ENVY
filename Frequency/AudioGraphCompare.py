import librosa
import matplotlib.pyplot as plt

# Load the audio file
filename1 = 'C:/Users/Matt/Documents/Project/CS-M/CS-M_Code-ENVY/Filters/FilterTesting/Test.wav'
y1, sr1 = librosa.load(filename1)

# Load 2nd the audio file
filename2 = 'C:/Users/Matt/Documents/Project/CS-M/CS-M_Code-ENVY/Filters/FilterTesting/ANC.wav'
y2, sr2 = librosa.load(filename2)

# Plot the filtered spectrum
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(y1)
plt.plot(y2)

plt.tight_layout()
plt.show()
