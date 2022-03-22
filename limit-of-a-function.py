import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sympy.abc import x
from sympy import sin
f = sym.lambdify (x, 0)
a = [-3,-0.1, -0.01, -0.001, 0, 0.001, 0.01, 0.1, 3]
y = [f(i) for i in a ]
for i in y:
  print(i)
plt.plot(a, y)
plt.show()