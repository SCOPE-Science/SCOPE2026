#!/usr/bin/env python3
"""Exact checks for a quartic gradient map with alternating step sizes.
Run: python3 verify.py   (requires SymPy).
The implicit-function continuation in RESULT.md is a mathematical argument,
not an exhaustive computer-aided certificate.
"""
import sympy as s

x, a, b = s.symbols('x a b', real=True)
G = lambda step, z: s.expand(z - step*z*(z*z - 1))
F = s.expand(G(s.Rational(1, 2), G(2, x)))
P = s.factor(F-x)
expected = x*(x*x-1)*(2*x*x-1)*(4*x**4-12*x*x+7)/2
assert s.expand(P-expected) == 0, (P,expected)

positive = [s.sqrt(s.Rational(1, 2)), s.Integer(1),
            s.sqrt((3-s.sqrt(2))/2), s.sqrt((3+s.sqrt(2))/2)]
all_roots = [s.Integer(0)]+[sgn*z for z in positive for sgn in (-1,1)]
for z in all_roots:
    assert s.simplify(F.subs(x,z)-z)==0, z
assert len(set(map(str,all_roots)))==9
D=s.diff(F,x)
for z in [-s.Integer(1),s.Integer(1),-s.sqrt(s.Rational(1,2)),s.sqrt(s.Rational(1,2))]:
    assert s.simplify(D.subs(x,z))==0,z
for z in (s.sqrt((3-s.sqrt(2))/2),-s.sqrt((3-s.sqrt(2))/2)):
    assert s.simplify(D.subs(x,z)-(27-18*s.sqrt(2)))==0,z
for z in (s.sqrt((3+s.sqrt(2))/2),-s.sqrt((3+s.sqrt(2))/2)):
    assert s.simplify(D.subs(x,z)-(27+18*s.sqrt(2)))==0,z
assert D.subs(x,0)==s.Rational(9,2)
assert s.simplify(G(2,s.sqrt(s.Rational(1,2)))-s.sqrt(2))==0
assert s.simplify(G(s.Rational(1,2),s.sqrt(2))-s.sqrt(s.Rational(1,2)))==0
loss=lambda z: (z*z-1)**2/4
assert s.simplify(loss(s.sqrt(s.Rational(1,2)))-s.Rational(1,16))==0
assert s.simplify(loss(s.sqrt(2))-s.Rational(1,4))==0
assert s.simplify((loss(s.sqrt(2))+loss(s.sqrt(s.Rational(1,2))))/2-s.Rational(5,32))==0
assert 27-18*s.sqrt(2)>1
F_ab=s.expand(G(b,G(a,x)))
assert s.simplify(F_ab.subs(x,1)-1)==0
assert s.simplify(F_ab.subs(x,-1)+1)==0
assert s.simplify(s.diff(F_ab,x).subs(x,1)-(1-2*a)*(1-2*b))==0
assert s.simplify(s.diff(F_ab,x).subs(x,-1)-(1-2*a)*(1-2*b))==0
for z in [s.sqrt(s.Rational(1,2)),-s.sqrt(s.Rational(1,2))]:
    assert s.simplify((s.diff(F_ab,x)-1).subs({a:2,b:s.Rational(1,2),x:z})+1)==0
    # In the neighboring (a,b) schedule this non-minimum fixed point persists by IFT.
print('VERIFY_OK exact_epoch_factorization=1 fixed_points=9 attracting=4 repelling=5 loss_mean=5/32 IFT_nondegenerate=2')
