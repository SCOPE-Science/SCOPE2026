#!/usr/bin/env python3
"""Finite consistency checks for explicit Cauchy sampling formulas.

Run: python CHECK.py
Only algebraic/finite numerical consistency is tested; infinite-dimensional
and all-parameter results require the proof in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial,comb,pi,sqrt
import numpy as np
import mpmath as mp

def det(M):
    M=[list(r) for r in M]; n=len(M); sign=1; d=Fraction(1)
    for p in range(n):
        j=next((j for j in range(p,n) if M[j][p]),None)
        if j is None: return Fraction(0)
        if j!=p: M[j],M[p]=M[p],M[j];sign=-sign
        z=M[p][p];d*=z
        for j in range(p+1,n):
            q=M[j][p]/z
            for k in range(p+1,n):M[j][k]-=q*M[p][k]
            M[j][p]=Fraction(0)
    return sign*d

def cauchy(J,L):
    return [[Fraction(2,2*(k-j)+1) for j in J]for k in L]

checks=0
for m in range(1,5):
    for J in combinations(range(-2,3),m):
        for L in combinations(range(0,5),m):
            mat=cauchy(J,L)
            dv=abs(det(mat))
            num=1
            for r in range(m):
                for s in range(r+1,m):num*=abs(L[s]-L[r])*abs(J[s]-J[r])
            den=1
            for k in L:
                for j in J:den*=abs(2*(k-j)+1)
            assert dv == Fraction((2**(m*m))*num,den)
            checks+=1

# Arbitrary balanced/unbalanced pairs: compare principal-angle block eigenvalues.
for J,L in [([0],[0]),([0],[9]),([-1,2],[0,4]),([0,1],[0,1]),([0,1],[1]),([0],[0,2]),([0,2,5],[1,4,6])]:
    m=len(J);ell=len(L)
    C=1j*np.array(cauchy(J,L),dtype=float)/np.pi
    singular=np.linalg.svd(C,compute_uv=False)
    assert all(0<z<1 for z in singular[:min(m,ell)])
    T_eigs=[]
    for z in singular[:min(m,ell)]:T_eigs.extend([(1-sqrt(1-z*z))/2,(1+sqrt(1-z*z))/2])
    T_eigs += ([1.0]*max(0,ell-m)+[0.0]*max(0,m-ell))
    assert (min(T_eigs)>0) == (ell>=m)
    if ell>=m:
       assert abs(min(T_eigs)-(1-sqrt(1-min(singular)**2))/2)<1e-12
    checks+=1

# Exact Cauchy inverse formula checked against exact rational multiplication.
for m in range(1,5):
 for N in [1,2,7]:
    B=[[Fraction(2,2*(N+r-s)+1) for s in range(m)]for r in range(m)]
    V=[]
    for s in range(m):
        row=[]
        for r in range(m):
            top=Fraction(1)
            for h in range(m):top*=Fraction(2*(N+r-h)+1,2)
            for h in range(m):
                if h!=r:top*=Fraction(2*(s-N-h)-1,2)
            bot=1
            for h in range(m):
                if h!=r:bot*=r-h
                if h!=s:bot*=s-h
            row.append(top/bot)
        V.append(row)
    for r in range(m):
        for s in range(m):
            got=sum(B[r][h]*V[h][s] for h in range(m))
            assert got==int(r==s)
            checks+=1

mp.mp.dps=95
for m in [1,2,3,4]:
    Sm=mp.binomial(2*m-2,m-1)/mp.factorial(m-1)**2
    ratios=[]
    for N in [20,100,500]:
        B=mp.matrix([[1/(mp.mpf(N)+r-s+mp.mpf('0.5')) for s in range(m)] for r in range(m)])
        B_inv=B**-1
        sigma=1/(mp.pi*mp.svd(B_inv,compute_uv=False)[0])
        ratio=sigma*mp.pi*Sm*N**(2*m-1)
        ratios.append(float(ratio))
        assert 0.5<ratio<1.01
        checks+=1
    assert abs(ratios[-1]-1)<0.03
    assert abs(ratios[-1]-1)<abs(ratios[0]-1)
    checks+=2
print('PASS:',checks,'finite exact and numerical consistency checks')
