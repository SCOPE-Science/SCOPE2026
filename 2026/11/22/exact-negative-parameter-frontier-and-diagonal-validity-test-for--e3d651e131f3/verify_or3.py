#!/usr/bin/env python3
"""Independent symbolic identities and exact endpoint witness for the OR3 copula.

The universal sign arguments are proved in RESULT.md, not by the finite tests here.
Requires Python 3 and SymPy.
"""
from fractions import Fraction
from math import factorial
import sympy as sp

x, y, a, b = sp.symbols('x y a b', real=True)
t = (1 - x) * (1 - y)
z = sp.exp(a * t)
h = x + y - 3*x*y
u = x*y*t
C = (b + 1)*x*y/(b + z)
N = (b + z)**2 + a*z*(b + z)*h + a**2*z*(z-b)*u

assert sp.simplify(sp.diff(C,x,y) - (b+1)*N/(b+z)**3) == 0

T, S, Z = sp.symbols('T S Z', real=True)
N2=(b+Z)**2 +a*Z*(b+Z)*(-1+2*S-3*T) +a*a*Z*(Z-b)*T*(1-S+T)
assert sp.diff(N2,S,2) == 0
N_axis = (b+Z)*(b+Z+a*Z*(1-T))
assert sp.expand(N2.subs(S,1+T)-N_axis)==0
v=sp.symbols('v', real=True)
N_diag=(b+Z)**2+a*Z*(b+Z)*(1-v)*(3*v-1)+a*a*Z*(Z-b)*v**2*(1-v)**2
assert sp.expand(N2.subs({T:v*v,S:2*v})-N_diag)==0

# The admissible parameter a=2, b=1 has nonnegative diagonal density:
# N=(1+Z)(1+Z+2Zh)+4Z(Z-1)u;
# h >= -1+v because 4v-3v²>=v; and 1-exp(-2v²)<=2v²<=2v.
assert sp.simplify((4*v-3*v**2)-v-3*v*(1-v))==0

# At the inadmissible pair (a,b)=(21,20), x=y=2/3, z=exp(7/3):
Zval=sp.symbols('Zval')
witness=sp.factor(N.subs({a:21,b:20,x:sp.Rational(2,3),y:sp.Rational(2,3)}))
polynomial=sp.Rational(400)+sp.Rational(-3560,9)*Zval+sp.Rational(205,9)*Zval**2
assert sp.simplify(witness.subs({sp.exp(sp.Rational(7,3)):Zval})-polynomial)==0
assert polynomial.subs(Zval,10)==-sp.Rational(11500,9)
assert polynomial.subs(Zval,11)==-1195

# Rigorous rational enclosure 10 < exp(7/3) < 11.
r=Fraction(7,3)
E4=sum(r**j/factorial(j) for j in range(5))
E6=sum(r**j/factorial(j) for j in range(7))
# Each ratio of successive terms in the tail after n=4 is <= r/6 < 1.
tail_upper=(r**5/factorial(5))/(1-r/6)
assert E6>10 and E4+tail_upper<11
print('PASS: exact mixed-derivative identity, affine fixed-product reduction,')
print('      axis and diagonal restrictions, and rational exponential witness.')
print('bounds:', str(E6), '< exp(7/3) <',str(E4+tail_upper))
