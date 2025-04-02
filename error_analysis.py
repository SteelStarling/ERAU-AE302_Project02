"""Error analysis software for supersonic and hypersonic equations
Author: Taylor Hancock
Date:   03/31/2025
Class:  AE302 - Aerodynamics 2
Assignment: Project 02 - Error Analysis
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ------------ CONSTANTS & PARAMETERS ------------

NUM_STEPS = 5000

MACH_RANGE = (1, 15) # mach number
BETA_RANGE = (0, 90) # in degrees

GAMMA = 1.4


# ------------ AERODYNAMICS FORMULAE ------------

def calc_normal_mach(mach: float, beta: float) -> float:
    """Calculates a normal mach number for a given mach number and angle"""
    return mach * np.sin(np.deg2rad(beta))


def calc_supersonic_pressure(mach: float, beta: float, gamma: float = 1.4) -> float:
    """Calculates the supersonic pressure given a mach number and angle"""
    normal_mach_squared = pow(calc_normal_mach(mach, beta), 2)
    return 1 + ((2 * gamma) * (normal_mach_squared - 1) / (gamma + 1))


def calc_hypersonic_pressure(mach: float, beta: float, gamma: float = 1.4) -> float:
    """Calculates the supersonic pressure given a mach number and angle"""
    normal_mach_squared = pow(calc_normal_mach(mach, beta), 2)
    return (2 * gamma * normal_mach_squared) / (gamma + 1)


def calc_supersonic_density(mach: float, beta: float, gamma: float = 1.4) -> float:
    """Calculates the supersonic density given a mach number and angle"""
    normal_mach_squared = pow(calc_normal_mach(mach, beta), 2)
    return ((gamma + 1) * normal_mach_squared) / (2 + (gamma - 1) * normal_mach_squared)


def calc_hypersonic_density(gamma: float = 1.4) -> float:
    """Calculates the supersonic density"""
    return (gamma + 1) / (gamma - 1)


# ------------ ERROR CALCULATIONS ------------

def calc_absolute_error(actual: float, expected: float) -> float:
    """Calculates the absolute error between actual and expected values"""
    return abs(actual - expected)


def calc_relative_error(actual: float, expected: float) -> float:
    """Calculates the relative error between actual and expected values"""
    return abs(actual - expected) / expected


# ------------ COMBINED CALCULATIONS ------------

def calc_absolute_error_pressure(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates absolute error in the pressure equations"""
    supersonic = calc_supersonic_pressure(mach, beta, gamma)
    hypersonic = calc_hypersonic_pressure(mach, beta, gamma)

    return calc_absolute_error(supersonic, hypersonic)


def calc_relative_error_pressure(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates the region where the relative error in pressure is less than 0.1"""
    supersonic = calc_supersonic_pressure(mach, beta, gamma)
    hypersonic = calc_hypersonic_pressure(mach, beta, gamma)

    return calc_relative_error(supersonic, hypersonic)
    

def calc_absolute_error_density(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates absolute error in the density equations"""
    supersonic = calc_supersonic_density(mach, beta, gamma)
    hypersonic = calc_hypersonic_density(gamma)

    return calc_absolute_error(supersonic, hypersonic)
    

def calc_relative_error_density(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates the region where the relative error in density is less than 0.1"""
    supersonic = calc_supersonic_density(mach, beta, gamma)
    hypersonic = calc_hypersonic_density(gamma)

    return calc_relative_error(supersonic, hypersonic)


# ------------ GENERAL PLOTTING ------------

def plot_absolute_error(error_data: np.ndarray, x_range: np.linspace, y_range: np.linspace) -> None:
    """Plots the provided absolute error in the provided range"""


def plot_relative_error(error_data: np.ndarray, x_range: np.linspace, y_range: np.linspace) -> None:
    """Plots the provided relative error in the provided range"""
    

# ------------ COMBINED EQUATIONS ------------

def plot_absolute_error_pressure(mach_axis, beta_axis, gamma: float = GAMMA) -> None:
    """Plot absolute error in the pressure equations"""
    error_data = calc_absolute_error_pressure(mach_axis[:, None], beta_axis[None, :], gamma)

    print(error_data)

def plot_relative_error_pressure(mach_axis, beta_axis, gamma: float = GAMMA) -> None:
    """Plot the region where the relative error in pressure is less than 0.1"""
    error_data = calc_relative_error_pressure(mach_axis[:, None], beta_axis[None, :], gamma)

    print(error_data)

def plot_absolute_error_density(mach_axis, beta_axis, gamma: float = GAMMA) -> None:
    """Plot absolute error in the density equations"""
    error_data = calc_absolute_error_density(mach_axis[:, None], beta_axis[None, :], gamma)

    print(error_data)

def plot_relative_error_density(mach_axis, beta_axis, gamma: float = GAMMA) -> None:
    """Plot the region where the relative error in density is less than 0.1"""
    error_data = calc_relative_error_density(mach_axis[:, None], beta_axis[None, :], gamma)

    print(error_data)


def plot_relative_error_intersection() -> None:
    """Plot the region where the relative error of pressure and density are both < 0.1"""
    

if __name__ == "__main__":
    # generate axes based on range values
    mach_axis = np.linspace(MACH_RANGE[0], MACH_RANGE[1], NUM_STEPS)
    beta_axis = np.linspace(BETA_RANGE[0], BETA_RANGE[1], NUM_STEPS)

    mach_grid, beta_grid = np.meshgrid(mach_axis, beta_axis)

    error_data = calc_absolute_error_pressure(mach_grid, beta_grid)

    plt.pcolormesh(mach_grid, beta_grid, error_data)

    plt.show()

    # plot values
    #plot_absolute_error_pressure(mach_axis, beta_axis)
    #plot_absolute_error_density(mach_axis, beta_axis)

    #plot_relative_error_pressure(mach_axis, beta_axis)
    #plot_relative_error_density(mach_axis, beta_axis)

    #plot_relative_error_intersection(mach_axis, beta_axis)
