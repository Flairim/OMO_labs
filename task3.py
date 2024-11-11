import numpy as np
import matplotlib.pyplot as plt

# Визначення функції f(x)
def f(x):
    return x**2 + 5 * np.sin(x) - 1

# Побудова графіка функції
x_vals = np.linspace(-3, 3, 400)
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
    return np.arcsin((1 / 5) * (1 - x**2))

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
    
    if stop_iter == 0:
        stop_iter = iter_count

    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

x0 = 0.5
eps = 0.0001

root_iter, steps_iter = simple_iteration(g, x0, eps)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")

# Метод релаксації з виведенням усіх ітерацій
def relaxation_method(g, x0, eps, omega=1.5, max_iter=1000):
    iter_count = 0
    x_prev = x0
    x_next = x_prev + omega * (g(x_prev) - x_prev)
    stop_iter = 0
    
    print("\nМетод релаксації:")
    print(f"Ітерація {iter_count}: x = {x_prev}")
    
    while iter_count < max_iter:
        iter_count += 1
        x_prev = x_next
        x_next = x_prev + omega * (g(x_prev) - x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}")
        
        if abs(x_next - x_prev) <= eps and stop_iter == 0:
            stop_iter = iter_count  # фіксуємо ітерацію апостеріорної оцінки
    
    if stop_iter == 0:
        stop_iter = iter_count
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

root_relax, steps_relax = relaxation_method(g, x0, eps)
print(f"Корінь методом релаксації: {root_relax}, кількість ітерацій апостеріорної оцінки: {steps_relax}")
