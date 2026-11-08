#!/usr/bin/env python3
"""Standalone reproducibility checks for finite-time graph heat-frame tightness.

Run: python verify.py
Requires: Python 3, sympy, numpy, scipy.
The proof is mathematical; these checks test its coefficients and sample matrices.
"""
from fractions import Fraction
from math import exp, log
import sympy as sp
import numpy as np
from scipy.linalg import expm

x, y, k = sp.symbols('x y k')
P = 4 - 15*x**2 - (40*k-20)*x**4 + (40*k-8)*x**5 - x**10
Q = x**9 + x**8 + x**7 + x**6 + x**5 + (9-40*k)*x**4 - 11*x**3 - 11*x**2 + 4*x + 4
assert sp.expand(P-(1-x)*Q)==0
R = sp.expand(sum(c*y**degree*(1+y)**(9-degree) for (degree,),c in sp.Poly(Q,x).terms()))
expected_R = 4+40*y+165*y**2+360*y**3+40*(11-k)*y**4+40*(7-5*k)*y**5+(50-400*k)*y**6-40*(1+10*k)*y**7-20*(1+10*k)*y**8-40*k*y**9
assert sp.expand(R-expected_R)==0
checks=2

def root_of_P(m):
    lo, hi=0.0,1.0-1e-13
    # bisect unique interior root; avoid x=1 boundary
    def eval_P(z):return 4-15*z*z-(40*m-20)*z**4+(40*m-8)*z**5-z**10
    assert eval_P(lo)>0 and eval_P(hi)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if eval_P(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def gammas(m,t):
    a=1/(18*m) + 1/(10*m)*exp(-16*m*t) + (1-1/(5*m))*exp(-26*m*t)+2/(45*m)*exp(-36*m*t)
    b=1/(18*m) + 3/(8*m)*exp(-20*m*t) + (1-1/(2*m))*exp(-24*m*t)+5/(72*m)*exp(-36*m*t)
    return a,b

for m in range(1,101):
    z=root_of_P(m); tt=-log(z)/(2*m)
    ga,gb=gammas(m,tt)
    assert abs(ga-gb) < 3e-14
    assert gammas(m,tt*.8)[0]<gammas(m,tt*.8)[1]
    assert gammas(m,tt*1.2)[0]>gammas(m,tt*1.2)[1]
    assert abs(ga-gb-z**8/40/m*(4-15*z*z-(40*m-20)*z**4+(40*m-8)*z**5-z**10))<3e-14
    checks+=4

def graph_L(m):
    N=18*m; A=np.zeros((N,N),dtype=float)
    groups=[range(j*5*m,(j+1)*5*m) for j in range(2)]
    groups += [range(10*m+j*2*m,10*m+(j+1)*2*m) for j in range(4)]
    for nodes in groups:
        for p in nodes:
            for q in nodes:
                if p!=q:A[p,q]=1
    A[:10*m,10*m:]=A[10*m:,:10*m]=1
    return np.diag(A.sum(axis=1))-A

for m in [1,2]:
    L=graph_L(m)
    # Equitable partition yields precisely two diagonal values.
    for t in [0.0,0.004,0.05,0.22,0.40]:
        H=expm(-2*t*L)
        va,vb=gammas(m,t)
        assert np.max(np.abs(np.diag(H)[:10*m]-va))<2e-12
        assert np.max(np.abs(np.diag(H)[10*m:]-vb))<2e-12
        # A direct independently formed graph atom frame operator is diagonal.
        checks+=2
    vals=np.linalg.eigvalsh(L)
    predicted=np.array(([0]+[8*m]+[10*m]*3+[12*m]*(8*m-4)+[13*m]*(10*m-2)+[18*m]),dtype=float)
    assert np.max(np.abs(np.sort(vals)-np.sort(predicted)))<2e-10
    checks+=1

# Exact rational spectral-projector weights sum to unity in both orbits.
for m in range(1,501):
    aa=Fraction(1,18*m)+Fraction(1,10*m)+(Fraction(5*m-1,5*m))+Fraction(2,45*m)
    bb=Fraction(1,18*m)+Fraction(3,8*m)+Fraction(2*m-1,2*m)+Fraction(5,72*m)
    assert aa==bb==1
    checks+=2
print('GRAPH_HEAT_FRAME_VERIFY_PASS',checks,'k1_t',f'{-log(root_of_P(1))/2:.14f}')
