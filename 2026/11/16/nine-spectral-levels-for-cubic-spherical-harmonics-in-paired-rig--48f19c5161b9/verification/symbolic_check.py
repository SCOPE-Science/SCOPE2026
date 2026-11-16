#!/usr/bin/env python3
"""Exact symbolic identities underlying the cubic spherical-sector spectrum."""
import sympy as s
m=s.symbols('m',positive=True,integer=True)
d=m+2
E=lambda k:s.factor(s.factorial(k)/s.rf(1+m/s.Integer(2),k))
c0=s.Rational(4)/(m+4)
u0=s.factor(E(3)-c0*E(2))
a0=E(3)
b0=s.factor(E(3)-2*c0*E(2)+c0*c0*E(1))
assert s.simplify(u0**2/a0/b0-m/(3*(m+4)))==0
c1=s.Rational(2)/(m+4)
W=lambda k:s.factor(E(k)-E(k+1))
u1=s.factor(W(2)-c1*W(1))
a1=W(2)
b1=s.factor(W(2)-2*c1*W(1)+c1*c1*W(0))
assert s.simplify(u1**2/a1/b1-(m+2)/(2*(m+4)))==0
eta=s.symbols('eta',real=True)
K=s.Matrix([[0,eta,0,-s.Rational(1,3)],
            [eta,0,1,0],
            [0,1,0,eta],
            [-s.Rational(1,3),0,eta,0]])
t=s.symbols('t')
expected=s.expand((t**2-(s.sqrt(s.Rational(4,9)+eta**2)+s.Rational(1,3))**2)*
                  (t**2-(s.sqrt(s.Rational(4,9)+eta**2)-s.Rational(1,3))**2))
assert s.simplify(K.charpoly(t).as_expr()-expected)==0
h2=(m+2)*(m-1)/2
h3=m*(m-1)*(m+4)/6
assert s.simplify(4+3*m+2*h2+h3-d*(d-1)*(d+4)/6)==0
assert s.simplify(m+h3-d*(d-1)*(d-2)/6)==0
assert s.factor(u0)>0 if m.is_number else s.factor(u0/m).is_positive is True
assert s.factor(u1)>0 if m.is_number else s.factor(u1/m).is_positive is True
# Show the outer branch is strictly greater than the fixed 1/pi branch.
assert s.factor((7*d+2)/(d+2)-4)==3*(d-2)/(d+2)
print('Exact beta-ratio, characteristic-polynomial, multiplicity, and ordering identities pass.')
