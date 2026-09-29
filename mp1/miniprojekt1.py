import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
från beräkningarna i fråga 1

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

# fråga 2 del b
"""
def w(x):
    return 20 * np.exp(-0.01 * x**1.5)

def hydro(x):
    return 62.5 * x * w(x)

Int, error = quad(hydro, 0, 20)

print(Int, error)

"""

#f5 implementation av trapets
"""
def trapets(func, a, b, n):
    # func är funktionen vi integrerar
    # a är lower bound
    # b är upper bound
    # n är antal delintervall vi vill använda
    h = (b-a)/n # steglängd 
    x = np.linspace(a, b, n+1) # x punkter som är bounds för våra trapetser
    fx = func(x)
    T = h*(np.sum(fx) - (fx[0] + fx[-1])/2) # trapetsarea över alla intervall gånger h (summera allt och dra av halva ändpunkterna)
    return T
"""

def trapets(func, a, b, n):
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    fx = func(x)
    T = h*(np.sum(fx) - (fx[0]+fx[-1])/2)
    return T
def humps(x):
    return 1 / ((x-.3)**2 + .01) + 1/((x-.9)**2 + .04) - 6
def enkel(x):
    output = 1 / (1 + x)
    return output
# implementation av simpsons

def simpsons(func, a, b, n):
    if n % 2 != 0:
        raise RuntimeError("Bara jämna n tillåtna i Simpsons.")
    h = (b-a)/n # steglängd som i trapets
    x = np.linspace(a, b, n+1) # punkter som i trapets
    # vikta, sen funktion
    fx = func(x)
    fx[2:-1:2] *= 2 # viktar alla jämna index MEN ändrar inte på första och sista elementet
    fx[1:-1:2] *= 4 # viktar alla udda index
    S = (h/3) * np.sum(fx)
    return S


# använd humps funktion
def humps(x):
    return 1 / ((x-.3)**2 + .01) + 1/((x-.9)**2 + .04) - 6
# ta steglängder
steglista = [2**n for n in range(2, 17)]
print(steglista)
real_integral, err = quad(humps, 0, 1, epsabs=1e-12, epsrel=1e-12) # = ln2

felkvoter = []
felmarginal = []
for i in steglista:
    experiment1 = simpsons(humps, 0, 1, int(i)) # Q(h)
    experiment2 = simpsons(humps, 0, 1, int(i/2)) # Q(2h)
    fel1 = real_integral - experiment1
    fel2 = real_integral - experiment2
    testkvot = fel2/fel1
    felmarginal.append(np.abs(fel1))
    felkvoter.append(testkvot)
    
    
felmarginal = np.array(felmarginal)
felmarginal = 1 / felmarginal
steglista = np.array(steglista)
steglista = 1 / steglista

steglista = steglista[::-1]
#plt.loglog(h_lista, fel_trapets, "*-", label="Trapets")
#plt.loglog(h_lista, h_lista**2, "--", label="h^2")

print(felkvoter)
plt.loglog(steglista, felmarginal, "*-", label="Simpson")
 
plt.loglog(steglista, steglista**4, "--", label="h^4")
plt.xlabel("h"); plt.legend()

plt.show()
