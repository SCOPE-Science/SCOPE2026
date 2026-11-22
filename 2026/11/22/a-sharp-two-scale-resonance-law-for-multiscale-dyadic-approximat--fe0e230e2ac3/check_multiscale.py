#!/usr/bin/env python3
"""Exact-arithmetic sanity checks for the dyadic multiscale BV bound.
The all-depth theorem is proved analytically, not by finite enumeration.
"""
from fractions import Fraction as F
from math import floor

def frac(x): return x - (x.numerator // x.denominator)
def q(x):
    y=frac(x)
    return y*(1-y)
def distance(x):
    y=frac(x)
    return min(abs(y-F(1,3)), abs(y-F(2,3)))
def finite(J,t): return sum((F(1,2**j)*q(2**j*t) for j in range(J)),F(0))
def paired(m,t):
    top=F(4,9)*(1-F(1,4**m))
    deficit=3*sum((F(1,4**k)*distance(4**k*t)**2 for k in range(m)),F(0))
    return top-deficit

def cell_optimum(J,cell):
    K=2**(J-1)
    left,right=F(cell,K),F(cell+1,K)
    mid=(left+right)/2
    qs=[(2**j*mid).numerator//(2**j*mid).denominator for j in range(J)]
    a=2**J-1
    b=sum(1+2*z for z in qs)
    v=F(b,2*a)
    v=max(left,min(right,v))
    return (finite(J,v),v)

assert finite(1,F(1,2))==F(1,4)
for m in range(1,7):
    J=2*m
    bound=F(4,9)*(1-F(1,4**m))
    assert finite(J,F(1,3))==bound
    assert finite(J,F(2,3))==bound
    ans=max((cell_optimum(J,cell) for cell in range(2**(J-1))),key=lambda v:v[0])
    assert ans[0]==bound,(m,ans,bound)
    for num in range(1,37):
        t=F(num,37)
        assert finite(J,t)==paired(m,t)
        assert finite(J,t)<=bound
    print('exact checked m=',m,'J=',J,'intervals=',2**(J-1),'bound squared=',bound)
# random rationalized multi-jump BV data represented by signed measure:
# Hilbert direct-sum triangle + Jensen bound is checked using the exact
# inner products of conditional expectation residuals.
def cell_average_step(t, j, k):
    h=F(1,2**j); L=k*h; R=(k+1)*h
    if t <= L:return F(1)
    if t >= R:return F(0)
    return (R-t)/h

def step_cross_resid(t,s,j):
    h=F(1,2**j)
    # inner product <(I-E_j)H_t, (I-E_j)H_s>:
    # E_j projection, equals <H_t,H_s>-<E_j H_t,E_j H_s>
    base=1-max(t,s)
    K=2**j
    average=sum((h*cell_average_step(t,j,k)*cell_average_step(s,j,k) for k in range(K)),F(0))
    return base-average
for m in (1,2,3,4):
    pts=(F(1,5),F(1,3),F(3,4))
    signs=(F(2,3),F(-1,4),F(5,7))
    V=sum(map(abs,signs),F(0))
    error=sum((sum((u*v*step_cross_resid(t,s,j) for t,u in zip(pts,signs) for s,v in zip(pts,signs)),F(0)) for j in range(2*m)),F(0))
    rhs=V*V*F(4,9)*(1-F(1,4**m))
    assert 0<=error<=rhs
    print('BV multi-jump test m=',m,'error=',float(error),'bound=',float(rhs))
print('All finite exact checks passed; infinite scope requires the proof in RESULT.md.')
