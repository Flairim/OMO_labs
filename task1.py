import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25

# Метод дихотомії з апріорною і апостеріорною оцінками
def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція повинна змінювати знак на кінцях інтервалу.")
    
    # Апріорна оцінка кількості ітерацій
    apriori_estimate = int(np.ceil(np.log2((b - a) / tol)))
    print(f"Апріорна оцінка кількості ітерацій для методу дихотомії: {apriori_estimate}")
    
    iter_count = 0
    stop_iter = 0  # для фіксації ітерації апостеріорної оцінки
    print("Метод дихотомії:")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        c = (a + b) / 2
        print(f"Ітерація {iter_count}: c = {c}, f(c) = {f(c)}")
        
        if (b - a) / 2 <= tol and stop_iter == 0:
            stop_iter = iter_count  # фіксуємо ітерацію, на якій зупинилася апостеріорна оцінка
        
        if f(c) == 0:
            print("Знайдено точний корінь.")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    # Якщо апостеріорна оцінка не спрацювала раніше, зупиняємось на останній ітерації
    if stop_iter == 0:
        stop_iter = iter_count
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return (a + b) / 2, stop_iter

a, b = -4, 4
eps = 0.0001

root_bisect, steps_bisect = bisection_method(f, a, b, eps)
print(f"Корінь методом дихотомії: {root_bisect}, кількість ітерацій апостеріорної оцінки: {steps_bisect}")

# Метод простої ітерації з апріорною і апостеріорною оцінками
def g(x):
    return (x**2 + np.sin(x) - 0.25) / 12

def simple_iteration(g, x0, eps, max_iter=1000):
    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)
    
    # Апріорна оцінка для методу простої ітерації (максимальна кількість ітерацій)
    apriori_estimate = max_iter
    print(f"\nАпріорна оцінка кількості ітерацій для методу простої ітерації: {apriori_estimate}")
    
    stop_iter = 0  # для фіксації ітерації апостеріорної оцінки
    print("Метод простої ітерації:")
    print(f"Ітерація {iter_count}: x = {x_prev}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_prev = x_next
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}")
        
        if abs(x_next - x_prev) <= eps and stop_iter == 0:
            stop_iter = iter_count  # фіксуємо ітерацію, на якій зупинилася апостеріорна оцінка
        
    if stop_iter == 0:
        stop_iter = iter_count
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

x0 = 2

root_iter, steps_iter = simple_iteration(g, x0, eps)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
