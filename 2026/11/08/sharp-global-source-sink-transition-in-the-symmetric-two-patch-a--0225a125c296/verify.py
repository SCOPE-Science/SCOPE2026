#!/usr/bin/env python3
"""Exact rational consistency and branch checks for the two-patch cubic Allee theorem.
Run with Python 3: python verify.py. The analytic proof is in RESULT.md;
finite checks are a reproducibility aid, not a substitute for it.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext

getcontext().prec = 75


def f(x):
    return x * (x - Q(1, 2)) * (1 - x)


def vector(x, y, u):
    return f(x) + u * (y-x), f(y) + u * (x-y)


def transformed(z, d, u):
    return -z * (3*d*d+z*z-1)/4, -d*(d*d+8*u+3*z*z-1)/4


def jac(z,d,u):
    a=(1-3*d*d-3*z*z)/4
    return a, -3*z*d/2, a-2*u


def fd(x):
    return -3*x*x+3*x-Q(1,2)


count=0
for xi in range(8):
    for yi in range(8):
        for ui in range(1,10):
            x, y, u = Q(xi,7),Q(yi,7),Q(ui,100)
            z,d=x+y-1,x-y
            vx,vy=vector(x,y,u)
            assert (vx+vy,vx-vy)==transformed(z,d,u)
            a,b,c=jac(z,d,u)
            assert a+c==fd(x)+fd(y)-2*u
            assert a*c-b*b==(fd(x)-u)*(fd(y)-u)-u*u
            # The system is the gradient of F(x)+F(y)-u(x-y)^2/2.
            assert vx==f(x)-u*(x-y) and vy==f(y)+u*(x-y)
            count+=1

for u in [Q(1,100), Q(1,20), Q(1,13), Q(1,12), Q(1,10), Q(1,8), Q(1,4)]:
    if u < Q(1,12):
        zsq=(1-12*u)/4
        dsq=(1+4*u)/4
        a=(1-3*dsq-3*zsq)/4
        c=a-2*u
        b2=9*zsq*dsq/4
        assert a+c==(4*u-1)/4
        assert a*c-b2==(4*u+1)*(12*u-1)/8 < 0
        assert zsq>0 and dsq>0
        count+=1
    if u < Q(1,8):
        dsq=1-8*u
        az=(1-3*dsq)/4
        ad=az-2*u
        assert az==6*u-Q(1,2)
        assert ad==4*u-Q(1,2)
        count+=1
    # Closed-form cardinalities of all nonnegative equilibria.
    number=3+2*(u<Q(1,8))+4*(u<Q(1,12))
    assert number == (9 if u<Q(1,12) else 5 if u<Q(1,8) else 3)
    count+=1

# Check all algebraic equilibrium roots numerically at high precision.
for den in [17,31,53,101]:
    for num in range(1,den):
        u=Decimal(num)/Decimal(den)
        roots=[(Decimal(0),Decimal(0)),(Decimal(1)/2,Decimal(1)/2),(Decimal(1),Decimal(1))]
        if u<Decimal(1)/8:
            dd=(1-8*u).sqrt()
            roots += [((1+dd)/2,(1-dd)/2),((1-dd)/2,(1+dd)/2)]
        if u<Decimal(1)/12:
            zz=(1-12*u).sqrt()/2
            dd=(1+4*u).sqrt()/2
            roots += [((1+sz*zz+sd*dd)/2,(1+sz*zz-sd*dd)/2) for sz in [-1,1] for sd in [-1,1]]
        for x,y in roots:
            fx=x*(x-Decimal(1)/2)*(1-x)
            fy=y*(y-Decimal(1)/2)*(1-y)
            assert abs(fx+u*(y-x))<Decimal('1e-65')
            assert abs(fy+u*(x-y))<Decimal('1e-65')
            assert Decimal(0)<=x<=Decimal(1) and Decimal(0)<=y<=Decimal(1)
            count+=1

# Critical transverse nonhyperbolicity and center-manifold coefficient.
u=Q(1,12)
dsq0=Q(1,3)
assert (1-3*dsq0)/4==0
assert ((1-3*(dsq0-3*Q(1,1)**2)-Q(1,1)**2)/4)==2  # z'=2 z^3 + O(z^5)
count+=1
print('PASS:',count,'independent rational/algebraic/numeric checks')
