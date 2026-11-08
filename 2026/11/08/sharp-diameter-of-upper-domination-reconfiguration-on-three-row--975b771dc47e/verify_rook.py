#!/usr/bin/env python3
"""Independent exhaustive vertex-subset validation of upper domination on 3 by n rook graphs."""
from itertools import combinations
from math import comb


def dominated(s,n):
    rows = 0; cols = 0
    for v in s:
        rows |= 1 << (v//n)
        cols |= 1 << (v%n)
    return rows == 7 or cols == (1 << n)-1


def is_minimal(s,n):
    return dominated(s,n) and all(not dominated((u for u in s if u != v),n) for v in s)

for n in range(4,8):
    upper = []
    for k in range(3*n, n,-1):
        z=0
        for s in combinations(range(3*n),k):
            if is_minimal(s,n):z+=1
        assert z==0, (n,k,z)
    for s in combinations(range(3*n),n):
        if is_minimal(s,n):upper.append(frozenset(s))
    expect=3*(2**n)-3
    assert len(upper)==expect,(n,len(upper),expect)
    assert all(len({v%n for v in s})==n and len({v//n for v in s})<3 for s in upper)
    U=set(upper)
    jumps=slides=0
    for s in U:
        for v in s:
            for w in range(3*n):
                if w in s:continue
                t=s.difference((v,)).union((w,))
                if t in U:
                    jumps+=1
                    if v%n==w%n or v//n==w//n:slides+=1
    assert jumps==slides==6*n*(2**(n-1)+1),(n,jumps,slides)
    print(f'n={n} upper={len(upper)} jump_edges={jumps//2} slide_edges={slides//2} matched')
print('DIRECT_ROOK_OK')
