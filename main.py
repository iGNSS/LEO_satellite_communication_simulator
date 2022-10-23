import numpy as np
import Visualization as Viz
from Simulator import Simulate
from Orbit import *
from Instrument import probe

print("Start of Simulation")

state = np.vstack(([position_0, velocity_0, attitude_0, omega_0])) # , [position_1, velocity_0, attitude_0, omega_0]
test = np.vstack(([position_1, velocity_0, attitude_0, omega_0]))   # 3+3+4+3 for position, velocity, attitude, and omega
combine = np.vstack((state, test))
number_of_orbits: float = 0.1
# status is the function to print progress %
data, time = Simulate(number_of_orbits, state, status=Viz.status, timestep=5)   # timestep is for the fineness of the orbit calculation

print("End of Simulation")

data = np.array(data)
data = np.concatenate((data, probe.get()), axis=1)

np.savetxt("simulation.csv", data, delimiter=',')

Viz.View(data, time)
