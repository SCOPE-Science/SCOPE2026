#!/usr/bin/env python3
"""Exact rational certificate for the four-coexistence equilibrium example.

Run with: python3 verify_equilibria.py
Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import zip_longest


def add(u, v):
    return [a+b for a,b in zip_longest(u,v,fillvalue=F(0))]


def sub(u, v):
    return [a-b for a,b in zip_longest(u,v,fillvalue=F(0))]


def mul(u, v):
    w=[F(0)]*(len(u)+len(v)-1)
    for i,a in enumerate(u):
        for j,b in enumerate(v):
            w[i+j] += a*b
    return w


def val(p, x):
    return sum((a*x**i for i,a in enumerate(p)),F(0))


a,b,c,d = [F(s) for s in ('3.66','0.49','3.29','1.91')]
ap,bp,cp,dp = [F(s) for s in ('0.57','0.18','0.25','2.22')]
K=F(687,1000)
assert all(z>0 for z in (a,b,c,d,ap,bp,cp,dp,K))

# Prey-type payoff rates and their differences.
uA=[b,a-b]
uB=[d,c-d]
vA=[bp,ap-bp]
vB=[dp,cp-dp]
g=sub(uA,uB)
h=sub(vA,vB)
r=add(uB,mul([F(0),F(1)],g))
delta=add(vB,mul([F(0),F(1)],h))

# Key cancellation, independently formed from two descriptions.
D1=sub(mul(r,h),mul(delta,g))
D2=sub(mul(uB,h),mul(vB,g))
assert D1[:3]==D2 and all(z==0 for z in D1[3:]) and len(D2)==3

# Equilibrium eliminant Q = K*delta*(r*h-delta*g)-h.
Q=sub([K*z for z in mul(delta,D1)],h)
expected=[F(905295840,10**9),F(-8056257752,10**9),
          F(23130348810,10**9),F(-26920918713,10**9),
          F(10997575692,10**9),F(0)]
assert Q==expected and Q[4]!=0 and Q[5]==0

# Four disjoint rational intervals with strict opposite endpoint signs.
intervals=[(F(1,5),F(1,4)),(F(1,2),F(3,5)),
           (F(7,10),F(3,4)),(F(9,10),F(1))]
expected_signs=[(1,-1),(-1,1),(1,-1),(-1,1)]
for (left,right),(sl,sr) in zip(intervals,expected_signs):
    ql,qr=val(Q,left),val(Q,right)
    assert (ql>0)-(ql<0)==sl and (qr>0)-(qr<0)==sr
    # Affine g,h never vanish within each bracket and share their signs.
    assert val(g,left)*val(h,left)>0
    assert val(g,right)*val(h,right)>0
    assert val(g,left)*val(g,right)>0
    assert val(h,left)*val(h,right)>0
    for endpoint in (left,right):
        assert val(delta,endpoint)>0
    print(f'[{left}, {right}]: Q(left)={ql}, Q(right)={qr}')

# Affine functions have unique zeros, both outside all four brackets.
assert -g[0]/g[1]==F(142,179)
assert -h[0]/h[1]==F(51,59)
assert F(3,4)<F(142,179)<F(51,59)<F(9,10)

# For any root x in a bracket, x is in (0,1), P=1/delta(x)>0,
# Y=g(x)/h(x)>0 and A=xP, B=(1-x)P are strictly positive.
# Q(x)=0 is then exactly P'=0, while x'=Y'=0 by construction.
# IVT gives at least one root in each of four disjoint brackets;
# the nonzero quartic Q allows at most four, so all are simple.
print('PASS: quartic cancellation, exact polynomial, four positive equilibria, sharp bound.')
