#!/usr/bin/env python3
"""Direct finite checks of the crown-graph limited-domination formulas.

Uses only the Python standard library. Finite tests support, but do not prove,
the all-parameter combinatorial identities established in the accompanying proof.
"""
from collections import Counter
from math import comb


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def formulas(n, k):
    assert 3 <= n and 1 <= k <= n - 2
    r = n - 1 - k
    out = Counter()
    for x in range(2, n + 1):
        for y in range(2, n + 1):
            disjoint = c(n, x) * c(n - x, y)
            all_pairs = c(n, x) * c(n, y)
            count = (disjoint if x >= r and y >= r else 0)
            count += (all_pairs - disjoint if x >= r + 1 and y >= r + 1 else 0)
            if count:
                out[(x, y)] = count
    return out


def predicted_min_and_count(n, k):
    r = n - 1 - k
    if r == 1:
        return 4, c(n, 2) ** 2
    if n >= 2 * r:
        return 2 * r, c(n, r) * c(n - r, r)
    return 2 * (r + 1), c(n, r + 1) ** 2


def all_actual_sets(n, k):
    """Exhaust all subsets with explicit adjacency, not the profile formula."""
    nbr = []
    for a in range(n):
        nbr.append(sum(1 << (n + b) for b in range(n) if a != b))
    for b in range(n):
        nbr.append(sum(1 << a for a in range(n) if a != b))
    res = Counter()
    full = (1 << (2 * n)) - 1
    for mask in range(1, full + 1):
        outside = full ^ mask
        feasible = True
        for v in range(2 * n):
            neighbours_in_d = (nbr[v] & mask).bit_count()
            if mask & (1 << v):
                if (nbr[v] & outside).bit_count() > k:
                    feasible = False
                    break
            elif neighbours_in_d == 0:
                feasible = False
                break
        if feasible:
            res[(mask & ((1 << n) - 1)).bit_count(), (mask >> n).bit_count()] += 1
    return res


def verify():
    for n in range(3, 9):
        for k in range(1, n - 1):
            observed = all_actual_sets(n, k)
            expected = formulas(n, k)
            assert observed == expected, (n, k, observed, expected)
            low = min(x + y for x, y in observed)
            num = sum(v for (x, y), v in observed.items() if x + y == low)
            assert (low, num) == predicted_min_and_count(n, k), (n, k, low, num)
        print('DIRECT_CROWN_ENUM_OK', n, 'last_k', n - 2,
              'last_total', sum(all_actual_sets(n, n - 2).values()))

    for n in range(3, 61):
        for k in range(1, n - 1):
            co = formulas(n, k)
            low = min(x + y for x, y in co)
            multiplicity = sum(v for (x, y), v in co.items() if x + y == low)
            predicted = predicted_min_and_count(n, k)
            assert (low, multiplicity) == predicted, (n, k, low, multiplicity, predicted)
            complete_bipartite_min = 2 * (n - k)
            r = n - 1 - k
            expected_gap = 2 if r >= 2 and n >= 2*r else 0
            assert complete_bipartite_min - low == expected_gap, (n, k)
    print('ALL_COEFFICIENT_MINIMA_AND_MATCHING_DELETION_GAP_OK', 'n=3..60')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
