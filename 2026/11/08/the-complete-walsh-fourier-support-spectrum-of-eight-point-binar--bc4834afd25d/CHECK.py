"""Exact, dependency-free verification of eight-point Walsh support classification.

Run with Python 3.10+: python CHECK.py
All arithmetic is integral; no randomized testing is used.
"""
from collections import Counter
from itertools import combinations
from math import comb

EXPECTED = {
    3: {1: 1},
    4: {5: 10, 9: 20, 11: 135},
    5: {13: 10, 21: 90, 23: 150, 25: 75},
    6: {29: 1, 45: 35, 49: 21},
    7: {93: 1},
}


def dot(x, y):
    return (x & y).bit_count() & 1


def support_size_direct(E, r):
    return sum(
        sum(1 if not dot(a, u) else -1 for a in E) != 0
        for u in range(1 << r)
    )


def support_size_weight_four(E, r):
    # For 0 in E, the sum equals 8 minus twice the number of
    # nonzero elements of E pairing to 1 with u.
    return (1 << r) - sum(
        sum(dot(a, u) for a in E[1:]) == 4
        for u in range(1 << r)
    )


def normalized_sets(r):
    basis = [0] + [1 << i for i in range(r)]
    rest = [v for v in range(1 << r) if v not in basis]
    for extra in combinations(rest, 7-r):
        yield tuple(basis) + extra


def period_count(E, r):
    Eset = set(E)
    return sum({x ^ v for x in E} == Eset for v in range(1 << r))


def main():
    r4_minima = 0
    tested = 0
    for r in range(3, 8):
        counts = Counter()
        for E in normalized_sets(r):
            assert len(E) == len(set(E)) == 8
            assert 0 in E
            s = support_size_direct(E, r)
            assert s == support_size_weight_four(E, r)
            counts[s] += 1
            tested += 1
            if r == 4 and s == 5:
                assert period_count(E, r) == 2
                r4_minima += 1
        assert counts == EXPECTED[r], (r, counts)
        assert sum(counts.values()) == comb((1 << r)-r-1, 7-r)
    assert tested == 1+165+325+57+1 == 549
    assert r4_minima == 10

    # The 12 local support sizes, multiplied by the kernel fiber size,
    # are pairwise distinct in ambient dimension seven.
    scaled = [(r, s * (1 << (7-r))) for r, hist in EXPECTED.items() for s in hist]
    assert len(scaled) == 12
    assert len({v for _, v in scaled}) == len(scaled)
    assert min(v for r,v in scaled if r>3) == 40

    # Independent full-cardinality check in dimension four.
    all_counts = Counter()
    for E in combinations(range(16), 8):
        all_counts[support_size_direct(E, 4)] += 1
    assert all_counts == {2:30, 5:840, 9:1920, 11:10080}
    assert sum(all_counts.values()) == comb(16,8) == 12870

    # Construct the sharp non-affine extremizer as two parallel copies
    # of a four-point affine-independent configuration.
    E = (0,1,2,3,4,5,8,9)
    assert support_size_direct(E,4) == 5
    assert period_count(E,4) == 2
    print('CHECK_OK normalized_representatives=549 support_types=12 dimension_four_subsets=12870')


if __name__ == '__main__':
    main()
