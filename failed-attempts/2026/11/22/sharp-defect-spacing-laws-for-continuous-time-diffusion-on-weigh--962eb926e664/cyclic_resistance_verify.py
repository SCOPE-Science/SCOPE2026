#!/usr/bin/env python3
"""Exact rational independent checks for cyclic resistance placement theorem.
Requires Python 3 standard library. Optional SymPy cross-check if installed.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd

def f(n,d): return d*(n-d)

def pair_energy(n, pos):
    return sum(f(n,b-a) for a,b in combinations(pos,2))

def extremes_formula(n,k):
    g=gcd(n,k)
    return (Fraction(k*(k*k-1)*(2*n-k),12),
            Fraction(n*n*(k*k-1)-k*k+g*g,12))

def balanced(n, pos):
    k=len(pos)
    gaps=[pos[(i+1)%k]-pos[i] if i<k-1 else n+pos[0]-pos[-1] for i in range(k)]
    for ell in range(1,k):
        lo=(ell*n)//k
        for i in range(k):
            s=sum(gaps[(i+j)%k] for j in range(ell))
            if s not in (lo,lo+1) or (ell*n)%k==0 and s!=lo:
                return False
    return True

def clustered(n,pos):
    k=len(pos)
    gaps=[pos[i+1]-pos[i] for i in range(k-1)]+[n+pos[0]-pos[-1]]
    return sorted(gaps)==[1]*(k-1)+[n-k+1]

def effective_K(n, marked, r):
    e=[r if i in marked else Fraction(1) for i in range(n)]
    R=sum(e)
    out=Fraction(0)
    for u in range(n):
        s=Fraction(0)
        for v in range(u+1,n):
            s+=e[v-1]
            out+=s*(R-s)/R
    return out

def claimed_K(n,k,r,S):
    delta=r-1
    return (Fraction(n*n*(n*n-1),12)+delta*Fraction(k*n*(n*n-1),6)+delta**2*S)/(n+k*delta)

checks=0
for n in range(4,13):
    for k in range(2,n-1):
        mn,mx=extremes_formula(n,k)
        assert mn <= mx and mn.denominator==mx.denominator==1
        for pos in combinations(range(n),k):
            S=pair_energy(n,pos)
            assert mn<=S<=mx,(n,k,pos,S,mn,mx)
            assert (S==mn)==clustered(n,pos),(n,k,pos,'min')
            assert (S==mx)==balanced(n,pos),(n,k,pos,'max')
            for r in (Fraction(1,2),Fraction(3)):
                exact=effective_K(n,set(pos),r)
                rhs=claimed_K(n,k,r,S)
                assert exact==rhs,(n,k,pos,r,exact,rhs)
                checks+=1
print('PASS: '+str(checks)+' all-subset rational resistance and exact equality checks, n=4..12')

# Independently compute resistance via grounding the graph Laplacian for samples.
try:
    import sympy as sp
    matchecks=0
    for n in range(4,9):
        for k in range(2,n-1):
            for pos in [tuple(range(k)), tuple(sorted(set((i*n)//k for i in range(k))))]:
                if len(pos)!=k: continue
                r=sp.Rational(3,2)
                rates=[1/r if i in pos else 1 for i in range(n)]
                L=sp.zeros(n)
                for i,c in enumerate(rates):
                    j=(i+1)%n;L[i,i]+=c;L[j,j]+=c;L[i,j]-=c;L[j,i]-=c
                G=L[:n-1,:n-1].inv()
                total=0
                for i in range(n):
                    for j in range(i+1,n):
                        if j==n-1: total+=G[i,i]
                        else: total+=G[i,i]+G[j,j]-2*G[i,j]
                assert total==sp.Rational(effective_K(n,set(pos),Fraction(3,2)))
                matchecks+=1
    print('PASS: '+str(matchecks)+' grounded-Laplacian independent resistance checks')
except ImportError:
    print('SymPy not installed: grounded-Laplacian optional check skipped')
