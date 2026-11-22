#!/usr/bin/env python3
"""Standalone symbolic and finite checks for the rational-moment Hankel classification.

The universal positivity argument appears in RESULT.md; these checks supplement it.
Run with: python checker.py
Requires Python 3 and SymPy.
"""
import sympy as S

x, y, u, a = S.symbols('x y u a', real=True)
F = (3*u**3 - 12*u**2 + 9*u - 2
     + (-15*u**2 + 24*u - 9)*y
     + (9*u - 12)*y**2 - 5*y**3)
r = [1/((x+j)**2+y) for j in range(5)]
H2 = S.Matrix(2, 2, lambda i, j: r[i+j])
H3 = S.Matrix(3, 3, lambda i, j: r[i+j])
expected_H2 = (2*(x+1)**2-2*y-1)/(
    (x**2+y)*((x+1)**2+y)**2*((x+2)**2+y))
expected_H3 = 8*F.subs(u, (x+2)**2)/S.prod(
    ((x+j)**2+y)**p for j,p in enumerate([1,2,3,2,1]))
assert S.factor(H2.det() - expected_H2) == 0
assert S.factor(H3.det(method='domain-ge') - expected_H3) == 0
assert S.factor(S.discriminant(S.diff(F,y),y) + 36*(16*u**2-16*u-1)) == 0
assert S.factor(S.discriminant(F,u) + 108*(4*y+1)**3*(4*y**3+9*y**2+6*y+2)) == 0
assert S.factor(F.subs({u:(a+2)**2,y:(a+1)**2-S.Rational(1,2)})
    +(2*a+1)**2*(2*a+3)**2*(4*a**2+20*a+33)/8) == 0
assert S.factor(F.subs(y,0).subs(u,4)) == 34
assert F.subs({u:9,y:1}) == 350

# Exact rational checks: 3x3 Hankel determinants stay positive at all tested
# shifts in an interior parameter example. This is not an infinite proof.
for n in range(40):
    vals = [S.Rational(2, (n+j+1)**2+1) for j in range(5)]
    block = S.Matrix(3,3,lambda i,j:vals[i+j])
    assert block[:2,:2].det() > 0 and block.det() > 0

# Certified numerical illustrations of the unique root for rational a.
for a0 in [S.Rational(1,10),S.Rational(1,2),S.Integer(1), S.Integer(4), S.Integer(20)]:
    u0=(a0+2)**2
    limit=(a0+1)**2-S.Rational(1,2)
    assert F.subs({u:u0,y:0})>0 and F.subs({u:u0,y:limit})<0
    roots=S.polys.polytools.intervals(F.subs(u,u0),eps=S.Rational(1,1000000))
    positive=[t for (t,mult) in roots if t[1]>0 and t[0]>=0]
    assert len(positive)==1 and 0<positive[0][0] < positive[0][1] < limit

# Leading asymptotic coefficient strictly decreases in r>=0.
z=S.symbols('z',real=True)
g=3-15*z+9*z**2-5*z**3
assert S.factor(S.discriminant(S.diff(g,z),z)) < 0
assert g.subs(z,0)>0 and g.subs(z,1)<0
root=float(S.nroots(g)[0].as_real_imag()[0])
assert 0.22 < root < 0.23
print('PASS: five exact symbolic determinant/discriminant identities;')
print('PASS: exact rational examples and 40 shifted 3x3 blocks;')
print('PASS: five certified root brackets and asymptotic cubic sign tests.')
print('Asymptotic b^2/a^2 constant:',format(root,'.12f'))
