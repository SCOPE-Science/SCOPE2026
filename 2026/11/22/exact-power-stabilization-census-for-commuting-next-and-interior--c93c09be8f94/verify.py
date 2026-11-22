#!/usr/bin/env python3
"""Independent finite checks for open finite-chain dynamics and power-index census."""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def predicted(n, r, t):
    if not (1 <= n and 0 <= r < n):
        return 0
    if r == 0:
        return int(t == 0)
    if t < 1:
        return 0
    k = n-r
    return sum(comb(r, s)*predicted(k, s, t-1)
               for s in range(min(r,k-1)+1))

def actual_index(f):
    n = len(f)
    power = tuple(range(n))
    for t in range(n+1):
        nxt = tuple(f[x] for x in power)
        if nxt == power:
            return t
        power = nxt
    raise AssertionError('finite chain failed to stabilize')

def all_open_maps(n):
    for bits in product((0,1),repeat=n-1):
        vals=[n-1-sum(bits)]
        for b in bits:
            vals.append(vals[-1]+b)
        yield tuple(vals)

def upper_interior(n, part):
    return frozenset(i for i in range(n) if all(j in part for j in range(i,n)))

def commute(n, f):
    for bits in product((0,1),repeat=n):
        p = frozenset(i for i,b in enumerate(bits) if b)
        interior=upper_interior(n,p)
        left=frozenset(i for i in range(n) if f[i] in interior)
        preimage=frozenset(i for i in range(n) if f[i] in p)
        right=upper_interior(n,preimage)
        if left!=right:
            return False
    return True

def run():
    testcount=0
    # Direct semantic verification against ALL functions and valuations on small chains.
    for n in range(1,6):
        expected=set(all_open_maps(n))
        for f in product(range(n),repeat=n):
            assert commute(n,f)==(f in expected), ('commutation',n,f)
            testcount+=1
    # Literally compose independently of the recurrence; compare full joint histogram.
    for n in range(1,13):
        freq=Counter()
        for f in all_open_maps(n):
            r=n-len(set(f))
            freq[(r,actual_index(f))]+=1
            testcount+=1
        assert sum(freq.values())==2**(n-1)
        for r in range(n):
            for t in range(n):
                assert freq[r,t]==predicted(n,r,t), ('count',n,r,t,freq[r,t],predicted(n,r,t))
                testcount+=1
            assert sum(freq[r,t] for t in range(n))==comb(n-1,r)
            if r>0:
                assert {t for t in range(n) if freq[r,t]>0}==set(range(1,n-r+1))
                assert freq[r,n-r]==(r if n-r>=2 else 1)
    print('VERIFY_OK',testcount)

if __name__=='__main__':
    run()
