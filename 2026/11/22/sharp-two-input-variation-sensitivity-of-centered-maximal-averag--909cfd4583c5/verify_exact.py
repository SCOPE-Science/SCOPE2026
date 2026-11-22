#!/usr/bin/env python3
"""Exact arithmetic checks for the three small-cycle pairwise BV constants.

The proof uses the algebraic extremal structure of cyclic variation;
this finite checker verifies every interval-box vertex and the witnesses.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def radius_rows(n):
    assert n in (3, 4, 5)
    out = []
    for r in range(n // 2 + 1):
        rows = []
        for i in range(n):
            indices = list(range(n)) if 2 * r + 1 >= n else [((i + d) % n) for d in range(-r, r + 1)]
            rows.append(tuple(Q(int(j in indices), len(indices)) for j in range(n)))
        out.append(tuple(rows))
    return tuple(out)


def variance(v):
    return sum(abs(v[(i + 1) % len(v)] - v[i]) for i in range(len(v)))


def M(v):
    mat = radius_rows(len(v))
    return tuple(max(sum(row[j] * v[j] for j in range(len(v))) for row in (layer[i] for layer in mat)) for i in range(len(v)))


def actual_boxes(n, length):
    a = tuple(Q(int(j < length)) for j in range(n))
    arrays = radius_rows(n)
    modes = [[sum(arrays[r][i][j] * a[j] for j in range(n)) for r in range(len(arrays))] for i in range(n)]
    return [min(z) for z in modes], [max(z) for z in modes]


def test_boxes():
    expected = {
        (3, 1): (Q(2), Q(1)),
        (4, 1): (Q(5, 2), Q(5, 4)),
        (4, 2): (Q(2), Q(1)),
        (5, 1): (Q(12, 5), Q(6, 5)),
        (5, 2): (Q(14, 5), Q(7, 5)),
    }
    nverts = 0
    for (n, length), (expected_var, expected_norm) in expected.items():
        low, high = actual_boxes(n, length)
        # Convexity places a maximum of V on this box at a vertex.
        candidates = []
        for bitset in product((0, 1), repeat=n):
            values = tuple((low[i], high[i])[bitset[i]] for i in range(n))
            candidates.append(variance(values))
            nverts += 1
        assert max(candidates) == expected_var, (n, length, max(candidates), expected_var)
        assert expected_var / 2 == expected_norm
        print('BOX_VERTEX_MAX_PASS', n, length, expected_var, expected_norm)
    assert nverts == 8 + 16 + 16 + 32 + 32
    print('ALL_EXACT_BOX_VERTICES_PASS', nverts)


def test_witnesses():
    witnesses = [
        ((Q(1), Q(1), Q(0)), (Q(1), Q(0), Q(0)), Q(1)),
        ((Q(1), Q(1), Q(0), Q(1)), (Q(1), Q(0), Q(0), Q(0)), Q(5,4)),
        ((Q(1), Q(1), Q(1), Q(1), Q(0)), (Q(0), Q(1), Q(1), Q(0), Q(0)), Q(7,5)),
    ]
    eps = Q(1, 100)
    for f, h, sharp in witnesses:
        g = tuple(f[i] + eps * h[i] for i in range(len(f)))
        assert min(f) >= 0 and min(g) >= 0
        delta = tuple(M(g)[i] - M(f)[i] for i in range(len(f)))
        assert variance(delta) == eps * sharp * variance(h), (f, h, sharp, delta)
        print('STRICT_ACTIVE_PAIR_WITNESS_PASS', len(f), sharp, delta)


def test_random_pairs():
    rng = Random(271828)
    expected = {3: Q(1), 4: Q(5, 4), 5: Q(7, 5)}
    count = 0
    for n in (3, 4, 5):
        for _ in range(1000):
            f = tuple(Q(rng.randrange(0, 33), rng.randrange(1, 15)) for __ in range(n))
            g = tuple(Q(rng.randrange(0, 33), rng.randrange(1, 15)) for __ in range(n))
            input_dist = variance(tuple(f[i] - g[i] for i in range(n)))
            output_dist = variance(tuple(M(f)[i] - M(g)[i] for i in range(n)))
            assert output_dist <= expected[n] * input_dist, (n, f, g)
            count += 1
    print('RANDOM_EXACT_RATIONAL_TWO_INPUT_TESTS_PASS', count)

if __name__ == '__main__':
    test_boxes()
    test_witnesses()
    test_random_pairs()
    print('ALL_CYCLIC_CENTERED_MAXIMAL_TWO_INPUT_VARIATION_CHECKS_PASS')
