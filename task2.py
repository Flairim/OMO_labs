import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**4 + 4*x - 2

# # Побудова графіка функції
# x_vals = np.linspace(-2, 2, 400)
# y_vals = f(x_vals)

# plt.plot(x_vals, y_vals)
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Графік функції f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.grid(True)
# plt.show()

def g(x):
    return (2 - x**4) / 4

def df(x):
    return 4*x**3 + 4

def apriori_iteration_estimate(L, initial_error, eps):

    return math.ceil(math.log((eps * (1 - L)) / initial_error) / math.log(L))

def simple_iteration(f, g, x0, eps, L, initial_error):

    apriori_estimate = apriori_iteration_estimate(L, initial_error, eps)
    print(f"\nАпріорна оцінка кількості ітерацій: {apriori_estimate}")

    iter_count = 0
    aposter_iter = 0
    x_prev = x0
    x_next = g(x_prev)
    x_prev1 = x0
    x_next1 = g(x_prev)

    print("Метод простої ітерації:")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_prev = x_next
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")

    while aposter_iter < apriori_estimate:
        aposter_iter += 1
        x_prev1 = x_next1
        x_next1 = g(x_prev1)
        
        if abs(x_next1 - x_prev1) <= eps:
            break

    print(f"Апостеріорна оцінка зупинилася на ітерації: {aposter_iter}")
    return x_next, iter_count

x0 = 1
L = 0.5                  
initial_error = abs(g(x0) - x0)
eps = 0.0001

root_iter, steps_iter = simple_iteration(f, g, x0, eps, L, initial_error)

print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
def df(x):
    return 4*x**3 + 4

import numpy as np

def newton_method(f, df, x0, eps):
    # Обчислення апріорної оцінки кількості ітерацій
    apriori_estimate = int(np.ceil(np.log2((x0 - (-x0)) / eps)))  # Прикладна апріорна оцінка на основі розміру інтервалу
    
    iter_count = 0
    x_next = x0 - f(x0) / df(x0)
    stop_iter = 0

    print("\nМетод Ньютона:")
    print(f"Апріорна оцінка кількості ітерацій: {apriori_estimate}")
    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")
    
    # Виконання ітерацій методу Ньютона
    while iter_count < apriori_estimate:
        iter_count += 1
        x_prev = x_next
        x_next = x_prev - f(x_prev) / df(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        # Якщо апостеріорна оцінка досягнута
        if abs(f(x_next)) <= eps and stop_iter == 0:
            stop_iter = iter_count
    
    if stop_iter == 0:
        stop_iter = iter_count
    
    # Виведення результату
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    
    return x_next, stop_iter

# Приклад використання
root_newton, steps_newton = newton_method(f, df, x0, eps)
print(f"Корінь методом Ньютона: {root_newton}, кількість ітерацій апостеріорної оцінки: {steps_newton}")
