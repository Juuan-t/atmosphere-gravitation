<h1>Simulation of Gravitation in an atmosphere</h1>

<h2>Parameters</h2>
Parameters are entered under the initialisation and include the number of steps calculated, the delta of time inbetween each step, the planets mass and radius as well as the objects mass, starting velocity, starting position, cw value and frontal area.

<h2>Step calculation</h2>
Each individual step is calculated using verlet integration.

<h2>Calculating pressure, temperature and density</h2>
The air pressure is calcualted using the barometric formula:
![grafik](https://github.com/user-attachments/assets/450de190-96fc-4a31-a88b-8c4b388beab4)


The temperature can then be approximated using the following formula:
![grafik](https://github.com/user-attachments/assets/51fbabe4-58cc-4f18-8f30-8cb34b5365d3)

Finally, the density follows out of the calculated pressure and temperature using the general gas equation:
![grafik](https://github.com/user-attachments/assets/e34ab061-8798-4a45-9b2a-c89af511ed7b)


<h2>Animating and displaying the simulation</h2>
After calculating the relevant data for every step, said data is visualized using matplotlib. The planet is visualized as a green circular patch with the atmosphere displayed as a blue gradient around it.
To calculate the relevant values for the gradient, the air density as calculated at different distances from the planet from the height of the relevant object down to the surface of the planet in set steps. The size of the steps can be adjusted by adjusting the step value of the loop. Once the densities are calcualted each distance and density pair gets visualized as a new blue circular patch with an opacity based on the density value in comparison the maximal density calculated.
Lastly, the data gets animated via the animate() function and put in a plot.

<h2>image sources</h2>
https://en.wikipedia.org/wiki/Density_of_air
