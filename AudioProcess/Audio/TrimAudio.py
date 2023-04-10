from scipy.io import wavfile

for i in range (1,8):
    file = 'C:/Users/Matt/Downloads/'+str(i)+'00 Hz Test Tone.wav'
    output = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/ControlledVaribles/Noise/('+str(i)+').wav'

    sampleRate, waveData = wavfile.read( file )
    startSample = int( 10 * sampleRate )
    endSample = int( 20 * sampleRate )
    wavfile.write( output, sampleRate, waveData[startSample:endSample])