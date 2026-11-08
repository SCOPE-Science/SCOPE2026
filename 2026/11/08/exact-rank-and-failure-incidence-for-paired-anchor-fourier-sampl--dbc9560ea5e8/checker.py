#!/usr/bin/env python3
"""Reproduce the exact paired-column, balanced-row Fourier rank census.
No external packages are required. Python 3.8+.
"""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random

def exact_minor_zero(p, A, B, y0, y1, y2):
    # Exact root-of-unity expansion after anchored-column elimination.
    # Signed group-ring coefficients sum to zero; hence zero at a primitive
    # pth root is equivalent to every coefficient being zero.
    counts = Counter()
    t1, t2 = (y1-y0)%p, (y2-y0)%p
    for x,sx in ((A[0],1),(A[1],-1)):
        for u,su in ((B[0],1),(B[1],-1)):
            counts[(x*t1+u*t2)%p] += sx*su
            counts[(x*t2+u*t1)%p] -= sx*su
    assert sum(counts.values()) == 0
    return all(v == 0 for v in counts.values())

def criterion(p,A,B,y0,y1,y2):
    same_mid = (sum(A)-sum(B))%p == 0
    return same_mid and (A == B or (y1+y2-2*y0)%p == 0)

def test(p, exhaustive):
    pairs = list(combinations(range(p),2))
    examined=singular=0
    if exhaustive:
        for A in pairs:
            for B in pairs:
                for y0 in range(p):
                    ys=[y for y in range(p) if y != y0]
                    for y1,y2 in combinations(ys,2):
                        got=exact_minor_zero(p,A,B,y0,y1,y2)
                        expect=criterion(p,A,B,y0,y1,y2)
                        assert got==expect,(p,A,B,y0,y1,y2,got,expect)
                        examined+=1
                        singular+=int(got)
        # Each configuration above has two choices of the majority parity.
        singular*=2; examined*=2
        predicted=p*p*(p-1)**2*(3*p-7)//4
        total=comb(p,2)**2*2*p*comb(p-1,2)
        assert (singular,examined)==(predicted,total),(singular,examined,predicted,total)
        print('p=',p,'EXHAUSTIVE','samples=',examined,'rank3=',singular,'rank4=',examined-singular)
    else:
        rng=Random(421+p)
        for _ in range(3500):
            A,B=rng.choice(pairs),rng.choice(pairs)
            y0=rng.randrange(p)
            y1,y2=rng.sample([y for y in range(p) if y!=y0],2)
            got=exact_minor_zero(p,A,B,y0,y1,y2)
            exp=criterion(p,A,B,y0,y1,y2)
            assert got == exp,(p,A,B,y0,y1,y2)
        print('p=',p,'RANDOM_EXACT','samples=',3500)

for p in (3,5,7,11): test(p,True)
for p in (13,17,19,23): test(p,False)
print('PAIR_ANCHOR_FOURIER_RANK_CENSUS_PASS')
