"""
All calculations in SI units
"""
import random
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

h = 10e-2  # Distance between plates = 10cm
lattice_points = 30  # Number of Points in lattice
d = h / lattice_points  # Lattice size
boundary_voltage_high = 5.0  # 5 Volts at Positive Plate
boundary_voltage_low = 0.0  # 0 Volts at Negative Plate
epsilon_naught = 8.854e-12  # Permittivity of Vaccum
charge_density = 6e-16  # Coulomb per meter cube
N = 400  # Number of Random Walks


def f(x):
    # The Function \nabla^2(phi)  = f
    # For Laplace f = 0
    return 0


def g(x):
    # Two Dimentional Boundary Conditions: two parallel metal plates at x=0,x=h
    # the plate at x=h is at high potential and x=0 is low potential
    # Assume that there are metal plates along y=0 and y=h (uncharged)
    # this is because I dont know how to simulate open boundry conditions
    if x[0] <= 0:
        return boundary_voltage_low
    if x[0] >= h:
        return boundary_voltage_high
    if x[1] <= 0 or x[1] >= h:
        return boundary_voltage_low


def f_2(x):
    # Alternative charge distribution: A charged Sphere in the centre of metal box
    if (h / 2 - x[0]) ** 2 + (h / 2 - x[1]) ** 2 <= (h / 5) ** 2:
        return -charge_density * 5 / epsilon_naught
    else:
        return 0


def g_2(x):
    # Two Dimentional Alternative Boundary Conditions: uncharged metal box
    return 0


def f_3(x):
    # Alternative charge distribution: TWO charged Sphere in the centre of metal box
    if (h / 3 - x[0]) ** 2 + (h / 2 - x[1]) ** 2 <= (h / 5) ** 2:
        return -charge_density * 5 / epsilon_naught
    if (2 * h / 3 - x[0]) ** 2 + (h / 2 - x[1]) ** 2 <= (h / 5) ** 2:
        return charge_density * 5 / epsilon_naught
    else:
        return 0


@np.vectorize
def poisson_approximation_fixed_step(*A):
    # Returns the Value of Potential Feild at a given point A with N random walks
    result = 0
    for i in range(N):
        x = list(A)
        F = 0
        while True:
            if x[0] <= 0 or x[0] >= h or x[1] <= 0 or x[1] >= h:
                break
            random_number = random.randint(0, 3)
            if random_number == 0:
                x[0] += d
            elif random_number == 1:
                x[0] -= d
            elif random_number == 2:
                x[1] += d
            elif random_number == 3:
                x[1] -= d
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
    # Experiment E: 2D Capacitor
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks"
    )
    lattice_x, lattice_y = np.mgrid[
        0: h: lattice_points * 1j, 0: h: lattice_points * 1j
    ]
    z = poisson_approximation_fixed_step(lattice_x.ravel(), lattice_y.ravel()).reshape(
        lattice_x.shape
    )
    plot(lattice_x, lattice_y, z)

    # Experiment F: Metal box with positively charged metal ball inside
    f = f2
    g = g2
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for {'Laplace' if laplace else 'Poisson'}"
    )
    lattice_x, lattice_y = np.mgrid[
        0: h: lattice_points * 1j, 0: h: lattice_points * 1j
    ]
    z = poisson_approximation_fixed_step(lattice_x.ravel(), lattice_y.ravel()).reshape(
        lattice_x.shape
    )
    plot(lattice_x, lattice_y, z)

    # Experiment G: Metal Box with two spheres (positive and negative)

    f = f_3
    g = g_2
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for {'Laplace' if laplace else 'Poisson'}"
    )
    lattice_x, lattice_y = np.mgrid[
        0: h: lattice_points * 1j, 0: h: lattice_points * 1j
    ]
    z = poisson_approximation_fixed_step(lattice_x.ravel(), lattice_y.ravel()).reshape(
        lattice_x.shape
    )
    plot(lattice_x, lattice_y, z)
