import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2 + 5 * np.sin(x) - 1

def g(x):
    return -np.sqrt(1-5*np.sin(x))


x0 = -2.5

def apriori_iteration_estimate(q):

    return  np.floor(np.log(abs( (g(x0) - x0) / (1 - q) / eps))/ np.log(1/q)) + 1
    
def itersimple_iteration(f, g, x0):

    apriori_estimate = apriori_iteration_estimate(q)
    iter_count = 0
    x_prev = x0

    print("Метод простої ітерації(Апріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        x_prev = x_next

def simple_iteration(f, g, x0, eps, max_iter = 100):

    iter_count = 0
    x_prev = x0

    print("\nМетод простої ітерації(Апостеріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < max_iter:
        iter_count += 1
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        if abs(x_next - x_prev) < ((1-q)/q)*eps:
            break
        
        x_prev = x_next

q = 0.7
eps = 0.0001

itersimple_iteration(f, g, x0)
simple_iteration(f, g, x0, eps)


def apriori_estimation_relaxation(z0, q):
    return np.floor(np.log(abs(z0) / eps) / np.log(1/q)) + 1

def iterrelaxation_method_(x0,tau, z0, q):
    iter_count = 0
    apriori_estimate = apriori_estimation_relaxation(z0, q)

    print("\nМетод релаксації(Апріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")

    while iter_count < apriori_estimate:
        iter_count += 1
        x1 = x0 + tau * f(x0)
        print(f"Ітерація {iter_count}: x = {x1}, f(x) = {f(x1)}")
        x0 = x1

def relaxation_method_(x0,tau, max_iter = 100):
    iter_count = 0

    print("\nМетод релаксації(Апостеріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")

    while iter_count < max_iter:
        iter_count += 1
        x1 = x0 + tau * f(x0)
        error = abs(x1 - x0)
        print(f"Ітерація {iter_count}: x = {x1}, f(x) = {f(x1)}")
        if error < eps:
            break

        x0 = x1

m1 = 2.92926
M1 = 7.93646
z0 = x0 + 2.22727
q1 = (M1 - m1) / (M1 + m1)
tau_opt = 2 / (m1 + M1)
print(f"tau_opt = {tau_opt}")
print(f"q1 = {q1}")
print(f"z0 = {z0}")

iterrelaxation_method_(x0, tau_opt, z0, q1)
relaxation_method_(x0, tau_opt)