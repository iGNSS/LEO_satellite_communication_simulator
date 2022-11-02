import numpy as np
import backup_useless_model.Visualization as Viz
from Orbit import Orbit
# from Instrument import probe
from EarthValues import R
from math import pi

print("Start of Simulation")

# list store orbit position etc
orbit_list = []
orbit_list.append(Orbit(position = [[R + 600e3, 0, 0]], orbit_inclination = 54.24*(pi/180), attitude = [[1, 0, 0, 0]], omega = [[0.08, -0.02, 0.03]]))
# 3+3+4+3 for position, velocity, attitude, and omega
# position: x(altitude), y, z (position cartesian)
# velocity: 0, y-axis , z-axis positive northward coincident with Earth's rotational axis
# attitude: quaternion https://www.youtube.com/watch?v=LK4z7hMyFcM&list=PL_D7_GvGz-v3mDQ9iR-cfjXsQf4DeR1_H&index=10
# omega: angular_speed, The dimensional formula of angular velocity is [M0 L0 T-1]

# the partition of orbit calculation, 0.1 mean calculate 10% of orbit
# number_of_orbits: float = 0.1
# status is the function to print progress %
# output of data is 13 value state + delta_state (to-do: understand what is going on)
# data, time = Simulate(number_of_orbits, state, status=Viz.status, timestep=5)   # timestep is for the fineness of the orbit calculation

print("End of Simulation")

data = np.array(orbit_list[0].data)
print(np.array(orbit_list[0].time))
# data = np.concatenate((data, probe.get()), axis=1)

np.savetxt("simulation.csv", data, delimiter=',')

# Viz.View(data, orbit_list[0].time)
