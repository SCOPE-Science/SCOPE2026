#!/usr/bin/env python3
"""Independent finite checks for the two local monotonicity lemmas.
No external packages or files are needed.
"""
from itertools import product

def T(w):
    i = w.find('1')
    return w if i < 0 else w[:i] + w[i+1:] + '1'

def iterate(w, k):
    for _ in range(k):
        w = T(w)
    return w

n_swap = n_last = 0
for length in range(0, 11):
    for b in product('01', repeat=length):
        a = ''.join(b)
        for split in range(length+1):
            x, y = a[:split], a[split:]
            left, right = x+'01'+y, x+'10'+y
            r = x.count('1') + 1
            for k in range(0, 13):
                u, v = iterate(left, k), iterate(right, k)
                assert (u == v) == (r <= k), (left,right,k,u,v)
                assert u <= v, (left,right,k,u,v)
                if k < r:
                    assert u < v
                n_swap += 1
        for k in range(0, 13):
            u, v = iterate(a+'0',k), iterate(a+'1',k)
            assert u < v, (a,k,u,v)
            n_last += 1
print(f'PASS local_swap={n_swap} terminal_change={n_last}')
