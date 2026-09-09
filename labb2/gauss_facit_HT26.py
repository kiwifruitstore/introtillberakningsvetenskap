#!/usr/bin/env python3
"""Facit till uppgifterna 5-8 i NumPy-labben HT26."""
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

# ----------------------------------------------------------------
# Uppgift 5: Gausskurvan (samma som tidigare Gauss.py)
# ----------------------------------------------------------------
sigma = 0.1
mu = 0.5

x = np.linspace(0, 1, 400)
fx = 1/(sigma*sqrt(2*pi))*np.exp(-(x - mu)**2/(2*sigma**2))

plt.figure()
plt.plot(x, fx, label='$y = f(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.show()

# ----------------------------------------------------------------
# Uppgift 6: flera sigma i samma figur
# ----------------------------------------------------------------
def gauss(x, sigma, mu):
    return 1/(sigma*sqrt(2*pi))*np.exp(-(x - mu)**2/(2*sigma**2))

plt.figure()
for sigma in [0.05, 0.1, 0.2]:
    plt.plot(x, gauss(x, sigma, 0.5), label=f'$\\sigma = {sigma}$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.show()
# Mindre sigma ger en smalare och högre kurva (arean är alltid 1).

# ----------------------------------------------------------------
# Uppgift 7: linjärt ekvationssystem
# ----------------------------------------------------------------
A = np.array([[2, -1], [-4, 8]])
b = np.array([1, 16])
xlsg = np.linalg.solve(A, b)
print("Lösning:", xlsg)             # [2, 3]
print("Kontroll A@x:", np.dot(A, xlsg))  # ska bli b = [1, 16]

# ----------------------------------------------------------------
# Uppgift 8: rättad kod (tre fel)
# ----------------------------------------------------------------
x = np.linspace(-2, 2)   # 50 punkter (default) mellan -2 och 2
y = x**3 - x             # FEL 1: ** i stället för ^
print("Första värdet:", y[0])   # FEL 2: första elementet har index 0
plt.figure()
plt.plot(x, y)
plt.show()               # FEL 3: plt.show() saknades
