#!/usr/bin/env python3
"""Independent finite checks for sharp parallel right-Euclidean completion depth."""
import random, math

def next_relation(R):
    n=len(R)
    B=[row[:] for row in R]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if R[x][y] and R[x][z]:
                    B[y][z]=True
    return B

def depth(R):
    t=0
    while True:
        S=next_relation(R)
        if S==R: return t
        t+=1
        assert t<=100
        R=S

def binary_relation(bits,n):
    return [[bool(bits & (1 << (i*n+j))) for j in range(n)] for i in range(n)]

def check(R, expected_bound):
    n=len(R)
    T={y for y in range(n) if any(R[x][y] for x in range(n))}
    S=next_relation(R)
    U=next_relation(S)
    for x in range(n):
        if x not in T: assert U[x]==R[x],('outside-target change',n)
    for x in T:
        assert U[x][x]
        for y in T: assert U[x][y]==U[y][x],('not symmetric',n)
    # Every pair at R2 graph-distance <= 2^s appears after another s rounds.
    current=U
    for s in range(max(0,expected_bound-2)+1):
        comp=[set([x]) for x in range(n)]
        for x in T:
            reached={x}; frontier={x}
            for _ in range(2**s):
                frontier={z for v in frontier for z in T if U[v][z]}-reached
                reached|=frontier
                if not frontier:break
            for y in T: assert current[x][y] == (y in reached),('distance formula',n,s,x,y)
        if s<expected_bound-2: current=next_relation(current)
    assert depth(R)<=expected_bound

checks=0
for n in range(1,5):
    b=0 if n==1 else (1 if n==2 else 2+math.ceil(math.log2(n-2)))
    mx=0
    for mask in range(1 << (n*n)):
        R=binary_relation(mask,n)
        if n>=3: check(R,b)
        t=depth(R)
        assert t<=b
        mx=max(mx,t); checks+=1
    assert mx==b,('incorrect extremal',n,mx,b)
for n in range(3,65):
    path=[[i+1==j for j in range(n)] for i in range(n)]
    b=2+math.ceil(math.log2(n-2))
    assert depth(path)==b,(n,b,depth(path))
    check(path,b);checks+=1
rng=random.Random(314159)
for n in range(5,13):
    for _ in range(200):
        p=rng.uniform(0.03,0.5)
        R=[[rng.random()<p for j in range(n)] for i in range(n)]
        b=2+math.ceil(math.log2(n-2))
        check(R,b);checks+=1
print('VERIFY_OK',checks)
