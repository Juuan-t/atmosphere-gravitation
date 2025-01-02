<h1>Simulation of Gravitation in an atmosphere</h1>

<h2>Parameters</h2>
Parameters are entered under the initialisation and include the number of steps calculated, the delta of time inbetween each step, the planets mass and radius as well as the objects mass, starting velocity, starting position, cw value and frontal area. If the planets values are set to mimic earth, in order to ensure accurate data, the object should not be farther than 18km away from the planet, as the calculated temperatures are most accurate within the troposphere.

<h2>Step calculation</h2>
Each individual step is calculated using verlet integration.

<h2>Calculating pressure, temperature and density</h2>
The air pressure is calcualted using the barometric formula:<br/>

$p = p_0 * (1 - \frac{L * h}{T_0})^\frac{g * M}{R * L}$

<br/>

The temperature can then be approximated using the following formula:<br/>
$T = T_0 - L * h$

<br/>

Finally, the density follows out of the calculated pressure and temperature using the general gas equation:<br/>
$\rho = \frac{p * M}{R * T}$

with<br/>
$p_0 = sea\ level\ standard\ atmospheric\ pressure$<br/>
$L = temperature\ lapse\ rate$<br/>
$h = height$<br/>
$T_0 = sea\ level\ standard\ temperature$<br/>
$g = gravitational\ acceleration$<br/>
$M = molar\ mass\ of\ air$<br/>
$R = ideal\ gas\ constant$<br/>

<h2>Animating and displaying the simulation</h2>
After calculating the relevant data for every step, said data is visualized using matplotlib. The planet is visualized as a green circular patch with the atmosphere displayed as a blue gradient around it.<br/>
To calculate the relevant values for the gradient, the air density as calculated at different distances from the planet from the height of the relevant object down to the surface of the planet in set steps. The size of the steps can be adjusted by adjusting the step value of the loop. Once the densities are calcualted each distance and density pair gets visualized as a new blue circular patch with an opacity based on the density value in comparison the maximal density calculated.
Lastly, the data gets animated via the animate() function and put in a plot.

<h2>formula sources</h2>
https://en.wikipedia.org/wiki/Density_of_air
