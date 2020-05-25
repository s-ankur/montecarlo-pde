"""
All calculations in SI units
"""
import random
import matplotlib.pyplot as plt
import gif
import numpy as np

h = 10e-2  # Distance between plates = 10cm
lattice_points = 15  # Number of Points in lattice
d = h / lattice_points  # Lattice size
laplace = False  # False-> Poisson, True-> Laplace
boundary_voltage_high = 5.0  # 5 Volts at Positive Plate
boundary_voltage_low = 0.0  # 0 Volts at Negative Plate
epsilon_naught = 8.854e-12  # Permittivity of Vaccum
charge_density = 1e-14  # Coulomb per meter cube
N = 400  # Number of Random Walks


def f(x):
    # The Function \nabla^2(phi)  = f
    if laplace:
        # For Laplace f = 0
        return 0
    else:
        # For Poisson, assume that there is a constant charge density
        # between the plates
        # So f= - rho/epsilon
        return (x / h - 0.5) * -charge_density / epsilon_naught


def g(x):
    # One Dimentional Boundary Conditions:
    if x <= 0:
        return boundary_voltage_low
    return boundary_voltage_high


def poisson_approximation_fixed_step(A):
    # Returns the Value of Potential Feild at a given point A with N random walks
    result = 0
    F = 0
    for i in range(N):
        x = A
        while True:
            if x <= 0 or x >= h:
                break
            if random.randint(0, 1):
                x += d
            else:
                x -= d
            F += f(x) * d ** 2
        result += g(x) / N
    result = result - F
    return result


# Function for plotting the potential


def plot(x, y, y2=None):
    plt.figure(figsize=(7, 5), dpi=100)
    plt.plot(x, y, "r.-")
    if y2 is not None:
        plt.plot(x, y2, "b-")
    plt.text(h, 0, f"N = {N}", ha="right")
    plt.text(h, 0.4, f"L = {lattice_points}", ha="right")
    plt.ylim(-2, 7)
    plt.xlabel("Distance from negative plate (Meters)")
    plt.ylabel("Potential (Volts)")


plotgif = gif.frame(plot)

if __name__ == "__main__":
    # Experiment D: One Dimensional Capacitor with constant charge distribution (Poisson Equation)
    laplace = False
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for Poisson Equation"
    )
    lattice = np.linspace(0, h, num=lattice_points, endpoint=True)
    plot(lattice, [poisson_approximation_fixed_step(A) for A in lattice])
    plt.show()

    # Experiment A: One Dimensional Capacitor (Laplace Equation)
    N = 400
    lattice_points = 15
    print(
        f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for Laplace Equation"
    )
    lattice = np.linspace(0, h, num=lattice_points, endpoint=True)
    feild_real = (boundary_voltage_high - boundary_voltage_low) / h * lattice
    plot(lattice, [poisson_approximation_fixed_step(A) for A in lattice], feild_real)
    plt.show()

    # Experiment B: Variation of solution with number of random walks (Laplace Equation)
    frames = []
    lattice_points = 15
    lattice = np.linspace(0, h, num=lattice_points, endpoint=True)
    feild_real = (boundary_voltage_high - boundary_voltage_low) / h * lattice
    feild_diff = []
    for N in range(10, 1000, 20):
        print(
            f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for Laplace Equation"
        )
        feild_approx = np.array([poisson_approximation_fixed_step(A) for A in lattice])
        frame = plotgif(lattice, feild_approx, feild_real)
        feild_diff.append(abs(feild_real - feild_approx).sum())
        frames.append(frame)
        gif.save(
            frames, f"Figures/{'Laplace' if laplace else 'Poisson'}_N.gif", duration=100
        )
    plt.plot(range(10, 1000, 20), feild_diff, "g.-")
    plt.xlabel("Number of Random Walks")
    plt.ylabel("Abs Error")
    plt.show()

    # Experiment C: Variation of solution with number of lattice points (Laplace Equation)
    frames = []
    feild_diff = []
    N = 400
    for lattice_points in range(2, 30):
        print(
            f"Calculating Monte Carlo with {lattice_points}x{lattice_points} lattice points and {N} random walks for Laplace Equation"
        )
        d = h / lattice_points
        lattice = np.linspace(0, h, num=lattice_points, endpoint=True)
        feild_real = (boundary_voltage_high - boundary_voltage_low) / h * lattice
        feild_approx = np.array([poisson_approximation_fixed_step(A) for A in lattice])
        frame = plotgif(lattice, feild_approx, feild_real)
        feild_diff.append(abs(feild_real - feild_approx).sum())
        frames.append(frame)
        gif.save(
            frames,
            f"Figures/{'Laplace' if laplace else 'Poisson'}_Lattice.gif",
            duration=100,
        )
    plt.plot(range(2, 30), feild_diff)
    plt.xlabel("Number of Lattice Points")
    plt.ylabel("Abs Error")
    plt.show()
