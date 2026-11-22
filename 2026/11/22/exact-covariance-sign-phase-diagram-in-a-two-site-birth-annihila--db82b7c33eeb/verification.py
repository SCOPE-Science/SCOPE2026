#!/usr/bin/env python3
"""Standalone exact checks of a two-site reaction-transport covariance theorem.
Requires Python 3 and SymPy. Run: python verification.py
"""
import sympy as sp

t, r = sp.symbols('t r', positive=True)
D = r**2 + 3*r*t + r + 2*t**2 + 3*t
Z = (r+t)*D
p = sp.Matrix([
    (r**3+2*r**2*t+r**2+2*r*t+t**2)/Z,
    t/D,
    t*(r+2*t)/D,
    t*(r**2+2*r*t+r+t)/Z,
])
Q = sp.Matrix([
    [-t,  0,       t,       0],
    [ t, -(2*t+r), 0,       t+r],
    [ 0,  1,     -(1+r),    r],
    [ r,  0,       t,     -(t+r)],
])
assert sp.simplify(sum(p)-1)==0
assert all(sp.cancel(x)==0 for x in Q.T*p)
P = (r**5+(4*t+2)*r**4+(4*t**2+6*t+1)*r**3+
     (3*t**2+3*t)*r**2+3*t**2*(1-t)*r+t**3*(1-2*t))
c = sp.factor(p[0]*p[3]-p[1]*p[2])
assert sp.factor(c-t*P/Z**2)==0
assert sp.factor(c.subs(r,0)-(1-2*t)/(2*t+3)**2)==0
assert sp.limit(r*c,r,sp.oo)==t
assert sp.simplify(P.subs(t,1)-(r**5+6*r**4+11*r**3+6*r**2-1))==0
assert sp.diff(P,t).subs({t:sp.Rational(1,2),r:0}) == -sp.Rational(1,4)
assert sp.diff(P,r).subs({t:sp.Rational(1,2),r:0}) == sp.Rational(3,8)
# Rational checks at a mesh spanning all sign regimes.
from fractions import Fraction
for a in [Fraction(1,6),Fraction(1,2),Fraction(2,3),Fraction(1,1)]:
    for x in [Fraction(0),Fraction(1,20),Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(5)]:
        vals = [sp.Rational(v.numerator,v.denominator) for v in (a,x)]
        pp = [sp.factor(pi.subs({t: vals[0],r: vals[1]})) for pi in p]
        qq = Q.subs({t:vals[0],r:vals[1]})
        assert all(v >= 0 for v in pp)
        assert sum(pp)==1
        assert all(v==0 for v in qq.T*sp.Matrix(pp))
print('PASS: symbolic stationary generator, normalization, covariance polynomial, endpoints, and 24 rational-state tests')
