#!/usr/bin/env python3
"""Exact algebraic verifier for two-site ring-restart tricritical coordinates.

Requires Python 3 and SymPy 1.11 or later. Uses exact rationals for the
polynomial identities, root brackets and the sign of the cubic coefficient.
Numerical evaluations at the end are illustrative, not proofs.
"""
from fractions import Fraction
from math import cosh, pi, sqrt
from sympy import symbols, factorial, simplify, factor, together, fraction, Poly, rem, diff, Rational, nroots, N

b, p, y = symbols('b p y')
Q = b**3 + 15*b**2 - 16*b + 4
P1 = 6*b**2*p**2 - (b**2+6*b)*p + 1
P2 = 90*b**3*p**3 - 30*b**3*p**2 + b**3*p - 90*b**2*p**2 + 15*b**2*p + 15*b*p - 1
A0 = (1-b*p)/2
A1 = P1/24
A2 = -P2/720
A3 = (2520*b**4*p**4-1260*b**4*p**3+126*b**4*p**2-b**4*p
      -2520*b**3*p**3+840*b**3*p**2-28*b**3*p+420*b**2*p**2
      -70*b**2*p-28*b*p+1)/40320
# Exact quotient-series recursion for cosh(sqrt(y))/(1-p+p*cosh(sqrt(b*y))).
c = [1/factorial(2*k) for k in range(5)]
d = [1] + [p*b**k/factorial(2*k) for k in range(1,5)]
a = [1]
for k in range(1,5):
    a.append(factor(c[k] - sum(d[j]*a[k-j] for j in range(1,k+1))))
for k, expected in enumerate((A0,A1,A2,A3),1):
    assert simplify(a[k]-expected) == 0, ('Taylor coefficient',k)

# Subresultant elimination. Any physical P1=P2=0 solves the linear identity.
assert factor(P2 - Rational(5,2)*b*(6*p-1)*P1 + (3*b**3*p-5*b+2)/2) == 0
psub=(5*b-2)/(3*b**3)
assert factor(P1.subs(p,psub) + 2*(b-1)*Q/(3*b**4)) == 0
assert factor(P2.subs(p,psub) - 5*(b-1)*(b**3-10*b+4)*Q/(3*b**6)) == 0

# Exactly two Q roots in (0,1): Q(0)>0, Q(1/2)<0, Q(1)>0,
# and Q' has exactly one positive root. Only the smaller gives p in (0,1).
q = lambda x: x**3+15*x**2-16*x+4
assert q(Rational(0))>0 and q(Rational(1,2))<0 and q(Rational(1))>0
assert q(Rational(2,5))>0 and q(Rational(9,20))<0
assert q(Rational(1,2))<0 and q(Rational(3,5))>0
# Tight interval with exact rational signs, enabling exact positivity proof of A3.
lo=Rational(420030658800268,10**15)
hi=Rational(420030658800270,10**15)
assert 0<lo<hi<Rational(9,20) and q(lo)>0 and q(hi)<0
assert 0<psub.subs(b,lo)<Rational(1,2) and 0<psub.subs(b,hi)<Rational(1,2)
H=915202561*b**2-928637484*b+228590912
assert H.subs(b,hi)>0
assert diff(H,b).subs(b,lo)<0 and diff(H,b).subs(b,hi)<0
# At Q(b)=0, the cubic Taylor coefficient A3 equals H(b)/(5670*b**8).
raw = together(A3.subs(p,psub)-H/(5670*b**8))
numerator,denominator=fraction(raw)
assert rem(numerator,Q,b) == 0
# The local control parameters (A1,A2) are independent.
J=factor(diff(A1,b)*diff(A2,p)-diff(A1,p)*diff(A2,b))
assert factor(J + b**2*p*(90*b**2*p**2+6*b**2*p+b**2-180*b*p+12*b+75)/17280) == 0
# On the isolated physical interval 0<b<9/20, 0<p<1/2,
# the bracket exceeds 75-180*(9/20)*(1/2)>0.
assert 75-180*Rational(9,20)*Rational(1,2)>0
B=90*b**2*p**2+6*b**2*p+b**2-180*b*p+12*b+75
# For physical b,p below bounds, it is safely positive (coarse bound).
assert B.subs({b:lo,p:psub.subs(b,lo)})>0
assert B.subs({b:hi,p:psub.subs(b,hi)})>0
# Formal nonzero: J reduced modulo Q after substituting psub.
jnum,jden=fraction(together(J.subs(p,psub)))
assert rem(jnum,Q,b) != 0

roots= [r for r in nroots(Q,n=35,maxsteps=100) if abs(float(r.as_real_imag()[1]))<1e-20 and 0<float(r)<1]
assert len(roots)==2
b0=roots[0]
p0=psub.subs(b,b0)
m0=p0/(1-p0)
ang=sqrt(float(b0))-0.5
aval=float(A3.subs({b:b0,p:p0}))
assert lo < b0 < hi and 0 < p0 < 1 and aval>0
print('All exact symbolic identities and rational root/sign certificates passed.')
print('b0=',N(b0,27),'p0=',N(p0,27),'m0=',N(m0,27))
print('phi2/pi=',format(ang,'.16g'),'A3=',format(aval,'.16g'))
print('Jacobian=',format(float(J.subs({b:b0,p:p0})),'.16g'))
# Numerical sanity: F(y)-A0 is cubic at the derived root.
from mpmath import mp
mp.dps=70
br=mp.mpf(str(N(b0,35)));pr=mp.mpf(str(N(p0,35)))
def f(z):return (mp.cosh(mp.sqrt(z))/(1-pr+pr*mp.cosh(mp.sqrt(br*z)))-1)/z
for z in [mp.mpf('0.00001'),mp.mpf('0.00002'),mp.mpf('0.00005')]:
    ratio=(f(z)-(1-br*pr)/2)/z**3
    print('F cubic-ratio at y='+str(z)+':',mp.nstr(ratio,14))
