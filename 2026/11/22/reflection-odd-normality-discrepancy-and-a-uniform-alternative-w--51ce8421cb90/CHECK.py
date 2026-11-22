#!/usr/bin/env python3
"""Independent algebraic and numerical spot-checks for the stated signed normality statistic.

Requires Python 3 and mpmath. The general identities are proved in RESULT.md;
finite checks and quadrature here do not substitute for those proofs.
"""
from fractions import Fraction as Q
from itertools import product
import mpmath as mp

checks = 0

def verify(ok, msg):
    global checks
    assert ok, msg
    checks += 1

def stat(x):
    n = len(x)
    mean = sum(x, Q(0))/n
    ss = sum((t-mean)**2 for t in x)
    if ss == 0:
        return None
    s2 = ss/(n-1)
    h = sum(min(x[i],x[j])**2-x[i]*x[j]
            for i in range(n) for j in range(i+1,n))
    return h / (Q(n*(n-1),2)*2*s2) - Q(1,2)

def ordinal(x):
    n = len(x)
    mean = sum(x,Q(0))/n
    ss = sum((t-mean)**2 for t in x)
    if ss == 0:
        return None
    s2=ss/(n-1)
    z=sorted(x)
    numerator=sum((2*j-n-1)*z[j-1]**2 for j in range(1,n+1))
    return -numerator/(2*n*(n-1)*s2)

for n in range(2,7):
    alphabet = [-2,-1,0,1,2] if n<=5 else [-1,0,1]
    for t in product(alphabet,repeat=n):
        x=tuple(Q(v) for v in t)
        if len(set(x))<2:
            continue
        a=stat(x)
        verify(a==ordinal(x),"order-statistic identity")
        verify(stat(tuple(-v for v in x))==-a,"reflection oddness")
        verify(stat(tuple(3*v for v in x))==a,"positive scale invariance")
        verify(stat(tuple(-2*v for v in x))==-a,"negative scale oddness")

# Under any law symmetric about zero, odd pair kernel has exact expectation zero.
for support in [(-1,1),(-2,-1,1,2),(-3,-1,0,1,3)]:
    pts=list(map(Q,support))
    avg=sum((x+y)*abs(x-y) for x in pts for y in pts)/len(pts)**2
    verify(avg==0,"symmetric alternative population contrast")

# Explicit uniform(-1,1) projection: piecewise polynomial integration.
for x in [Q(-1),Q(-3,4),Q(-1,3),Q(0),Q(1,5),Q(3,4),Q(1)]:
    left=Q(2,3)*x**3+x*x-Q(1,3)
    right=Q(1,3)-x*x+Q(2,3)*x**3
    verify((left+right)/2==Q(2,3)*x**3,"uniform projection")
verify((Q(4,9)*Q(1,7))/(4*Q(1,3)**2)==Q(1,7),"uniform asymptotic variance")

mp.mp.dps=38
phi=lambda z: mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
G=lambda z: 2*z*phi(z)+(z*z-1)*mp.erf(z/mp.sqrt(2))
for x in [-2,-1,0,mp.mpf('0.3'),1,2]:
    numerical = mp.quad(lambda y:(x+y)*abs(x-y)*phi(y),[-mp.inf,x,mp.inf])
    verify(abs(numerical-G(x))<mp.mpf('1e-30'),"Gaussian projection")
nu0 = mp.quad(lambda x:phi(x)*G(x)**2,[-mp.inf,-1,0,1,mp.inf])/4
verify(abs(nu0-mp.mpf('0.4423311143775626914223299158'))<mp.mpf('5e-25'),"Gaussian asymptotic variance")
z975=mp.sqrt(2)*mp.erfinv(mp.mpf('.95'))
power=mp.erfc(z975*mp.sqrt(7*nu0)/mp.sqrt(2))
verify(abs(power-mp.mpf('0.00056303647010484157624'))<mp.mpf('5e-20'),"uniform limiting power")
print('checks:',checks)
print('gaussian variance:',mp.nstr(nu0,32))
print('uniform variance:',Q(1,7))
print('uniform limiting 5-percent rejection:',mp.nstr(power,30))
