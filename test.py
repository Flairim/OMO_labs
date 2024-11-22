import numpy as np
from scipy.misc import derivative
def g(x):
    return (x**2 + np.sin(x) - 0.25) / 12

x = 1.5

g_derivative_at_x = derivative(g, x, dx=1e-6)
print("Похідна g'(1.5):", g_derivative_at_x)