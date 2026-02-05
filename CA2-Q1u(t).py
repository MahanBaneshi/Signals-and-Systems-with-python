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

# f = 5 Hz
signal_step_5Hz = 0.1 * np.heaviside(t - 0.5, 1.0)
signal_step_50Hz = 0.5 * np.heaviside(t - 0.25, 1.0)
signal_step_120Hz = 0.2 * np.heaviside(t - 0.75, 1.0)

# f = 50 Hz
cft_signal_step_5Hz = continuous_fourier_transform(signal_step_5Hz, t, freqs)
cft_signal_step_50Hz = continuous_fourier_transform(signal_step_50Hz, t, freqs)
cft_signal_step_120Hz = continuous_fourier_transform(signal_step_120Hz, t, freqs)

# f = 120 Hz
reconstructed_step_5Hz = inverse_continuous_fourier_transform(cft_signal_step_5Hz, freqs, t)
reconstructed_step_50Hz = inverse_continuous_fourier_transform(cft_signal_step_50Hz, freqs, t)
reconstructed_step_120Hz = inverse_continuous_fourier_transform(cft_signal_step_120Hz, freqs, t)


fig, axs = plt.subplots(3, 3, figsize=(18, 14))

# D = 0.1
axs[0, 0].plot(t, signal_step_5Hz)
axs[0, 0].set_title('Original Step Signal (0.1 Amplitude)', fontsize=14)
axs[0, 1].plot(t, reconstructed_step_5Hz.real)
axs[0, 1].set_title('new Step Signal (0.1 Amplitude)', fontsize=14)
axs[0, 2].plot(freqs, np.abs(cft_signal_step_5Hz))
axs[0, 2].set_title('CFT of Step Signal (0.1 Amplitude)', fontsize=14)

# D = 0.5
axs[1, 0].plot(t, signal_step_50Hz)
axs[1, 0].set_title('Original Step Signal (0.5 Amplitude)', fontsize=14)
axs[1, 1].plot(t, reconstructed_step_50Hz.real)
axs[1, 1].set_title('new Step Signal (0.5 Amplitude)', fontsize=14)
axs[1, 2].plot(freqs, np.abs(cft_signal_step_50Hz))
axs[1, 2].set_title('CFT of Step Signal (0.5 Amplitude)', fontsize=14)

# D = 0.2
axs[2, 0].plot(t, signal_step_120Hz)
axs[2, 0].set_title('Original Step Signal (0.2 Amplitude)', fontsize=14)
axs[2, 1].plot(t, reconstructed_step_120Hz.real)
axs[2, 1].set_title('new Step Signal (0.2 Amplitude)', fontsize=14)
axs[2, 2].plot(freqs, np.abs(cft_signal_step_120Hz))
axs[2, 2].set_title('CFT of Step Signal (0.2 Amplitude)', fontsize=14)

for ax in axs.flat:
    ax.set_xlabel('Time [s]', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.subplots_adjust(wspace=0.5, hspace=0.7, top=0.95, bottom=0.05)
plt.show()
