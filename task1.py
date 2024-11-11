import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25

def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція повинна змінювати знак на кінцях інтервалу.")
    
    apriori_estimate = int(np.ceil(np.log2((b - a) / tol)))
    print(f"Апріорна оцінка кількості ітерацій для методу дихотомії: {apriori_estimate}")
    
    iter_count = 0
    stop_iter = 0 
    print("Метод дихотомії:")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        c = (a + b) / 2
        print(f"Ітерація {iter_count}: c = {c}, f(c) = {f(c)}")
        
        if (b - a) / 2 <= tol and stop_iter == 0:
            stop_iter = iter_count  
        
        if f(c) == 0:
            print("Знайдено точний корінь.")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    if stop_iter == 0:
        stop_iter = iter_count
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return (a + b) / 2, stop_iter

a, b = -4, 4
eps = 0.0001

root_bisect, steps_bisect = bisection_method(f, a, b, eps)
print(f"Корінь методом дихотомії: {root_bisect}, кількість ітерацій апостеріорної оцінки: {steps_bisect}")

def g(x):
    return (x**2 + np.sin(x) - 0.25) / 12

def apriori_iteration_estimate(L, initial_error, eps):

    return math.ceil(math.log((eps * (1 - L)) / initial_error) / math.log(L))

def simple_iteration(f, g, x0, eps, L, initial_error):

    apriori_estimate = apriori_iteration_estimate(L, initial_error, eps)
    print(f"\nАпріорна оцінка кількості ітерацій: {apriori_estimate}")

    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)

    print("Метод простої ітерації:")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_prev = x_next
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        if abs(x_next - x_prev) <= eps:
            break

    print(f"Апостеріорна оцінка зупинилася на ітерації: {iter_count}")
    return x_next, iter_count

x0 = 2
L = 0.5                  
initial_error = abs(g(x0) - x0)

root_iter, steps_iter = simple_iteration(f, g, x0, eps, L, initial_error)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
