"""Reproducibility checks for the finite Gaussian cooling-cycle Jeffreys-rate theorem."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def H(t,c):
    y=math.exp(-t)
    return (1-y)**2/(1-c*y)

def J(z,c):
    return z*z*quad(lambda t:math.exp(-z*t)*H(t,c),0,math.inf,epsabs=1e-12)[0]

def jseries(z,c,N=120):
    return 2*z*z*sum(c**n/((z+n)*(z+n+1)*(z+n+2)) for n in range(N))

def second(t,c):
    x=math.exp(-t)
    p=(c-2)+(4-2*c+c*c)*x-3*c*x*x+c*c*x*x*x
    return x*p/(1-c*x)**3

def dF(z,c):
    return -quad(lambda t:t*math.exp(-z*t)*second(t,c),0,math.inf,epsabs=2e-12)[0]

assert abs(J(math.sqrt(2),0)-2*math.sqrt(2)/((math.sqrt(2)+1)*(math.sqrt(2)+2)))<1e-10
for c in [0.01,0.2,0.5,0.8,0.95]:
    for z in [0.2,0.7,1.5,3.,9.]:
        assert abs(J(z,c)-jseries(z,c,500))<3e-10,(c,z,J(z,c),jseries(z,c,500))
    root=brentq(lambda z:dF(z,c),0.1,100)
    assert dF(root*0.8,c)>0 and dF(root*1.2,c)<0
    print('contrast',c,'opt_z',root,'objective_J',J(root,c))
coeff=(24+27*math.sqrt(2))/98
for c in [0.01,0.002,0.0005]:
    root=brentq(lambda z:dF(z,c),.3,8)
    err=abs((root-math.sqrt(2))/c-coeff)
    assert err<2*c
    print('weak_c',c,'observed slope',(root-math.sqrt(2))/c,'theory',coeff)
print('checks PASS')
