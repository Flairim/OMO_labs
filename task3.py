import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2 + 5 * np.sin(x) - 1

def g(x):
    return np.arcsin((1-x**2)/5)


x0 = -2.25

def apriori_iteration_estimate(q):

    return  np.floor(np.log(abs( (g(x0) - x0) / (1 - q) / eps))/ np.log(1/q)) + 1
    
def simple_iteration(f, g, x0, eps, q):

    apriori_estimate = apriori_iteration_estimate(q)
    iter_count = 0
    x_prev = x0
    stop_iter = 0
    stop_x = 0

    print("\nМетод простої ітерації:")
    print(f"\nАпріорна оцінка кількості ітерацій: {apriori_estimate}")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")

        
        if stop_iter == 0 and stop_x == 0 and abs(x_next - x_prev) < ((1-q)/q)*eps:
            stop_iter = iter_count
            stop_x = x_next
        
        x_prev = x_next

        

    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return stop_x, stop_iter

q = 0.20
eps = 0.0001

root_iter, steps_iter = simple_iteration(f, g, x0, eps, q)

print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")


def apriori_estimation_relaxation(z0, q):
    return np.floor(np.log(abs(z0) / eps) / np.log(1/q)) + 1

def relaxation_method_(x0,tau, z0, q):
    iter_count = 0
    stop_iter = 0
    stop_x = 0
    apriori_estimate = apriori_estimation_relaxation(z0, q)

    print("\nМетод релаксації:")
    print(f"\nАпріорна оцінка кількості ітерацій: {apriori_estimate}")
    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")

    while iter_count < apriori_estimate:
        iter_count += 1
        x1 = x0 + tau * f(x0)
        error = abs(x1 - x0)
        print(f"Ітерація {iter_count}: x = {x1}, f(x) = {f(x1)}")

        if stop_iter == 0 and stop_x == 0 and error < eps:
            stop_iter = iter_count
            stop_x = x1

        x0 = x1

    return stop_x, stop_iter

m1 = 6.8955
M1 = 8.0863
z0 = x0 + 2.22727
q1 = (M1 - m1) / (M1 + m1)
tau_opt = 2 / (m1 + M1)

root_iter, steps_iter = relaxation_method_(x0, tau_opt, z0, q1)
print(f"Корінь методом релаксції: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
