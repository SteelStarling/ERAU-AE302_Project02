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

NUM_STEPS = 2000

MACH_START = 1
MACH_END   = 15
MACH_STEP  = 1

BETA_START = 0
BETA_END   = 90
BETA_STEP  = 10

HIGHLIGHT_VALUE = 0.1

# ------------ GENERAL PLOTTING ------------

def fig_settings(fig: plt.figure, figure_name: str) -> None:
    """Initialize the provided figure"""
    fig.canvas.manager.set_window_title(figure_name)
    fig.suptitle(figure_name, fontsize=20)


def plot_settings(ax: plt.Axes, table_name: str) -> None:
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


def plot_absolute_error(ax: plt.Axes, name: str, error: np.meshgrid, \
                        mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the provided absolute error in the provided range"""
    plot = ax.pcolormesh(mach_grid, beta_grid, error)
    cbar = plt.colorbar(plot, ax=ax, label=r"$\epsilon$")

    cbar.set_ticks([])
    cbar.set_ticklabels([])

    plot_settings(ax, name)


def plot_relative_error(ax: plt.Axes, name: str, error: np.meshgrid, \
                        mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the provided relative error in the provided range"""

    # remove all values over 1.0
    error_clipped = np.ma.masked_greater(error, 1.0)

    # plot it
    plot = ax.pcolormesh(mach_grid, beta_grid, error_clipped, vmin=0, vmax=1)
    cbar = plt.colorbar(plot, ax=ax, label=r"$\epsilon_{rel}$")

    # fix settings
    cbar_ticks = [x / 10 for x in range(0, 11)]
    cbar.set_ticks(cbar_ticks)

    plot_settings(ax, name)

    # highlight region
    ax.contourf(mach_grid, beta_grid, error_clipped, [0, HIGHLIGHT_VALUE], \
                colors='red', alpha=0.3)

    # draw contour over highlighted region boundary
    ax.contour(mach_grid, beta_grid, error_clipped, [HIGHLIGHT_VALUE], colors='red', alpha=1)


def plot_intersection(ax: plt.Axes, pressure_region: np.meshgrid, density_region: np.meshgrid, \
                      mach_grid: np.linspace, beta_grid: np.linspace) -> None:
    """Plots the intersection region where both regions are less than HIGHLIGHT_VALUE"""

    plot_settings(ax, f"Intersection where Pressure & Density $\\epsilon_{{rel}} \\leq$ {HIGHLIGHT_VALUE}")

    # highlight region (pressure)
    ax.contourf(mach_grid, beta_grid, pressure_region, [0, HIGHLIGHT_VALUE], \
                colors='red', alpha=0.3)

    # draw contour over highlighted region boundary
    ax.contour(mach_grid, beta_grid, pressure_region, [HIGHLIGHT_VALUE], colors='red', alpha=1)

    # highlight region (density)
    ax.contourf(mach_grid, beta_grid, density_region, [0, HIGHLIGHT_VALUE], \
                colors='blue', alpha=0.3)

    # draw contour over highlighted region boundary
    ax.contour(mach_grid, beta_grid, density_region, [HIGHLIGHT_VALUE], colors='blue', alpha=1)


if __name__ == "__main__":
    # generate axes based on range values
    mach_range = np.linspace(MACH_START, MACH_END, NUM_STEPS) # mach number
    beta_range = np.linspace(BETA_START, BETA_END, NUM_STEPS) # in degrees

    mach_axis, beta_axis = np.meshgrid(mach_range, beta_range)

    # pressure
    relative_pressure_error = aero.calc_relative_error_pressure(mach_axis, beta_axis)
    absolute_pressure_error = aero.calc_absolute_error_pressure(mach_axis, beta_axis)

    pressure_highlights = np.ma.masked_where(relative_pressure_error > HIGHLIGHT_VALUE, \
                                             np.ones_like(relative_pressure_error))

    # density
    relative_density_error = aero.calc_relative_error_density(mach_axis, beta_axis)
    absolute_density_error = aero.calc_absolute_error_density(mach_axis, beta_axis)

    density_highlights = np.ma.masked_where(relative_density_error > HIGHLIGHT_VALUE, \
                                            np.ones_like(relative_density_error))

    # plot values
    fig_pressure,     axs_pressure     = plt.subplots(ncols=2, figsize=(15, 6))
    fig_density,      axs_density      = plt.subplots(ncols=2, figsize=(15, 6))
    fig_intersection, axs_intersection = plt.subplots(figsize=(6, 6))

    fig_settings(fig_pressure, "Pressure Error")
    plot_absolute_error(axs_pressure[0], "Absolute Pressure Error", \
                        absolute_pressure_error, mach_axis, beta_axis)
    plot_relative_error(axs_pressure[1], "Relative Pressure Error", \
                        relative_pressure_error, mach_axis, beta_axis)

    fig_settings(fig_density, "Density Error")
    plot_absolute_error(axs_density[0],  "Absolute Density Error", \
                        absolute_density_error, mach_axis, beta_axis)
    plot_relative_error(axs_density[1], "Relative Density Error", \
                        relative_density_error, mach_axis, beta_axis)

    fig_settings(fig_intersection, "Error Intersection")
    plot_intersection(axs_intersection, relative_pressure_error, \
                      relative_density_error, mach_axis, beta_axis)

    plt.show()

    # plot_relative_error_intersection(mach_axis, beta_axis)
