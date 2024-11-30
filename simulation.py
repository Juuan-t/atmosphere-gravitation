import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# constants
steps = 500
dt = 0.1
time_max = dt * steps
zeroVector = np.array([0, 0])

G = 6.674e-11

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

planet = thing(mass = 5.9722e24, radius = 6378000, startingVelocity = zeroVector, startingPosition = zeroVector, startingAcceleration = zeroVector)

mass = 1000
startpos = np.array([6400000, 0])
radius = np.sqrt(pow(startpos[0], 2) + pow(startpos[1], 2))
force = -G * mass * planet.mass * startpos / pow(radius, 3)
startaccel = force / mass

obj = thing(mass = mass, radius = 1, startingVelocity = np.array([-760, 7600]), startingPosition = startpos, startingAcceleration = startaccel)

for i in range(1, steps):
    pos = obj.position[i-1] + obj.velocity[i-1] * dt + 0.5 * obj.acceleration[i-1] * pow(dt, 2)
    radius = np.sqrt(pow(pos[0], 2) + pow(pos[1], 2))
    force = -G * obj.mass * planet.mass * pos / pow(radius, 3)
    accel = force / obj.mass
    velocity = obj.velocity[i - 1] + dt * 0.5 * (accel + obj.acceleration[i - 1])

    if(radius <= planet.radius):
        obj.position[i] = obj.position[i - 1]
        obj.acceleration[i] = obj.acceleration[i - 1]
        obj.velocity[i] = obj.velocity[i - 1]
    else:
        obj.position[i] = pos
        obj.acceleration[i] = accel
        obj.velocity[i] = velocity

x_vals = []
y_vals = []
for i in range(len(obj.position)):
    x_vals.append(obj.position[i][0])
    y_vals.append(obj.position[i][1])

#animation
fig, ax = plt.subplots()
line = ax.plot(x_vals, y_vals)[0]
line.set_color("orange")

ax.add_patch(Circle([0, 0], planet.radius))
ax.set_xlim(-obj.position[0][0] - 50000, obj.position[0][0] + 50000)
ax.set_ylim(-obj.position[0][0] - 50000, obj.position[0][0] + 50000)
ax.set_aspect("equal")

def animate(frame):
    line.set_xdata(x_vals[:frame])
    line.set_ydata(y_vals[:frame])

animation = FuncAnimation(fig = fig, func = animate, frames = len(obj.position), interval = 1)
plt.show()