import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def psi_0(x):
    return np.where(x <= 0, 0, np.exp(-1/x))

def psi_2(x, y):
    norm_squared = x**2 + y**2
    return psi_0(1 - norm_squared)

x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
x, y = np.meshgrid(x, y)

z = psi_2(x, y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel(r'$x_0$')
ax.set_ylabel(r'$x_1$')
ax.set_zlabel(r'$\psi_2((x_0,x_1))$')
ax.set_title(r'$ \psi_2(x) = \psi_0(1 - \|\|x\|\|^2) $')

plt.show()
