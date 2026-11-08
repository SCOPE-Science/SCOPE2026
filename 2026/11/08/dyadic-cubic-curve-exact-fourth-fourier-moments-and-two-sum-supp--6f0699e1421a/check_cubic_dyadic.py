#!/usr/bin/env python3
"""Reproduce the dyadic cubic-curve two-sum identities by direct integer counts.

Only Python's standard library is required. Run: python check_cubic_dyadic.py
"""
from collections import Counter


def v2_nonzero(z):
    assert z > 0
    return (z & -z).bit_length() - 1


def square_roots_closed(m, y):
    """The number of roots z**2=y modulo 2**m, m>=1."""
    n = 1 << m
    y %= n
    if y == 0:
        return 1 << (m // 2)
    val = v2_nonzero(y)
    if val % 2:
        return 0
    j = val // 2
    length = m - 2*j
    unit = y >> (2*j)
    if length == 1:
        return 1 << j
    if length == 2:
        return (1 << (j+1)) if unit % 4 == 1 else 0
    return (1 << (j+2)) if unit % 8 == 1 else 0


def convolution_prediction(k, s, t):
    n = 1 << k
    s %= n
    t %= n
    if s == 0:
        return n if t == 0 else 0
    if s & 1:
        return 2 if (t & 1) else 0
    v = v2_nonzero(s)
    m = k - v
    h = s // 2
    center = (2 * pow(h, 3, n)) % n
    delta = (t - center) % n
    if delta % (1 << v):
        return 0
    u = s >> v
    y = ((delta >> v) * pow(3*u, -1, 1 << m)) % (1 << m)
    return (1 << v) * square_roots_closed(m, y)


def target_sumset(k):
    n = 1 << k
    return (5*n*n+(13 if k & 1 else 14)*n-10)//18


def target_energy(k):
    n = 1 << k
    return n*n*(k*k-k+8)//4


def run():
    for m in range(1, 11):
        n = 1 << m
        roots = Counter((x*x) % n for x in range(n))
        assert all(roots.get(y, 0) == square_roots_closed(m, y) for y in range(n)), m
        assert sum(r*r for r in roots.values()) == m*n, m
        q = len(roots)
        assert q == (2**(m-1) + (5 if m&1 else 4)) // 3, m
    for k in range(1, 11):
        n = 1 << k
        cubes = [(x*x*x) % n for x in range(n)]
        # Directly enumerate all ordered pairs; this branch does not use the formula.
        counts = Counter(((x+y) % n, (cubes[x]+cubes[y]) % n)
                         for x in range(n) for y in range(n))
        assert sum(counts.values()) == n*n
        assert len(counts) == target_sumset(k), (k, len(counts), target_sumset(k))
        energy = sum(c*c for c in counts.values())
        assert energy == target_energy(k), (k, energy, target_energy(k))
        # All target points are checked, including those absent from the support.
        for s in range(n):
            for t in range(n):
                expected = convolution_prediction(k, s, t)
                assert counts.get((s,t), 0) == expected, (k,s,t,counts.get((s,t),0),expected)
        print(f'k={k:2d} N={n:4d} nonzero_targets={len(counts):7d} energy={energy:12d} verified')
    print('DYADIC_CUBIC_CURVE_CONVOLUTION_CHECK_PASS')


if __name__ == '__main__':
    run()
