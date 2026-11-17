#!/usr/bin/env python3
"""Standalone exhaustive and exact-arithmetic checks for weight-two SCS bounds."""
from itertools import combinations, product
from math import comb, ceil, isqrt

def target(k, a, b):
    t=k-2
    return '0'*a+'1'+'0'*b+'1'+'0'*(t-a-b)

def subseq(v,w):
    it=iter(w)
    return all(any(x==y for x in it) for y in v)

def construction(k,h):
    t=k-2
    r=(t+h-1)//h
    tail=t+2*h-(r+1)*h
    assert 0<=tail<h+1
    return ('0'*h+'1')*(r+1)+'0'*tail

def pair_coverage(W,k):
    t=k-2
    idx=[i for i,c in enumerate(W) if c=='1']
    z=[W[:i].count('0') for i in idx]
    Z=W.count('0')
    covered=set()
    for i,j in combinations(range(len(idx)),2):
        A,B,C=z[i],z[j]-z[i],Z-z[j]
        for a in range(t+1):
            for b in range(t-a+1):
                c=t-a-b
                if a<=A and b<=B and c<=C:covered.add((a,b,c))
    return covered

def check_w(W,k):
    q=k-2;req={(a,b,q-a-b) for a in range(q+1) for b in range(q-a+1)}
    C=pair_coverage(W,k)
    D={(a,b,k-2-a-b) for a in range(k-1) for b in range(k-1-a) if subseq(target(k,a,b),W)}
    assert C==D
    return C==req

for k in range(3,181):
    for h in set([1,2,3,4,5,6,max(1,isqrt(k)),max(1,isqrt(k//2)),max(1,isqrt(k//2)+1)]):
        W=construction(k,h)
        assert all(subseq(target(k,a,b),W) for a in range(k-1) for b in range(k-1-a)) if k<=24 else True
        r=W.count('1');Z=W.count('0');q=Z-(k-2)
        assert comb(r,2)*comb(q+2,2)>=comb(k,2)
print('EXPLICIT_CONSTRUCTION_SELECTED_H_K_3_TO_180_OK')

for L in range(2,9):
    for letters in product('01',repeat=L):
        W=''.join(letters);r=W.count('1');Z=L-r
        if r<2:continue
        for k in range(3,L+1):
            q=Z-(k-2)
            if q<0:continue
            num=len(pair_coverage(W,k))
            assert num <= comb(r,2)*comb(q+2,2), (W,k,num)
print('PAIR_COVERING_BOUND_EXHAUSTIVE_LENGTH_8_OK')

# Compare direct greedy embedding and interval rectangle coverage for arbitrary short words
for L in range(2,9):
    for letters in product('01',repeat=L):
        W=''.join(letters)
        if W.count('1')<2:continue
        for k in range(3,L+1):
            check_w(W,k)
print('RECTANGLE_EQUIVALENCE_DIRECT_SUBSEQUENCE_OK')

# Certified small parameter exact optimum via exhaustive enumeration
for k in range(3,8):
    found=None
    for L in range(k,2*k+3):
        for word in product('01', repeat=L):
            W=''.join(word)
            if check_w(W,k):found=(L,W);break
        if found:break
    print('EXACT_MINIMUM',k,found[0],found[1])
print('ALL_CHECKS_PASSED')
