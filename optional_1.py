from sympy import *
x = Symbol('x')
print (diff(sin(x**2)*x, x))

# result
# 2*x**2*cos(x**2) + sin(x**2)
