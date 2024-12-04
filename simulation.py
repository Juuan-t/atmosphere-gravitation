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
tempChangeGradient = 0.0065 #0.01 #kelvin / meter
molarMass = 0.029 #molar mass of air
gasConstant = 8.314

#objects
class thing():
    def __init__(self, mass, radius, startingVelocity = zeroVector, startingPosition = zeroVector, startingAcceleration = zeroVector, cwValue = 1, frontalArea = 1):
        self.mass = mass
        self.radius = radius
        self.velocity = np.empty((steps, 2))
        self.position = np.empty((steps, 2))
        self.acceleration = np.empty((steps, 2))
        self.velocity[0] = startingVelocity
        self.position[0] = startingPosition
        self.acceleration[0] = startingAcceleration
        self.cwValue = cwValue
        self.frontalArea = frontalArea

#functions
def calcForce(objMass, objPos, planetMass, planetRadius):
    radius = np.sqrt(pow(objPos[0], 2) + pow(objPos[1], 2))
    force = -G * objMass * planetMass * objPos / pow(radius, 3)

    return force

def calcForceWithDrag(forceWithoutDrag, objVelocity, objCwValue, objFrontalArea, objPos, planetRadius):
    radius = np.sqrt(pow(objPos[0], 2) + pow(objPos[1], 2))
    distance = radius - planetRadius
    if(distance < 0 ):
        distance = 0
    
    airPressure = 101325 * pow(1 - (tempChangeGradient * distance) / 288.15, (9.81 * molarMass) / (gasConstant * tempChangeGradient))#barometric formula
    temperature = 288.15 - distance * tempChangeGradient
    airDensity = (airPressure * molarMass) / (gasConstant * temperature)
    drag_x = 0.5 * airDensity * pow(objVelocity[0], 2) * objCwValue * objFrontalArea
    drag_y = 0.5 * airDensity * pow(objVelocity[1], 2) * objCwValue * objFrontalArea

    force_x = forceWithoutDrag[0] - drag_x
    force_y = forceWithoutDrag[1] - drag_y

    forceWithDrag = np.array([force_x, force_y])
    
    return forceWithDrag

#initialisation
planetMass = 5.9722e24
planetRadius = 6378000

planet = thing(mass = planetMass, radius = planetRadius)

objMass = 1000
objStartVel = np.array([-760, 7600])
objStartpos = np.array([6400000, 0])
objCwValue = 0.8
objFrontalArea = 3

objForce = calcForce(objMass, objStartpos, planet.mass, planet.radius)
objStartaccel = objForce / objMass

objForce = calcForceWithDrag(objForce, objStartVel, objCwValue, objFrontalArea, objStartpos, planet.radius)
objStartaccel = objForce / objMass

obj = thing(mass = objMass, radius = 1, startingVelocity = objStartVel, startingPosition = objStartpos, startingAcceleration = objStartaccel, cwValue = objCwValue, frontalArea = objFrontalArea)


#loops for calculating data
for i in range(1, steps):
    pos = obj.position[i-1] + obj.velocity[i-1] * dt + 0.5 * obj.acceleration[i-1] * pow(dt, 2)
    radius = np.sqrt(pow(pos[0], 2) + pow(pos[1], 2))
    force = calcForce(obj.mass, pos, planet.mass, planet.radius)
    accel = force / obj.mass
    velocity = obj.velocity[i - 1] + dt * 0.5 * (accel + obj.acceleration[i - 1])
    force = calcForceWithDrag(force, velocity, obj.cwValue, obj.frontalArea, pos, planet.radius)
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