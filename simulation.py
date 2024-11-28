import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# constants
steps = 10000
dt = 0.01
time_max = dt * steps

G = 1.0

#objects
class thing():
    def __init__(self, mass, radius, startingVelocity, startingPosition, startingAcceleration):
        self.mass = mass
        self.radius = radius
        self.velocity = np.empty((steps, 2))
        self.position = np.empty((steps, 2))
        self.acceleration = np.empty((steps, 2))
        self.velocity[0] = startingVelocity
        self.position[0] = startingPosition
        self.acceleration[0] = startingAcceleration

planet = thing(mass = 10, radius = 10, startingVelocity = np.array([0, 0]), startingPosition = np.array([0, 0]), startingAcceleration = np.array([0, 0]))
obj = thing(mass = 1, radius = 1, startingVelocity = np.array([0, -20]), startingPosition = np.array([20, 0]), startingAcceleration = np.array([0, 1]))

for i in range(1, steps):
    pos = obj.position[i-1] + obj.velocity[i-1] * dt + 0.5 * obj.acceleration[i-1] * pow(dt, 2)
    force = G * (obj.mass * planet.mass) / np.sqrt(pow(pos[0], 2) + pow(pos[1], 2))
    accel = force / obj.mass
    velocity = obj.velocity[i - 1] + dt * 0.5 * (accel + obj.acceleration[i - 1])

    obj.position[i] = pos
    obj.acceleration[i] = accel
    obj.velocity[i] = velocity

x_vals = []
y_vals = []
for i in range(steps):
    x_vals.append(obj.position[i][0])
    y_vals.append(obj.position[i][1])

#animation
fig, ax = plt.subplots()
line = ax.plot(x_vals, y_vals)[0]

ax.add_patch(Circle([0, 0], planet.radius))
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

def animate(frame):
    line.set_xdata(x_vals[:frame])
    line.set_ydata(y_vals[:frame])

animation = FuncAnimation(fig = fig, func = animate, frames = steps, interval = 1)
plt.show()