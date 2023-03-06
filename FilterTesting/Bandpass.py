import numpy as np
import scipy.signal as signal
import wave




# Filter Effectiveness Tests
# Calculate the SNR (High is good)
signal_power = np.sum(np.square(frames))
noise_power = np.sum(np.square(frames - filtered_frames))
SNR = 10 * np.log10(signal_power / noise_power)

# Calculate the MSE (low is good)
MSE = np.mean(np.square(frames - filtered_frames))


# Output the value of SNR and MSE
print("SNR: ", SNR)
print("MSE: ", MSE)