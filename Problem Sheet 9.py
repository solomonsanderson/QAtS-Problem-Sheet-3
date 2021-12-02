'''
This is my solution for problem sheet 9 of my Quantum Approach to Solids module

The aim of this task is to calculate the deby heat capacity for a monatomic
solid in the range of 0 K to 300 K with Debye temperatures of 50 K and 750 K
'''

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from scipy import constants

# Defining Constants
k_B = constants.Boltzmann
N = 1

def integrand(x):
    ''' 
    Parameters: 
    
    - x: int, value to be integrated

    Returns: 

    - 

    '''
    integral = (x ** 4 * np.exp(x)) / ((np.exp(x) - 1) ** 2)
    return integral


def debye_heat_capacity(Theta_D, T):
    '''
    Finds the Debye heat capacity

    Parameters:

    - Theta_D: float, Debye Temperature
    - T: array

    Returns:
    
    - C_vs: array, Debye heat capacity values
    '''
    C_vs = []
    for t in T:
        integral, error = integrate.quad(integrand, 0, Theta_D / t)

        C_v = 9 * N * k_B * (t / Theta_D) ** 3 * integral
        C_vs.append(C_v)

    C_vs = np.array(C_vs)

    return C_vs

temps = np.linspace(0.1, 300, 1000)
debye_temperature1 = 50
C_v1 = debye_heat_capacity(debye_temperature1, temps)
debye_temperature2 = 750
C_v2 = debye_heat_capacity(debye_temperature2, temps)

# Plotting Graph
fig, ax = plt.subplots(1,1, figsize = (12,9))
ax.plot(temps, C_v1, label="$\Theta_D = 50$ K")
ax.plot(temps, C_v2, label="$\Theta_D = 750$ K")
ax.plot(temps, np.ones(1000) * 3 * N * k_B, label="Dulong Petit Heat Capacity", linestyle="--")
ax.set_title("Plot of Debye Heat Capacity vs. Temperature")
ax.set_xlabel(" Temperature (K)")
ax.set_ylabel("Debye Heat Capacity (JK$^{-1}$)")
ax.legend()

# Extension
temps_ext = np.linspace(0.1, 50, 500)
C_v1 = debye_heat_capacity(debye_temperature1, temps_ext)
C_v2 = debye_heat_capacity(debye_temperature2, temps_ext)


fig2, ax2 = plt.subplots(1,1, figsize = (12,9))
ax2.plot(temps_ext ** 2, C_v1/temps_ext, label="$\Theta_D = 50$ K")
ax2.plot(temps_ext ** 2, C_v2/temps_ext, label="$\Theta_D = 750$ K")
ax2.set_title("Plot of $\\frac{C}{T}$ vs. T$^{2}$")
ax2.set_xlabel(" T$^{2}$ (K$^{2}$)")
ax2.set_ylabel("C / T (J K$^{-2})$ ")
ax2.legend()

plt.show()
