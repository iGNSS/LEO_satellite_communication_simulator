import numpy as np
from EarthValues import mu
from math import pi
# from Simulator import Simulate
import backup_useless_model.Visualization as Viz
from Integrator import RK4
from Satellite import Model

BB = np.array([[0, 0, 0]], dtype=float).T
# varable for orbit calculation
# the percent of orbit calculation, 0.01 mean calculate 1% of orbit
# timestep is for the fineness of the orbit calculation, 0.001 mean calculate for per 10 Millisecond
timestep: float = 0.01
percent_of_orbits: float = 0.01

def velocity(circular_vel: float, orbit_inclination: float) -> float:
    # 0, y, z
    return np.array([[0, circular_vel * np.cos(orbit_inclination), circular_vel * np.sin(orbit_inclination)]], dtype=float).T

class Orbit:
    def __init__(self, position, orbit_inclination: float, attitude, omega):
        position = np.array(position, dtype=float).T
        semi_major: float = np.linalg.norm(position)
        circular_vel: float = np.sqrt(mu/semi_major)
        attitude = np.array(attitude, dtype=float).T
        omega = np.array(omega, dtype=float).T
        # the unit of period is seconds
        self.period: float = 2*pi/np.sqrt(mu)*semi_major**(3/2)

        self.state = np.vstack(([position, velocity(circular_vel, orbit_inclination), attitude, omega]))
        self.data, self.time = self.Simulate(self.state)

    def Simulate(self, state):
        tfinal: float = self.period * percent_of_orbits
        time = np.arange(0.0, tfinal, timestep, dtype=float)

        view_state = []
        for i in range(len(time)):
            # print the progess %
            print('Progress: \033' + ('%.2f' %  float(i/len(time)*100.0)) + '%')

            state = RK4(Model, state, time[i], timestep)
            view_state.append(state[:, 0])

            self.data = view_state
            self.time = time