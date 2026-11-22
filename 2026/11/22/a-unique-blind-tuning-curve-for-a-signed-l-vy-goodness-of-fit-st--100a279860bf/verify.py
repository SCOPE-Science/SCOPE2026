"""Numerical checks for the Gamma blind-weight curve of a Levy Laplace goodness-of-fit statistic.

Requires scipy >= 1.10 and numpy. The theorem is analytic; these checks are not its proof.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq

def integrand(t,k,a):
    h=k-1.0
    return t**1.5*math.exp(-a*t)*((1.0+t/h)**(-k)-(1.0+t/(4*h))**(-2*k))

def F(k,a):
    return quad(integrand,0.0,math.inf,args=(k,a),epsabs=3e-11,epsrel=1e-10,limit=500)[0]

def Fprime(k,a):
    return quad(lambda t: -t*integrand(t,k,a),0.0,math.inf,epsabs=1e-10,epsrel=1e-10,limit=500)[0]

checks=0
for k in (2.02,2.25,2.5):
    tstar=8*(k-1)
    for r in (.05,.2,.8,1.2,2.5,20.):
        t=r*tstar
        s=integrand(t,k,.4)
        assert (s<0)==(r<1)
        checks+=1
    lo=0.0001 if k<2.5 else 0.000001
    hi=1.
    assert F(k,lo)>0 and F(k,hi)<0
    root=brentq(lambda a:F(k,a),lo,hi,xtol=1e-14)
    assert abs(F(k,root)) < 5e-8
    assert F(k,root*.8)>0 and F(k,root*1.2)<0
    assert Fprime(k,root) < 0
    checks+=5
    print(f'k={k:.5f} a_root={root:.14f} F={F(k,root):+.3e} Fprime={Fprime(k,root):+.6e}')
print('numerical assertions passed:',checks)
