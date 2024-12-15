import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25

x_vals = np.linspace(-4, 4, 400)
y_vals = f(x_vals)

def iterbisection_method(f, a, b, eps):
    apriori_estimate = np.floor(np.log2((b - a) / eps))
    
    iter_count = 0
    x = (a + b) / 2
    
    print("Метод дихотомії(Апріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x}, f(x) = {f(x)}, a = {a}, b = {b}")   
    
    while iter_count < apriori_estimate:
        
        iter_count += 1
        x = (a + b) / 2
        print(f"Ітерація {iter_count}: x = {x}, f(x) = {f(x)}, a = {a}, b = {b}")
        
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x


def bisection_method(f, a, b, eps):
    iter_count = 0
    x = (a + b) / 2
    print("\nМетод дихотомії(Апостеріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x}, f(x) = {f(x)}, a = {a}, b = {b}")    
    
    while f(x) != 0 and (b - a) / 2 >= eps :
        iter_count += 1
        x = (a + b) / 2
        print(f"Ітерація {iter_count}: x = {x}, f(x) = {f(x)}, a = {a}, b = {b}")
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    

a, b = -0.1, 0.1
eps = 0.0001
x0 = 0
q = 0.18

iterbisection_method(f, a, b, eps)
bisection_method(f, a, b, eps)


def g(x):
    return (x**2 + np.sin(x) - 0.25) / 12

def apriori_iteration_estimate(q):

    return  np.floor(np.log(abs( (g(x0) - x0) / (1 - q) / eps))/ np.log(1/q)) + 1
    
def itersimple_iteration(f, g, x0, eps):

    apriori_estimate = apriori_iteration_estimate(q)
    iter_count = 0
    x_prev = x0
    stop_iter = 0
    stop_x = 0

    print("\nМетод простої ітерації(Апріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")

        
        if stop_iter == 0 and stop_x == 0 and abs(x_next - x_prev) < ((1-q)/q)*eps:
            stop_iter = iter_count
            stop_x = x_next
        
        x_prev = x_next

def simple_iteration(f, g, x0, eps, max_iter = 100):

    iter_count = 0
    x_prev = x0

    print("\nМетод простої ітерації(Апостеріорна оцінка):")
    print(f"Ітерація {iter_count}: x = {x_prev}, f(x) = {f(x_prev)}")
    
    while iter_count < max_iter:
        iter_count += 1
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        if abs(x_next - x_prev) < ((1-q)/q)*eps:
            break
        
        x_prev = x_next


itersimple_iteration(f, g, x0, eps)
simple_iteration(f, g, x0, eps)