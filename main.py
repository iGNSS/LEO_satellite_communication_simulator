import numpy as np
import Visualization as Viz
from Simulator import Simulate
from Orbit import *
from Instrument import probe

print("Start of Simulation")

# list store orbit position etc
orbit_list = []
# data store a list of dictionary of orbit data and time
orbit_data = []


state = np.vstack(([position_0, velocity_0, attitude_0, omega_0])) # , [position_1, velocity_0, attitude_0, omega_0]
# 3+3+4+3 for position, velocity, attitude, and omega
# position: x(altitude), y, z (position cartesian)
# velocity: 0, y-axis , z-axis positive northward coincident with Earth's rotational axis
# attitude: quaternion https://www.youtube.com/watch?v=LK4z7hMyFcM&list=PL_D7_GvGz-v3mDQ9iR-cfjXsQf4DeR1_H&index=10
# omega: angular_speed, The dimensional formula of angular velocity is [M0 L0 T-1]

# the partition of orbit calculation, 0.1 mean calculate 10% of orbit
number_of_orbits: float = 0.1
# status is the function to print progress %
# output of data is 13 value state + delta_state (to-do: understand what is going on)
data, time = Simulate(number_of_orbits, state, status=Viz.status, timestep=5)   # timestep is for the fineness of the orbit calculation

# idea, may bug, without testing
for i in range(len(orbit_list)):
    data, time = Simulate(number_of_orbits, orbit_list[i], status=Viz.status, timestep=1)   # timestep is for the fineness of the orbit calculation
    orbit_data[i] = {
        data: data,
        time: time
    }

print("End of Simulation")

data = np.array(data)
# data = np.concatenate((data, probe.get()), axis=1)

np.savetxt("simulation.csv", data, delimiter=',')

Viz.View(data, time)
