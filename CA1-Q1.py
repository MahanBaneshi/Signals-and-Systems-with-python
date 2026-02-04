import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-4, 5)
x = np.array([-3, 4, 3, 1, 5, -3, 2, -1, 2])

# even part of our signal
x_even = (x + x[::-1]) / 2

# odd part of our signal
x_odd = (x - x[::-1]) / 2

# create original signal
plt.subplot(3, 1, 1)
plt.stem(n, x) 
plt.title('Original Signal')
plt.xlabel('n')
plt.ylabel('x[n]')

# create even signal
plt.subplot(3, 1, 2)
plt.stem(n, x_even)  
plt.title('Even Part')
plt.xlabel('n')
plt.ylabel('x_{even}[n]')

# create odd signal
plt.subplot(3, 1, 3)
plt.stem(n, x_odd) 
plt.title('Odd Part')
plt.xlabel('n')
plt.ylabel('x_{odd}[n]')

plt.tight_layout()
plt.show()
