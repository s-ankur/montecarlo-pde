"""
All calculations in SI units
"""
import random
import matplotlib.pyplot as plt
import gif
import numpy as np

h = 10e-2  # Distance between plates = 10cm
lattice_points = 15  # Number of Points in lattice
d = h / lattice_points  # Lattice size = 1cm
laplace = False  # False-> Poisson, True-> Laplace
boundary_voltage_high = 5.0  # 5 Volts at Positive Plate
boundary_voltage_low = 0.0  # 0 Volts at Negative Plate
epsilon_naught = 8.854e-12  # Permittivity of Vaccum
charge_density = 2e-15  # Coulomb per meter cube
N = 500  # Number of Random Walks

# The Function \nabla^2(phi)  = f


def f(x):
    if laplace:
        # For Laplace f = 0
        return 0
    else:
        # For Poisson, assume that there is a constant charge density
        # between the plates
        # So f=rho/epsilon
        return charge_density / epsilon_naught

# One Dimentional Boundary Conditions


def g(x):
    if x <= 0:
        return boundary_voltage_low
    return boundary_voltage_high

# Returns the Value of Potential Feild at a given point A with N random walks


def poisson_approximation(A, N):
    result = 0
    for i in range(N):
        x = A
        F = 0
        while True:
            if x <= 0 or x >= h:
                break
            if random.randint(0, 1):
                x += d
            else:
                x -= d
            F += f(x) / h**2
        result += g(x) - F
    result = result / N
    return result

# Function for plotting the potential
@gif.frame
def plot(x, y):
    plt.figure(figsize=(7, 5), dpi=100)
    plt.plot(x, y)
    plt.text(h, 0, f'N = {N}', ha='right')
    plt.text(h, 0.4, f'L = {lattice_points}', ha='right')
    plt.ylim(-2, 7)
    plt.xlabel('Distance from negative plate (Meters)')
    plt.ylabel('Potential (Volts)')
#    plt.show()


if __name__ == "__main__":
    for laplace in True, False:
        # Analysis with respect to Number of Random Walks
        frames = []
        lattice_points = 15
        for N in range(10, 1500, 20):
            print(f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for {'Laplace' if laplace else 'Poisson'}")
            lattice = np.linspace(0, h, num=lattice_points, endpoint=True)
            frame = plot(lattice, [poisson_approximation(A, N) for A in lattice])
            frames.append(frame)
            gif.save(frames, f"{'Laplace' if laplace else 'Poisson'}_N.gif", duration=100)

        # Analysis with respect to number of Lattice Points
        frames = []
        N = 500
        for lattice_points in range(2, 41):
            print(f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for {'Laplace' if laplace else 'Poisson'}")
            d = h / lattice_points
            lattice = np.linspace(0, h, num=lattice_points, endpoint=True)
            frame = plot(lattice, [poisson_approximation(A, N) for A in lattice])
            frames.append(frame)
            gif.save(frames, f"{'Laplace' if laplace else 'Poisson'}_Lattice.gif", duration=100)
