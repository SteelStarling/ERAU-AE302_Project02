"""Helper functions for Project 02
Author: Taylor Hancock
Date:   03/31/2025
Class:  AE302 - Aerodynamics 2
Assignment: Project 02 - Error Analysis
"""

import numpy as np

# ------------ CONSTANTS ------------

GAMMA = 1.4

# ------------ AERODYNAMICS FORMULAE ------------

def calc_normal_mach(mach: float, beta: float) -> float:
    """Calculates a normal mach number for a given mach number and angle"""
    return mach * np.sin(np.deg2rad(beta))


def calc_supersonic_pressure(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates the supersonic pressure given a mach number and angle"""
    normal_mach_squared = pow(calc_normal_mach(mach, beta), 2)
    return 1 + ((2 * gamma) * (normal_mach_squared - 1) / (gamma + 1))


def calc_hypersonic_pressure(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates the supersonic pressure given a mach number and angle"""
    normal_mach_squared = pow(calc_normal_mach(mach, beta), 2)
    return (2 * gamma * normal_mach_squared) / (gamma + 1)


def calc_supersonic_density(mach: float, beta: float, gamma: float = GAMMA) -> float:
    """Calculates the supersonic density given a mach number and angle"""
    normal_mach_squared = pow(calc_normal_mach(mach, beta), 2)
    return ((gamma + 1) * normal_mach_squared) / (2 + (gamma - 1) * normal_mach_squared)


def calc_hypersonic_density(gamma: float = GAMMA) -> float:
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