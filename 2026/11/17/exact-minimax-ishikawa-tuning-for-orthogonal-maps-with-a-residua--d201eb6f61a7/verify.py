"""Supplementary exact and numerical checks for a sharp Ishikawa minimax theorem.

Run with: python3 verify.py
The theorem is proved analytically; these finite checks do not prove universal claims.
"""
from fractions import Fraction
import cmath
import math
import random

def exact(h):
    b = (1-h)/(3-h)
    a = 1/(3-h)
    c = a
    q = (1+h)/(3-h)
    alpha = (2-h)/(3-h)
    beta = 1/(2-h)
    assert a+b+c == 1
    assert (1-alpha) == a
    assert alpha*(1-beta) == b
    assert alpha*beta == c
    assert abs(a-b+c) == q
    assert b+(a+c)*h == q
    assert b-(a+c) == -q
    k = Fraction(1, 2)/(1-h)
    assert q == (4*k-1)/(4*k+1)
    return a,b,c,q

num=0
for den in range(2,23):
    for n in range(-den+1,den):
        h = Fraction(n,den)
        a,b,c,q=exact(h)
        num += 1
        for u in (Fraction(-1),h,Fraction(-1)+Fraction(1,10)*(h+1)):
            if not -1 <= u <= h: continue
            mod2=(b+(a+c)*u)**2+(1-u*u)*(a-c)**2
            assert mod2 <= q*q
            num+=1

rnd=random.Random(921067)
for it in range(3000):
    h=rnd.uniform(-.99,.99)
    a,b,c,q=map(float,exact(Fraction(h).limit_denominator(1000000)))
    angle=rnd.uniform(math.acos(h),math.pi)
    z=cmath.exp(1j*angle)
    assert abs(a+b*z+c*z*z) <= q+1e-12
    # Any non-optimal probability coefficients cannot beat the sharp factor.
    weights=[rnd.random() for _ in range(3)]
    weights=[w/sum(weights) for w in weights]
    aa,bb,cc=weights
    lower=max(abs(aa-bb+cc),abs(aa+bb*z+cc*z*z))
    # Evaluate at endpoints, not the random angle, for a decisive lower bound.
    z_h=complex(h,math.sqrt(1-h*h))
    endpoint=max(abs(aa-bb+cc), abs(aa+bb*z_h+cc*z_h*z_h))
    assert endpoint >= q-1e-11
    num += 2

print('PASS: {} exact rational identities/inequalities and numerical checks'.format(num))
