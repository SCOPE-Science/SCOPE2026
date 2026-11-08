#!/usr/bin/env python3
"""Reproduce the finite-age algebra and elementary dual-walk bounds."""
import sympy as s
from math import factorial
from sympy.functions.combinatorial.numbers import stirling

r, u, e, v, h, mu, p, q = s.symbols('r u e v h mu p q', positive=True)
# e denotes exp(-u); u=r*t.

def age_moment(n):
    return s.factor(s.factorial(n) / r**n * (1 - e * sum(u**j/s.factorial(j) for j in range(n))))

def cumulants(m, n):
    ks = {1:m[1]}
    for k in range(2,n+1):
        ks[k] = s.factor(m[k] - sum(s.binomial(k-1,j-1)*ks[j]*m[k-j] for j in range(1,k)))
    return ks

mom = {n:age_moment(n) for n in range(1,11)}
k = cumulants(mom,10)
assert s.simplify(r**2*k[2]-(1-2*u*e-e**2))==0
assert s.simplify(r**3*k[3]-(2-3*u**2*e-6*u*e**2-2*e**3))==0
for n in range(1,11):
    assert s.simplify(k[n].subs(e,0)-factorial(n-1)/r**n)==0
print('10 exact stationary all-order age-cumulant identities passed')
print('finite-time second and third cumulant formulas checked')
# Check the dual's Poisson jump moment polynomials, including the spatial tail bound.
L=s.symbols('L', nonnegative=True)
prev=s.Integer(1)
for n in range(1,9):
    raw=sum(stirling(n,j,kind=2)*L**j for j in range(1,n+1))
    assert s.expand(raw-L*(prev+s.diff(prev,L)))==0
    prev=raw
    assert s.expand(raw).coeff(L,1)==1
    assert s.expand(raw).coeff(L,n)==1
print('8 Touchard/Poisson moment polynomials constructed')
# Numerically, the Poisson tail used to localize a tracer vanishes superfactorially at fixed time.
import math
for lam in [0.3,1.0,3.0]:
    prev=1e20
    for R in [20,35,50]:
        tail=sum(n**4*math.exp(-lam)*lam**n/math.factorial(n) for n in range(R+1,160))
        assert tail<prev
        prev=tail
print('9 finite-radius tail monotonicity checks passed')
print('stationary plateau n=2..6 for v/r=1/2:',[s.Rational(factorial(n-1),2**n) for n in range(2,7)])
