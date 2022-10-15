import numpy as np
from EarthValues import R, mu
from math import pi

altitude: float = 600e3
position_0 = np.array([[R + altitude, 0, 0]], dtype=float).T
position_1 = np.array([[R + 700e3, 0, 0]], dtype=float).T

orbit_inclination: float = 54.24 * (pi/180)
semi_major: float = np.linalg.norm(position_0)
circular_vel: float = np.sqrt(mu/semi_major)
period: float = 2*pi/np.sqrt(mu)*semi_major**(3/2)

vel_y_0: float = circular_vel * np.cos(orbit_inclination)
vel_z_0: float = circular_vel * np.sin(orbit_inclination)
velocity_0 = np.array([[0, vel_y_0, vel_z_0]], dtype=float).T

attitude_0 = np.array([[1, 0, 0, 0]], dtype=float).T
omega_0 = np.array([[0.08, -0.02, 0.03]], dtype=float).T

BB = np.array([[0, 0, 0]], dtype=float).T

def semi_major(position: float):
    return np.linalg.norm(position)

def circular_vel(semi_major: float):
    return np.sqrt(mu/semi_major)

def period(semi_major: float):
    return 2*pi/np.sqrt(mu)*semi_major**(3/2)

def vel_y(circular_vel: float, orbit_inclination: float):
    return circular_vel * np.cos(orbit_inclination)

def vel_z(circular_vel: float, orbit_inclination: float):
    return circular_vel * np.sin(orbit_inclination)

def velocity(circular_vel: float, orbit_inclination: float):
    return np.array([[0, (circular_vel * np.cos(orbit_inclination)), (circular_vel * np.sin(orbit_inclination))]], dtype=float).T