# fuck va nice det kommer vara att koda i svenska
# INTE


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
"""
y = [0, 5, 10, 15, 20]
w = [20.00, 19.51, 18.03, 15.75, 13.43]
p = 62.5
f = []
for value in range(5):
    f.append(y[value] * w[value] * p)

s_5 = (5/3) * (0.0 + 4*6096.875 + 2*11268.75 + 4*14765.625 + 16787.5)
s_10 = (10/3) * (0.0 + 4*11268.75 + 16787.5)
print(s_10)
error = (s_5 - s_10) / (2**4 - 1)
print(error)
print(2**4)
"""


x = np.linspace(0, 20, 21) # punkter som i trapets
    # [x1, x2, x3, x4...]
    # vill ge:
    # [x1, 4x2, 2x3, 4x4, ... ]
    # 0, 1, 2, 3
    # udda indicer ska få 4
    # jämna indicer ska få 2, förutom första och sista elementet
    # jämn först, sen udda, sen fixa första och sista elementet
    # udda [1:-1:2]
    # jämn [0:-1:2] # ÄNDRAR INTE PÅ FÖRSTA OCH SISTA 
print(x)
x[0:-1:2] *= 2
print(x)
x[1:-1:2] *= 4
print(x)
print(np.sum(x))


r = np.linspace(0, 100, 101)
print(r)
r[0:-1:2] *= 2
r[1:-1:2] *= 4
print(r)