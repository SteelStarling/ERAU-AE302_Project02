"""Error analysis software for supersonic and hypersonic equations
Author: Taylor Hancock
Date:   03/31/2025
Class:  AE302 - Aerodynamics 2
Assignment: Project 02 - Error Analysis
"""

import numpy as np
import matplotlib.pyplot as plt
import aerodynamics_formulae as aero


# ------------ PARAMETERS ------------

NUM_STEPS = 5000

MACH_RANGE = np.linspace(1, 15, NUM_STEPS) # mach number
BETA_RANGE = np.linspace(0, 90, NUM_STEPS) # in degrees


# ------------ GENERAL PLOTTING ------------

def init_plot(fig, ax, table_name: str):
    """Initialize the provided plot"""
    plt.title(table_name)
    plt.xlabel(r"$M_1$")
    plt.ylabel(r"Shock-wave angle $\beta$, degrees")


def plot_absolute_error(error: np.meshgrid, mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the provided absolute error in the provided range"""
    plt.pcolormesh(mach_grid, beta_grid, error)
    plt.colorbar()


def plot_relative_error(error: np.meshgrid, mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the provided relative error in the provided range"""
    plt.pcolormesh(mach_grid, beta_grid, error, vmin=0, vmax=1)
    plt.colorbar()


# ------------ PLOTTING ------------

def plot_absolute_error_pressure(mach_grid: np.meshgrid, beta_grid: np.meshgrid) -> None:
    """Plot absolute error in the pressure equations"""
    init_plot("Absolute Pressure Error")

    error_data = aero.calc_absolute_error_pressure(mach_grid, beta_grid)

    plot_absolute_error(error_data, mach_grid, beta_grid)


def plot_relative_error_pressure(mach_grid: np.meshgrid, beta_grid: np.meshgrid) -> None:
    """Plot the region where the relative error in pressure is less than 0.1"""
    init_plot("Relative Pressure Error")

    error_data = aero.calc_relative_error_pressure(mach_grid, beta_grid)

    plot_relative_error(error_data, mach_grid, beta_grid)


def plot_absolute_error_density(mach_grid: np.meshgrid, beta_grid: np.meshgrid) -> None:
    """Plot absolute error in the density equations"""
    init_plot("Absolute Density Error")

    error_data = aero.calc_absolute_error_density(mach_grid, beta_grid)

    plot_absolute_error(error_data, mach_grid, beta_grid)


def plot_relative_error_density(mach_grid: np.meshgrid, beta_grid: np.meshgrid) -> None:
    """Plot the region where the relative error in density is less than 0.1"""
    init_plot("Relative Density Error")

    error_data = aero.calc_relative_error_density(mach_grid, beta_grid)

    plot_relative_error(error_data, mach_grid, beta_grid)


def plot_relative_error_intersection() -> None:
    """Plot the region where the relative error of pressure and density are both < 0.1"""


if __name__ == "__main__":
    # generate axes based on range values

    mach_axis, beta_axis = np.meshgrid(MACH_RANGE, BETA_RANGE)

    # plot values
    plot_absolute_error_pressure(mach_axis, beta_axis)
    plot_absolute_error_density(mach_axis, beta_axis)

    plot_relative_error_pressure(mach_axis, beta_axis)
    plot_relative_error_density(mach_axis, beta_axis)

    plt.show()

    # plot_relative_error_intersection(mach_axis, beta_axis)
