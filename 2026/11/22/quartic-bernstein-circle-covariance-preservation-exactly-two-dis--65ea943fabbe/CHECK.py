#!/usr/bin/env python3
"""Exact Fourier coefficient verification for fourth-degree Bernstein circle sampling.

Python 3, SymPy; independent symbolic reconstruction and finite supplementary tests.
The finitary tests are not a proof of global positivity.
"""
import sympy as s
from math import cos, pi
from fractions import Fraction

u,c,d=s.symbols('u c d', real=True)
from math import comb

def bernstein(values):
    return s.expand(sum(s.binomial(4,j)*u**j*(1-u)**(4-j)*values[j] for j in range(5)))

def coefficient(P, parity):
    sign = 1 if parity==0 else -1
    a=sign*s.diff(P,u).subs(u,1)-s.diff(P,u).subs(u,0)
    b=sign*s.diff(P,u,3).subs(u,1)-s.diff(P,u,3).subs(u,0)
    return s.simplify(a),s.simplify(b)

Podd=bernstein([1,c,0,-c,-1]); Peven=bernstein([1,c,d,c,1])
assert s.simplify(s.integrate(Podd,(u,0,1)))==0
assert s.simplify(2*s.integrate(Peven,(u,0,1)) - s.Rational(2,5)*(2+2*c+d))==0
# C_k = 2*(A/(pi*k)^2 - B/(pi*k)^4)
assert coefficient(Podd,0)==(0,0)
assert coefficient(Podd,1)==(8-8*c,48-96*c)
assert coefficient(Peven,1)==(0,0)
assert coefficient(Peven,0)==(8-8*c,-192*c+144*d+48)
print('symbolic_coefficients_verified')

# Exact integer arithmetic cyclic order classification up to 300;
# generalized equidistribution argument in proof handles arbitrary orders.
for N in range(2,301):
    admissible=[]
    for p in range(1,N//2+1):
        if 2*p>=N: continue
        # a=pi*p/N; z=e^{2*pi*i*p/N}
        from math import gcd
        L=N//gcd(p,N)
        if L in (3,4): admissible.append(p)
    assert all(N*1==p*3 or N*1==p*4 for p in admissible)
print('root_of_unity_orders_checked')

# Evaluate finite modes: m=1..100, spatial frequencies k=1..150, a=pi/4 or pi/3
checks=0
for a in (pi/4,pi/3):
    for m in range(1,101):
        cc=cos(m*a)
        dd=cos(m*pi/2)
        for k in range(1,151):
            if m%2:
                if k%2==0: continue
                bracket=(1-cc)*(pi*k)**2-6+12*cc
                assert bracket >= -1e-9, (a,m,k,bracket)
            else:
                if k%2: continue
                bracket=(1-cc)*(pi*k)**2+24*cc-18*dd-6
                assert bracket >= -1e-9, (a,m,k,bracket)
            checks += 1
        if m%2==0:
            assert 2+2*cc+dd >= -1e-9
print('finite_mode_pairs_checked',checks)
