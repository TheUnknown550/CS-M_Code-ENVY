from pydub import AudioSegment

# Set the file paths for the two audio files
original_file_path = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Original/All/(1).wav'
noise_file_path = 'C:/Users/Matt/Documents/Project/CS-M/Experiments/NoiseCancelTests/Datasets/Noise/(1).wav'

# Load the audio files using PyDub
original_audio = AudioSegment.from_wav(original_file_path)
noise_audio = AudioSegment.from_wav(noise_file_path)

# Mix the two audio files together
mixed_audio = original_audio.overlay(noise_audio)

# Set the output file path and export the mixed audio file
output_file_path = 'MixedAudio.wav'
mixed_audio.export(output_file_path, format='wav')
