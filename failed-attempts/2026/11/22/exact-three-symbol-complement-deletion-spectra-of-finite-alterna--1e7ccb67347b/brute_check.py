#!/usr/bin/env python3
"""Independent direct enumeration of prescribed positional deletions."""
from itertools import combinations, product
from math import comb

def C(n,k):
    return comb(n,k) if 0<=k<=n else 0

def predicted(u, length):
    if length%2==0:
        n=length//2
        if u in ('000','111'): return C(n,3)
        if u in ('001','011'): return C(n-1,3)+C(n,2)
        if u in ('010','101'): return C(n-1,3)+(n-1)
        if u in ('100','110'): return C(n-2,3)+C(n-1,2)
    else:
        n=(length-1)//2
        if u=='000': return C(n+1,3)
        if u=='111': return C(n,3)
        if u in ('001','011','100','110'): return C(n,2)+C(n-1,3)
        if u=='010': return n+C(n,3)
        if u=='101': return (n-1)+C(n-1,3)
    raise AssertionError(u)

def direct(w,u):
    rem=set()
    for inds in combinations(range(len(w)),3):
        if ''.join(w[i] for i in inds)==u:
            bad=set(inds)
            rem.add(''.join(w[j] for j in range(len(w)) if j not in bad))
    return rem

if __name__=='__main__':
    tests=0
    for length in range(3,25):
        w=''.join(str(i%2) for i in range(length))
        for p in product('01',repeat=3):
            u=''.join(p)
            actual=len(direct(w,u))
            assert actual==predicted(u,length),(length,u,actual,predicted(u,length))
            # Bit-complement symmetry covers the opposite starting symbol.
            w1=''.join('1' if c=='0' else '0' for c in w)
            u1=''.join('1' if c=='0' else '0' for c in u)
            assert len(direct(w1,u1))==actual
            tests+=1
    print('BRUTE_CHECK_OK',tests,'host-pattern cases, host lengths 3..24, both starting phases')
