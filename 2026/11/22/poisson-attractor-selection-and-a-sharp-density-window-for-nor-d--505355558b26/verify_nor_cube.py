#!/usr/bin/env python3
"""Finite checks of synchronous open-neighborhood NOR dynamics on cubes.

No external packages or files are required. This verifies finite instances;
it does not serve as a proof of asymptotic claims.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def build_neighborhoods(d):
    n = 1 << d
    return [sum(1 << (v ^ (1 << j)) for j in range(d)) for v in range(n)]


def nor(mask, nbr):
    result = 0
    for v, nm in enumerate(nbr):
        if not mask & nm:
            result |= 1 << v
    return result


def run():
    for d in range(1, 5):
        nbr = build_neighborhoods(d)
        n = 1 << d
        counts = Counter()
        pairmom = 0
        cycles = set()
        singleton_ucs = set()
        universal_count = 0
        isolated = 0
        for x in range(1 << n):
            y = nor(x, nbr)
            z = nor(y, nbr)
            w = nor(z, nbr)
            assert w == y, (d, x)
            k = y.bit_count()
            counts[k] += 1
            pairmom += k * (k - 1)
            if set((y, z)) == {0, (1 << n) - 1}:
                universal_count += 1
            if k == 1:
                singleton_ucs.add(y)
                assert nor(z, nbr) == y
                if d >= 3:
                    assert y != z
            if d >= 3:
                pos = [i for i in range(n) if (y >> i) & 1]
                if all((a ^ b).bit_count() >= 5 for i, a in enumerate(pos) for b in pos[i + 1:]):
                    isolated += 1
                    assert z.bit_count() == n - d * k
            cycles.add(tuple(sorted((y, z))))
        # Independent exact moment polynomial via neighborhood-union inclusion/exclusion.
        # For every subset S of output vertices, the number of inputs for which
        # all sites in S are NOR-active is 2^(N-|N(S)|).
        union_neighborhood = [0] * (1 << n)
        factorial_sums = [0] * (n + 1)
        for subset in range(1 << n):
            if subset:
                low = subset & -subset
                v = low.bit_length() - 1
                union_neighborhood[subset] = union_neighborhood[subset ^ low] | nbr[v]
            factorial_sums[subset.bit_count()] += 1 << (n - union_neighborhood[subset].bit_count())
        via_images = {}
        for k in range(n + 1):
            value = sum((-1) ** (j-k) * comb(j, k) * factorial_sums[j]
                        for j in range(k, n + 1))
            if value:
                via_images[k] = value
        assert dict(counts) == via_images, (d, counts, via_images)
        assert universal_count == counts.get(0, 0) + 1
        total = 1 << n
        mean = Fraction(sum(k * v for k, v in counts.items()), total)
        second = Fraction(pairmom, total)
        lam = Fraction(n, 1 << d)
        var = second + mean - mean * mean
        expected = lam * (1 - Fraction(1, 1 << d)) + n * comb(d, 2) * (Fraction(1, 2 ** (2 * d - 2)) - Fraction(1, 2 ** (2 * d)))
        assert mean == lam and var == expected, (mean, var, expected)
        if d >= 3:
            assert len(singleton_ucs) == n
        print(f'd={d}: states={total}, EW={mean}, VarW={var}, distinct image-cycles={len(cycles)}, singleton images={len(singleton_ucs)}, well-separated images={isolated}')
    print('PASS: exhaustive dynamics, independent polynomial, exact moments, and one-step recurrence')


if __name__ == '__main__':
    run()
