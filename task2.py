import numpy as np
import matplotlib.pyplot as plt

# Визначення функції f(x)
def f(x):
    return x**4 + 4*x - 2

# Побудова графіка функції
x_vals = np.linspace(-2, 2, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# Функція для методу простої ітерації
def g(x):
    return (2 - x**4) / 4

# Метод простої ітерації з виведенням усіх ітерацій
def simple_iteration(g, x0, eps, max_iter=1000):
    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)
    stop_iter = 0
    
    print("Метод простої ітерації:")
    print(f"Ітерація {iter_count}: x = {x_prev}")
    
    while iter_count < max_iter:
        iter_count += 1
        x_prev = x_next
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}")
        
        if abs(x_next - x_prev) <= eps and stop_iter == 0:
            stop_iter = iter_count  # фіксуємо ітерацію апостеріорної оцінки

    # Якщо апостеріорна оцінка не спрацювала раніше, зупиняємось на останній ітерації
    if stop_iter == 0:
        stop_iter = iter_count

    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

x0 = 1
eps = 0.0001

root_iter, steps_iter = simple_iteration(g, x0, eps)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")

# Метод Ньютона з виведенням усіх ітерацій
def df(x):
    return 4*x**3 + 4

def newton_method(f, df, x0, eps, max_iter=1000):
    iter_count = 0
    x_next = x0 - f(x0) / df(x0)
    stop_iter = 0
    
    print("\nМетод Ньютона:")
    print(f"Ітерація {iter_count}: x = {x0}")
    
    while iter_count < max_iter:
        iter_count += 1
        x_prev = x_next
        x_next = x_prev - f(x_prev) / df(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}")
        
        if abs(f(x_next)) <= eps and stop_iter == 0:
            stop_iter = iter_count  # фіксуємо ітерацію апостеріорної оцінки

    if stop_iter == 0:
        stop_iter = iter_count
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

root_newton, steps_newton = newton_method(f, df, x0, eps)
print(f"Корінь методом Ньютона: {root_newton}, кількість ітерацій апостеріорної оцінки: {steps_newton}")
