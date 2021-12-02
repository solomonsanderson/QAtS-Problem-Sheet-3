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

def integrand(x):
    (x ** 4 * np.exp(x)) / ((np.exp(x) - 1) ** 2)


def debye_heat_capacity(Theta_D, T):
    '''
    Finds the Debye heat capacity

    Parameters:

    - Theta_D: float, Debye Temperature
    - T: array

    Returns:
    
    - C_v: float, Debye heat capacity
    '''


    integral = integrate.quad(integrand(x), 0, Theta_D / T)
    C_v = 9 * N * k_B * (T / Theta_D) ** 3
    
    return C_v