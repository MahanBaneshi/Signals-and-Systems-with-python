In the codes of this Repository, we have used the features of the Python language (numpy, matplotlib libraries) for the university course of signals and systems.

- In file CA1-Q1, we have defined an arbitrary discrete language signal and then, using mathematical formulas and numpy features, we calculate the even and odd parts of that signal and plot them using matplotlib.
- In file CA1-Q2, we have calculated the real and imaginary parts of several complex signals using numpy and plotted them in matplotlib using the subplot command.
- In file CA1-Q3, we have performed the convolution operation for two functions using numpy features (its ready-made functions) and plotted the resulting function.
- In file CA1-Q4, we have defined the convolution operation for one-dimensional arrays ourselves with two for loops and compared its performance with the numpy ready-made function itself.
- In file CA1-Q5, we first implemented and plotted the impulse and step basis functions, which play an important role in the concepts of the lesson, using the stem command. Then, we proved that the result of convolution of a function with the impulse function is the same function.

---
  
- in file CA2-Q1, we have first defined the Fourier transform and inverse Fourier transform methods and passed some mathematical functions to them.
- in file CA2-Q1cos, we applied Fourier transforms and inverse Fourier transforms to 3 cosine signals with different frequencies. For each function, we have 3 figures. One is the original form of the function, one is the form of the Fourier series coefficients, and the other is the reconstructed signal from the inverse Fourier transform.
- in file CA2-Q1sin, we do the same thing, but this time the signals are sinusoidal.
- in file CA2-Q1u(t), we do this for the step function. However, here the reconstructed signal is different from the original signal. Because we consider the Fourier transform in a limited range and this range does not include all harmonics. So the signal is not reconstructed 100%. But in sine and cosine signals, since the non-zero harmonics were not infinite, the complete signal was reconstructed.
- in file CA2-Q2, we generate a complex sinusoidal signal, add Gaussian noise to it, and visualize the original and noisy signals in the time domain. We compute an approximate continuous Fourier transform of the noisy signal, apply low-pass, high-pass, and band-pass Butterworth filters in the frequency domain, and plot their magnitude responses. Finally, we reconstruct the filtered signals using the inverse Fourier transform and compare the results with the noisy signal in the time domain.
- In file CA2-Q3, we generate single-frequency sine waves with different frequencies and compute their spectrograms using a fixed sampling rate. We visualize the time–frequency representation of each signal to show how increasing frequency appears in the spectrogram.


