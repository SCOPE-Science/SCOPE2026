#!/usr/bin/env python3
"""Finite computational tests for rank and retraction spectra of semidihedral groups.

Elements are pairs (i,e), representing a**i*b**e for 0 <= i < m, e in {0,1}.
The parameter m is a power of two at least 8.
No external mathematical packages are required.
"""
from collections import Counter


def group_ops(m):
    alpha = m // 2 - 1
    identity = (0, 0)

    def mul(x, y):
        return ((x[0] + (alpha if x[1] else 1) * y[0]) % m,
                (x[1] + y[1]) % 2)

    def power(x, e):
        # Positive powers suffice for the relation and all conjugation tests.
        z = identity
        while e:
            if e & 1:
                z = mul(z, x)
            x = mul(x, x)
            e >>= 1
        return z

    def inv(x):
        if x[1] == 0:
            return ((-x[0]) % m, 0)
        return ((-alpha * x[0]) % m, 1)

    return mul, power, inv


def predictions(m):
    n = m.bit_length()  # 2*m = 2**n
    d = Counter({1: 1, 2: 3*m//2 + 3, 4: 3*m//2, 2*m: m*m//4})
    for j in range(3, n):
        d[2**j] = m*2**(j-3)
    return d


def direct_endomorphisms(m):
    alpha = m//2 - 1
    mul, power, inv = group_ops(m)
    all_elements = [(j, v) for v in (0, 1) for j in range(m)]
    count = Counter()
    retractions = []
    homs = 0
    for x in all_elements:
        if power(x, m) != (0, 0):
            continue
        for y in all_elements:
            if power(y, 2) != (0, 0):
                continue
            if mul(mul(y, x), inv(y)) != power(x, alpha):
                continue
            homs += 1
            def mapped(z):
                return mul(power(x, z[0]), power(y, z[1]))
            image = {mapped(z) for z in all_elements}
            count[len(image)] += 1
            if mapped(x) == x and mapped(y) == y:
                retractions.append((x, y))
    return homs, count, retractions


def automorphism_orbits(m, ids):
    mul, power, inv = group_ops(m)
    remaining = set(ids)
    sizes = []
    while remaining:
        x, y = next(iter(remaining))
        orb = set()
        for u in range(1, m, 2):
            iu = pow(u, -1, m)
            for v in range(m//2):
                def automorphism(z):
                    return ((u*z[0] + 2*v*z[1]) % m, z[1])
                xx = automorphism(power(x, iu))
                yy = automorphism(mul(power(x, (-2*v*iu) % m), y))
                orb.add((xx, yy))
        assert orb <= set(ids), (m, orb-set(ids))
        sizes.append(len(orb))
        remaining -= orb
    return sorted(sizes)


def run():
    for m in (8, 16, 32, 64):
        actual, rank, ids = direct_endomorphisms(m)
        expected = predictions(m)
        assert rank == expected, (m, dict(rank), dict(expected))
        assert actual == m*m//2 + 2*m + 4, (m, actual)
        assert len(ids) == m+2, (m, len(ids))
        mul, power, inv = group_ops(m)
        n = m.bit_length()
        image_ranks = Counter()
        elems = [(j,v) for v in (0,1) for j in range(m)]
        for x,y in ids:
            image_ranks[len({mul(power(x,z[0]), power(y,z[1])) for z in elems})] += 1
        assert image_ranks == Counter({1:1,2:m,2*m:1}), (m, image_ranks)
        orbit_sizes = automorphism_orbits(m, ids)
        assert orbit_sizes == [1,1,m//2,m//2], (m,orbit_sizes)
        print('m=%d group_order=%d endomorphisms=%d retractions=%d conjugacy_orbits=%s rank_counts=%s' %
              (m,2*m,actual,len(ids),orbit_sizes,sorted(rank.items())))
    print('SEMIDIHEDRAL_RANK_AND_RETRACTION_TESTS_PASSED')


if __name__ == '__main__':
    run()
