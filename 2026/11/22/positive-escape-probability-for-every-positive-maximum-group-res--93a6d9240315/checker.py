#!/usr/bin/env python3
"""Independent finite diagnostics for an analytic first-passage result.

Requires Python 3, NumPy, SciPy, SymPy. No external data or network.
Numerical checks DO NOT certify any infinite-time conclusion.
"""
from math import sqrt, erfc, exp, erf, pi
import numpy as np
from scipy.integrate import quad
import sympy as sp

u=sp.symbols('u',positive=True)
assert sp.simplify(sp.Rational(4,3)*(1-1/sp.sqrt(7))+(4/sp.sqrt(7)-1)/3-1)==0
delta=float((4/sp.sqrt(7)-1)/3)
assert 0 < delta < 1

cases=[(1.,1.,0.5),(2.4,0.7,0.3),(0.6,3.0,0.21),(5.1,0.8,0.65)]
for r,D,fraction in cases:
    k=fraction*sqrt(r/D)
    algebraic=r/(r-D*k*k)*(1-k*sqrt(D/2)/sqrt(r-D*k*k/2))
    integ=quad(lambda t: r*exp(-(r-D*k*k)*t)*erfc(k*sqrt(D*t/2)),
               0,np.inf,epsabs=2e-11,epsrel=2e-11,limit=200)[0]
    assert abs(algebraic-integ)<2e-10,(r,D,k,algebraic,integ)

# For all x>0 and N>=2, N exp(-lambda x) + N/delta exp(-kappa x) A2
# <= N/delta exp(-kappa x); check broad finite samples as a diagnostic.
for N in (2,3,5,15):
    for x in np.linspace(0.01,60,151):
        A2=1-delta
        lhs=N*exp(-x)+(N/delta)*exp(-x/2)*A2
        rhs=(N/delta)*exp(-x/2)
        assert lhs <= rhs*(1+1e-14)

# Independent time-tail check against reflection principle asymptotics.
for N in (1,2,3,7):
    x=1.3; D=0.8; t=1e8
    survival=erf(x/sqrt(4*D*t))**N
    leading=(x/sqrt(pi*D))**N*t**(-N/2)
    assert abs(survival/leading-1)<1e-7

print('PASS: four independent transform quadratures, super-solution grid,')
print('       exact critical constant, and no-reset tail checks')
print('Analytic proof required for all-time, all-parameter conclusions.')
