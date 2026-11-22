#!/usr/bin/env python3
"""Reproducibility checks for balanced double-star Laplacian-width design.

Requires Python 3.9+ and NumPy. These finite checks supplement, but do not
replace, the all-integer proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose
import random
import numpy as np


def exact_opt(m):
    den = 9*m*m + 10*m + 1
    a0 = F(6*m+2, den)
    a = min(a0, F(1, 2*m))
    b = 1-2*m*a
    squared = 4-(12*m+4)*a+den*a*a
    return a,b,squared


def L_full(m, spoke, bridge):
    n=2*m+2
    L=np.zeros((n,n),dtype=float)
    edges=[]
    for j in range(m):
        edges.append((0,2+j,spoke[j]))
        edges.append((1,m+2+j,spoke[m+j]))
    edges.append((0,1,bridge))
    for u,v,w in edges:
        L[u,u]+=w; L[v,v]+=w
        L[u,v]-=w; L[v,u]-=w
    return L


def width(m, spoke, bridge):
    eig=np.linalg.eigvalsh(L_full(m,spoke,bridge))
    return float(eig[-1]-eig[1]), eig


def claimed_width(m,a,b):
    return sqrt(float(((m+1)*a+2*b)**2-8*a*b))


def run():
    assertions=0
    for m in range(1,29):
        a,b,q=exact_opt(m)
        assert a>0 and b>=0 and 2*m*a+b==1; assertions+=1
        if m==1:
            assert (a,b,q)==(F(2,5),F(1,5),F(4,5));assertions+=1
        if m==2:
            assert (a,b,q)==(F(14,57),F(1,57),F(32,57)); assertions+=1
        if m>=3:
            assert b==0 and a==F(1,2*m) and q==F((m+1)**2,4*m*m);assertions+=1
        eig_width,e=width(m,[float(a)]*(2*m),float(b))
        assert abs(eig_width-sqrt(float(q)))<5e-12; assertions+=1
        # Each arbitrary symmetric point is no better than the claimed optimizer.
        for j in range(1,20):
            aa=F(j,20)*F(1,2*m)
            bb=1-2*m*aa
            w,_=width(m,[float(aa)]*(2*m),float(bb))
            assert w+1e-11>=sqrt(float(q));assertions+=1
            assert abs(w-claimed_width(m,aa,bb))<1e-11;assertions+=1
        if m<=10:
            rng=random.Random(3901+m)
            for z in range(20):
                arr=[rng.uniform(.03,1) for i in range(2*m+1)]
                total=sum(arr);arr=[v/total for v in arr]
                spoke=arr[:2*m];bridge=arr[-1]
                val,_=width(m,spoke,bridge)
                assert val+1e-11>=sqrt(float(q));assertions+=1
                # Symmetry averaging cannot worsen the width.
                asy=sum(spoke)/(2*m)
                vs,_=width(m,[asy]*(2*m),bridge)
                assert vs<=val+1e-11;assertions+=1
    # Exact symbolic identity for all integer m: derivative of squared spread.
    from sympy import symbols, simplify, factor
    m,a=symbols('m a')
    b=1-2*m*a
    expr=((m+1)*a+2*b)**2-8*a*b
    assert simplify(expr-(4-(12*m+4)*a+(9*m*m+10*m+1)*a*a))==0;assertions+=1
    assert factor((9*m*m+10*m+1)-(9*m+1)*(m+1))==0;assertions+=1
    print('PASS',assertions,'checks, dimensions m=1..28, full Laplacian eigenvalues, random asymmetric allocations, exact rational thresholds, and symbolic identity')

if __name__=='__main__':run()
