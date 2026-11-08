#!/usr/bin/env python3
"""Standalone exact and numerical checks for halving-chord moment reconstruction.

Requires SymPy; run: python verify.py
"""
from fractions import Fraction
from math import sqrt
from random import Random
import sympy as S


a, b, q, t = S.symbols('a b q t', real=True)
s = a + b
area2 = a*a*b*b - q*q

def from_integrals(k):
    u_side = S.integrate((b*b + a*a*t*t + 2*q*t)**k, (t, -1, 1))/2
    v_side = S.integrate((a*a + b*b*t*t + 2*q*t)**k, (t, -1, 1))/2
    return S.factor((a*u_side + b*v_side)/s)

formula = {
    1: s*s/3,
    2: s**4/5 - S.Rational(4, 3)*area2,
    3: s**6/7 - S.Rational(12, 5)*s*s*area2 + S.Rational(16, 5)*a*b*area2,
}
for k, target in formula.items():
    assert S.cancel(from_integrals(k) - target) == 0, ('symbolic', k)

# Exact rational shape inversions, including an obtuse generator and a rhombus.
shapes = [(S.Rational(3), S.Rational(2), S.Rational(18,5)),
          (S.Rational(1), S.Rational(1), S.Rational(0)),
          (S.Rational(4), S.Rational(1), S.Rational(-12,5)),
          (S.Rational(5,2), S.Rational(5,2), S.Rational(5,4))]
for aa,bb,qq in shapes:
    assert aa*aa*bb*bb > qq*qq
    sm = [S.factor(formula[k].subs({a:aa,b:bb,q:qq})) for k in (1,2,3)]
    ss = S.sqrt(3*sm[0]); area2_recovered = S.factor(S.Rational(3,4)*(ss**4/5 - sm[1]))
    prod_recovered = S.factor(S.Rational(5,16)/area2_recovered*(sm[2]-ss**6/7+S.Rational(12,5)*ss**2*area2_recovered))
    assert S.simplify(ss-(aa+bb))==0
    assert S.simplify(area2_recovered-(aa*aa*bb*bb-qq*qq))==0
    assert S.simplify(prod_recovered-aa*bb)==0

# Minimality: distinct rectangle and rhombus have same M2, M4.
ss=S.Rational(1); aaarea=S.Rational(3,16)
m2=ss**2/3; m4=ss**4/5-S.Rational(4,3)*aaarea**2
m6_rectangle=ss**6/7-S.Rational(12,5)*ss**2*aaarea**2+S.Rational(16,5)*aaarea**3
m6_rhombus=ss**6/7-S.Rational(8,5)*ss**2*aaarea**2
assert m6_rhombus>m6_rectangle and aaarea<ss**2/4
assert m2==S.Rational(1,3) and m4==S.Rational(1,5)-S.Rational(3,64)

# Sharp feasible interval and its endpoints, for rational parameter choices.
for j in range(1,18):
    area = S.Rational(j,100)
    rmin = area; rmax = ss**2/4
    for k in range(0,11):
        r = rmin + S.Rational(k,10)*(rmax-rmin)
        m6 = ss**6/7 - S.Rational(12,5)*ss**2*area**2+S.Rational(16,5)*r*area**2
        lo=ss**6/7 - S.Rational(12,5)*ss**2*area**2+S.Rational(16,5)*area**3
        hi=ss**6/7 - S.Rational(8,5)*ss**2*area**2
        assert lo <= m6 <= hi
        assert S.simplify((ss**2-4*r))>=0

# Independent numerical midpoint rule using actual Euclidean vectors, not symbolic polynomials.
u=(3.,0.); v=(1.2,1.6); al=3.; bl=2.; pp=al+bl; N=8192
numeric=[]
for k in (1,2,3):
    val=0.
    for j in range(N):
        tt=-1.+(2*j+1)/N
        d1=(v[0]+tt*u[0])**2+(v[1]+tt*u[1])**2
        d2=(u[0]+tt*v[0])**2+(u[1]+tt*v[1])**2
        val += (al*d1**k+bl*d2**k)/pp/N
    numeric.append(val)
A2=(u[0]*v[1]-u[1]*v[0])**2
pred=(pp**2/3, pp**4/5-4*A2/3, pp**6/7-12*pp**2*A2/5+16*al*bl*A2/5)
for got,expected in zip(numeric,pred):
    assert abs(got-expected) <= 1e-6*max(1.,abs(expected)), (got,expected)
print('VERIFY_OK symbolic_moment_identities=3 rational_inverse_shapes=4 feasibility_cases=187 midpoint_quadratures=3')
