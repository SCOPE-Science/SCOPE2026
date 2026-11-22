#!/usr/bin/env python3
"""Exact rational/integer reproducibility checks for three-tap binary CA cylinders."""
from itertools import combinations

def rem_p(bits):
    """Long division by P=1+z+z^2, GF(2), returns remainder bitmask."""
    while bits.bit_length()>=3:
        sh=bits.bit_length()-3
        bits ^= 7<<sh
    return bits

def vp(bits):
    v=0
    while bits and rem_p(bits)==0:
        q=0
        r=bits
        while r.bit_length()>=3:
            sh=r.bit_length()-3
            q ^= 1<<sh
            r ^= 7<<sh
        assert r==0
        bits=q
        v+=1
    return v

def pred(S):
    S=sorted(S); assert len(S)==3
    a,b,c=S
    if len({a%3,b%3,c%3})==3:
        ds=[b-a,c-a,c-b]
        m=min((d&-d).bit_length()-1 for d in ds)
        return 1+(1<<m)
    ds=[abs(x-y) for x,y in combinations(S,2) if (x-y)%3==0]
    return 1+max(1<<((d&-d).bit_length()-1) for d in ds)

def codim(S,n):
    """Exact index exponent for the image of any cylinder on three sites."""
    S=sorted(S); a,b,c=S
    residues=[a%3,b%3,c%3]
    if len(set(residues))==3:
        s=min(((d&-d).bit_length()-1 for d in (b-a,c-a,c-b)))
        return int(n<=1<<s)
    same=[x-y for x,y in combinations(S,2) if (x-y)%3==0]
    powers=sorted((1<<((abs(d)&-abs(d)).bit_length()-1) for d in same))
    if len(powers)==1: return int(n<=powers[0])
    return (2 if n<=powers[0] else 1 if n<=powers[-1] else 0)

def independent_val(S):
    vv=[]
    for r in range(1,len(S)+1):
        for subset in combinations(S,r):
            poly=sum(1<<i for i in subset)
            vv.append(vp(poly))
    return 1+max(vv)

def gf2rank(rows):
    basis={}
    for row in rows:
        x=row
        while x:
            p=x.bit_length()-1
            if p in basis: x ^=basis[p]
            else:
                basis[p]=x
                break
    return len(basis)

def matrix_codim(S,n):
    # F^n output polynomial at every location, coefficient mask of (1+z+z²)^n.
    q=1
    for _ in range(n):
        q=q^(q<<1)^(q<<2)
    L=max(S)+1
    rows=[]
    for i in range(L):
        row=(q<<i)
        for s in S: row &= ~(1<<s)
        rows.append(row)
    return L-gf2rank(rows)

cases=0; mat=0
for span in range(2,37):
    for a,b in combinations(range(1,span),2):
        S=(0,a,b)
        v=pred(S)
        w=independent_val(S)
        assert v==w,(S,v,w)
        cases+=1
        if span<=18:
            for n in range(1,min(24,v+2)):
                assert matrix_codim(S,n)==codim(S,n),(S,n,v, matrix_codim(S,n),codim(S,n))
                mat+=1
    S=(0,span-1,span)
    assert pred(S)==independent_val(S)
# all 3 sites within length<=60
for end in range(2,61):
    for a in range(1,end):
        S=(0,a,end)
        assert pred(S)==independent_val(S),(S,pred(S),independent_val(S))
        cases+=1
# two-site boundary
for d in range(1,81):
    valuation=vp(1|(1<<d))
    formula=(1<<((d&-d).bit_length()-1)) if d%3==0 else 0
    assert valuation==formula,(d,valuation,formula)
for L in range(2,121):
    bound=1<<( (L//2).bit_length()-1)
    theoretical=1+bound
    # exhaustive for L<=55, upper bound proved analytically
    if L<=55:
        maxdelay=max(pred((0,a,b)) for b in range(2,L+1) for a in range(1,b))
        assert maxdelay==theoretical,(L,maxdelay,theoretical)
    assert pred((0,bound,2*bound))==theoretical,(L,bound)
print('PASS: exact polynomial valuations and theoretical classification for',cases,'triads;')
print('PASS: independent GF(2) image codimension computations:',mat)
print('PASS: all pairs to spacing 80, sharp span extrema to 120')
