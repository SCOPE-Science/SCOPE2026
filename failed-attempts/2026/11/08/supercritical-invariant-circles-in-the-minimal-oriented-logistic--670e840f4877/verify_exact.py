#!/usr/bin/env python3
"""Exact symbolic and independent numerical checks for a cyclic logistic map.
Requires SymPy. The symbolic identities do not replace the standard
Neimark--Sacker theorem invoked in the proof.
"""
from sympy import symbols, I, sqrt, conjugate, factor, simplify, expand_complex, re
from math import sqrt as fsqrt

s = symbols('s', positive=True, real=True)
q = sqrt(s)
delta = 2/(1+s)
r = 1+delta
b = 2-r
lam = b+I*delta*q
beta = r*(-1-I*q)
h = -2*r/(1-b)
k = (s+1)*(s+3)/(2*(3*s-1))
gamma = r*(-2+I*q)*h
C = gamma + 2*beta*k
l1 = -(s+3)**3/(s+1)**2
assert simplify(lam*conjugate(lam)-1) == 0
assert simplify((conjugate(lam)**2-lam)*k-beta) == 0
assert simplify(h*(lam*conjugate(lam)-b)+2*r) == 0
assert simplify(re(expand_complex(conjugate(lam)*C))-l1) == 0
assert simplify(re(expand_complex(conjugate(lam)*C)) + (s+3)**3/(s+1)**2) == 0
assert simplify((1+s)**2/(s+3)**3 * (-l1) - 1) == 0
assert simplify(h*(1+s)**2/(s+3)**3 + (1+s)**2/(s+3)**2) == 0

# Independently reconstruct complex Fourier update for the actual 3-site map.
import cmath
omega = cmath.exp(2j*cmath.pi/3)
for a, rr, x in [(0.5,2.1,[0.25,0.51,0.39]), (0.2,2.5,[0.4,0.5,0.2]), (0.7,1.3,[0.21,0.3,0.5])]:
    xx = 1-1/rr
    u = [y-xx for y in x]
    m = sum(u)/3
    z = sum(u[j]*omega**(-j) for j in range(3))/3
    sig=fsqrt(3)*a
    rhs_m=(2-rr)*m-rr*m*m-2*rr*(abs(z)**2)
    rhs_z=(2-rr+1j*sig*(rr-1))*z + rr*(-2+1j*sig)*m*z + rr*(-1-1j*sig)*z.conjugate()**2
    yp=[rr*x[j]*(1-x[j]+a*(x[(j+1)%3]-x[(j-1)%3])) for j in range(3)]
    up=[y-xx for y in yp]
    mp=sum(up)/3
    zp=sum(up[j]*omega**(-j) for j in range(3))/3
    assert abs(mp-rhs_m)<1e-12 and abs(zp-rhs_z)<1e-12

# A convergence diagnostic only (not used to prove the bifurcation).
a=0.5
rc=15/7
eps=0.001
rr=rc+eps
x=[1-1/rr+0.001,1-1/rr-0.002,1-1/rr+0.0013]
rads=[]
for t in range(100000):
    y=[rr*x[j]*(1-x[j]+a*(x[(j+1)%3]-x[(j-1)%3])) for j in range(3)]
    x=[min(1,max(0,v)) for v in y]
    if t>90000 and t%100==0:
        z=sum((x[j]-(1-1/rr))*omega**(-j) for j in range(3))/3
        rads.append(abs(z))
observed=sum(rads)/len(rads)
predicted=fsqrt(float((1+3*a*a)**2/(3+3*a*a)**3)*eps)
assert abs(observed/predicted-1)<0.03, (observed,predicted)
print('VERIFY_OK formal_identities=7 Fourier_samples=3 numerical_diagnostic=1 s=3/4 l1=-3375/196 radial_ratio=%.6f' % (observed/predicted))
