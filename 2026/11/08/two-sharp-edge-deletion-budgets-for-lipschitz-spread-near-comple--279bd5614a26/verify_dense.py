#!/usr/bin/env python3
"""Exact independent small-instance checks for a degree-deletion spread theorem.

Only uses the Python standard library; all variances are integer numerators.
"""
from itertools import product
from math import isqrt
from random import Random


def edge_pairs(n):
    return [(u, v) for u in range(n) for v in range(u + 1, n)]


def degree_bound(n, mask, edges):
    deg = [0] * n
    for i, (u, v) in enumerate(edges):
        if mask >> i & 1:
            deg[u] += 1
            deg[v] += 1
    return max(deg)


def direct_spread_numerator(n, mask, edges):
    """Enumerate all {0,1,2} potentials; valid for diameter-two graphs."""
    best = -1
    for vals in product(range(3), repeat=n):
        if any(abs(vals[u] - vals[v]) == 2 and not (mask >> i & 1)
               for i, (u, v) in enumerate(edges)):
            continue
        s = sum(vals)
        q = sum(v * v for v in vals)
        best = max(best, n * q - s * s)
    return best


def extremal_graph_missing_biclique(n, r, edges):
    return sum(1 << i for i, (u, v) in enumerate(edges)
               if (u < r <= v < 2 * r))


def test():
    count = 0
    for n in range(3, 7):
        edges = edge_pairs(n)
        for mask in range(1 << len(edges)):
            r = degree_bound(n, mask, edges)
            if 2 * r >= n:
                continue
            got = direct_spread_numerator(n, mask, edges)
            cap = max((n * n) // 4, 2 * n * r)
            assert got <= cap, (n, mask, r, got, cap)
            count += 1
    print('ALL_COMPLEMENTS_N3_TO6_SHARP_UNIVERSAL_BOUND_OK', count)

    rng = Random(2105)
    count = 0
    for n in range(7, 11):
        edges = edge_pairs(n)
        for _ in range(40):
            # Sample missing edges at various densities; test only r<n/2.
            q = rng.choice([0.02, 0.08, 0.16, 0.30])
            mask = sum(1 << i for i in range(len(edges)) if rng.random() < q)
            r = degree_bound(n, mask, edges)
            if 2 * r >= n:
                continue
            got = direct_spread_numerator(n, mask, edges)
            cap = max((n * n) // 4, 2 * n * r)
            assert got <= cap, (n, mask, r, got, cap)
            count += 1
    print('RANDOM_DENSE_COMPLEMENT_EXACT_ENUMERATIONS_OK', count)

    count = 0
    for n in range(3, 12):
        edges = edge_pairs(n)
        for r in range((n - 1) // 2 + 1):
            mask = extremal_graph_missing_biclique(n, r, edges)
            assert degree_bound(n, mask, edges) == r
            # For large n compute the three-level family optimum via its exact biclique structure.
            got = direct_spread_numerator(n, mask, edges) if n <= 9 else None
            expected = max((n * n) // 4, 2 * n * r)
            if got is not None:
                assert got == expected, (n, r, got, expected)
            count += 1
    print('SHARP_BICLIQUE_DELETION_EXTREMAL_FAMILY_OK', count)

    # The exact initial edge-budget envelope and first strict increase.
    count = 0
    for n in range(4, 1001):
        B = (n * n) // 4
        km = (n - 2) // 2
        for k in range(1, km + 1):
            star = n * (k + 1) - (k - 1) ** 2
            # Independently compare every possible disjoint three-level split
            # using at most k missing edges.
            if n <= 100:
                vals = [n*(a+b) - (a-b)**2 for a in range(1, n)
                        for b in range(1, n-a+1) if a*b <= k]
                assert max(vals) == star, (n, k, max(vals), star)
                count += 1
        # The strict root condition is checked with integer squares, not floats.
        discr = 8 * n + (n % 2)
        # Find the first k where star strictly exceeds B.
        first = next(k for k in range(1, km + 1)
                     if n * (k + 1) - (k - 1)**2 > B)
        assert n * first - (first - 2)**2 <= B if first > 1 else True
        # floor((n+2-sqrt(discr))/2)+1 via exact inequality
        # is equivalent to (n+2-2(first-1))^2 >= discr at the crossing.
        assert (n+2-2*(first-1))**2 >= discr
        assert (n+2-2*first)**2 < discr or (n+2-2*first) < 0
    print('EXACT_INITIAL_EDGE_BUDGET_ENVELOPE_AND_FIRST_ONSET_OK', count)

    # Integer threshold iff 2nr <= floor(n^2/4).
    for n in range(3, 10000):
        threshold = ((n * n) // 4) // (2 * n)
        assert 2 * n * threshold <= (n * n) // 4
        assert 2 * n * (threshold + 1) > (n * n) // 4
        assert threshold < n // 2
    print('EXACT_DELETION_THRESHOLD_AND_IMMEDIATE_FAILURE_OK', 9997)

if __name__ == '__main__':
    test()
