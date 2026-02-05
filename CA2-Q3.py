import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Creating sine wave
def plot_spectrogram(freq, fs=1000, duration=5):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    signal = np.sin(2 * np.pi * freq * t)
    f, t_spec, Sxx = spectrogram(signal, fs)
    
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title(f'f = {freq} Hz')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Intensity [dB]')
    plt.ylim(0, 300)  # Create a domain
    plt.show()

plot_spectrogram(5)
plot_spectrogram(20)
plot_spectrogram(50)
plot_spectrogram(100)
plot_spectrogram(200)

