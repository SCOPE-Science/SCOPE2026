"""Self-contained arithmetic checks for the two-stage RK negativity frontier.
These finite checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random

def tableau_from_d(d):
    # d=1/2-c1, q/p = 12*d*d, c2=1/2+1/(12*d).
    p = 1 / (1 + 12 * d * d)
    q = 1 - p
    c1 = F(1,2) - d
    c2 = F(1,2) + 1 / (12*d)
    a11, a12 = p/2, c1-p/2
    a21, a22 = c2-q/2, q/2
    return p, q, c1, c2, ((a11,a12),(a21,a22))

def orders_and_M(p,q,c1,c2,A):
    (a11,a12),(a21,a22)=A
    assert a11+a12 == c1 and a21+a22 == c2
    assert p+q == 1
    assert p*c1+q*c2 == F(1,2)
    assert p*c1*c1+q*c2*c2 == F(1,3)
    assert p*(a11*c1+a12*c2)+q*(a21*c1+a22*c2) == F(1,6)
    assert 2*p*a11-p*p == 0
    assert p*a12+q*a21-p*q == 0
    assert 2*q*a22-q*q == 0

assertions=0
for d in [F(1,6),F(1,5),F(1,4),F(1,3),F(2,5),F(1,2)]:
    p,q,c1,c2,A = tableau_from_d(d)
    orders_and_M(p,q,c1,c2,A)
    assert F(0)<=c1<c2<=F(1)
    assert A[0][1]<0<A[1][0]
    assertions += 10

# Exact rational root bracket for p^3(1-p)=1/12.
lo,hi=F(586106,1000000),F(586107,1000000)
pol=lambda p:p*p*p*(1-p)-F(1,12)
assert pol(lo)<0<pol(hi)
assert F(1,4)<lo<hi<F(3,4)
assertions+=2
root=(float(lo)+float(hi))/2
for _ in range(60):
    root -= (root**3*(1-root)-1/12)/(root**2*(3-4*root))
negative=lambda p:sqrt((1-p)/(12*p))-(1-p)/2
delta=negative(root)
assert 0.03563906<delta<0.03563908
assert abs(root**3*(1-root)-1/12)<1e-14
assertions+=2
rng=Random(210724)
for _ in range(1500):
    p=.25+.5*rng.random()
    assert negative(p)>=delta-2e-13
    c1=.5-sqrt((1-p)/(12*p)); q=1-p
    # The least possible negative a12 among M>=0 is -(p/2-c1).
    a11=p/2+rng.random()*.3
    assert c1-a11<=-delta+2e-13
    assertions+=2
print(f"PASS: {assertions} arithmetic assertions; pstar={root:.12f}; delta={delta:.12f}")
