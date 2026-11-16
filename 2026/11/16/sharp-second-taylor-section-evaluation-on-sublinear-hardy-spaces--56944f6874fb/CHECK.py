#!/usr/bin/env python3
"""Reproducibility checks for a sharp finite Taylor-section Hardy functional."""
from fractions import Fraction as F
from math import sqrt

def Q(t,x):
    return ((t-1)**2*(t-2)*x**4+(t-1)*(3*t-4)*x**3
            -2*(t-1)*(t-4)*x**2-2*(2*t-3)*x-2)

def objective(t,x,y):
    return (1+t*(x+y)+t*(t-1)*x*x/2)/(1+x*x+y*y)**(t/2)

def root(t):
    low, high = 0., 1.
    for _ in range(90):
        mid=(low+high)/2
        if Q(t,mid)>0: high=mid
        else: low=mid
    return (low+high)/2

count=0
for t in (F(9,4),F(5,2),F(3),F(4),F(5),F(8),F(12),F(32)):
    assert Q(t,F(0))==-2
    assert Q(t,F(1))==(t-1)*(t*t-2*t+2)
    # All these fixed-exponent polynomial identities are verified exactly.
    for x in (F(0),F(1,11),F(1,5),F(3,7),F(8,9),F(1)):
        d=1+(t-1)*x
        y=x/d
        R=1+x*x+y*y
        N=1+t*(x+y)+t*(t-1)*x*x/2
        assert R-y*N==-Q(t,x)/(2*d*d)
        count+=1
    tt=float(t)
    xx=root(tt)
    yy=xx/(1+(tt-1)*xx)
    assert 0<xx<1 and 0<yy<1 and xx<1+yy
    assert abs(Q(tt,xx))<max(1e-5,1e-10*tt**4)
    # Quadratic Schur-Cohn inequalities (strictly zero-free closed disk).
    assert yy < 1 and xx < 1+yy
    best=objective(tt,xx,yy)
    for i in range(131):
        for j in range(131):
            u=2*i/130
            v=2*j/130
            assert objective(tt,u,v)<=best+1e-10
            count+=1
print('CHECK_OK exponents=8 rational_identities=48 comparisons=',count)
