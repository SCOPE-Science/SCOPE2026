#!/usr/bin/env python3
"""Finite replay of the stated cyclic binary pair-profile theorem.
Requires only Python 3.10+ standard library.
"""
from itertools import product

def domain(n):
    return {(0,0),(n,0)} | {(k,t) for t in range(1,n//2+1)
                              for k in range(t,n-t+1)}

def profile(n,p):
    k,t=p
    return (n-k-t,t,t,k-t)

def d(a,b):
    dk=a[0]-b[0]; dt=a[1]-b[1]
    return max(abs(dk),abs(dt))+abs(dt)

def word_profile(bits):
    n=len(bits)
    return tuple(sum((bits[i],bits[(i+1)%n]) == (a,b)
                     for i in range(n)) for a,b in product((0,1),repeat=2))

def rep(n,point):
    k,t=point
    if t==0: return (0,)*n if k==0 else (1,)*n
    return (0,)*(n-k-t+1)+(1,0)*(t-1)+(1,)*(k-t+1)

def tiles(m):
    if m==0:return []
    c=[]
    for j in range(m-1):
        c.append(((4*j+1,1),(4*j+2,1),(4*j+3,1),(4*j+2,2)))
        c.append(((4*j+4,1),(4*j+3,2),(4*j+4,2),(4*j+5,2)))
    c.append(((4*m-3,1),(4*m-2,1),(4*m-1,1),(4*m-2,2)))
    return c+[tuple((k+2,t+2) for k,t in q) for q in tiles(m-1)]

def max_independent(points):
    pts=sorted(points); adj=[0]*len(pts)
    for i in range(len(pts)):
        for j in range(i):
            if d(pts[i],pts[j])<=2:
                adj[i]|=1<<j;adj[j]|=1<<i
    best=0
    def rec(available,size):
        nonlocal best
        if size+available.bit_count()<=best:return
        if not available:
            best=max(best,size);return
        v=available.bit_length()-1
        rec(available&~(1<<v)&~adj[v],size+1)
        rec(available&~(1<<v),size)
    rec((1<<len(pts))-1,0)
    return best

for n in range(1,14):
    observed={word_profile(bits) for bits in product((0,1),repeat=n)}
    assert observed=={profile(n,p) for p in domain(n)}
    for p in domain(n):
        word=rep(n,p)
        assert len(word)==n and word_profile(word)==profile(n,p)
        for q in domain(n):
            assert 2*d(p,q)==sum(abs(a-b) for a,b in zip(profile(n,p),profile(n,q)))
print('CYCLIC_WORD_ENUMERATION_OK')
for m in range(1,61):
    n=4*m; cs=tiles(m); D=domain(n)-{(0,0),(n,0)}
    flatten=[p for c in cs for p in c]
    assert len(cs)==m*m and len(flatten)==len(set(flatten))==len(D)
    assert set(flatten)==D
    for c in cs:
        assert len(c)==4
        assert all(d(c[i],c[j])<=2 for i in range(4) for j in range(i))
        assert {(k-2*t)%4 for k,t in c}=={0,1,2,3}
    S={p for p in domain(n) if p[1]==0 or (p[0]-2*p[1])%4==0}
    assert len(S)==m*m+2
    assert all(len(set(c)&S)==1 for c in cs)
    if m<=5:
        T=sorted(S)
        assert all(d(a,b)>=3 for i,a in enumerate(T) for b in T[:i])
print('RECURSIVE_TILE_AND_RESIDUE_CODE_OK')
for m in (1,2):
    assert max_independent(domain(4*m))==m*m+2
print('DIRECT_SMALL_OPTIMA_OK')
print('THEOREM_CHECKS_OK')
