import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 2) # 50 punkter mellan -2 och 2
y = x**3 - x
print("Första värdet:", y[0])
plt.plot(x, y)
plt.show()