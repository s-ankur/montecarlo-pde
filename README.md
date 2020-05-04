# montecarlo-pde
The Poisson Equation, and its special case, the
Laplace Equation, are important partial differential equations
within electrostatics, as they describe the electric potential field
caused by a particular charge distribution. Solving the Poisson
equation for a given set of boundary conditions is a fundamental
problem within the field. This report describes an algorithm for a
Monte Carlo Method solution to the Poisson and Laplace
equations. Monte Carlo Method is a parallelizable non-
deterministic numerical approach towards solving this problem.
A Python implementation is also provided for three versions of the
Monte Carlo Method: Fixed Step, Semi-Floating and Full
Floating. Several examples including the one-dimensional and
two-dimensional parallel plate capacitors are performed to
illustrate the function of the implementation.


Keywords: Poisson Equation, Laplace Equation, Monte Carlo
Methods, Electrostatics, Parallel Plate Capacitor, Python
Implementation


A. One dimentional capacitor (Laplace Equation)
<p float="left">
  <img src="Figures/A1.png"/>
   <img src="Figures/A2.png"/>
</p>

B. Variation of solution with number of random walks
(Laplace Equation)
<p float="left">
  <img src="Figures/B1.gif" width="50%" />
  <img src="Figures/B2.png" width="50%" /> 
</p>

C. Variation of solution with number of lattice points
(Laplace Equation)
<p float="left">
  <img src="Figures/C1.gif" width="50%" />
  <img src="Figures/C2.png" width="50%" /> 
</p>

D.One dimensional capacitor with a linear charge
distribution (Poisson Equation)
<p float="left">
  <img src="Figures/D1.png"  />
</p>

E. Two dimentional capacitor (Laplace Equation)
<p float="left">
  <img src="Figures/E1.png" width="50%" />
  <img src="Figures/E2.png" width="50%" /> 
</p>
<p float="left">
  <img src="Figures/E4.png" width="50%" />
  <img src="Figures/E5.png" width="50%" /> 
</p>

F.Two dimentional metal box with a spherical charge in
centre (Poisson Equation)
<p float="left">
  <img src="Figures/F1.png" width="33%" />
  <img src="Figures/F2.png" width="33%" /> 
  <img src="Figures/F2.png" width="33%" /> 
</p>

G. Two dimentional metal box with a two oppositely charged
spheres (Poisson Equation)
<p float="left">
  <img src="Figures/G1.png" width="50%" />
  <img src="Figures/G2.png" width="50%" /> 
</p>
<p float="left">
  <img src="Figures/G4.png" width="50%" />
  <img src="Figures/G5.png" width="50%" /> 
</p>

H.Two dimentional metal box with a spherical charge at
center using semi-floating random walk algorithm
(Poisson Equation)

<p float="left">
  <img src="Figures/H1.png" width="50%" />
  <img src="Figures/H2.png" width="50%" /> 
</p>

I. Two dimentional metal box with a spherical charge at
center using full floating random walk algorithm (Poisson
Equation)
<p float="left">
  <img src="Figures/I1.png" />
</p>
