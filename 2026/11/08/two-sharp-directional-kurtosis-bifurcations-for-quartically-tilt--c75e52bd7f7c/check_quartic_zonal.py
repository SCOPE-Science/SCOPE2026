#!/usr/bin/env python3
"""Exact independent checks of weighted spherical fourth-moment identities.
Only science and reproducibility; no external dependencies other than SymPy.
"""
from fractions import Fraction as F
from math import comb, factorial
import sympy as s

n,u,t=s.symbols('n u t', positive=True)
Z=(n*(n+2)+3*u)/(n*(n+2))
D=(n+2)*(n+4)+u*(3+12*t)
N=3*(n+4)*(n+6)+u*(9+72*t+24*t*t)
C=(n+4)*(n*(n+2)+3*u)/(n+6)
K=C*N/D**2
Q=(n+2)*(n+4)-15*u
assert s.factor(s.diff(N,t)*D-2*N*s.diff(D,t)-48*u*(Q*t-6*(n+4)))==0
B=-(n-10)*(n+2)*(n+4)**2+(12*n*n+180*n+528)*u+45*u*u
assert s.factor(N.subs(t,1)*D.subs(t,0)**2-N.subs(t,0)*D.subs(t,1)**2+24*u*B)==0
assert s.factor(B.subs(u,0)+(n-10)*(n+2)*(n+4)**2)==0
m=(n*n-16)/15
uc=(n+4)*(s.sqrt(9*n*n+48*n+384)-2*n-22)/15
for j in range(11,90):
 assert 0<float(uc.subs(n,j))<float(m.subs(n,j))
print('SYMBOLIC_DERIVATIVE_AND_ENDPOINT_DIFFERENCE_IDENTITIES_OK')

def doublefact(k):
 return 1 if k<1 else k*doublefact(k-2)

def sphere_even(n,a,b):
 return F(doublefact(2*a-1)*doublefact(2*b-1),1) / F(__import__('math').prod(n+2*i for i in range(a+b)),1)

def direct(n,u,A,B):
 u=F(u); Z=1+3*u/F(n*(n+2))
 # independent exact moment expansion for q=A*x1+B*x2
 def moment(order):
  def mixed(degree):
   v=F(0)
   for k in range(degree+1):
    if k%2 or (degree-k)%2:continue
    v+=comb(degree,k)*A**k*B**(degree-k)*sphere_even(n,k//2,(degree-k)//2)
   return v
  return (mixed(order)+u*sum(F(comb(order,k))*A**k*B**(order-k)*sphere_even(n,(k+4)//2,(order-k)//2) for k in range(order+1) if k%2==0 and (order-k)%2==0))/Z
 q2=direct2=moment(2)
 q4=moment(4)
 return q4/q2**2
for j in range(3,25):
 for v in [F(1,7),F(2),F(19,3),F(60)]:
  for A,B in [(F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(2),F(3))]:
   tt=F(A*A,A*A+B*B)
   rhs=K.subs({n:j,u:s.Rational(v.numerator,v.denominator),t:s.Rational(tt.numerator,tt.denominator)})
   assert s.Rational(direct(j,v,A,B))==rhs,(j,v,A,B)
print('DIRECT_EXACT_INDEPENDENT_SPHERICAL_MONOMIAL_CHECKS_OK',22*4*4)
# compare global classification for rational parameters sampled on grid, with exact endpoint checks
for j in range(3,45):
 for v in [s.Rational(1,17),s.Rational(1,4),s.Rational(2),s.Rational(10),s.Rational(100),s.Rational(10000)]:
  start=min([s.Rational(0),s.Rational(1)],key=lambda xx:K.subs({n:j,u:v,t:xx}))
  candidates=[s.Rational(0),s.Rational(1)]
  xstar=s.cancel((6*(n+4)/Q).subs({n:j,u:v}))
  if xstar>0 and xstar<1:candidates.append(xstar)
  hi=max(candidates,key=lambda xx:K.subs({n:j,u:v,t:xx}))
  lo=min(candidates,key=lambda xx:K.subs({n:j,u:v,t:xx}))
  samples=[s.Rational(i,80) for i in range(81)]
  hlo=[K.subs({n:j,u:v,t:xx}) for xx in samples]
  assert K.subs({n:j,u:v,t:lo})<=min(hlo)
  assert K.subs({n:j,u:v,t:hi})>=max(hlo)
print('EXACT_FULL_CLASSIFICATION_GRID_DIAGNOSTICS_OK',42*6*81)

# analytic stability when an interior minimum exists: exact identity as rational functions
xstar=6*(n+4)/Q
Dstar=s.factor(D.subs(t,xstar))
rstar=s.factor(N.subs(t,xstar)/Dstar**2)
assert s.factor(N/D**2-rstar-24*u*Q/Dstar*(t-xstar)**2/D**2)==0
print('EXACT_INTERIOR_STABILITY_IDENTITY_OK')

# Lower even-power axial tilt provides a structural contrast: no interior minimum.
D2=n+2+u+2*u*t
N2=n+4+u+4*u*t
assert s.factor(s.diff(N2,t)*D2-2*N2*s.diff(D2,t)+8*u*(1+u*t))==0
print('QUADRATIC_TILT_STRICT_MONOTONICITY_OK')

print('ALL_CHECKS_PASSED')
