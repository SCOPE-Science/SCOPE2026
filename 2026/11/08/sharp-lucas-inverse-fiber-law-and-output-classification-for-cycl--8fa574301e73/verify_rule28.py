#!/usr/bin/env python3
"""Independent finite checks for the exact inverse fibers of periodic elementary Rule 28.
Uses only Python's standard library; does not rely on any precomputed result table.
"""
from collections import Counter
from itertools import product

def step(x,n):
    out=0
    for i in range(n):
        a=(x>>((i-1)%n))&1
        b=(x>>i)&1
        c=(x>>((i+1)%n))&1
        out|=(((28>>((a<<2)|(b<<1)|c))&1)<<i)
    return out

def mat_mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def mat_trace(A):
    return A[0][0]+A[1][1]

F=[[1,1],[1,0]]
E=[[0,1],[0,0]]

def pred_count_from_gaps(y,n):
    pos=[i for i in range(n) if (y>>i)&1]
    if not pos:return 2
    gaps=[]
    for a,b in zip(pos,pos[1:]+[pos[0]+n]):
        gaps.append(b-a-1)
    P=[[1,0],[0,1]]
    for gap in gaps:
        P=mat_mul(P,F if gap>0 else E)
    return mat_trace(P)

def lucas(k):
    a,b=2,1
    for _ in range(k):a,b=b,a+b
    return a

def is_winner(y,n):
    if n<4:return y==0
    k=n//2
    if y.bit_count()!=k:return False
    return all(not ((y>>i)&1 and (y>>((i+1)%n))&1) for i in range(n))

# Independent exhaustive direct lookup: all indexed sources and all indexed targets.
checks=0
for n in range(1,18):
    c=Counter(step(x,n) for x in range(1<<n))
    M=max(c.values())
    assert M==(2 if n<4 else lucas(n//2)), (n,M)
    actual_winners={y for y,z in c.items() if z==M}
    expected_winners={y for y in range(1<<n) if is_winner(y,n)}
    assert actual_winners==expected_winners, (n,actual_winners^expected_winners)
    for y in range(1<<n):
        got=c.get(y,0)
        predicted=pred_count_from_gaps(y,n)
        assert got==predicted,(n,y,got,predicted)
        checks+=1

# Exact transfer reduction identities, independent of the finite census.
Z=[[1,1,0,0],[0,0,0,0],[0,1,0,0],[0,0,1,1]]
O=[[0,0,0,0],[0,0,1,1],[1,0,0,0],[0,0,0,0]]

def mul4(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

Z2=mul4(Z,Z)
assert Z2==mul4(Z,Z2)
assert [[O[i][j] for j in [1,2]] for i in [1,2]]==E
assert [[mul4(O,Z)[i][j] for j in [1,2]] for i in [1,2]]==F
assert all((E[0][j] if i==0 else E[1][j])<=F[i][j] for i in range(2) for j in range(2))
assert mat_mul(E,F)==[[1,0],[0,0]]

# Longer Fibonacci/Lucas identities and representative output profiles.
for m in range(2,300):
    n=2*m
    y=sum(1<<i for i in range(0,n,2))
    assert pred_count_from_gaps(y,n)==lucas(m)
    n+=1
    assert pred_count_from_gaps(y,n)==lucas(m)
print(f'VERIFY_OK exhaustive_outputs={checks} n=1..17 longer_profiles=596')
