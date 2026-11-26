#!/usr/bin/env python3
"""Exact rational spherical-moment checks and deterministic uniform-sphere diagnostic."""
from fractions import Fraction as F
from math import comb, cos, pi, sqrt
from random import Random


def double_odd(k):
    a = 1
    for j in range(k, 0, -2): a *= j
    return a


def moment(e):
    if any(j % 2 for j in e): return F(0)
    return F(double_odd(e[0]-1)*double_odd(e[1]-1)*double_odd(e[2]-1), double_odd(sum(e)+1))


def legendre(n):
    a, b = {0:F(1)}, {1:F(1)}
    if n==0:return a
    for k in range(1,n):
        c={}
        for j,v in b.items(): c[j+1]=c.get(j+1,F(0))+F(2*k+1,k+1)*v
        for j,v in a.items(): c[j]=c.get(j,F(0))-F(k,k+1)*v
        a,b=b,c
    return b


def framepoly(n):
    p={}
    for d in range(3):
        for j,v in legendre(n).items():
            e=tuple(j if i==d else 0 for i in range(3))
            p[e]=p.get(e,F(0))+v
    return {e:v for e,v in p.items() if v}


def integrate(p): return sum((v*moment(e) for e,v in p.items()),F(0))


def multiply(a,b):
    c={}
    for e,v in a.items():
        for f,w in b.items():
            g=tuple(e[i]+f[i] for i in range(3))
            c[g]=c.get(g,F(0))+v*w
    return c

for deg in (2,4,6,8,10,12):
    p=framepoly(deg)
    variance=integrate(multiply(p,p))-integrate(p)**2
    eigen=3*(1+2*(-1)**(deg//2)*F(comb(deg,deg//2),4**(deg//2)))
    assert variance==eigen*F(1,2*deg+1)
    print('exact',deg,'variance',variance,'multiplier',eigen)
assert integrate(multiply(framepoly(4),framepoly(6)))==0
# Independent randomized geometric check: the last row of a Haar rotation
# is uniform on S^2, and the three frame columns give its components.
rng=Random(197301)
for deg, ratio in ((4,F(21,4)),(6,F(9,8))):
    coeff=legendre(deg)
    samples=[]
    for k in range(40000):
        z=2*rng.random()-1
        phi=2*pi*rng.random()
        s=sqrt(1-z*z)
        xyz=(s*cos(phi),s*__import__('math').sin(phi),z)
        samples.append(sum(sum(float(v)*x**j for j,v in coeff.items()) for x in xyz))
    avg=sum(samples)/len(samples)
    v=sum((x-avg)**2 for x in samples)/len(samples)
    exact=float(ratio)/float(2*deg+1)
    assert abs(v/exact-1)<0.07,(deg,v,exact)
    print('empirical',deg,'variance',round(v,7),'reference',round(exact,7))
print('All checks passed.')
