#!/usr/bin/env python3
"""Symbolic and finite checks for two-scale geometric radial kernels on regular trees.

These tests support, but do not replace, the spectral-measure proof.
Requires SymPy (for exact polynomial arithmetic); NumPy for finite Gram checks.
"""
import itertools
import sympy as sp
import numpy as np

q, u, s, r, t = sp.symbols('q u s r t', positive=True, real=True)
F = lambda a: (1 - a**2)/(1+q*a*a-a*t)
v = 1/(q*u)
B = q*(1-u*u)/(q*q*u*u-1)
A = (q+1)*(q*u*u-1)/(q*q*u*u-1)
T = 1/u+q*u
assert sp.simplify(F(u)-B*F(v)) == 0
assert sp.simplify(A+B-1) == 0
assert sp.simplify(B*v+A*T/(q+1)-u) == 0
assert sp.simplify((1-u*u)/(1-u*t+q*u*u)-F(u)) == 0
R = sp.factor(F(r)/F(s))
assert sp.simplify(R-(1-r*r)/(1-s*s)*(1+q*s*s-s*t)/(1+q*r*r-r*t)) == 0
D = sp.factor(sp.diff(R,t))
# After clearing square-positive denominators, derivative sign is 1-q*r*s.
assert sp.simplify(D / ((r-s)*(1-q*r*s)*(1-r*r)/(1-s*s)/(1+q*r*r-r*t)**2)) == 1
C = sp.factor(R.subs(s,1/(q*r)))
assert sp.simplify(sp.diff(C,t)) == 0
assert sp.factor(C-q*(1-r*r)/(q*q*r*r-1)) == 0

# Exact spectral collapse for q=2, r=4/5, s=5/8, lambda=6/13.
Q, U, S, L = 2, sp.Rational(4,5), sp.Rational(5,8), sp.Rational(6,13)
T0 = 1/U+Q*U
p0,p1 = sp.Integer(1),T0/(Q+1)
phis=[p0,p1]
for n in range(1,35):
    phis.append(sp.simplify((T0*phis[-1]-phis[-2])/Q))
for n in range(0,35):
    assert sp.simplify(U**n-L*S**n-sp.Rational(7,13)*phis[n]) == 0

# Build the radius-three finite rooted ball of the (q+1)-regular tree (q=2).
# The first-level branching is q+1; deeper branching is q.
verts=[()]
for depth in range(1,5):
    if depth == 1:
        verts += [(j,) for j in range(Q+1)]
    else:
        verts += [v+(j,) for v in verts if len(v)==depth-1 for j in range(Q)]
assert len(verts)==1+3+6+12+24

def distance(x,y):
    c=0
    for a,b in zip(x,y):
        if a!=b:break
        c+=1
    return len(x)+len(y)-2*c

Dmat=np.array([[distance(x,y) for y in verts] for x in verts], dtype=np.float64)
for rr,ss in [(0.8,0.5),(0.8,0.625),(0.6,0.4)]:
    k=(rr**Dmat)-(0.05)*(ss**Dmat)
    assert np.linalg.eigvalsh(k)[0] > 0
# At qrs=1 boundary, each finite Gram remains at least semidefinite.
k=(0.8**Dmat)-(6/13)*(0.625**Dmat)
assert np.linalg.eigvalsh(k)[0] > -5e-12
print('ALL_CHECKS_PASSED: resolvent, spherical recurrence, spectral ratio, 35 exact moments, 4 finite Gram tests')
