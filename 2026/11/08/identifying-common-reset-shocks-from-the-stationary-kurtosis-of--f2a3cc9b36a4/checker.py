#!/usr/bin/env python3
"""Independent algebraic and integral checks for the shared-clock reset theorem.
Requires Python 3 with sympy and mpmath. All model parameters are positive
except the admissible common-clock intensity, which may be zero.
"""
import math
import random
from fractions import Fraction
import mpmath as mp
import sympy as sp

L,R,Q,c=sp.symbols('L R Q c', positive=True)
r,q=R-c,Q-c
m02=2*L**2/Q
m04=24*L**4/Q**2
m20=2*m02/R
m22=sp.factor((2*m04+2*L**2*m20)/(R+Q-c))
m40=sp.factor(12*m22/R)
K=sp.factor(m40/m20**2)
assert sp.simplify(m22-8*L**4*(6*R+Q)/(R*Q**2*(R+Q-c)))==0
assert sp.simplify(m40-96*L**4*(6*R+Q)/(R**2*Q**2*(R+Q-c)))==0
assert sp.simplify(K-6*(6*R+Q)/(R+Q-c))==0
assert sp.simplify(sp.diff(K,c)-6*(6*R+Q)/(R+Q-c)**2)==0
assert sp.simplify(K.subs({R:Q,c:0})-21)==0
assert sp.simplify(K.subs({R:Q,c:Q})-42)==0
assert sp.simplify(K.subs({R:Q,c:Q/2})-28)==0
# Lagged second-order covariances obey the exact first-degree semigroup
# generator equations L x=-R*x and L omega=-Q*omega.
t=sp.symbols('t', real=True, nonnegative=True)
xlag=m20*sp.exp(-R*t)
wlag=m02*sp.exp(-Q*t)
assert sp.simplify(sp.diff(xlag,t)+R*xlag)==0
assert sp.simplify(sp.diff(wlag,t)+Q*wlag)==0
# The cross moment x*omega has pure negative reset drift
# -(R+Q-c)*x*omega, implying stationary E[x*omega]=0.
assert sp.simplify(r+q+c-(R+Q-c))==0

# Generator recurrences, each exactly zero using the claimed stationary moments.
assert sp.simplify(2*L**2-Q*m02)==0
assert sp.simplify(12*L**2*m02-Q*m04)==0
assert sp.simplify(2*m02-R*m20)==0
assert sp.simplify(2*m04+2*L**2*m20-(R+Q-c)*m22)==0
assert sp.simplify(12*m22-R*m40)==0

# Independent Poisson-Palm calculation. In the absence of a position reset,
# the internal variable evolves with the uncoupled reset rate q=Q-c.
# Let A=int_{last X reset}^0 omega_s^2 ds. E[X^4]=12 E[A^2].
mp.mp.dps=45
rng=random.Random(52799)
checks=0
for a,b in [(1,1),(1,3),(3,1),(2,5),(5,2),(7,9)]:
  for shared in [0, min(a,b)/4, min(a,b)/2, min(a,b)]:
    for amp in [0.4,1.0,2.0]:
      rr=mp.mpf(a); qq=mp.mpf(b); cc=mp.mpf(str(shared)); aa=mp.mpf(str(amp))
      iq=qq-cc
      mom2=2*aa**2/qq
      mom4=24*aa**4/qq**2
      def correlation(s):
        if iq==0:
          return mom4+2*aa**2*mom2*s
        return mp.exp(-iq*s)*mom4+(2*aa**2/iq)*(-mp.expm1(-iq*s))*mom2
      integrated=(2/rr)*mp.quad(lambda s:mp.exp(-rr*s)*correlation(s),[0,mp.inf])
      closed=8*aa**4*(6*rr+qq)/(rr**2*qq**2*(rr+qq-cc))
      assert mp.almosteq(integrated,closed,rel_eps=mp.mpf('1e-38'))
      ratio=(12*integrated)/(4*aa**2/(rr*qq))**2
      explicit=6*(6*rr+qq)/(rr+qq-cc)
      assert mp.almosteq(ratio,explicit,rel_eps=mp.mpf('1e-38'))
      checks+=2
# Exact rational inversions over a grid with no floating-point error.
for rr in range(1,9):
  for qq in range(1,9):
    for h in range(0,min(rr,qq)+1):
      Rr=Fraction(rr);Qq=Fraction(qq);cc=Fraction(h)
      amp=Fraction(2,3)
      v=Fraction(4)*amp**2/(Rr*Qq)
      omega_v=Fraction(2)*amp**2/Qq
      k=Fraction(6)*(6*Rr+Qq)/(Rr+Qq-cc)
      Qfit=2*amp**2/omega_v
      Rfit=2*omega_v/v
      cfit=Rfit+Qfit-6*(6*Rfit+Qfit)/k
      assert (Qfit,Rfit,cfit)==(Qq,Rr,cc)
      assert 6*(6*Rr+Qq)/(Rr+Qq)<=k<=6*(6*Rr+Qq)/max(Rr,Qq)
      checks+=2
print('PASS: symbolic generator identities, strictly increasing kurtosis, synchronized/independent endpoints,',checks,'independent integral and exact rational assertions')
