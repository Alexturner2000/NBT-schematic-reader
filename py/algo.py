import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate a 4x4x4 3D array with random numbers
arr = np.random.rand(4, 4, 4)

# Plot the 3D array in a 3D image
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = np.indices((4, 4, 4))

ax.scatter(x, y, z, c=arr)

plt.show()
