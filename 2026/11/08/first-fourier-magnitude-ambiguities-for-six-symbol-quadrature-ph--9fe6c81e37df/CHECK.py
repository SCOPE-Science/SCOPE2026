#!/usr/bin/env python3
"""Exact short QPSK Fourier-magnitude fiber census; Python >=3.8, stdlib only."""
from collections import defaultdict
from itertools import product

# Gaussian integers represented by integer ordered pairs.
ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def product_g(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def conjugate(x):
    return (x[0], -x[1])

def correlation(exponents):
    a = [ROOTS[e] for e in exponents]
    result = []
    for k in range(1, len(a)):
        products = [product_g(a[j+k], conjugate(a[j]))
                    for j in range(len(a)-k)]
        result.append((sum(x for x,y in products), sum(y for x,y in products)))
    return tuple(result)

def trivial_partner(exponents):
    n = len(exponents)
    return tuple((exponents[-1]-exponents[n-1-j]) % 4 for j in range(n))

def canonical(exponents):
    return min(exponents, trivial_partner(exponents))

def census(n):
    # Every global-QPSK-phase orbit has one element beginning with 1.
    spectra = defaultdict(set)
    for tail in product(range(4), repeat=n-1):
        e = (0,) + tail
        spectra[correlation(e)].add(canonical(e))
    return spectra

EXPECTED = ((1, 1, 1, 0),
            (4, 4, 4, 0),
            (16, 10, 10, 0),
            (64, 40, 40, 0),
            (256, 136, 136, 0),
            (1024, 540, 544, 4))
ALL = []
for n in range(1, 7):
    spectra = census(n)
    stats = (4 ** (n-1), len(spectra),
             sum(len(orbits) for orbits in spectra.values()),
             sum(len(orbits) > 1 for orbits in spectra.values()))
    assert stats == EXPECTED[n-1], (n, stats)
    ALL.append(stats)

ambiguous = {sig: sorted(orbits) for sig, orbits in census(6).items()
             if len(orbits) > 1}
assert all(len(v) == 2 for v in ambiguous.values())
BASE = ((-1, 0), (-2, 0), (1, 0), (0, 0), (-1, 0))
assert BASE in ambiguous
A = (0, 0, 2, 2, 0, 2)
B = (0, 1, 2, 0, 3, 2)
assert ambiguous[BASE] == [A, B]

# Every exceptional spectrum is obtained by frequency modulation by i^(tj).
def modulate(e, t):
    return tuple((e[j]+t*j) % 4 for j in range(len(e)))
for t in range(4):
    sig = correlation(modulate(A, t))
    assert sig in ambiguous
    assert {canonical(modulate(A, t)), canonical(modulate(B, t))} == set(ambiguous[sig])
assert len({correlation(modulate(A,t)) for t in range(4)}) == 4

# An independent exact Gaussian-integer polynomial-product certificate of A/B.
def polymul(a, b):
    r = [(0, 0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            z = product_g(x, y)
            r[j+k] = (r[j+k][0] + z[0], r[j+k][1] + z[1])
    return r
G = ((0, 1), (0, 1), (1, 0))           # z^2 + i*z + i
H = ((0, -1), (0, -1), (1, 0))         # z^2 - i*z - i
H_flip = ((0, -1), (1, 0), (1, 0))    # -i*z^2*conj(H(1/conj(z)))
F = ((1, 0), (-1, 0))                   # 1-z
assert tuple(polymul(polymul(F, H), G)) == tuple(ROOTS[e] for e in A)
assert tuple(polymul(polymul(F, H_flip), G)) == tuple(ROOTS[e] for e in B)
print('CHECK_OK table=', ALL, 'ambiguous_spectra=4 orbit_sizes=(2,2,2,2)')
