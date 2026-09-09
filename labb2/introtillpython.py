import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
"""
x = np.linspace(0,1,101)

def gauss(x, sigma, mu): # definierar f(x) = x^2
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp((-((x - mu)**2))/(2*(sigma**2)))

plt.plot(x,gauss(x, 0.1, 0.5), "r", markersize=1.0)
plt.plot(x,gauss(x, 0.05, 0.5), "g", markersize=1.0)
plt.plot(x,gauss(x, 0.2, 0.5), "b", markersize=1.0)
plt.legend(["0.1", "0.05", "0.2"])
plt.show()

"""

# matris
A = np.array([[2, -1], [-4, 8]])
b = np.array([1, 16])

x = np.linalg.solve(A,b)
print(x)

print(np.dot(A,x))



