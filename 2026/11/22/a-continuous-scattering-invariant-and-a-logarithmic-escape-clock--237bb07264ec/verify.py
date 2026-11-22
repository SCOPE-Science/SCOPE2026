#!/usr/bin/env python3
"""Standalone science checks for the scattering clock; diagnostics are not a proof."""
from fractions import Fraction as Q
import math
import sympy as sp
from scipy.integrate import solve_ivp
x, p, q = sp.symbols('x p q', positive=True, real=True)
e = q*x
xdot = -q*p*x*x
qdot = 4*x
pdot = 1-p+2*e*p*p
edot = sp.expand(qdot*x+q*xdot)
assert sp.simplify(edot-x*x*(4-q*q*p)) == 0
assert sp.simplify(xdot/x+q*qdot/4-e*(1-p)) == 0
assert Q(1,2)+2*Q(0)*Q(1,4)>0
assert -1+8*Q(1,10)<0
assert 4-Q(3)**2*Q(1,2)<0

def ode(t, s):
    xx, pp, qq=s
    return [-qq*pp*xx**2, 1-pp+2*qq*xx*pp**2, 4*xx]
times=[100.,1000.,10000.,100000.]
r=solve_ivp(ode, (0, times[-1]), [0.02, 1., 4.], t_eval=times, rtol=1e-11, atol=1e-13)
assert r.success
Js=[]
for tt, (xx,pp,qq) in zip(r.t, r.y.T):
    assert xx>0 and qq>3 and 0.5<pp<2 and 0<qq*xx<0.1
    Js.append(math.log(xx)+qq*qq/8)
assert all(Js[j]>Js[j+1] for j in range(len(Js)-1))
assert abs(times[-1]*r.y[2,-1]*r.y[0,-1]-1) < 0.08
assert abs(times[-1]*(r.y[1,-1]-1)-2) < 0.15
print('SCATTER_VERIFY_OK')
