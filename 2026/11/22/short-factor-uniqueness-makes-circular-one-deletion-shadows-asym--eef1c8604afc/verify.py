#!/usr/bin/env python3
"""Finite verification of circular one-deletion support under unique short factors."""
from itertools import product
from math import comb
from fractions import Fraction

def canon(word):
    return min(word[i:]+word[:i] for i in range(len(word)))

def profile(word):
    n=len(word)
    r=sum(word[i]!=word[(i+1)%n] for i in range(n))
    d=len({canon(word[:i]+word[i+1:]) for i in range(n)})
    return max(r,1),d

def distinct_factors(word,k):
    n=len(word)
    return len({tuple(word[(i+j)%n] for j in range(k)) for i in range(n)})==n

def expected_run_count(q,n,r):
    if r==0:
        return q
    return comb(n,r)*((q-1)**r+(q-1)*(-1)**r)

for q,nmax in [(2,14),(3,8),(4,6)]:
    checked=0; eligible=0; exceptions=0
    for n in range(2,nmax+1):
        hist=[0]*(n+1)
        for w in product(range(q),repeat=n):
            r,d=profile(w)
            hist[0 if r==1 else r]+=1
            checked+=1
            for k in range(1,(n-1)//2+1):
                if distinct_factors(w,k):
                    eligible+=1
                    assert r==d,(q,n,k,w,r,d)
            exceptions+=d<r
        assert hist[0]==q,(q,n,hist[0])
        for r in range(1,n+1):
            assert hist[r]==expected_run_count(q,n,r),(q,n,r,hist[r],expected_run_count(q,n,r))
    print('checked_q',q,'nmax',nmax,'words',checked,'unique-factor-instances',eligible,'run-collision-words',exceptions)

# The factor-repeat probability is exactly q^{-k} for each distinct pair
# of cyclic starts as long as k <= floor(n/2).
for q in [2,3]:
    for n in range(4,9):
        for k in range(1,n//2+1):
            counts={d:0 for d in range(1,n)}
            for word in product(range(q),repeat=n):
                u=word[:k]
                for d in range(1,n):
                    if u==tuple(word[(d+j)%n] for j in range(k)):
                        counts[d]+=1
            target=q**(n-k)
            assert set(counts.values())=={target},(q,n,k,counts,target)
print('VERIFY_OK')
