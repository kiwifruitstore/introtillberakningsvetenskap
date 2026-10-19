

import numpy as np
from sympy import * 

#CSN

def function(r):
    return 1200 * ((1+r) / r) * (((1+r)**(7))-1) - 60000

r = symbols('r')

f = 1200 * ((1+r) / r) * (((1+r)**(7))-1) - 60000
print(function(0.0000001))
print(function(1))


def bisektionsmetoden(f, a, b, tol):
    s_fa = np.sign(f(a))
    s_fb = np.sign(f(b))
    assert(s_fa !=s_fb)
    x = (a+b)/2
    niter = 0
    while ((b-a)/2 > tol):
        niter = niter + 1
        s_fx = np.sign(f(x))
        if (s_fa == s_fx):
            a = x
        else:
            b = x
        x = (a+b)/2
        print(niter, x)
    return x, niter

def newton(fun, fprim, x0, tol):
    maxiter = 100
    x = x0
    dx = 2*tol
    niter = 0

    while np.abs(dx) > tol:
        niter = niter + 1
        dx = -fun(x)/fprim(x)
        x = x + dx

        assert(niter < maxiter)
        print(niter, x)

    return x, niter


fprim = diff(f, r)

# Gör om uttrycken till funktioner så att vi kan sätta in numeriska värden
function = lambdify(r, f)
derivative = lambdify(r, fprim)

#x, niter = bisektionsmetoden(function, 0.0000001, 1, 10**(-6))
#print()
#print("bisektion:", x, "efter", niter, "iterationer")  

x, niter = newton(function, derivative, -1, 10**(-6))

print()
print("Newton:", x, "efter", niter, "iterationer")  