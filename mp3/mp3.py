import numpy as np
import matplotlib.pyplot as plt

# begynnelsedata
t_span = np.arange(0, 301)
u0 = 1
u0_prim = 0
lam = 100

def fun(t, u): # diffekvationen
    u1 = u[0]
    u2 = u[1]
    return np.array ([
        u2, lam * (1 - u1**2) * u2 - u1])

def ralstons(fun, t0, y0, T, n): # ralstons metod
    h = (T - t0) / n # steglängd
    t = t0 # starttid
    u = y0 
    
    t_values = np.zeros(n + 1) # array med nollor
    u_values = np.zeros((n + 1, 2)) # array med nollor
    
    t_values[0] = t # lägg in t som första värde
    u_values[0] = u # lägg in u som första värde
    
    for i in range(n):
        k1 = fun(t, u) # definera k1
        k2 = fun(t + (2 * h) / 3, u + ((2 * h) / 3) * k1) # definera k2
        u = u + h / 4 * (k1 + 3 * k2) # beräkna u_(i+1)
        t = t + h # beräkna nästa tid m.h.a steglängden
        
        t_values[i + 1] = t # lägg till t vid index i + 1 för alla i i range(n)
        u_values[i + 1] = u # lägg till u vid index i + 1 för alla i i range(n)
        
    return t_values, u_values # returnerar arrayerna

t0 = 0 # starttid
T = 300 # sluttid
n = 10000 # punkter
y0 = np.array([u0, u0_prim]) # y_0, vektor med startvärden för u(0) och u'(0)


#t, un1000000 = ralstons(fun, t0, y0, T, 1000000) # t, u är lika med metoden med parametrar nedan
t, un100000 = ralstons(fun, t0, y0, T, 1000000)
#t, un10000 = ralstons(fun, t0, y0, T, 10000)
#t, un79 = ralstons(fun, t0, y0, T, 79)

#plt.plot(un1000000[:, 0], un1000000[:, 1], "r")
plt.plot(un100000[:, 0], un100000[:, 1], "r")
#plt.plot(un10000[:, 0], un10000[:, 1], "g")
#plt.plot(un79[:, 0], un79[:, 1], "m") # plotta
plt.xlabel("u1(t)")
plt.ylabel("u2(t)")
plt.grid()
plt.show()
