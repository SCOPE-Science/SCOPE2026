#!/usr/bin/env python3
"""Exact graph-level and recurrence verification for minimal forts of wheels.

Requires only Python 3 standard library. Does not substitute for the proof.
"""
from collections import Counter
from fractions import Fraction
from math import ceil


def add(a, b, sign=1):
    out = a.copy()
    for degree, count in b.items():
        out[degree] = out.get(degree, 0) + sign * count
    return {k: v for k, v in out.items() if v}


def shift(a, shift_by):
    return {k + shift_by: v for k, v in a.items()}


def block_polynomials(limit):
    """Compute coefficients of -x A_x/A and -x B_x/B by exact recurrence."""
    p = [dict() for _ in range(limit + 1)]
    q = [dict() for _ in range(limit + 1)]
    for n in range(1, limit + 1):
        if n >= 2:
            p[n] = add(p[n], shift(p[n - 2], 1))
            q[n] = add(q[n], shift(q[n - 2], 1))
        if n >= 3:
            p[n] = add(p[n], shift(p[n - 3], 2))
            q[n] = add(q[n], shift(q[n - 3], 1))
        if n >= 4:
            q[n] = add(q[n], shift(q[n - 4], 2))
        if n >= 6:
            q[n] = add(q[n], shift(q[n - 6], 3), -1)
        for nn, degree, multiplicity in ((2, 1, 2), (3, 2, 3)):
            if n == nn:
                p[n] = add(p[n], {degree: multiplicity})
        for nn, degree, multiplicity in ((2, 1, 2), (3, 1, 3),
                                         (4, 2, 4), (6, 3, -6)):
            if n == nn:
                q[n] = add(q[n], {degree: multiplicity})
    return p, q


def expected_poly(n, p, q):
    result = add(p[n], shift(q[n], 1))
    if n % 2 == 0:
        result = add(result, {n // 2 + 1: 2}, -1)
    return result


def brute_wheel(n):
    hub = n
    adjacency = [(1 << hub) | (1 << ((i + 1) % n)) |
                 (1 << ((i - 1) % n)) for i in range(n)]
    adjacency.append((1 << n) - 1)

    def is_fort(mask):
        if mask == 0:
            return False
        for v in range(n + 1):
            if not (mask >> v) & 1 and (adjacency[v] & mask).bit_count() == 1:
                return False
        return True

    forts = [s for s in range(1, 1 << (n + 1)) if is_fort(s)]
    minimal = []
    for s in forts:
        t = (s - 1) & s
        while t:
            if is_fort(t):
                break
            t = (t - 1) & s
        else:
            minimal.append(s)
    return (Counter(s.bit_count() for s in minimal),
            Counter(s.bit_count() for s in minimal if s & (1 << hub)),
            minimal, len(forts))


def main():
    p, q = block_polynomials(160)
    known_hub = [3, 4, 5, 3, 14, 12, 21, 25, 44, 55, 78, 112, 158]
    for n, val in enumerate(known_hub, start=3):
        assert sum(q[n].values()) - (2 if n % 2 == 0 else 0) == val
    candidate_count, minimal_count, fort_count = 0, 0, 0
    for n in range(3, 13):
        got, got_hub, minimal, nf = brute_wheel(n)
        expected = expected_poly(n, p, q)
        assert dict(got) == expected, (n, got, expected)
        expected_hub = shift(q[n], 1)
        if n % 2 == 0:
            expected_hub = add(expected_hub, {n // 2 + 1: 2}, -1)
        assert dict(got_hub) == expected_hub, (n, got_hub, expected_hub)
        a, b = ceil(n / 2), ceil(n / 3)
        weights = [Fraction(1, a)] * n + [Fraction(a - b, a)]
        assert all(sum(weights[v] for v in range(n + 1) if s & (1 << v)) >= 1
                   for s in minimal)
        assert sum(weights) == Fraction(1, 1) + Fraction(n - b, a)
        assert any((s & t) == 0 for i, s in enumerate(minimal)
                   for t in minimal[i + 1:])
        candidate_count += (1 << (n + 1)) - 1
        minimal_count += len(minimal)
        fort_count += nf
    for n in range(3, 161):
        poly = expected_poly(n, p, q)
        assert poly and all(c > 0 for c in poly.values()), (n, poly)
        # Sum of coefficients is the scalar specialization.
        assert sum(poly.values()) == sum(p[n].values()) + sum(q[n].values()) - (2 if n % 2 == 0 else 0)
    print('VERIFY_OK rim_orders=3..12 candidate_nonempty_subsets=%d forts=%d minimal_forts=%d' %
          (candidate_count, fort_count, minimal_count))
    print('VERIFY_OK hub_sequence_13_terms=PASS polynomial_orders=3..160=PASS exact_fractional_cover=PASS disjoint_forts=PASS')


if __name__ == '__main__':
    main()
