#!/usr/bin/env python3
"""Exact standalone small-modulus and high-precision checks for the Narayana branches."""
from collections import Counter
from random import Random

A = ((0,1,0),(0,0,1),(1,0,1))
I = ((1,0,0),(0,1,0),(0,0,1))
B = ((1,1,2),(2,1,3),(3,2,4))
C = ((10,7,15),(15,10,22),(22,15,32))

def matmul(X,Y,mod=None):
    rows = tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    if mod is not None:
        return tuple(tuple(v%mod for v in row) for row in rows)
    return rows

def matpow(X,n,mod=None):
    Q=I
    while n:
        if n&1:Q=matmul(Q,X,mod)
        X=matmul(X,X,mod)
        n>>=1
    return Q

def state(n,mod):
    m=matpow(A,n,mod)
    return tuple((m[i][1]+m[i][2])%mod for i in range(3))

assert matpow(A,7)==tuple(tuple(I[i][j]+2*B[i][j] for j in range(3)) for i in range(3))
assert matpow(A,14)==tuple(tuple(I[i][j]+4*C[i][j] for j in range(3)) for i in range(3))
assert state(3,128)==(1,2,3) and state(4,128)==(2,3,4)
for k in range(1,15):
    mod=1<<k
    period=7*(1<<(k-1))
    a,b,c=0,1,1
    observed=[]
    for n in range(period):
        observed.append(a)
        a,b,c=b,c,(a+c)%mod
    assert (a,b,c)==(0,1,1),('not period',k)
    # No smaller full period: the 3-branch is injective in its index modulo 2^(k-1).
    for r,parity in ((3,1),(4,0)):
        xs=[observed[r+7*j] for j in range(1<<(k-1))]
        assert len(set(xs))==len(xs)
        assert set(xs)==set(range(parity,mod,2))
    assert len(set(observed))==mod
    if k>=3:
        counts=Counter(observed)
        for y in range(mod):
            if y%8 in (2,7):
                assert counts[y]==1, ('singleton cylinder',k,y,counts[y])
        for r0 in range(7):
            possible={observed[r0+7*j]%8 for j in range(1<<(k-1))}
            if r0==3:
                assert 7 in possible and 2 not in possible
            elif r0==4:
                assert 2 in possible and 7 not in possible
            else:
                assert not ({2,7}&possible),('other row sector',k,r0)
    if k>1:
        # Period 7*2^(k-2) is not a period of the value sequence.
        assert observed[3] != observed[(3+period//2)%period]
    for r in (3,4):
        for h in range(k-1):
            step=1<<h
            idx=r+7*step
            assert (state(idx,1<<(h+2))[0]-state(r,1<<(h+2))[0])%(1<<(h+2))==(1<<(h+1))
print('EXHAUSTIVE_OK k=1..14')

rng=Random(20261117)
for h in range(0,80):
    modulus=1<<(h+2)
    for r in (3,4):
        for _ in range(12):
            j=rng.randrange(1<<20)
            y=state(r+7*j,modulus)[0]
            z=state(r+7*(j+(1<<h)),modulus)[0]
            assert (z-y)%modulus==1<<(h+1),(r,h,j)
print('HIGH_PRECISION_OK 1920 matrix increment comparisons')
print('VERIFY_OK')
