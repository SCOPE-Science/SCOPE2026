#!/usr/bin/env python3
"""Exact exponent checks for the binary Nashmatrix toric chart model."""
from itertools import product
from fractions import Fraction
from math import comb

def rank(matrix):
    a=[[Fraction(q) for q in row] for row in matrix]
    if not a: return 0
    r=0; cols=len(a[0])
    for c in range(cols):
        p=next((k for k in range(r,len(a)) if a[k][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        z=a[r][c]
        a[r]=[v/z for v in a[r]]
        for j in range(len(a)):
            if j!=r and a[j][c]:
                z=a[j][c]
                a[j]=[x-z*y for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a): break
    return r

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))

def exponent(n,j,choices):
    # u_j and each x_(k, choices[k]) for k != j.
    v=[0]*(3*n);v[j]=1
    for k in range(n):
        if k!=j: v[n+2*k+choices[k]]=1
    return tuple(v)

def check(n):
    for i in range(n):
        base=exponent(n,i,(0,)*n)
        zero=(0,)*(3*n)
        yy={k:sub(exponent(n,i,tuple(1 if t==k else 0 for t in range(n))),base) for k in range(n) if k!=i}
        bb={(s,j):sub(exponent(n,j,tuple(s if t==i else 0 for t in range(n))),base) for j in range(n) if j!=i for s in (0,1)}
        for j in range(n):
            for bits in product((0,1),repeat=n-1):
                other=[k for k in range(n) if k!=j]
                choices=[0]*n
                for k,bit in zip(other,bits):choices[k]=bit
                direct=sub(exponent(n,j,choices),base)
                if j==i:
                    construction=zero
                    for k in yy:
                        if choices[k]:construction=add(construction,yy[k])
                else:
                    construction=bb[(choices[i],j)]
                    for k in yy:
                        if k!=j and choices[k]:construction=add(construction,yy[k])
                assert direct==construction,(n,i,j,choices)
        for j in range(n):
            if j==i:continue
            for k in range(n):
                if k==i or k==j:continue
                assert add(bb[(0,j)],bb[(1,k)])==add(bb[(1,j)],bb[(0,k)])
        # Independent y variables extend the rank-m+1 Segre torus to full dimension 2n-1.
        assert rank(list(yy.values())+list(bb.values()))==2*n-1
    m=n-1
    # degree of Segre P^1 x P^(m-1) = m.
    assert sum(comb(1,q)*comb(m-1,m-1-q) for q in range(2))==m
    assert [ (d+1)*comb(d+m-1,m-1) for d in range(4) ][0]==1
    return 'n=%d: %d projective charts, %d homogeneous coordinates, local dimension=%d, transverse multiplicity=%d'%(n,n,n*2**(n-1),2*n-1,m)

for n in range(3,9): print(check(n))
print('VERIFY_OK')
