"""Reproducible arithmetic checks for a sharp refuge-feedback coexistence census.

Python 3 standard library only. Run: python checker.py
These finite checks supplement the complete analytical proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt
import random

ONE=Q(1)

def field(x,y,a,b,mu):
    s=1+x+y
    return (x-x*x*(1+y*y)/(1+y)**2-a*x*y/s,
            y*(-mu+b*x/s))

def jac(x,y,a,b,mu):
    s=1+x+y; q=(1+y*y)/(1+y)**2
    qp=2*(y-1)/(1+y)**3
    return ((1-2*x*q-a*y*(s-x)/s**2,-x*x*qp-a*x*(s-y)/s**2),
            (b*y*(s-x)/s**2,-mu+b*x*(s-y)/s**2))

def trace_det(m):
    return m[0][0]+m[1][1],m[0][0]*m[1][1]-m[0][1]*m[1][0]

mu=Q(10); b=Q(19); a=Q(38,81); lam=b/mu-1
assert lam==Q(9,10)
expected=((Q(1),Q(0),Q(-3,2),Q(1,2)),
          (Q(4,3),Q(1,5),Q(-889,513),Q(-5,19)),
          (Q(5,3),Q(1,2),Q(-1265,513),Q(10,19)))
for x,y,tr,det in expected:
    assert field(x,y,a,b,mu)==(0,0)
    assert trace_det(jac(x,y,a,b,mu))==(tr,det)

# Exact algebra of the predator-nullcline reduction at rational test points.
rng=random.Random(20261117)
for i in range(600):
    lam=Q(rng.randrange(1,200),rng.randrange(201,400))
    a=Q(rng.randrange(1,100),rng.randrange(101,400))
    mu=Q(rng.randrange(1,50),rng.randrange(51,100))
    b=mu*(1+lam)
    y=Q(rng.randrange(1,100),rng.randrange(101,200))
    x=(1+y)/lam
    B=lam-a*lam*lam/(1+lam)
    P=y*y-B*y+1-lam
    F,G=field(x,y,a,b,mu)
    assert G==0
    assert F==-P/(lam*lam)

# The rational example has a positive lower saddle, upper sink and prey-only sink.
assert expected[0][2]<0 and expected[0][3]>0
assert expected[1][3]<0
assert expected[2][2]<0 and expected[2][3]>0
print('PASS: 3 exact equilibria and Jacobians; 600 rational nullcline identities')
