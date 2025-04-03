"""Error analysis software for supersonic and hypersonic equations
Author: Taylor Hancock
Date:   03/31/2025
Class:  AE302 - Aerodynamics 2
Assignment: Project 02 - Error Analysis
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import aerodynamics_formulae as aero


# ------------ PARAMETERS ------------

NUM_STEPS = 5000

MACH_START = 1
MACH_END   = 15
MACH_STEP  = 1

BETA_START = 0
BETA_END   = 90
BETA_STEP  = 10

# ------------ GENERAL PLOTTING ------------

def plot_settings(ax: plt.Axes, table_name: str):
    """Initialize the provided plot"""
    ax.set_title(table_name)
    ax.set_xlabel(r"$M_1$")
    ax.set_ylabel(r"Shock-wave angle $\beta$, degrees")

    x_ticks = list(range(MACH_START, MACH_END + MACH_STEP, MACH_STEP))
    ax.set_xticks(x_ticks)
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))

    y_ticks = list(range(BETA_START, BETA_END + BETA_STEP, BETA_STEP))
    ax.set_yticks(y_ticks)
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))


def plot_absolute_error(ax: plt.Axes, name: str, error: np.meshgrid, mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the provided absolute error in the provided range"""
    plot = ax.pcolormesh(mach_grid, beta_grid, error)
    cbar = plt.colorbar(plot, ax=ax, label=r"$\epsilon$")

    cbar.set_ticks([])
    cbar.set_ticklabels([])

    plot_settings(ax, name)


def plot_relative_error(ax: plt.Axes, name: str, error: np.meshgrid, mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the provided relative error in the provided range"""

    # remove all values over 1.0
    error_clipped = np.ma.masked_greater(error, 1.0)

    plot = ax.pcolormesh(mach_grid, beta_grid, error_clipped, vmin=0, vmax=1)
    cbar = plt.colorbar(plot, ax=ax, label=r"$\epsilon_{ref}$")

    cbar_ticks = list([x / 10 for x in range(0, 11)])
    cbar.set_ticks(cbar_ticks)

    plot_settings(ax, name)


if __name__ == "__main__":
    # generate axes based on range values
    mach_range = np.linspace(MACH_START, MACH_END, NUM_STEPS) # mach number
    beta_range = np.linspace(BETA_START, BETA_END, NUM_STEPS) # in degrees

    mach_axis, beta_axis = np.meshgrid(mach_range, beta_range)

    # pressure
    relative_pressure_error = aero.calc_relative_error_pressure(mach_axis, beta_axis)
    absolute_pressure_error = aero.calc_absolute_error_pressure(mach_axis, beta_axis)

    # density
    relative_density_error = aero.calc_relative_error_density(mach_axis, beta_axis)
    absolute_density_error = aero.calc_absolute_error_density(mach_axis, beta_axis)

    # plot values
    fig, axs = plt.subplots(2, 2, figsize=(15, 15))

    plot_absolute_error(axs[0, 0], "Absolute Pressure Error", absolute_pressure_error, mach_axis, beta_axis)
    plot_absolute_error(axs[1, 0], "Absolute Density Error", absolute_density_error, mach_axis, beta_axis)
    plot_relative_error(axs[0, 1], "Relative Pressure Error", relative_pressure_error, mach_axis, beta_axis)
    plot_relative_error(axs[1, 1], "Relative Density Error", relative_density_error, mach_axis, beta_axis)

    plt.show()

    # plot_relative_error_intersection(mach_axis, beta_axis)
