#!/usr/bin/env python3
"""Exact independent Walsh checks for C4-free 3-by-n binary matrices."""
from itertools import combinations, permutations
from math import comb
from random import Random

PAIRS = (3, 5, 6)
PAIR_MASK = tuple(sum((1 << i) for i, pair in enumerate(PAIRS)
                      if (c & pair) == pair) for c in range(8))

def signed(c, s):
    return -1 if (c & s).bit_count() & 1 else 1

def closed_formula(frequency):
    n = len(frequency)
    light = [1+signed(1,s)+signed(2,s)+signed(4,s) for s in frequency]
    ans = 0
    for k in range(4):
        for pair_set in combinations(PAIRS, k):
            for js in permutations(range(n),k):
                used=set(js)
                term=1
                for pair, j in zip(pair_set, js):
                    term*=signed(pair,frequency[j])
                for j in range(n):
                    if j not in used:
                        term*=light[j]
                ans+=term
    for j in range(n):
        term=signed(7,frequency[j])
        for h in range(n):
            if h!=j:
                term*=light[h]
        ans+=term
    return ans

def state_sum(frequency):
    states={0:1}
    for s in frequency:
        new={}
        for used, count in states.items():
            for c in range(8):
                p=PAIR_MASK[c]
                if p&used: continue
                nxt=used|p
                new[nxt]=new.get(nxt,0)+count*signed(c,s)
        states=new
    return sum(states.values())

def brute_spectrum(n):
    f=[0]*(1<<(3*n))
    for x in range(len(f)):
        used=0
        good=True
        for j in range(n):
            p=PAIR_MASK[(x>>(3*j))&7]
            if p&used:
                good=False
                break
            used|=p
        if good: f[x]=1
    number=sum(f)
    for step in (1 << i for i in range(3*n)):
        for base in range(0,len(f),2*step):
            for j in range(step):
                u,v=f[base+j],f[base+j+step]
                f[base+j],f[base+j+step]=u+v,u-v
    return number,f

EXPECTED = {2:(54,0,2),3:(334,0,2),4:(1952,621,4),5:(10944,3138,8)}
for n,(want_n,want_zero,want_gap) in EXPECTED.items():
    count, w=brute_spectrum(n)
    zero=sum(v==0 for v in w)
    gap=min(abs(v) for v in w if v!=0)
    assert (count,zero,gap)==(want_n,want_zero,want_gap)
    assert sum(v*v for v in w)==len(w)*count
    for frequency_mask in range(len(w)):
        freq=tuple((frequency_mask>>(3*j))&7 for j in range(n))
        if n<=3 or (frequency_mask%(1+len(w)//100))==0:
            assert w[frequency_mask]==closed_formula(freq)
    print("BRUTE",n,count,zero,gap)
rng=Random(2037)
for n in range(2,21):
    witness=[3,3] if n==2 else [1]*(n-3)+[3,3,5]
    assert state_sum(witness)==closed_formula(witness)==-(2 if n==2 else 2**(n-2))
    if n>=4:assert state_sum([3]*n)==closed_formula([3]*n)==0
    for _ in range(12):
        freq=[rng.randrange(8) for j in range(n)]
        a=closed_formula(freq)
        assert a==state_sum(freq)
        if n>=3: assert a%2**(n-2)==0
print("C4FREE_INDEPENDENT_BRUTE_AND_FORMULA_PASS")
