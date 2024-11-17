import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25

x_vals = np.linspace(-4, 4, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def bisection_method(f, a, b, eps):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція повинна змінювати знак на кінцях інтервалу.")
    
    apriori_estimate = int(np.ceil(np.log2((b - a) / eps)))
    print(f"Апріорна оцінка кількості ітерацій для методу дихотомії: {apriori_estimate}")
    
    iter_count = 0
    stop_iter = 0  

    print("Метод дихотомії:")

    while iter_count < apriori_estimate:
        iter_count += 1
        c = (a + b) / 2
        print(f"Ітерація {iter_count}: x = {c}, f(x) = {f(c)}")
        
        if f(c) == 0:
            print(f"Знайдено точний корінь: {c}")
            stop_iter = iter_count
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        if stop_iter == 0 and (b - a) / 2 <= eps:
            stop_iter = iter_count

    if stop_iter == 0:
        stop_iter = iter_count
    
    root = (a + b) / 2
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return root, stop_iter



a, b = -2, 2
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

x0 = 2
L = 0.5                  
initial_error = abs(g(x0) - x0)

root_iter, steps_iter = simple_iteration(f, g, x0, eps, L, initial_error)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
