import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

t1 = np.linspace(-10, 10, 400)
x1 = np.gradient(np.exp(-t1) * np.sin(t1) * np.exp(1j * (np.pi * t1 / 2)))

magnitude_x1 = np.abs(x1)
phase_x1 = np.angle(x1)

t2 = np.linspace(-15, 15, 400)
x2 =  np.convolve((t2 ** 3), (t2), mode='same') * np.exp(1j * t2)

magnitude_x2 = np.abs(x2)
phase_x2 = np.angle(x2)

omega3 = np.linspace(-5 * np.pi, 5 * np.pi, 400)
x3 = 2 ** np.log((1j + np.pi) / (-1j * omega3 ** 8 + 8)) / np.log(8)

magnitude_x3 = np.abs(x3)
phase_x3 = np.angle(x3)

omega4 = np.linspace(-10 * np.pi, 10 * np.pi, 400)
integral_values = []

for omega in omega4:
    integrand = lambda t: np.exp(-(1 + 1j * omega * np.pi / 2) * t)
    result, _ = quad(integrand, 0, np.inf)
    integral_values.append(result)

x4 = np.array(integral_values)
magnitude_x4 = np.abs(x4)
phase_x4 = np.angle(x4)

plt.figure(figsize=(10, 15))

plt.subplot(4, 2, 1)
plt.plot(t1, magnitude_x1)
plt.title('Magnitude of x1(t)')
plt.xlabel('t')
plt.ylabel('|x1(t)|')

plt.subplot(4, 2, 2)
plt.plot(t1, phase_x1)
plt.title('Phase of x1(t)')
plt.xlabel('t')
plt.ylabel('∠x1(t)')

plt.subplot(4, 2, 3)
plt.plot(t2, magnitude_x2)
plt.title('Magnitude of x2(t)')
plt.xlabel('t')
plt.ylabel('|x2(t)|')

plt.subplot(4, 2, 4)
plt.plot(t2, phase_x2)
plt.title('Phase of x2(t)')
plt.xlabel('t')
plt.ylabel('∠x2(t)')

plt.subplot(4, 2, 5)
plt.plot(omega3, magnitude_x3)
plt.title('Magnitude of X3(ω)')
plt.xlabel('ω')
plt.ylabel('|X3(ω)|')

plt.subplot(4, 2, 6)
plt.plot(omega3, phase_x3)
plt.title('Phase of X3(ω)')
plt.xlabel('ω')
plt.ylabel('∠X3(ω)')

plt.subplot(4, 2, 7)
plt.plot(omega4, magnitude_x4)
plt.title('Magnitude of X4(ω)')
plt.xlabel('ω')
plt.ylabel('|X4(ω)|')

plt.subplot(4, 2, 8)
plt.plot(omega4, phase_x4)
plt.title('Phase of X4(ω)')
plt.xlabel('ω')
plt.ylabel('∠X4(ω)')

plt.tight_layout()
plt.show()
