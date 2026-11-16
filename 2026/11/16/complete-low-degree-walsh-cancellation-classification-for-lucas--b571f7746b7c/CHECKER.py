#!/usr/bin/env python3
"""Exact arithmetic verification of the first three Boolean Fourier levels on cycle independent-set families."""
from itertools import product,combinations
from math import comb

A=((1,1),(1,0))
B=((1,-1),(1,0))
I=((1,0),(0,1))

def mm(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def powA(k):
    assert k>=0
    x=I
    for _ in range(k): x=mm(x,A)
    return x

def trace(X):return X[0][0]+X[1][1]

def trace_marks(gaps):
    P=I
    for g in gaps:
        P=mm(mm(P,B),powA(g-1))
    return trace(P)

# The seed region {1,2,3,H} where H represents every integer >=4.
# A high coordinate is evaluated at its first two values, 4 and 5.
# Because A^2=A+I, fixed-sign seed pairs propagate to the full high range.
zero_triples=set()
rows=[]
for labels in product((1,2,3,4),repeat=3):
    options=[[v] if v<4 else [4,5] for v in labels]
    vals=[trace_marks(g) for g in product(*options)]
    signs={0 if z==0 else (1 if z>0 else -1) for z in vals}
    assert len(signs)==1,(labels,vals)
    sign=signs.pop()
    if sign==0:
        assert labels in set(product((1,2,3),repeat=3))
        zero_triples.add(labels)
    rows.append((labels,sign))
assert zero_triples==set(__import__('itertools').permutations((1,2,3)))

# First and second order, including the only triangle exception.
for n in range(3,40):
    assert trace_marks((n,))>0
    for d in range(1,n):
        w=trace_marks((d,n-d))
        if n==3:assert w==0
        elif d in (1,n-1):assert w<0
        else:assert w>0

# Independent direct enumeration of every low-degree Walsh character up to n=12.
for n in range(3,13):
    valid=[mask for mask in range(1<<n) if not any((mask>>i)&(mask>>((i+1)%n))&1 for i in range(n))]
    fib=[0,1]
    for _ in range(n+2):fib.append(fib[-1]+fib[-2])
    assert len(valid)==fib[n-1]+fib[n+1]
    for degree in range(1,4):
        for coord in combinations(range(n),degree):
            s=sum(1<<j for j in coord)
            direct=sum(1 if (mask&s).bit_count()%2==0 else -1 for mask in valid)
            g=tuple(((coord[(i+1)%degree]-coord[i])%n or n) for i in range(degree))
            matrix=trace_marks(g)
            assert direct==matrix,(n,coord,direct,matrix)
            if degree==1:assert direct>0
            if degree==2:assert (direct==0)==(n==3)
            if degree==3:
                assert (direct==0)==(n==6 and tuple(sorted(g))==(1,2,3))

print('LUCAS_CYCLE_CUBIC_WALSH_PASS; 64 sign regions; complete sparse Fourier checks n=3..12')
