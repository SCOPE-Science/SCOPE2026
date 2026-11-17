#!/usr/bin/env python3
"""Exact symbolic checks for the resonant polynomial predator-prey map."""
import sympy as s
m,d,x,y=s.symbols('m d x y', positive=True)
S=m-1
k=(d+1)/S
a=d*S/(d+1)
b=m*k
H=m*x+a*y
e=H-S
X=s.expand(x*(m-H))
Y=s.expand(y*(-d+k*H))
assert s.simplify(X-(m*x*(1-x)-a*x*y))==0
assert s.simplify(Y-(-d*y*(1-y)+b*x*y))==0
assert s.simplify(m*X+a*Y-S-e*(1-m*x+d*y))==0
J=s.Matrix([X,Y]).jacobian([x,y])
# On the line H=S, use x=(S-a*y)/m.
J0=s.simplify(J.subs(x,(S-a*y)/m))
lam=s.simplify(2-m+(a+d)*y)
t=s.symbols('t')
assert s.factor(J0.charpoly(t).as_expr()-(t-1)*(t-lam))==0
assert s.simplify(a*k-d)==0
assert s.simplify(b-m*k)==0
# An entirely rational witness for the parameter family.
m0,d0=s.Rational(2),s.Rational(1)
a0=s.Rational(1,2);b0=s.Rational(4);k0=s.Rational(2)
X0=lambda u,v:u*(m0-m0*u-a0*v)
Y0=lambda u,v:v*(-d0+b0*u+d0*v)
q=(s.Rational(2,5),s.Rational(2,5))
assert (X0(*q),Y0(*q))==q
assert 1-m0*q[0]+d0*q[1]==s.Rational(3,5)
z=(s.Rational(3,5),s.Rational(1,5))
assert (X0(*z),Y0(*z))==(s.Rational(21,50),s.Rational(8,25))
assert 2*X0(*z)+s.Rational(1,2)*Y0(*z)==1
E=s.symbols('E')
assert s.expand(1-(1-E)**2*(1+2*E)-E**2*(3-2*E))==0
print('PASS: all exact symbolic identities, spectrum, and rational witness.')
