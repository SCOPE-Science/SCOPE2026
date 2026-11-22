#!/usr/bin/env python3
"""Exact Boolean second-polar witness census for cubic-symplectic functions.

No third-party packages. All finite cases use the defining polynomial, rather
than the rank formulas used in the mathematical argument.
"""
from collections import Counter


def value(x, m):
    a = x & 7
    w = x >> 3
    total = int(a == 7)
    for j in range(m):
        total ^= ((w >> (2*j)) & 1) & ((w >> (2*j+1)) & 1)
    return total


def exact(m):
    q = 1 << (2*m)
    n = 8*q
    vals = [value(x,m) for x in range(n)]
    rows = []
    for x in range(n):
        mask=0
        for z in range(n):
            if vals[x ^ z] ^ vals[x] ^ vals[z]:
                mask |= 1 << z
        rows.append(mask)
    allmask=(1<<n)-1
    hist=Counter()
    for x in range(1,n):
        for y in range(1,n):
            if x != y:
                witness=(rows[x]&(~rows[y]&allmask)).bit_count()
                hist[witness]+=1
    expected={q:98*q-62, 2*q:64*(q-1)*(q-2), 3*q:70*q-70, 5*q:6}
    assert hist == expected, (m, hist,expected)
    assert sum(hist.values()) == (n-1)*(n-2)
    print(f'EXACT_WITNESS_SPECTRUM_OK m={m} Q={q} n={n} hist={dict(sorted(hist.items()))}')

if __name__=='__main__':
    for m in (1,2,3): exact(m)
