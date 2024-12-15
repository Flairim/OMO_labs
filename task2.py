import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**4 + 4*x - 2

def g(x):
    return (2 - x**4) / 4

def df(x):
    return 4*x**3 + 4

def apriori_iteration_estimate(q):

    return  np.floor(np.log(abs( (g(x0) - x0) / (1 - q) / eps))/ np.log(1/q)) + 1
    
def itersimple_iteration(f, g, x0, eps):

    apriori_estimate = apriori_iteration_estimate(q)
    iter_count = 0
    x_prev = x0
    stop_iter = 0
    stop_x = 0

    print("Метод простої ітерації(Апріорна оцінка):")
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

x0 = 0.5
q = 0.15
eps = 0.0001

itersimple_iteration(f, g, x0, eps)
simple_iteration(f, g, x0, eps)

def df(x):
    return 4*x**3 + 4

def apriori_estimation_iteration(q):
    return math.log(np.floor((math.log(0.12/eps))/(math.log(1/q)) + 1), 2) + 1

def iternewton_method(f, df, x0, eps, q1):

    apriori_estimate = apriori_estimation_iteration(q1)
    
    iter_count = 0
    x_next = x0 - f(x0) / df(x0)
    x_prev = x0


    print("\nМетод Ньютона(Апріорна оцінка):")

    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")
    
    while iter_count < apriori_estimate:
        iter_count += 1
        x_next = x_prev - f(x_prev) / df(x_prev)
        x_prev = x_next
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")

def newton_method(f, df, x0, eps, q1, max_iter = 100):

    
    iter_count = 0
    x_next = x0 - f(x0) / df(x0)
    x_prev = x0


    print("\nМетод Ньютона(Апостеріорна оцінка):")

    print(f"Ітерація {iter_count}: x = {x0}, f(x) = {f(x0)}")
    
    while iter_count < max_iter:
        iter_count += 1
        x_next = x_prev - f(x_prev) / df(x_prev)
        erorr = abs(x_next - x_prev)
        x_prev = x_next
        print(f"Ітерація {iter_count}: x = {x_next}, f(x) = {f(x_next)}")
        
        if erorr <= eps:
            break


q1 = 0.00708

iternewton_method(f, df, x0, eps, q1)
newton_method(f, df, x0, eps, q1)

