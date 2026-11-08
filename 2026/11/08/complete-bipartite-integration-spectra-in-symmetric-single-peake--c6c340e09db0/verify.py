#!/usr/bin/env python3
"""Independent finite checks of complete-multipartite swap neutrality and biclique integration.
Run: python3 verify.py. Uses only the Python standard library.
Finite checks complement, not replace, the all-size proof in RESULT.md.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb
from collections import Counter


def adjacency(part_labels):
    n = len(part_labels)
    return tuple(tuple(j for j in range(n) if part_labels[i] != part_labels[j]) for i in range(n))


def utility(profile, adj, i):
    own = 1 + sum(profile[j] == profile[i] for j in adj[i])
    fraction = Fraction(own, 1 + len(adj[i]))
    # Strictly peaked and symmetric: peak at one half.
    return min(fraction, 1 - fraction)


def integration(profile, adj):
    return sum(any(profile[i] != profile[j] for j in adj[i]) for i in range(len(profile)))


def test_complete_multipartite():
    checks = 0
    for part_sizes in product((1, 2, 3), repeat=2):
        check_part_sizes(part_sizes)
        checks += 1
    for r in (3, 4):
        for sizes in product((1, 2, 3), repeat=r):
            if sum(sizes) > 8:
                continue
            check_part_sizes(sizes)
            checks += 1
    return checks


def check_part_sizes(sizes):
    parts = tuple(k for k, size in enumerate(sizes) for _ in range(size))
    n = len(parts)
    adj = adjacency(parts)
    for blue in range(1, n):
        for blue_positions in combinations(range(n), blue):
            profile = tuple(int(i in blue_positions) for i in range(n))
            before = tuple(utility(profile, adj, i) for i in range(n))
            for i in range(n):
                for j in range(i + 1, n):
                    if profile[i] == profile[j]:
                        continue
                    after_profile = list(profile)
                    after_profile[i], after_profile[j] = after_profile[j], after_profile[i]
                    after = (utility(after_profile, adj, i), utility(after_profile, adj, j))
                    assert not (after[1] > before[i] and after[0] > before[j]), (sizes, profile, i, j)
                    if parts[i] != parts[j]:
                        # The utility at each of the two original vertices stays fixed;
                        # hence the moving agents exchange their old utility levels.
                        assert after == (before[i], before[j]), (sizes, profile, i, j, before, after)
                    else:
                        assert after == (before[j], before[i]), (sizes, profile, i, j)


def expected_integration_max(a, b, k):
    n = a + b
    if min(a, b) == 1:
        return n - k + 1
    if k == 1:
        return 1 + max(a, b)
    return n


def test_bicliques():
    checks = 0
    for a in range(1, 8):
        for b in range(1, 8):
            n = a + b
            adj = adjacency((0,) * a + (1,) * b)
            for k in range(1, n // 2 + 1):
                vals = []
                for blue in combinations(range(n), k):
                    profile = tuple(int(i in blue) for i in range(n))
                    vals.append(integration(profile, adj))
                # Predicted full welfare enumerator via the number of blue
                # agents in the first part.
                predicted = Counter()
                for x in range(max(0, k-b), min(a, k)+1):
                    y = k-x
                    D = (x if y < b else 0) + (a-x if y > 0 else 0) \
                        + (y if x < a else 0) + (b-y if x > 0 else 0)
                    predicted[D] += comb(a, x) * comb(b, y)
                assert Counter(vals) == predicted, (a,b,k,Counter(vals),predicted)
                lo, hi = min(vals), max(vals)
                assert lo == k + min(a, b), (a, b, k, 'minimum', lo)
                assert hi == expected_integration_max(a, b, k), (a, b, k, 'maximum', hi)
                checks += 1
    return checks


if __name__ == '__main__':
    c = test_complete_multipartite()
    b = test_bicliques()
    print(f'PASS: {c} multipartite structures, all nonconstant colorings and opposite-color swaps')
    print(f'PASS: {b} biclique/minority-count configurations, exact integration extrema')
