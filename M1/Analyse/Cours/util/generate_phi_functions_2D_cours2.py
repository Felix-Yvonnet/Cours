import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def psi_0(x):
    return np.exp(-1/x) if x > 0 else 0

def integrand(t):
    return psi_0(t) * psi_0(1 - t)

def psi_1(x):
    result, _ = quad(integrand, 0, x)
    return result

def normalized_psi_1(x):
    result = psi_1(x)
    div = psi_1(1)
    return result / div

def psi_2(x):
    return psi_0(1 - np.abs(x)**2)

x_values = np.linspace(-2, 2, 400)
x2_values = np.linspace(-1.5, 2.5, 400)
x3_values = np.linspace(-0.5, 1.5, 400)

psi_0_values = np.array([psi_0(x) for x in x2_values])
psi_1_values = np.array([normalized_psi_1(x) for x in x3_values])
psi_2_values = np.array([10*psi_2(x) for x in x_values])


fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].plot(x2_values, psi_0_values, label=r'$\psi_0(x)$', color='blue')
axs[0].set_title(r'Graphe de $\psi_0(x)$')
axs[0].set_xlabel(r'$x$')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x3_values, psi_1_values, label=r'$H(x)$', color='green')
axs[1].set_title(r'Graphe de $H(x)=\frac{\psi_1(x)}{\psi_1(0)}$')
axs[1].set_xlabel(r'$x$')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(x_values, psi_2_values, label=r'$\psi_2\prime(x)$', color='red')
axs[2].set_title(r'Graphe de $\psi_2\prime(x)=10\cdot\psi_0(1-\|x\|²)$')
axs[2].set_xlabel(r'$x$')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
