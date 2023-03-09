import librosa
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Trim the Audio
def trim_wav( originalWavPath, start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( 'File.wav', sampleRate, waveData[startSample:endSample])

for i in range(1,496):
    print(i)
    # Load the audio file
    filename = 'C:/Users/Matt/Documents/Project/CS-M/Datasets/Normal/Lowpass/('+str(i)+').wav'
    trim_wav(filename,0,10)
    y, sr = librosa.load('File.wav')

    # Compute the Fourier transform of the audio signal
    fft = librosa.stft(y)

    # Convert the complex Fourier coefficients to magnitudes
    mag = librosa.amplitude_to_db(abs(fft))

    # Plot the filtered spectrum
    plt.figure(figsize=(10, 10))
    librosa.display.specshow(mag, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.savefig('C:/Users/Matt/Documents/Project/CS-M/Datasets/Normal/TestSpectrogram/('+str(i)+').png')

