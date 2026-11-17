#!/usr/bin/env python3
"""Exact algebraic checks for the synchronous two-cycle theorem.

Requires Python 3 and SymPy. This program checks identities; the stated
full parameter inequalities also follow analytically from the proof.
"""
from fractions import Fraction
import sympy as s

R, a, b, w=s.symbols('R a b w', real=True)
S=1+a+b
delta=s.sqrt(R**2-4)
qplus=(R+2+delta)/2
qminus=(R+2-delta)/2
sp=qplus/(R*S)
sm=qminus/(R*S)
f=lambda z:(1+R)*z-R*S*z*z
assert s.simplify(f(sp)-sm)==0
assert s.simplify(f(sm)-sp)==0
assert s.simplify(qplus*qminus-(R+2))==0
assert s.simplify(qplus+qminus-(R+2))==0

# Product of the two diagonal-state Jacobians, as a polynomial in C/S.
Aplus=s.simplify(1+R-R*S*sp)
Aminus=s.simplify(1+R-R*S*sm)
assert s.simplify(Aplus*Aminus-1)==0
cross=s.simplify((Aplus*sm+Aminus*sp)*R)
assert s.simplify(cross-(R+2)*(R-1)/S)==0
assert s.simplify(R**2*sp*sm-(R+2)/S**2)==0
C=s.Matrix([[1,a,b],[b,1,a],[a,b,1]])
I=s.eye(3)
Jplus=Aplus*I-R*sp*C
Jminus=Aminus*I-R*sm*C
P=(I-(R+2)*(R-1)*C/S+(R+2)*(C/S)**2)
for z in (Jminus*Jplus-P):
    assert s.simplify(z)==0

# The complex-eigenvalue formula follows by the Fourier modes of C.
eigplus=1-(a+b)/2+s.I*s.sqrt(3)*(a-b)/2
eigminus=s.conjugate(eigplus)
assert s.simplify(eigplus*eigminus-((1-(a+b)/2)**2+s.Rational(3,4)*(a-b)**2))==0
poly=lambda ww:1-(R+2)*(R-1)*ww+(R+2)*ww**2
assert s.factor(poly(1))==5-R**2
assert s.factor(poly(w)-1)==(R+2)*w*(w-(R-1))

r=Fraction(12,5)
expected={Fraction(1,100):Fraction(-12049,14450),
          Fraction(1,10):Fraction(-229,200),
          Fraction(1,2):Fraction(-53,200)}
for c, m in expected.items():
    ww=(1-c)/(1+2*c)
    exact=1-(r+2)*(r-1)*ww+(r+2)*ww**2
    assert exact==m
assert abs(expected[Fraction(1,100)])<1
assert expected[Fraction(1,10)]<-1
assert abs(expected[Fraction(1,2)])<1
assert 5-r*r==Fraction(-19,25)

# Sharp threshold lies strictly between 2.35 and 2.4, below sqrt(6).
g=lambda x:x**3-3*x-6
assert g(Fraction(47,20))<0<g(Fraction(12,5))
assert r*r<Fraction(6)
print('SYNC_LOTKA_VOL_TWOCYCLE_IDENTITIES_OK')
