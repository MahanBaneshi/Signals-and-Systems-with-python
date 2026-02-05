import numpy as np
import matplotlib.pyplot as plt

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


t = np.linspace(0, 1, 500, endpoint=False)
freqs = np.linspace(-200, 200, 1000)  

# define input signals
signal_sin_5Hz = 0.1 * np.sin(2 * np.pi * 2.5 * t)
signal_sin_50Hz = 0.5 * np.sin(2 * np.pi * 25 * t)
signal_sin_120Hz = 0.2 * np.sin(2 * np.pi * 50 * t)

# Fourier Transforms
cft_signal_sin_5Hz = continuous_fourier_transform(signal_sin_5Hz, t, freqs)
cft_signal_sin_50Hz = continuous_fourier_transform(signal_sin_50Hz, t, freqs)
cft_signal_sin_120Hz = continuous_fourier_transform(signal_sin_120Hz, t, freqs)

#  Inverse Fourier Transform
reconstructed_sin_5Hz = inverse_continuous_fourier_transform(cft_signal_sin_5Hz, freqs, t)
reconstructed_sin_50Hz = inverse_continuous_fourier_transform(cft_signal_sin_50Hz, freqs, t)
reconstructed_sin_120Hz = inverse_continuous_fourier_transform(cft_signal_sin_120Hz, freqs, t)

# Creating signals
fig, axs = plt.subplots(3, 3, figsize=(18, 14))

# f = 5 Hz
axs[0, 0].plot(t, signal_sin_5Hz)
axs[0, 0].set_title('Original Sine Signal (2.5 Hz)', fontsize=14)
axs[0, 1].plot(t, reconstructed_sin_5Hz.real)
axs[0, 1].set_title('new Sine Signal (2.5 Hz)', fontsize=14)
axs[0, 2].plot(freqs, np.abs(cft_signal_sin_5Hz))
axs[0, 2].set_title('CFT of Sine Signal (2.5 Hz)', fontsize=14)

# f = 50 Hz
axs[1, 0].plot(t, signal_sin_50Hz)
axs[1, 0].set_title('Original Sine Signal (25 Hz)', fontsize=14)
axs[1, 1].plot(t, reconstructed_sin_50Hz.real)
axs[1, 1].set_title('new Sine Signal (25 Hz)', fontsize=14)
axs[1, 2].plot(freqs, np.abs(cft_signal_sin_50Hz))
axs[1, 2].set_title('CFT of Sine Signal (25 Hz)', fontsize=14)

# f = 120 Hz
axs[2, 0].plot(t, signal_sin_120Hz)
axs[2, 0].set_title('Original Sine Signal (50 Hz)', fontsize=14)
axs[2, 1].plot(t, reconstructed_sin_120Hz.real)
axs[2, 1].set_title('new Sine Signal (50 Hz)', fontsize=14)
axs[2, 2].plot(freqs, np.abs(cft_signal_sin_120Hz))
axs[2, 2].set_title('CFT of Sine Signal (50 Hz)', fontsize=14)

for ax in axs.flat:
    ax.set_xlabel('Time [s]', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.subplots_adjust(wspace=0.5, hspace=0.7, top=0.95, bottom=0.05)
plt.show()
