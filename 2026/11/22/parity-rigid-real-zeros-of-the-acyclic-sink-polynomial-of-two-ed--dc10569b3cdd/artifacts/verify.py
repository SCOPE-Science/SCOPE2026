#!/usr/bin/env python3
"""Independent finite orientation enumeration for the acyclic sink polynomial of two-edge spiders."""
from collections import Counter
from math import comb
from fractions import Fraction


def poly_coeffs(m):
    return [
        (comb(m, k) * (3**k - 1) if 0 <= k <= m else 0)
        + (comb(m, k - 1) if 1 <= k <= m + 1 else 0)
        for k in range(m + 2)
    ]


def enumerate_orientations(m):
    # Hub 0, internal vertices 1..m, leaves m+1..2*m.
    edge_list = [(0, i) for i in range(1, m + 1)]
    edge_list += [(i, m + i) for i in range(1, m + 1)]
    counts = Counter()
    for mask in range(1 << (2*m)):
        outdegree = [0] * (2*m + 1)
        for bit, (a, b) in enumerate(edge_list):
            if (mask >> bit) & 1:
                outdegree[b] += 1
            else:
                outdegree[a] += 1
        counts[sum(d == 0 for d in outdegree)] += 1
    return [counts[k] for k in range(m + 2)]


def eval_poly(a, x):
    ans = Fraction(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans


def run():
    checked = 0
    for m in range(1, 8):
        expected = poly_coeffs(m)
        actual = enumerate_orientations(m)
        assert actual == expected, (m, actual, expected)
        checked += 1 << (2*m)
    print('INDEPENDENT_EDGE_ORIENTATION_ENUMERATION_PASS m=1..7 orientations=', checked)
    for m in range(1, 41):
        a = poly_coeffs(m)
        assert a[0] == 0 and a[1] == 2*m + 1 and a[-1] == 1
        assert sum(a) == 4**m
        assert all(x > 0 for x in a[1:])
        # Exact signs at the boundaries of the parity-dependent interval.
        assert eval_poly(a, Fraction(-1, 2)) < 0
        assert eval_poly(a, Fraction(-1)) == (-2)**m
    print('EXACT_COEFFICIENT_AND_RATIONAL_SIGN_CHECK_PASS m=1..40')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
