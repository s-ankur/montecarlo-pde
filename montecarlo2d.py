"""
All calculations in SI units
"""
import random
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

h=10e-2 # Distance between plates = 10cm
lattice_points = 15 # Number of Points in lattice
d=h/lattice_points  # Lattice size = 1cm
laplace = True # False-> Poisson, True-> Laplace
boundary_voltage_high = 5.0 # 5 Volts at Positive Plate
boundary_voltage_low = 0.0  # 0 Volts at Negative Plate
epsilon_naught = 8.854e-12  # Permittivity of Vaccum
charge_density = 6e-16 # Coulomb per meter cube
N = 500 # Number of Random Walks

# The Function \nabla^2(phi)  = f
def f(x):
    if laplace:
        # For Laplace f = 0
        return 0
    else:
        # For Poisson, assume that there is a constant charge density
        # between the plates
        # So f=rho/epsilon
        return charge_density/epsilon_naught 

# Two Dimentional Boundary Conditions
def g(x):
    if x[0]<=0:
        return boundary_voltage_low
    if x[0]>=h:
        return boundary_voltage_high
    if x[1]<=0 or x[1]>=h:
        return boundary_voltage_low

# Returns the Value of Potential Feild at a given point A with N random walks
@np.vectorize
def poisson_approximation(*A):
    result =0
    for i in range(N):
        x=list(A)
        F=0
        while True:
            if x[0]<=0 or x[0]>=h or x[1]<=0 or x[1]>=h:
                break
            random_number = random.randint(0,3)
            if random_number == 0:
                x[0]+=d
            elif random_number == 1:
                x[0]-=d
            elif random_number == 2:
                x[1]+=d
            elif random_number == 3:
                x[1]-=d
            F+=f(x)/h**2
        result+=g(x)-F
    result=result/N
    return result

# Function for plotting the potential
def plot(x, y,z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x,y, np.array(z),cmap=cm.jet, linewidth=0.1)
    plt.xlabel('(Meters)')
    plt.ylabel('(Meters)')
    plt.show()


if __name__=="__main__":
    for laplace in True, False:
        print(f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for {'Laplace' if laplace else 'Poisson'}")
        lattice_x,lattice_y = np.mgrid[0:h:lattice_points*1j,0:h:lattice_points*1j]
        z=poisson_approximation(lattice_x.ravel(),lattice_y.ravel()).reshape(lattice_x.shape)
        plot(lattice_x,lattice_y,z)
        
