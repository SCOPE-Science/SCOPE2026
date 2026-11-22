#!/usr/bin/env python3
"""Exact finite Fourier calculations for polygon quadrangulation incidence vectors.
Standalone Python 3.9+; all arithmetic integer. Public scientific calculations only.
"""
from collections import Counter
from itertools import combinations
from math import comb
from fractions import Fraction


def eligible_diagonals(N):
    assert N >= 4 and N % 2 == 0
    return [(a, b) for a in range(N) for b in range(a + 1, N)
            if (b - a) % 2 == 1 and b - a > 1 and (a, b) != (0, N - 1)]


def crosses(u, v):
    a, b = u
    c, d = v
    return (a < c < b < d) or (c < a < d < b)


def quadrangulations(N):
    """Every noncrossing (N-4)/2-subset of eligible diagonals partitions N-gon into quads."""
    D = eligible_diagonals(N)
    k = (N - 4) // 2
    family = []
    for subset in combinations(range(len(D)), k):
        if all(not crosses(D[i], D[j]) for i, j in combinations(subset, 2)):
            family.append(sum(1 << i for i in subset))
    return D, family


def fwht(vec):
    a = list(vec)
    n = len(a)
    assert n and n & (n - 1) == 0
    k = 1
    while k < n:
        for i in range(0, n, 2 * k):
            for j in range(i, i + k):
                x, y = a[j], a[j + k]
                a[j], a[j + k] = x + y, x - y
        k *= 2
    return a


def spectral_data(N):
    D, fam = quadrangulations(N)
    n = (N - 2) // 2
    assert len(fam) == comb(3 * n, n) // (2 * n + 1)
    v = [0] * (1 << len(D))
    for x in fam:
        assert v[x] == 0
        v[x] = 1
    return D, fam, fwht(v)


def check():
    d6, f6, w6 = spectral_data(6)
    assert len(d6) == 3 and len(f6) == 3
    assert all(z % 2 for z in w6)
    d8, f8, w8 = spectral_data(8)
    assert len(d8) == 8 and len(f8) == 12
    # Explicit independent presentation of the Wagner (8-vertex Mobius-ladder) graph:
    # the i-th vertex represents diagonal d8[cycle[i]].
    cycle = (0, 1, 4, 5, 7, 2, 3, 6)
    edges = {frozenset((cycle[i], cycle[(i + 1) % 8])) for i in range(8)}
    edges |= {frozenset((cycle[i], cycle[i + 4])) for i in range(4)}
    pair_edges = {frozenset((j for j in range(8) if x & (1 << j))) for x in f8}
    assert pair_edges == edges and len(edges) == 12
    degrees = [sum(i in edge for edge in edges) for i in range(8)]
    assert degrees == [3] * 8
    # Independent cut-size reconstruction of all Walsh multipliers.
    cut_sizes = []
    for s in range(256):
        boundary = sum(bool(s & (1 << min(e))) != bool(s & (1 << max(e)))
                       for e in (tuple(sorted(edge)) for edge in edges))
        cut_sizes.append(boundary)
        assert w8[s] == 12 - 2 * boundary
        assert w8[s] == sum(1 if (s & x).bit_count() % 2 == 0 else -1 for x in f8)
    assert Counter(cut_sizes) == {0: 2, 3: 16, 4: 28, 5: 48, 6: 72,
                                  7: 48, 8: 18, 9: 16, 10: 8}
    assert Counter(w8) == {-8: 8, -6: 16, -4: 18, -2: 48, 0: 72,
                            2: 48, 4: 28, 6: 16, 12: 2}
    assert sum(z != 0 for z in w8) == 184
    assert min(abs(z) for z in w8 if z) == 2
    zero_by_weight = Counter(s.bit_count() for s in range(256) if w8[s] == 0)
    assert zero_by_weight == {2: 16, 4: 40, 6: 16}
    assert all(w8[1 << i] == 6 for i in range(8))
    for i, j in combinations(range(8), 2):
        s = (1 << i) | (1 << j)
        assert w8[s] == (4 if frozenset((i, j)) in edges else 0)
    # Inverse Walsh transform of the exact nonzero-frequency projection mask.
    h = fwht([int(z != 0) for z in w8])
    assert Counter(h) == {-72: 1, -16: 8, -8: 2, -4: 32, 0: 160,
                           4: 32, 8: 8, 16: 8, 24: 4, 184: 1}
    assert h[0] == 184
    assert sum(abs(x) for x in h) == 944
    assert Fraction(sum(abs(x) for x in h), 256) == Fraction(59, 16)
    d10, f10, w10 = spectral_data(10)
    assert len(d10) == 15 and len(f10) == 55
    assert all(z & 1 for z in w10)
    assert min(abs(z) for z in w10) == 1
    idx = [d10.index(z) for z in [(0, 3), (0, 5), (1, 8)]]
    witness = sum(1 << i for i in idx)
    assert w10[witness] == 1
    assert max(abs(z) for z in w10) == 55
    print('PASS: 6-, 8-, 10-gon counts 3, 12, 55; M8 compatibility; all exact Walsh and cut values;')
    print('PASS: octagon rank 184, nullity 72, least nonzero 2, zero weights {2:16,4:40,6:16};')
    print('PASS: sharp unrestricted endpoint projection norm 59/16; decagon zero-free with gap 1.')


if __name__ == '__main__':
    check()
