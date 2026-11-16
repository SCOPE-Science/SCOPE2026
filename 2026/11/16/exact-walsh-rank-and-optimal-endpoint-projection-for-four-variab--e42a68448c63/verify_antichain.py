#!/usr/bin/env python3
"""Exact integer certificate for the Fourier support of four-variable antichains."""
from collections import Counter
from csv import reader
from pathlib import Path
from math import gcd
from functools import reduce

Q = 1 << 16
ROOT = Path(__file__).resolve().parent

def transform(a):
    assert len(a) == Q
    for bit in range(16):
        step = 1 << bit
        for start in range(0, Q, 2 * step):
            for i in range(start, start + step):
                x, y = a[i], a[i + step]
                a[i], a[i + step] = x + y, x - y
    return a

def comparison_pairs():
    return tuple((a, b) for a in range(16) for b in range(a+1, 16)
                 if (a & b) == a or (a & b) == b)

def antichain_mask(mask, edges):
    return all(((mask >> a) & (mask >> b) & 1) == 0 for a, b in edges)

def certificate(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as f:
        r = reader(f)
        assert next(r) == ['coefficient', 'multiplicity']
        return {int(a): int(b) for a, b in r}

def main():
    pairs = comparison_pairs()
    assert len(pairs) == 65
    f = [int(antichain_mask(i, pairs)) for i in range(Q)]
    assert sum(f) == 168
    w = transform(f)
    wc = Counter(w)
    assert dict(sorted(wc.items())) == certificate('signed_walsh.csv')
    assert sum(wc.values()) == Q
    assert sum(v*v*c for v,c in wc.items()) == Q*168
    assert reduce(gcd, (abs(x) for x in w)) == 2
    assert sum(x==0 for x in w) == 6611
    assert min(abs(x) for x in w if x) == 2
    assert max(abs(x) for x in w) == 168
    h = transform([int(x != 0) for x in w])
    hc = Counter(h)
    assert dict(sorted(hc.items())) == certificate('projection_kernel.csv')
    assert h[0] == 58925
    assert sum(x*x for x in h) == Q*58925
    assert sum(abs(x) for x in h) == 3052046
    assert sum(h) == Q  # nonzero frequency at the trivial character
    print('ANTICHAIN_B4_FOURIER_PASS antichains=168 frequencies=65536 zeros=6611 rank=58925 '
          'projection=1526023/32768')

if __name__ == '__main__':
    main()
