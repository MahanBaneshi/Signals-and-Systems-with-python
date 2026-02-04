import numpy as np
import matplotlib.pyplot as plt

# creating f(t)
def f_t(t):
    f = np.zeros_like(t)
    for i in range(len(t)):
        if np.abs(t[i]) <= np.pi:
            f[i] = np.abs(np.sin(t[i]))
        elif np.abs(t[i]) <= 2 * np.pi:
            f[i] = (np.abs(t[i]) - np.pi) ** 2
        elif np.abs(t[i]) <= 3 * np.pi:
            f[i] = -np.abs(t[i]) + np.pi ** 2 + 2 * np.pi
        else:
            f[i] = np.pi ** 2 - np.pi
    return f


# creating 1D Reverse Edge Detection kernel
def reverse_edge_kernel(t):
    kernel = np.zeros_like(t)
    for i in range(len(t)):
        if t[i] < 0:
            kernel[i] = -1
        elif t[i] == 0:
            kernel[i] = 0
        elif t[i] > 0:
            kernel[i] = 1
    return kernel


# creating convolution
def reverse_edge_detection(signal):
    kernel = reverse_edge_kernel(np.arange(-1, 2))
    convolved_signal = np.convolve(signal, kernel, mode='same')
    return convolved_signal


plt.figure(figsize=(12, 10))

# design f(t)
t = np.linspace(-10, 10, 400)
f_values = f_t(t)
plt.subplot(3, 1, 1)
plt.plot(t, f_values, label='f(t)')
plt.title('Function f(t)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()

# design 1D Reverse Edge Detection kernel
plt.subplot(3, 1, 2)
t_kernel = np.linspace(-1, 1, 400)
kernel_values = reverse_edge_kernel(t_kernel)
plt.plot(t_kernel, kernel_values)
plt.title('1D Reverse Edge Detection Kernel')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.grid(True)

# design convolution
convolved_signal = reverse_edge_detection(f_values)
plt.subplot(3, 1, 3)
plt.plot(t, convolved_signal, label='Convolution')
plt.title('Convolution of f(t) with 1D Reverse Edge Detection')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
