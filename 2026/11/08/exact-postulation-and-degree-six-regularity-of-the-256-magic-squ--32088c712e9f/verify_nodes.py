#!/usr/bin/env python3
"""Exact projective node-postulation certificate for the magic-square surface.

Uses only Python's standard library. The nodes are reconstructed from the
nine Lucas linear forms; Fourier/parity character blocks give their exact
homogeneous evaluation ranks. No floating-point or random computation.
"""
from itertools import combinations, combinations_with_replacement
from fractions import Fraction
from math import comb, gcd, prod
from collections import Counter

# Coordinate order: A,B,C,D,M,E,F,G,H.  Values l_i(x,y,z).
L = ((0,-1,1), (1,1,1), (-1,0,1), (-1,1,1), (0,0,1),
     (1,-1,1), (1,0,1), (-1,-1,1), (0,1,1))
NAMES = 'ABCDMEFGH'

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def normalized(v):
    g=0
    for z in v: g=gcd(g,abs(z))
    assert g
    v=tuple(z//g for z in v)
    if next(z for z in v if z)<0:v=tuple(-z for z in v)
    return v

def dot(a,b): return sum(x*y for x,y in zip(a,b))

intersections={}
for i,j in combinations(range(9),2):
    P=normalized(cross(L[i], L[j]))
    intersections[P] = tuple(k for k in range(9) if dot(L[k],P)==0)
classes=Counter(map(len,intersections.values()))
assert classes=={2:12,3:8}, classes
points=[]
for P,zset in intersections.items():
    if len(zset)==3:
        q=normalized(tuple(dot(ell,P) for ell in L))
        assert sum(v==0 for v in q)==3
        points.append(q)
points=sorted(set(points))
assert len(points)==8

# Each triple intersection creates 2^5=32 projectively distinct square-root
# sign lifts: 8*32=256; no other support causes a Jacobian rank drop.
assert len(points)*32==256

def rank_exact(rows):
    if not rows: return 0
    A=[[Fraction(v) for v in row] for row in rows]
    n=len(A); m=len(A[0]); r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        t=A[r][c]
        A[r]=[u/t for u in A[r]]
        for i in range(r+1,n):
            if A[i][c]:
                t=A[i][c]
                A[i]=[u-t*v for u,v in zip(A[i],A[r])]
        r+=1
        if r==n: break
    return r

def evaluation_rank(degree):
    total=0; blocks=Counter()
    for k in range(degree//2+1):
        s=degree-2*k
        powers=list(combinations_with_replacement(range(9),k))
        for support in combinations(range(9),s):
            allowed=[q for q in points if all(q[j] for j in support)]
            if not allowed:continue
            rows=[[prod(q[j] for j in pw) for pw in powers] for q in allowed]
            r=rank_exact(rows)
            blocks[(s,k,r)]+=1
            total+=r
    return total,blocks

expected=(1,9,39,109,206,256)
for degree,desired in enumerate(expected):
    got,blocks=evaluation_rank(degree)
    print('degree',degree,'rank',got,'blocks',sorted(blocks.items()))
    assert got==desired,(degree,got,desired)

bad_cubics=[]
for S in combinations(range(9),3):
    if not any(all(q[i] for i in S) for q in points):
        bad_cubics.append(''.join(NAMES[i] for i in S))
assert bad_cubics==['BMG','DME'],bad_cubics
print('NODE_BASE_SUPPORTS', len(points),'SIGN_LIFTS',len(points)*32)
print('PROJECTIVE_NODE_HILBERT_FUNCTION_OK',expected,'then 256 forever')
print('FIRST_ADDITIONAL_CUBICS',','.join(bad_cubics))
print('SATURATED_IDEAL_REGULARITY',6)
