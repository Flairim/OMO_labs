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

x0 = 0.7
q = 0.15
eps = 0.0001

root_iter, steps_iter = simple_iteration(f, g, x0, eps, q)

print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій апостеріорної оцінки: {steps_iter}")
def df(x):
    return 4*x**3 + 4

def apriori_estimation_iteration(q):
    return math.log(round((math.log(0.12/eps))/(math.log(1/q)) + 1), 2) + 1

def newton_method(f, df, x0, eps, q1):

    apriori_estimate = apriori_estimation_iteration(q1)
    
    iter_count = 0
    x_next = x0 - f(x0) / df(x0)
    x_prev = x0
    stop_iter = 0
    stop_x = 0

    print("\nМетод Ньютона:")
    print(f"Апріорна оцінка кількості ітерацій: {apriori_estimate}")
    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_next = x_prev - f(x_prev) / df(x_prev)
        erorr = abs(x_next - x_prev)
        x_prev = x_next
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        if erorr <= eps and stop_x == 0 and stop_iter == 0:
            stop_iter = iter_count
            stop_x = x_next
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {stop_iter}")
    
    return stop_x, stop_iter

q1 = 0.169

root_newton, steps_newton = newton_method(f, df, x0, eps, q1)
print(f"Корінь методом Ньютона: {root_newton}, кількість ітерацій апостеріорної оцінки: {steps_newton}")
