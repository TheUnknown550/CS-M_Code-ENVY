import soundfile as sf
import numpy as np
import librosa
from scipy.io import wavfile

#Varibles
dB = '50'

# File Number
for n in range(40):

    # Trim the Audio
    def trim_wav( originalWavPath, start, end, name ):
        sampleRate, waveData = wavfile.read( originalWavPath )
        startSample = int( start * sampleRate )
        endSample = int( end * sampleRate )
        wavfile.write( name, sampleRate, waveData[startSample:endSample])
    
    # Trim and Load the audio file
    trim_wav("C:/Users/Matt/Documents/Project/CS-M/Datasets/murmur/test/("+str(n+1)+").wav", 0,10, 'File.wav')
    data1, sample_rate1 = sf.read('File.wav')
    current_db1= 20 * np.log10(np.sqrt(np.mean(data1 ** 2)))
    print('dB1: ', current_db1)


    # Load the second audio file
    trim_wav("C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/Noises/"+dB+"dB.wav", 0,10, 'Noise.wav')
    data2, sample_rate2 = sf.read('Noise.wav')
    current_db2 = 20 * np.log10(np.sqrt(np.mean(data2 ** 2)))
    print('dB2: ', current_db2)


    # Convert stereo signals to mono if necessary
    if data1.ndim > 1:
        data1 = np.mean(data1, axis=1)
    if data2.ndim > 1:
        data2 = np.mean(data2, axis=1)

    # Resample the audio files if they have different sample rates
    if sample_rate1 != sample_rate2:
        print('Resampling audio files...')
        if sample_rate1 > sample_rate2:
            data1 = data1[::int(sample_rate1/sample_rate2)]
            sample_rate1 = sample_rate2
        else:
            data2 = data2[::int(sample_rate2/sample_rate1)]
            sample_rate2 = sample_rate1

    # Make the two signals the same length
    length = min(len(data1), len(data2))
    data1 = data1[:length]
    data2 = data2[:length]

    # Mix the two audio signals
    mixed_data = (data1 + data2) / 2

    # Write the mixed audio to a new file
    sf.write('C:/Users/Matt/Documents/Project/CS-M/Experiments/FilterTests/murmur/'+dB+'dB/('+str(n+1)+').wav', mixed_data, sample_rate1)