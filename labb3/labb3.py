#yurh 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import brentq

#funktion
"""
r_0 = 3 #set variable, pipe length
r = np.linspace(0, 3, 101)
def v(r):
    return 2*((1 - (r / r_0))**(1/6))

# vill ha v(r) = c
c = 1.8 # letad lösning

r = np.linspace(0, 3, 101)
def f(r, r_0, c):
    def v(r):
        return 2*((1 - (r / r_0))**(1/6))
    return v(r) - c

# vill alltid ha f(r) = 0 

plt.plot(r, f(r, 3, 4), "g")

t = np.arange(-4, 4, 0.1)

plt.axhline(0,color='black') # x = 0
plt.axvline(0,color='black') # y = 0
plt.grid()
plt.show()
root = brentq(f,0,3,args =(3,4))
print(root)
"""



#konstanter 
p = 3
k = 0.05

# funktion som är lika med K

def function(x):
    return (x / (1-x))*np.sqrt((2*p)/(2+x))

# numpy vektor
x = np.linspace(0, 0.2, 101)

# kolla funktionen
#plt.plot(x, function(x), "b")
plt.axhline(0,color='black') # x = 0
plt.axvline(0,color='black') # y = 0
plt.grid()


# nollställesfunktion
def f(x):
    return function(x) - k

plt.plot(x,f(x), "b")
plt.show()
# lös
root = brentq(f, 0.0001, 0.2)
print(root)