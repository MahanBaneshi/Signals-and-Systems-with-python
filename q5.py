import numpy as np
import matplotlib.pyplot as plt

# create δ[n]
def impulse_function(n):
    return np.where(n == 0, 1, 0)

# create u[n]
def step_function(n):
    return np.where(n >= 0, 1, 0)


n = np.arange(-10, 10, 1)
step_values = step_function(n)
impulse_values = impulse_function(n)

# design δ[n] and u[n]
plt.subplot(2, 1, 2)
plt.stem(n, impulse_values)
plt.title('Impulse Function')
plt.xlabel('n')
plt.ylabel('δ[n]')

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(n, step_values)
plt.title('Step Function')
plt.xlabel('n')
plt.ylabel('u[n]')

plt.tight_layout()
plt.show()

x = np.array([3, 6, 7, 5])

# create an impulse
delta = np.zeros(len(x))
delta[0] = 1

# calculating convolution with numpy
convolution_result = np.convolve(x, delta, mode='full')

# check the equals
are_equal = np.array_equal(x, convolution_result[:len(x)])
print(f"Are the results equal? {are_equal}")

# design convolution method
n_conv = np.arange(len(convolution_result))

plt.figure(figsize=(10, 3))
plt.stem(n_conv, convolution_result)
plt.title('Convolution of x[n] with δ[n]')
plt.xlabel('n')
plt.ylabel('Convolution Result')
plt.show()
