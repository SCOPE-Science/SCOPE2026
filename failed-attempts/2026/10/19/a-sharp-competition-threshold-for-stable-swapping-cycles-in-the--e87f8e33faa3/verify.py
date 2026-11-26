#!/usr/bin/env python3
"""Reproducible supplementary checks for the symmetric competitive Ricker swap-cycle theorem.
This program tests finite parameter instances and exact algebraic identities; it does not certify the analytic theorem.
Requires Python 3 standard library only. Run: python3 verify.py
"""
from fractions import Fraction as Q
import math
import cmath

count = 0

def u(t): return math.atanh(t)/t if t else 1.0

def v(t): return (1-t*t)*u(t)

def S(t,k): return 4*u(t)/(1-k)

def detB(t,k):
    s=S(t,k)
    return s-1-(1-k*k)*s*s*(1-t*t)/4

def bisect(fun,a,b):
    fa=fun(a); fb=fun(b)
    assert fa*fb<0
    for _ in range(130):
        m=(a+b)/2
        fm=fun(m)
        if fa*fm>0: a=m; fa=fm
        else: b=m; fb=fm
    return (a+b)/2

root=bisect(lambda t:v(t)-t*t,0.001,0.999)
kstar=(1-root*root)/(1+root*root)
assert abs(root-0.751759503598729)<2e-12
assert abs(kstar-0.277839040263657)<2e-12
count+=2

# Exact, independent rational check of the transformed Jacobian and Schur factors.
for i in range(1,101):
    x=Q(2*i+1,i+7)
    y=Q(i+3,2*i+7)
    k=Q(i%23,27)
    s=x+y
    b00=-k*x; b01=x/y*(1-y); b10=y/x*(1-x); b11=-k*y
    tr=b00+b11
    det=b00*b11-b01*b10
    assert tr==-k*s
    assert det==s-1-(1-k*k)*x*y
    assert 1+tr+det==(1-k)*(s-(1+k)*x*y)
    assert 1-tr+det==(1+k)*(s-(1-k)*x*y)
    count+=4

for k in [0,0.01,0.03,0.1,0.2,0.27,kstar,0.3,0.6,0.9]:
    left=0 if k==0 else bisect(lambda t:v(t)-(1-k)/(1+k),1e-9,1-1e-7)
    right=bisect(lambda t:detB(t,k)-1,1e-9,1-1e-7)
    if k<kstar-1e-9: assert left<right
    if k>kstar+1e-9: assert left>right
    if k==0.03:
        rleft=math.exp(2*(1+k)/(1-k)*u(left))
        rright=math.exp(2*(1+k)/(1-k)*u(right))
        assert abs(rleft-8.915749063958335)<1e-9
        assert abs(rright-14.760100029033133)<1e-9
        count+=2
    for j in range(1,96):
        d=j/100
        if abs(d-left)<1e-5 or abs(d-right)<1e-5: continue
        s=S(d,k)
        x=s*(1+d)/2; y=s*(1-d)/2
        logR=2*(1+k)/(1-k)*u(d)
        xp=x*math.exp(logR-x-k*y)
        yp=y*math.exp(logR-y-k*x)
        assert abs(xp-y)<2e-10*(1+x+y)
        assert abs(yp-x)<2e-10*(1+x+y)
        # Independent matrix construction: B=P DF(x,y).
        b00=-k*x; b01=x/y*(1-y)
        b10=y/x*(1-x); b11=-k*y
        tr=b00+b11
        det=b00*b11-b01*b10
        assert abs(det-detB(d,k)) < 1e-8*(1+abs(det))
        assert abs(tr+k*s) < 1e-10
        z=cmath.sqrt(tr*tr-4*det)
        eig1=(tr+z)/2; eig2=(tr-z)/2
        stable_direct=max(abs(eig1),abs(eig2))<1
        stable_wedge=(left<d<right)
        assert stable_direct==stable_wedge, (k,d,left,right,eig1,eig2)
        assert (1+tr+det>0 and 1-tr+det>0 and 1-det>0)==stable_direct
        count+=6

# Strict function monotonicity in relevant interval, checked by sampling only.
for j in range(1,995):
    t=j/1000
    assert v(t)>v(t+0.001)
    assert u(t)<u(t+0.001)
    for k in [0,.03,.2,.4,.8]: assert detB(t,k)<detB(t+0.001,k)
    count+=7
print('VERIFY_OK: exact rational Schur identities, map interchange, sampled Floquet stability, monotonicity; checks =',count)
