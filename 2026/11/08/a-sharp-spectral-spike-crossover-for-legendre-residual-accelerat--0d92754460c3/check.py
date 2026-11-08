#!/usr/bin/env python3
"""Finite arithmetic and numerical checks for the Legendre-outlier theorem.

The limiting probability law is established analytically; finite checks are not its proof.
Uses only Python's standard library.
"""
from fractions import Fraction as F
from math import pi, sqrt, log
import random


def legendre_eval(n, x):
    if n == 0:
        return 1*x**0
    u, v = 1*x**0, x
    for k in range(1, n):
        u, v = v, ((2*k+1)*x*v - k*u)/(k+1)
    return v


def add(a, b, sa=F(1), sb=F(1)):
    return [sa*(a[i] if i<len(a) else F(0)) + sb*(b[i] if i<len(b) else F(0))
            for i in range(max(len(a),len(b)))]


def mul(a, b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def legendre_poly(n):
    if n==0:return [F(1)]
    p0,p1=[F(1)],[F(0),F(1)]
    for k in range(1,n):
        p0,p1=p1,add([F(0)]+p1,p0,F(2*k+1,k+1),F(-k,k+1))
    return p1


def mean_poly(a):
    return sum((a[j]/F(j+1) for j in range(0,len(a),2)),F(0))


def test():
    checks=0
    for n in range(0,15):
        p=legendre_poly(n)
        assert mean_poly(mul(p,p))==F(1,2*n+1)
        checks+=1
        for z in [F(6,5),F(2),F(3),F(7,2)]:
            assert sum(t*z**i for i,t in enumerate(p))==legendre_eval(n,z)
            assert sum(t*(-z)**i for i,t in enumerate(p))==(-1)**n*legendre_eval(n,z)
            checks+=2
    a,b=F(1),F(2)
    z0=F(3)
    for n in range(1,15):
        p0=legendre_eval(n,z0)
        for c in [F(21,10),F(5,2),F(3),F(17,5)]:
            z=(2*c-a-b)/(b-a)
            response=legendre_eval(n,-z)/p0
            if c<a+b:assert abs(response)<1
            elif c==a+b:assert response==(-1)**n
            else:assert abs(response)>1
            checks+=1
    for z in (1.2,2.0,3.2):
        q=z+sqrt(z*z-1)
        const=q/(pi*sqrt(z*z-1))
        for n in (50,100,180):
            # Evaluate recurrence without under/overflow for these values.
            p=legendre_eval(n,z)
            ratio=(2*n+1)*p*p/(const*q**(2*n))
            assert abs(ratio-1)<0.015, (z,n,ratio)
            checks+=1
    for n in (4,7,10):
        M=20000
        mean=sum(legendre_eval(n,1-2*(j+.5)/M)**2 for j in range(M))/M
        assert abs(mean-F(1,2*n+1))<0.0002, (n,mean)
        checks+=1
    n=7; M=20000; rng=random.Random(739182)
    values=[legendre_eval(n,1-2*(j+.5)/M)**2 for j in range(M)]
    realized=sum(rng.gauss(0,1)**2*t for t in values)
    expected=M/(2*n+1)
    assert 0.92<realized/expected<1.08, realized/expected
    checks+=1
    print('CHECK_OK',checks)
    print('Finite recurrence, exact Legendre norms, reflection barrier, exterior constants, and grid concentration checked.')
    print('Asymptotic theorem relies on proof, not finite tests.')

if __name__=='__main__':test()
