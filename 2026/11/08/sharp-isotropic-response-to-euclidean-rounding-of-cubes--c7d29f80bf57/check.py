#!/usr/bin/env python3
"""Independent exact and numerical checks for rounded-cube moment formulas."""
import math
from math import comb
import sympy as sp

p=sp.pi
t=sp.symbols('t', nonnegative=True)

def orthant_monomial(exponents):
    """Exact integral of a monomial over the positive unit-radius orthant ball."""
    k=len(exponents)
    if k==0:return sp.Integer(1)
    total=sum(exponents)
    coeff=sp.prod(sp.gamma(sp.Rational(a+1,2)) for a in exponents)
    coeff /= 2**k*sp.gamma(sp.Rational(k+total,2)+1)
    return sp.simplify(coeff*t**(k+total))

def volume_moment(d):
    V=S=sp.Integer(0)
    for k in range(d+1):
        pref=sp.Integer(comb(d,k))*2**d
        J0=orthant_monomial((0,)*k)
        V+=pref*J0
        S+=pref*(sp.Rational(d-k,3)+k)*J0
        if k:
            S+=pref*2*k*orthant_monomial((1,)+(0,)*(k-1))
            S+=pref*k*orthant_monomial((2,)+(0,)*(k-1))
    return sp.simplify(sp.expand(V)),sp.simplify(sp.expand(S))

V,S=volume_moment(3)
V_expected=8+24*t+6*p*t**2+sp.Rational(4,3)*p*t**3
S_expected=8+40*t+(24+14*p)*t**2+(40+4*p)*t**3+6*p*t**4+sp.Rational(4,5)*p*t**5
assert sp.simplify(V-V_expected)==0
assert sp.simplify(S-S_expected)==0
D=sp.factor(sp.expand(5*sp.diff(V,t)*S-3*V*sp.diff(S,t)))
c=(24*(4-p),8*(19*p-54),-480+32*p+42*p**2,24*p*(p-3),p*(16-5*p))
assert sp.simplify(D-8*t*sum(c[j]*t**j for j in range(5)))==0
# Exact rational enclosures of pi: all five coefficients are strictly positive.
lo=sp.Rational(31,10); hi=sp.Rational(22,7)
assert 4-hi>0 and 19*lo-54>0
assert (-480+32*lo+42*lo**2)>0
assert lo>3 and (16-5*hi)>0
d=sp.symbols('d',integer=True,positive=True)
v1=d
v2=p*d*(d-1)/8
s1=d+2
s2=3+p*(d+4)*(d-1)/8
exponent=1+2/d
quadratic=sp.factor(s2-exponent*v2+exponent*(exponent+1)*v1*v1/2-exponent*v1*s1)
assert sp.simplify(quadratic-(d-1)*(p-4)/4)==0
checks=1

# Independent numerical volume and raw squared-radius moment via a Sobol grid.
try:
    import numpy as np
    from scipy.stats import qmc
    for x in (0.5,1.0,2.0):
        u=qmc.Sobol(d=3,scramble=True,seed=137).random_base2(m=18)
        pts=(2+2*x)*u-(1+x)
        outside=np.maximum(np.abs(pts)-1,0.)
        inside=np.sum(outside*outside,axis=1) <= x*x
        boxvol=(2+2*x)**3
        vest=boxvol*np.mean(inside)
        sest=boxvol*np.mean(np.sum(pts*pts,axis=1)*inside)
        vex=float(V.subs(t,x)); sex=float(S.subs(t,x))
        assert abs(vest-vex)/vex < 0.004,(x,'volume',vest,vex)
        assert abs(sest-sex)/sex < 0.004,(x,'moment',sest,sex)
        checks+=2
except ImportError:
    print('Independent numerical integration skipped: scipy/numpy unavailable')
print('ROUNDED_CUBE_MOMENT_AND_SIGN_CHECKS_PASSED',checks)
