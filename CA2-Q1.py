import numpy as np
import matplotlib.pyplot as plt

def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def idft(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N
    return x

t = np.linspace(0, 1, 500, endpoint=False)
signal_sin = np.sin(2 * np.pi * 5 * t)
signal_cos = np.cos(2 * np.pi * 5 * t)
signal_step = np.heaviside(t - 0.5, 1.0)

ft_signal_sin = dft(signal_sin)
ft_signal_cos = dft(signal_cos)
ft_signal_step = dft(signal_step)

reconstructed_sin = idft(ft_signal_sin)
reconstructed_cos = idft(ft_signal_cos)
reconstructed_step = idft(ft_signal_step)

fig, axs = plt.subplots(3, 2, figsize=(12, 8))

axs[0, 0].plot(t, signal_sin)
axs[0, 0].set_title('Original Sine Signal')
axs[0, 1].plot(t, reconstructed_sin.real)
axs[0, 1].set_title('Reconstructed Sine Signal')

axs[1, 0].plot(t, signal_cos)
axs[1, 0].set_title('Original Cosine Signal')
axs[1, 1].plot(t, reconstructed_cos.real)
axs[1, 1].set_title('Reconstructed Cosine Signal')

axs[2, 0].plot(t, signal_step)
axs[2, 0].set_title('Original Step Signal')
axs[2, 1].plot(t, reconstructed_step.real)
axs[2, 1].set_title('Reconstructed Step Signal')

for ax in axs.flat:
    ax.set(xlabel='Time', ylabel='Amplitude')

plt.tight_layout()
plt.show()
