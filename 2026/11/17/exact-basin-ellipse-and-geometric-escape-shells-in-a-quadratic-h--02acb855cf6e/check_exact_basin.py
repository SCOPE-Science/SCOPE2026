#!/usr/bin/env python3
"""Reproduce exact identities and illustrative finite-time checks for a quadratic map.
Requires SymPy (tested with Python 3). The mathematical proof is in RESULT.md.
"""
import sympy as sp
x, y, s, d = sp.symbols('x y s d', real=True)
q = x*x + x*y + y*y + (x+y)/sp.Integer(10)
r = sp.Rational(4, 15)
g = s/sp.Integer(5) + 3*s*s
h = (sp.sqrt(1+300*s)-1)/30
centered = (x+sp.Rational(1,30))**2 + (x+sp.Rational(1,30))*(y+sp.Rational(1,30)) + (y+sp.Rational(1,30))**2 - sp.Rational(1,300)
assert sp.expand(q-centered)==0
assert sp.expand(q.subs({x:s,y:s})-g)==0
assert sp.simplify(g.subs(s,r)-r)==0
assert sp.simplify(g.subs(s,h)-s)==0
assert sp.simplify(sp.diff(h,s).subs(s,r)-sp.Rational(5,9))==0
assert sp.expand(g.subs(s,r+d)-r-sp.Rational(9,5)*d-3*d*d)==0
assert sp.simplify(2*sp.pi/sp.sqrt(3)*(r+sp.Rational(1,300)) - 9*sp.sqrt(3)*sp.pi/50)==0
assert sp.simplify((9*sp.sqrt(3)*sp.pi/50)/(sp.Rational(8,15)**2)-81*sp.sqrt(3)*sp.pi/128)==0
# Verify representative inverse-iterate shells using 70-digit arithmetic.
H = sp.Rational(1,2)
T=sp.N(H,70)
for n in range(1,12):
    v=sp.N(h.subs(s,T),70)
    assert float(v)<float(T) and float(v)>float(r)
    T=v
# An exact interval-boundary test; arbitrary finite samples are not an exhaustive dynamical proof.
for X,Y in [(sp.Rational(1,3),sp.Rational(-1,4)),(0,0),(r,r),(-1,-1),(sp.Rational(1,10),sp.Rational(1,10))]:
    v=sp.factor(q.subs({x:X,y:Y}))
    if v<r:
        if v>=0: assert (v==0 or (0<g.subs(s,v)<v))
        else: assert v<g.subs(s,v)<0
    elif v==r:
        assert g.subs(s,v)==r
    else:
        assert g.subs(s,v)>v
print('EXACT_QUADRATIC_BASIN_AND_ESCAPE_IDENTITIES_OK')
