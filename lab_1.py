import numpy as np
import matplotlib.pyplot as plt

# Define parameters
A = 1.0 # Amplitude
omega = 2 * np.pi / 10 # Frequency (in this case, 10 points per cycle)
phi = np.pi / 2 # Phase shift

# Generate X-axis values
X = np.linspace(0, 10, 100) # 100 points from 0 to 10

# Calculate Y-axis values using the formula
Y = A * np.sin(omega * X + phi)

# Plot the phase pattern
plt.plot(X, Y)
plt.title('Phase Pattern')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()