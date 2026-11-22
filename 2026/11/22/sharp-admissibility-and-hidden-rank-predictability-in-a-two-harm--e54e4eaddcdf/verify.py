#!/usr/bin/env python3
"""Exact and grid sanity checks for the two-harmonic cosine-copula phase theorem.
Run with Python 3 and SymPy. The symbolic proof is in RESULT.md.
"""
import sympy as S
x,y,z,b,a=S.symbols('x y z b a',real=True)
P=1+2*a*x*y+2*b*(2*x*x-1)*(2*y*y-1)
assert S.expand(P.subs({x:1,y:-z}))==1-2*b-2*a*z+4*b*z*z
assert S.simplify(P.subs({x:S.sqrt(z),y:-S.sqrt(z)})-(1-2*a*z+2*b*(2*z-1)**2))==0
assert S.simplify((1-2*b-2*a*z+4*b*z*z).subs(z,a/(4*b))-(1-2*b-a*a/(4*b)))==0
assert S.simplify((1-2*b-2*a*z+4*b*z*z).subs(z,1)-(1+2*b-2*a))==0
assert S.simplify((4*b-31*b*b/4).subs(b,S.Rational(8,31))-S.Rational(16,31))==0
assert S.simplify(4*S.Rational(8,31)*(1-2*S.Rational(8,31))-S.Rational(480,961))==0
assert S.simplify((S.Rational(1,2)+b)**2+b*b/4-(S.Rational(1,4)+b+5*b*b/4))==0
assert S.simplify((1+2*b)/2-2*S.sqrt(b*(1-2*b))).subs(b,S.Rational(1,6))==0
assert S.simplify(4*b*(1-2*b)-S.Rational(1,2)+8*(b-S.Rational(1,4))**2)==0
# Spectral cosine orthogonality, on [0,1], is exact.
u=S.symbols('u',real=True)
phi=lambda j:S.sqrt(2)*S.cos(2*S.pi*j*u)
for j in [1,2]:
 assert S.integrate(phi(j),(u,0,1))==0
 assert S.integrate(u*phi(j),(u,0,1))==0
 for k in [1,2]:
  assert S.simplify(S.integrate(phi(j)*phi(k),(u,0,1))-(1 if j==k else 0))==0
  assert S.simplify(S.integrate(S.sin(2*S.pi*j*u)*S.cos(2*S.pi*k*u),(u,0,1)))==0
# Integral of the squared conditional CDF deviation.
for j in [1,2]:
 assert S.integrate(S.cos(2*S.pi*j*u)**2,(u,0,1))==S.Rational(1,2)
 assert S.integrate(S.sin(2*S.pi*j*u)**2,(u,0,1))==S.Rational(1,2)

# Exact conditional-CDF squared integral and both classical concordances.
v=S.symbols('v',real=True)
H=v+a/S.pi*S.cos(2*S.pi*u)*S.sin(2*S.pi*v)+b/(2*S.pi)*S.cos(4*S.pi*u)*S.sin(4*S.pi*v)
I=S.integrate(S.expand((H-v)**2),(u,0,1))
xi=S.simplify(6*S.integrate(I,(v,0,1)))
assert S.simplify(xi-3*(a*a+b*b/4)/(2*S.pi**2))==0
C=u*v+a/(2*S.pi**2)*S.sin(2*S.pi*u)*S.sin(2*S.pi*v)+b/(8*S.pi**2)*S.sin(4*S.pi*u)*S.sin(4*S.pi*v)
cdens=1+2*a*S.cos(2*S.pi*u)*S.cos(2*S.pi*v)+2*b*S.cos(4*S.pi*u)*S.cos(4*S.pi*v)
rho=S.simplify(12*S.integrate(S.integrate(C,(u,0,1)),(v,0,1))-3)
assert rho==0
tau=S.simplify(4*S.integrate(S.integrate(S.expand(C*cdens),(u,0,1)),(v,0,1))-1)
assert tau==0

# Strict exact rational interior and exterior probes (not full-domain proof).
from fractions import Fraction as F
cases=[(F(0),F(0),True),(F(1,2),F(1,4),True),
       (F(2,3),F(1,6),True),(F(7,10),F(1,4),True),
       (F(3,4),F(1,4),False),(F(1,10),F(-1,2),False),
       (F(1,4),F(-1,4),True),(F(1,2),F(1,2),False)]
for A,B,inside in cases:
 # Check exact min across z as a quadratic/endpoint problem.
 if B<0: m=1+2*B-2*abs(A)
 elif B==0: m=1-2*abs(A)
 elif abs(A)<=4*B: m=1-2*B-abs(A)**2/(4*B)
 else: m=1+2*B-2*abs(A)
 assert (m>=0)==inside,(A,B,m)
print('PASS exact algebra, trigonometric orthogonality, sharp phase contacts, and independent rational probes')
