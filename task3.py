import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2 + 5 * np.sin(x) - 1

# x_vals = np.linspace(-3, 3, 400)
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

x0 = 0.5
L = 0.5                  
initial_error = abs(g(x0) - x0)
eps = 0.0001

root_iter, steps_iter = simple_iteration(f, g, x0, eps, L, initial_error)

print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")

def relaxation_method(f, g, x0, eps, omega=1.5):
    iter_count = 0
    x_prev = x0
    x_next = x_prev + omega * (g(x_prev) - x_prev)
    aposter_iter = 0
    x_prev1 = x0
    x_next1 = x_prev + omega * (g(x_prev) - x_prev)
    stop_iter = 0

    M = np.eye(len(x0)) - omega * np.eye(len(x0))
    rho_M = np.max(np.abs(np.linalg.eigvals(M)))  
    
    apriori_estimate = int(np.ceil(np.log(eps) / np.log(rho_M)))
    
    print("\nМетод релаксації:")
    print(f"Апріорна оцінка кількості ітерацій: {apriori_estimate}")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_prev = x_next
        x_next = x_prev + omega * (g(x_prev) - x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
    
    while aposter_iter < apriori_estimate:
        aposter_iter += 1
        x_prev1 = x_next1
        x_next1 = x_prev1 + omega * (g(x_prev1) - x_prev1)
        
        if abs(x_next - x_prev) <= eps and stop_iter == 0:
            stop_iter = iter_count 

    if stop_iter == 0:
        stop_iter = iter_count
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    return x_next, stop_iter

root_relax, steps_relax = relaxation_method(f, g, x0, eps)
print(f"Корінь методом релаксації: {root_relax}, кількість ітерацій апостеріорної оцінки: {steps_relax}")
