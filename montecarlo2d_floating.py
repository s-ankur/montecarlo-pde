"""
All calculations in SI units
"""
import random
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math

h = 10e-2  # Distance between plates = 10cm
lattice_points = 30  # Number of Points in lattice
d = h / lattice_points  # Lattice size
boundary_voltage_high = 5.0  # 5 Volts at Positive Plate
boundary_voltage_low = 0.0  # 0 Volts at Negative Plate
epsilon_naught = 8.854e-12  # Permittivity of Vaccum
charge_density = 6e-16  # Coulomb per meter cube
N = 400  # Number of Random Walks


def f(x):
    # Alternative charge distribution: A charged Sphere in the centre of metal box
    if (h / 2 - x[0]) ** 2 + (h / 2 - x[1]) ** 2 <= (h / 5) ** 2:
        return -charge_density * 5 / epsilon_naught
    else:
        return 0


def g(x):
    # Two Dimentional Alternative Boundary Conditions: uncharged metal box
    return 0


@np.vectorize
def poisson_approximation_semi_floating(*A):
    print(A)
    # Returns the Value of Potential Feild at a given point A with N random walks
    result = 0
    for i in range(N):
        x = list(A)
        F = 0
        while True:
            if x[0] <= 0 or x[0] >= h or x[1] <= 0 or x[1] >= h:
                break
            random_angle = random.random() * 2 * math.pi
            random_unit_vector = np.array(
                [math.cos(random_angle), math.sin(random_angle)]
            )
            x += random_unit_vector * d
            F += f(x) / h ** 2
        result += g(x) - F
    result = result / N
    return result


@np.vectorize
def poisson_approximation_full_floating(*A):
    print(A)
    # Returns the Value of Potential Feild at a given point A with N random walks
    result = 0
    for i in range(N):
        x = list(A)
        F = 0
        while True:
            if x[0] <= 0 or x[0] >= h or x[1] <= 0 or x[1] >= h:
                break
            random_angle = random.random() * 2 * math.pi
            random_unit_vector = np.array(
                [math.cos(random_angle), math.sin(random_angle)]
            )
            random_step_size = random.random() * d
            x += random_unit_vector * random_step_size
            F += f(x) / h ** 2
        result += g(x) - F
    result = result / N
    return result


def plot(x, y, z):
    # Function for plotting the potential
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(x, y, np.array(z), cmap=cm.jet, linewidth=0.1)
    plt.xlabel("X (Meters)")
    plt.ylabel("Y (Meters)")
    ax.set_zlabel("Potential (Volts)")
    plt.show()


if __name__ == "__main__":
    # Experiment H : Semi Floating Random Walk
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for Semi Floating Random Walk Algorithm"
    )
    lattice_x, lattice_y = np.mgrid[
        0: h: lattice_points * 1j, 0: h: lattice_points * 1j
    ]
    z = poisson_approximation_semi_floating(lattice_x.ravel(), lattice_y.ravel()).reshape(
        lattice_x.shape
    )
    plot(lattice_x, lattice_y, z)

    # Experiment H :  Full Floating Random Walk
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for Full Floating Random Walk Algorithm"
    )
    lattice_x, lattice_y = np.mgrid[
        0: h: lattice_points * 1j, 0: h: lattice_points * 1j
    ]
    z = poisson_approximation_full_floating(lattice_x.ravel(), lattice_y.ravel()).reshape(
        lattice_x.shape
    )
    plot(lattice_x, lattice_y, z)
