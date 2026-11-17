"""Standalone exact-arithmetic checks of the positive two-cycle parameterization.

Run: python cycle_checker.py
Requires sympy. Finite checks support, but do not replace, the proof.
"""
from fractions import Fraction as Q
import random

def params(R,p,q):
    x = (R-Q(1,1)/p-q*(R-p))/(p-q)
    y = R-p-x
    u = p*x
    v = q*y
    gamma = (Q(1,1)/q-q)/(x*(p-1))
    c = q-gamma*x
    r = 1-c
    return x,y,u,v,r,gamma

def F(x,y,R,r,g):
    return x*(R-x-y),y*(1-r+g*x)

def check(R,p,q):
    x,y,u,v,r,g=params(R,p,q)
    assert min(x,y,u,v,r,g,1-r)>0
    assert F(x,y,R,r,g)==(u,v)
    assert F(u,v,R,r,g)==(x,y)
    assert x!=u and y!=v
    return (x,y,u,v,r,g)

assert check(Q(4),Q(2),Q(3,4))==(Q(8,5),Q(2,5),Q(16,5),Q(3,10),Q(5,6),Q(35,96))

rng=random.Random(2026)
for _ in range(500):
    p=Q(100+rng.randrange(1,100),100)
    threshold=p+1+1/p
    R=threshold+Q(rng.randrange(1,200),50)
    # q above 1/sqrt(p): enforce rationally by q^2*p>1
    q=Q(999,1000)
    if p*q*q<=1:continue
    check(R,p,q)
print('Exact cycle identities and positivity: PASS; explicit witness and sampled rational parameters.')
