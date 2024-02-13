import numpy as np
import random
import math
import matplotlib.pyplot as plt

def hill_climbing(func, x, step_size, max_iterations):
    """
    Hill Climbing algorithm to find the minimum of a function.
    :param func: The function to minimize
    :param x: The initial value of the input
    :param step_size: The size of the step to take at each iteration
    :param max_iterations: The maximum number of iterations to run the algorithm for
    :return: The minimum value found by the algorithm and the list of tried x values
    """
    x_values = [x]
    y_values = [func(x)]
    for i in range(max_iterations):
        x_new = x + step_size *  np.random.normal(0,1) # generate a random real variable
        x_values.append(x_new)
        y_values.append(func(x_new))
        if func(x_new) < func(x):
            x = x_new

    return x, x_values, y_values

def sinus_func(x):
    """
    Example sinus function to minimize.
    :param x: The input value
    :return: The value of the sinus function at x
    """
    return math.sin(x) + 0.01 * (x - 20)*(x - 20)

# Example usage
total_min = 0
x_values = [];
y_values = [];

for i in range(0, 1000):
    start_x = np.random.normal(0, 1)
    x_min, x_values, y_values = hill_climbing(sinus_func, start_x, 0.7, 100)

    if x_min < total_min:
        total_min = x_min


print("Minimum found at x =", total_min)

# Plot the minimum value found against the number of iterations
plt.plot(range(len(y_values)), y_values, 'ro')
plt.xlabel('Iteration')
plt.ylabel('Minimum Value')
plt.show()

# Plot the sinus function with the tried x values
x = [x / 100 for x in range(-3000, 3000)]
y = [sinus_func(i) for i in x]
plt.plot(x, y)
plt.plot(x_values, y_values, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
