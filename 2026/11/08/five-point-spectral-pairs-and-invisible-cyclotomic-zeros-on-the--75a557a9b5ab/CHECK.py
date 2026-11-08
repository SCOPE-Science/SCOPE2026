#!/usr/bin/env python3
"""Exact integer exhaustive certificate for five-site Fourier spectra on Z/30Z.

Run: python3 CHECK.py.  No dependencies beyond the standard library.
"""
from itertools import combinations
from collections import Counter
from math import gcd

N = 30
D = (2, 3, 5, 6, 10, 15, 30)

def exact_division(f, g):
    f = list(f)
    out = [0] * (len(f) - len(g) + 1)
    while len(f) >= len(g):
        c = f[-1]  # g is monic
        pos = len(f) - len(g)
        out[pos] = c
        for j in range(len(g)):
            f[pos + j] -= c * g[j]
        while f and f[-1] == 0:
            f.pop()
    assert not f
    return out

def cyclotomic(d):
    f = [-1] + [0] * (d-1) + [1]
    for e in range(1, d):
        if d % e == 0:
            f = exact_division(f, phi[e])
    return f

phi = {}
for d in (1, 2, 3, 5, 6, 10, 15, 30):
    phi[d] = cyclotomic(d)

powers = {}
for d in D:
    poly = phi[d]
    m = len(poly)-1
    v = [1] + [0] * (m-1)
    res = []
    for _ in range(N):
        res.append(tuple(v))
        lead = v[-1]
        v = [0] + v[:-1]
        for j in range(m):
            v[j] -= lead * poly[j]
    powers[d] = res

def zero_mask(A):
    mask = 0
    for i,d in enumerate(D):
        v = powers[d]
        if all(sum(v[a][j] for a in A) == 0 for j in range(len(v[0]))):
            mask |= 1 << i
    return mask

counts = Counter()
examples = {}
for A in combinations(range(N), 5):
    z = zero_mask(A)
    counts[z] += 1
    examples.setdefault(z, A)
assert sum(counts.values()) == 142506

requirements = Counter()
for B in combinations(range(N), 5):
    req = 0
    for x,y in combinations(B, 2):
        order = N // gcd(N, y-x)
        req |= 1 << D.index(order)
    requirements[req] += 1

expected = {
    (): 127590, (6,):7020, (5,):6840, (5,6):360,
    (5,10):480, (5,15):90, (6,30):120, (5,10,15,30):6,
}
key = lambda mask: tuple(d for i,d in enumerate(D) if mask >> i & 1)
assert {key(mask):num for mask,num in counts.items()} == expected

spectral = {}
for mask, count in counts.items():
    bcount = sum(c for req,c in requirements.items() if not (req & ~mask))
    if bcount:
        spectral[key(mask)] = (count,bcount)
assert spectral == {
    (5,):(6840,6), (5,6):(360,6), (5,10):(480,96),
    (5,15):(90,486), (5,10,15,30):(6,7776),
}
assert sum(a for a,b in spectral.values()) == 7776
assert sum(a*b for a,b in spectral.values()) == 179676
assert sum(a*b for a,b in spectral.values()) == sum(
    counts[mask] * sum(c for req,c in requirements.items() if not (req & ~mask))
    for mask in counts
)
print('CHECK_OK total_sets=142506 spectral_sets=7776 ordered_spectral_pairs=179676')
print('SPECTRUM_LEVELS 6:7200 96:480 486:90 7776:6')
print('FOURIER_ZERO_ANOMALY order_6_extra=360 rank_effect=0')
