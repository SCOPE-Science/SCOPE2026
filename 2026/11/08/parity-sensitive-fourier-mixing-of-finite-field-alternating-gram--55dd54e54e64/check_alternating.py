#!/usr/bin/env python3
"""Finite direct checks for wedge-walk Fourier mixing formulas.
Run with Python 3 standard library: python3 check_alternating.py
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import prod
import cmath

def finite_field(q):
    if q in (2,3,5):
        return (lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q), (lambda a: a%q)
    if q==4:
        def mul(a,b):
            z=0
            for i in range(2):
                if (a>>i)&1:
                    for j in range(2):
                        if (b>>j)&1:z^=1<<(i+j)
            if z&8:z^=0b1100
            if z&4:z^=0b111
            return z
        def trace(a):return a^mul(a,a)
        return (lambda a,b:a^b), mul, trace
    raise ValueError('unsupported test field')

def rank_matrix(B,q,add,mul):
    A=[list(row) for row in B]
    n=len(A); rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if A[i][col]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        inv=next(x for x in range(1,q) if mul(x,A[rank][col])==1)
        A[rank]=[mul(inv,z) for z in A[rank]]
        for row in range(rank+1,n):
            if A[row][col]:
                scalar=A[row][col]
                A[row]=[add(a, (-mul(scalar,b))%q if q !=4 else mul(scalar,b)) for a,b in zip(A[row],A[rank])]
        rank+=1
    return rank

def matrices(n,q,add,mul):
    pairs=list(combinations(range(n),2))
    for coords in product(range(q),repeat=len(pairs)):
        B=[[0]*n for _ in range(n)]
        for (i,j),z in zip(pairs,coords):
            B[i][j]=z
            B[j][i]=(-z)%q if q!=4 else z
        yield coords, B

def minus(x,q):return (-x)%q if q!=4 else x

def count_formula(n,q,r):
    if r==0:return 1
    # Gaussian binomial times number of nondegenerate 2r-forms.
    num=prod(q**(n-i)-1 for i in range(2*r))
    den=prod(q**(2*r-i)-1 for i in range(2*r))
    assert num%den==0
    return num//den*q**(r*(r-1))*prod(q**(2*j-1)-1 for j in range(1,r+1))

def tests(q,n,full=True):
    add,mul,tr=finite_field(q)
    pairs=list(combinations(range(n),2))
    N=q**len(pairs)
    counts=Counter()
    allmat=list(matrices(n,q,add,mul))
    for coords,B in allmat:
        rk=rank_matrix(B,q,add,mul)
        assert rk%2==0
        counts[rk]+=1
    for r in range(n//2+1):
        assert counts[2*r]==count_formula(n,q,r),(q,n,r,counts[2*r],count_formula(n,q,r))
    assert sum(counts.values())==N
    if full:
        vectors=list(product(range(q),repeat=n))
        increments=Counter()
        for u in vectors:
            for v in vectors:
                coords=tuple(add(mul(u[i],v[j]),minus(mul(v[i],u[j]),q)) for i,j in pairs)
                increments[coords]+=1
        assert sum(increments.values())==q**(2*n)
        for coords,B in allmat:
            rk=rank_matrix(B,q,add,mul)
            z=0j
            for a,count in increments.items():
                inner=0
                for aa,bb in zip(a,coords):inner=add(inner,mul(aa,bb))
                phase=(complex(-1 if tr(inner) else 1) if q==4 else cmath.exp(2j*cmath.pi*tr(inner)/q))
                z+=count*phase
            z/=q**(2*n)
            assert abs(z-q**(-rk))<1e-9,(q,n,coords,rk,z)
        def add_coords(x,y):return tuple(add(a,b) for a,b in zip(x,y))
        unif=Fraction(1,N)
        p=Counter({coords:Fraction(c,q**(2*n)) for coords,c in increments.items()})
        for t in (1,2,3):
            chi=sum((p.get(coords,Fraction(0))-unif)**2/unif for coords,_ in allmat)
            want=sum(Fraction(count_formula(n,q,r),q**(4*r*t)) for r in range(1,n//2+1))
            assert chi==want,(q,n,t,chi,want)
            if t<3:
                nxt=Counter()
                for a,pa in p.items():
                    for b,c in increments.items():
                        nxt[add_coords(a,b)]+=pa*Fraction(c,q**(2*n))
                p=nxt
    print('PASS',q,n,'rank_counts',dict(counts),'direct_characters',full)

for q,n,full in [(2,2,True),(2,3,True),(2,4,True),(2,5,False),(2,6,False),(3,2,True),(3,3,True),(3,4,False),(4,2,True),(4,3,True),(5,3,False)]:
    tests(q,n,full)
print('ALTERNATING_WEDGE_WALK_SPECTRAL_CHI2_CHECKS_PASS')
