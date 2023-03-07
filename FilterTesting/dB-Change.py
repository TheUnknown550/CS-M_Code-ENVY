import pydub

# Load the audio file
sound = pydub.AudioSegment.from_wav("Noise.wav")

# Set the desired decibel level (e.g. decrease by 3 dB)
target_db = -6.22 + 20 -50

# Apply the gain to the sound data
modified_sound = sound.apply_gain(target_db)

# Export the modified sound to a new file
modified_sound.export("C:/Users/Matt/Documents/Project/CS-M/Datasets/Testing/Noises/50dB.wav", format="wav")
