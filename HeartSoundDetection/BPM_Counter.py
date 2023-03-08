def homomorphic_envelope(y, fs, f_LPF=8, order=3):
        b, a = butter(order, 2 * f_LPF / fs, 'low')
        he = np.exp(filtfilt(b, a, np.log(np.abs(hilbert(y)))))
        return he