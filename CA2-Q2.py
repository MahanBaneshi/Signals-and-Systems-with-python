import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter


fs = 1000  
t = np.arange(0, 1, 1/fs)  # dt = 1ms

# initial signal
signal = 50 * np.exp(1j * 2 * np.pi * 100 * t)

# Adding Gaussian noise
noise_mean = 0
noise_std = 10
noise_real = np.random.normal(noise_mean, noise_std, t.shape)
noise_imag = np.random.normal(noise_mean, noise_std, t.shape)
noisy_signal = (signal.real + noise_real) + 1j * (signal.imag + noise_imag)

# Creating initail signal and noisy signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal.real, label='Original Signal (Real Part)')
plt.plot(t, noisy_signal.real, label='Noisy Signal (Real Part)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Original and Noisy Signal (Real Part)')
plt.subplot(2, 1, 2)
plt.plot(t, signal.imag, label='Original Signal (Imaginary Part)')
plt.plot(t, noisy_signal.imag, label='Noisy Signal (Imaginary Part)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Original and Noisy Signal (Imaginary Part)')
plt.tight_layout()
plt.show()

# 
def filter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def filter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def filter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band', analog=False)
    return b, a

def apply_filter(data, fs, filter_type='low', cutoff=None, lowcut=None, highcut=None, order=5):
    if filter_type == 'low':
        b, a = filter_lowpass(cutoff, fs, order=order)
    elif filter_type == 'high':
        b, a = filter_highpass(cutoff, fs, order=order)
    elif filter_type == 'band':
        b, a = filter_bandpass(lowcut, highcut, fs, order=order)
    else:
        raise ValueError("Invalid filter type")
    y = lfilter(b, a, data)
    return y

# Continuous Fourier Transform method
def continuous_fourier_transform(signal, t, freqs):
    dt = t[1] - t[0]  
    X = np.zeros(len(freqs), dtype=complex)
    for i, f in enumerate(freqs):
        X[i] = np.sum(signal * np.exp(-2j * np.pi * f * t)) * dt
    return X

# Inverse Continuous Fourier Transform method
def inverse_continuous_fourier_transform(X, freqs, t):
    df = freqs[1] - freqs[0] 
    signal = np.zeros(len(t), dtype=complex)
    for i, time in enumerate(t):
        signal[i] = np.sum(X * np.exp(2j * np.pi * freqs * time)) * df
    return signal

# Frequency range
freqs = np.linspace(-500, 500, 1000)

# Fourier Transforms
cft_noisy_signal = continuous_fourier_transform(noisy_signal.real, t, freqs)

# Showing Fourier Transform
plt.figure(figsize=(12, 6))
plt.plot(freqs, np.abs(cft_noisy_signal))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Continuous Fourier Transform of Noisy Signal')
plt.tight_layout()
plt.show()

# Apply filters

filtered_cft_lowpass = apply_filter(cft_noisy_signal, fs=fs, filter_type='low', cutoff=20)
filtered_cft_highpass = apply_filter(cft_noisy_signal, fs=fs, filter_type='high', cutoff=50)
filtered_cft_bandpass = apply_filter(cft_noisy_signal, fs=fs, filter_type='band', lowcut=50, highcut=100)

# Showing filtered signals of Fourier Transform signal
plt.figure(figsize=(12, 6))
plt.plot(freqs, np.abs(filtered_cft_lowpass))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('HighPass Filtered Signal in Frequency Domain')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(freqs, np.abs(filtered_cft_highpass))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('LowPass Filtered Signal in Frequency Domain')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(freqs, np.abs(filtered_cft_bandpass))
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('BandPass Filtered Signal in Frequency Domain')
plt.tight_layout()
plt.show()

# Inverse Fourier Transform
reconstructed_lowpass = inverse_continuous_fourier_transform(filtered_cft_lowpass, freqs, t)
reconstructed_highpass = inverse_continuous_fourier_transform(filtered_cft_highpass, freqs, t)
reconstructed_bandpass = inverse_continuous_fourier_transform(filtered_cft_bandpass, freqs, t)

# Showing new signals
plt.figure(figsize=(12, 6))
plt.plot(t, noisy_signal.real, label='Noisy Signal')
plt.plot(t, reconstructed_lowpass.real, label='LowPass Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('HighPass Filtered Signal in Time Domain')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(t, noisy_signal.real, label='Noisy Signal')
plt.plot(t, reconstructed_highpass.real, label='HighPass Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title(' LowPass Filtered Signal in Time Domain')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(t, noisy_signal.real, label='Noisy Signal')
plt.plot(t, reconstructed_bandpass.real, label='BandPass Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('BandPass Filtered Signal in Time Domain')
plt.tight_layout()
plt.show()
