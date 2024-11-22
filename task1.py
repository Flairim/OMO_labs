import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25

# x_vals = np.linspace(-4, 4, 400)
# y_vals = f(x_vals)

# plt.plot(x_vals, y_vals)
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Графік функції f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.grid(True)
# plt.show()

def bisection_method(f, a, b, eps):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція повинна змінювати знак на кінцях інтервалу.")
    
    apriori_estimate = np.floor(np.log2((b - a) / eps))
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



a, b = -1, 1
eps = 0.0001
x0 = 1.5
q = 0.15

root_bisect, steps_bisect = bisection_method(f, a, b, eps)
print(f"Корінь методом дихотомії: {root_bisect}, кількість ітерацій апостеріорної оцінки: {steps_bisect}")

def g(x):
    return (x**2 + np.sin(x) - 0.25) / 12

def apriori_iteration_estimate(q):

    return  round(math.log(abs( (g(2) - 2) / (1 - q) / eps))/ math.log(1/q)) + 1

def simple_iteration(f, g, x0, eps):

    apriori_estimate = apriori_iteration_estimate(q)
    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)
    stop_iter = 0

    print("Метод простої ітерації:")
    print(f"\nАпріорна оцінка кількості ітерацій: {apriori_estimate}")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_prev = x_next
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")

        
        if stop_iter == 0 and abs(x_next - x_prev) <= eps:
            stop_iter = iter_count

    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

root_iter, steps_iter = simple_iteration(f, g, x0, eps)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
