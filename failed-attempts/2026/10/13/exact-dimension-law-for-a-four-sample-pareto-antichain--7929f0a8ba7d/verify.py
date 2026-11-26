"""Exact, finite verification of the four-point Pareto-antichain dimension law.

Python 3 standard library only.  Does not rely on random sampling.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

N = 4
PAIRS = list(combinations(range(N), 2))
ORDERS = list(permutations(range(N)))
POSITIONS = [tuple(perm.index(i) for i in range(N)) for perm in ORDERS]
FULL = (1 << len(PAIRS)) - 1


def linear_extensions(edges):
    return sum(all(pos[i] < pos[j] for (i, j) in edges) for pos in POSITIONS)


def coefficient_table():
    coefficient = Counter()
    counts = Counter()
    for s in range(1 << len(PAIRS)):
        edges = [pair for bit, pair in enumerate(PAIRS) if (s >> bit) & 1]
        e = linear_extensions(edges)
        coefficient[e] += -1 if len(edges) % 2 else 1
        counts[e] += 1
    return coefficient, counts


def exact_formula(d, c):
    assert d >= 1
    return sum(Fraction(a * e ** (d - 1), 24 ** (d - 1)) for e, a in c.items())


def inversion_mask(pos):
    return sum(1 << bit for bit, (i, j) in enumerate(PAIRS) if pos[i] > pos[j])


def independent_dp_counts(max_dim):
    # Fix the first coordinate's increasing order. Each further coordinate
    # contributes an independent random inversion mask. Count all 24^(d-1)
    # equally likely rank-tuples using a 64-state exact transfer recurrence.
    masks = [inversion_mask(pos) for pos in POSITIONS]
    dp = Counter({0: 1})
    out = {1: 0}
    for d in range(2, max_dim + 1):
        nxt = Counter()
        for old_mask, multiplicity in dp.items():
            for new_mask in masks:
                nxt[old_mask | new_mask] += multiplicity
        dp = nxt
        out[d] = dp[FULL]
        assert sum(dp.values()) == 24 ** (d - 1)
    return out


def direct_small_counts(d):
    # A second representation: explicitly enumerate all rank permutations
    # after fixing the first coordinate. No coefficient or DP recurrence used.
    masks = [inversion_mask(pos) for pos in POSITIONS]
    return sum((__import__('functools').reduce(int.__or__, order_masks, 0) == FULL)
               for order_masks in product(masks, repeat=d - 1))


def main():
    c, counts = coefficient_table()
    expected = {1: 0, 2: 0, 3: 0, 4: 1, 5: -5,
                6: 1, 8: 8, 12: -6, 24: 1}
    expected_counts = {1: 8, 2: 10, 3: 12, 4: 9,
                       5: 5, 6: 5, 8: 8, 12: 6, 24: 1}
    assert dict(c) == expected, (dict(c), expected)
    assert dict(counts) == expected_counts
    assert sum(counts.values()) == 2 ** 6 == 64
    assert sum(c.values()) == 0
    dp = independent_dp_counts(12)
    for d, ways in dp.items():
        got = exact_formula(d, c)
        assert got == Fraction(ways, 24 ** (d - 1)), (d, got, ways)
    for d in range(2, 6):
        assert direct_small_counts(d) == dp[d]
    known = {1: Fraction(0), 2: Fraction(1, 24),
             3: Fraction(151, 576),
             4: Fraction(7207, 13824),
             5: Fraction(238555, 331776)}
    for d, p in known.items():
        assert exact_formula(d, c) == p
    assert all(exact_formula(d + 1, c) > exact_formula(d, c)
               for d in range(1, 12))
    print('VERIFY_OK subsets=64 orders=24 dimensions=12 explicit_tuples_to_d=5')
    print('COEFFICIENTS', sorted(c.items()))
    print('COUNTS', sorted(counts.items()))
    print('DIMENSIONS', [(d, str(exact_formula(d, c))) for d in range(1, 6)])


if __name__ == '__main__':
    main()
