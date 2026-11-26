#!/usr/bin/env python3
"""Finite combinatorial checks for the binary finite-group generator theorem.
The universal relative-rank conclusion is established by the accompanying proof,
not by these finite checks.
"""
from itertools import combinations

def bitparity(n):
    return n.bit_count() & 1

def index_four_kernels(r):
    q = 1 << r
    kernels = set()
    for u, v in combinations(range(1, q), 2):
        k = frozenset(x for x in range(q)
                      if bitparity(x & u) == 0 and bitparity(x & v) == 0)
        assert len(k) == q // 4
        kernels.add(k)
    return kernels

def translate_mask(mask, g, q):
    result = 0
    for x in range(q):
        if (mask >> x) & 1:
            result |= 1 << (x ^ g)
    return result

def check_orbits(r):
    q = 1 << r
    kernels = index_four_kernels(r)
    for h in kernels:
        same_stabilizer = []
        for mask in range(1 << q):
            stabilizer = frozenset(g for g in range(q)
                                   if translate_mask(mask, g, q) == mask)
            if stabilizer == h:
                same_stabilizer.append(mask)
        assert len(same_stabilizer) == 8
        remaining = set(same_stabilizer)
        orbits = []
        while remaining:
            mask = min(remaining)
            orbit = {translate_mask(mask, g, q) for g in range(q)}
            assert len(orbit) == 4 and orbit <= remaining
            orbits.append(orbit)
            remaining.difference_update(orbit)
        assert len(orbits) == 2
        for orbit in orbits:
            weights = {w.bit_count() // len(h) for w in orbit}
            assert weights in ({1}, {3})
    return len(kernels)

def main():
    counts = []
    for r in range(2, 6):
        expected = ((1 << r) - 1) * ((1 << r) - 2) // 6
        kernels = index_four_kernels(r)
        assert len(kernels) == expected
        counts.append((r, len(kernels)))
    assert counts == [(2, 1), (3, 7), (4, 35), (5, 155)]
    assert check_orbits(2) == 1
    assert check_orbits(3) == 7
    print('VERIFY_OK: kernels', counts, 'and two exact-stabilizer orbits for r=2,3')

if __name__ == '__main__':
    main()
