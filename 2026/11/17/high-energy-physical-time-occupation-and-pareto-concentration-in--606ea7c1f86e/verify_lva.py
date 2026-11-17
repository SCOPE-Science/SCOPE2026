"""Reproducible algebra and finite-energy diagnostics for the lifted-center theorem.

Requirements: Python 3, SymPy, NumPy, SciPy.
Finite-energy diagnostics do not constitute a proof of limiting statistics.
"""
import math

import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw

x, y, a, b, d = sp.symbols('x y a b d', positive=True)
lam = b - a
xdot = x*(a*x - b*y)
ydot = b*y*(x-y-d)
V = b*y/(a*x)
W = b*d/(lam*x)

def deriv(F):
    return sp.diff(F,x)*xdot+sp.diff(F,y)*ydot

assert sp.simplify(deriv(V)/x - lam*V*(1-W)) == 0
assert sp.simplify(deriv(W)/x - a*W*(V-1)) == 0
Vp, Wp = sp.symbols('V W',positive=True)
Hprime = a*(1-1/Vp)*lam*Vp*(1-Wp) + lam*(1-1/Wp)*a*Wp*(Vp-1)
assert sp.simplify(Hprime) == 0
assert sp.simplify(1/((b-a)/(b*d)) - b*d/(b-a)) == 0  # equilibrium concentration

# Exact physical-time quadrature for a=1, b=2, d=3.
a0, b0, d0 = 1.0, 2.0, 3.0
lam0 = b0-a0
wstar0 = lam0/(b0*d0)
def f(u):
    return u-1-math.log(u)

def numerical_period(h):
    low = brentq(lambda w: lam0*f(w)-h, math.exp(-h/lam0-3), 0.5)
    upper = brentq(lambda w: lam0*f(w)-h, 2.0, 2.0*h/lam0+30)
    def branch(w):
        q = max(h-lam0*f(w), 1.e-14)
        z = -math.exp(-1-q/a0)
        minus = -lambertw(z,0).real
        plus = -lambertw(z,-1).real
        return 1/(1-minus)+1/(plus-1)
    def g(theta):
        sn = math.sin(theta)
        w = low+(upper-low)*sn*sn
        return (upper-low)*math.sin(2*theta)*branch(w)
    integral = quad(g, 0, math.pi/2, epsabs=5.e-8, limit=150)[0]
    return wstar0*integral/a0

periods=[numerical_period(h) for h in (10.0,30.0,60.0)]
ratios=[t/h for t,h in zip(periods,(10.0,30.0,60.0))]
assert ratios[0]>ratios[1]>ratios[2]>1/(a0*b0*d0)
assert abs(ratios[-1]-1/(a0*b0*d0))<0.04
print('LIFTED_CENTER_SYMBOLIC_AND_FINITE_PERIOD_CHECK_OK')
print('finite_energies=', [10,30,60], 'physical_periods=', [round(z,9) for z in periods])
print('slopes=',[round(z,9) for z in ratios], 'asymptotic_slope=',1/(a0*b0*d0))
