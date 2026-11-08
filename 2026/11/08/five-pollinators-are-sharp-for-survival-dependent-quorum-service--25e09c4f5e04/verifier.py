#!/usr/bin/env python3
"""Exact finite enumeration for three-threshold-two service networks.
Run: python3 verifier.py. Uses Python standard library only.
"""
from itertools import combinations, combinations_with_replacement, permutations
from math import comb

PLANTS = (0, 1, 2)
CANONICAL = (1, 1, 2, 6, 7)
EXPECTED_EXCEPTION_SCORES = {
    (0, 0, 0, 2, 3, 1),
    (0, 0, 0, 3, 3, 1),
    (0, 0, 0, 3, 5, 1),
    (0, 0, 0, 4, 5, 1),
    (0, 0, 1, 3, 3, 1),
}


def feasible(profile):
    return all(sum((mask >> v) & 1 for mask in profile) >= 2 for v in PLANTS)


def modifications(profile):
    """All distinct one-link additions, keyed by old pollinator type and plant."""
    actions = {}
    for mask in set(profile):
        for v in PLANTS:
            if not (mask & (1 << v)):
                modified = list(profile)
                modified.remove(mask)
                modified.append(mask | (1 << v))
                actions[(mask, v)] = tuple(sorted(modified))
    return actions


def subset_score(profile):
    """Method 1: enumerate live pollinators and accumulate their plant degrees."""
    m = len(profile)
    tally = [0] * (m + 1)
    for bits in range(1 << m):
        count = [0, 0, 0]
        for j, mask in enumerate(profile):
            if bits & (1 << j):
                count[0] += mask & 1 != 0
                count[1] += mask & 2 != 0
                count[2] += mask & 4 != 0
        if min(count) >= 2:
            tally[bits.bit_count()] += 1
    return tuple(tally)


def neighbor_mask_score(profile):
    """Method 2: independently intersect plant-partner masks with k-subsets."""
    m = len(profile)
    neighbor_masks = []
    for v in PLANTS:
        neighbor_masks.append(sum(1 << j for j, mask in enumerate(profile)
                                  if mask & (1 << v)))
    tally = []
    for k in range(m + 1):
        count = 0
        for chosen in combinations(range(m), k):
            bits = sum(1 << j for j in chosen)
            if all((bits & neighbors).bit_count() >= 2 for neighbors in neighbor_masks):
                count += 1
        tally.append(count)
    return tuple(tally)


def dominates(u, v):
    return all(x >= y for x, y in zip(u, v))


def plant_permute(profile, perm):
    return tuple(sorted(sum(1 << perm[v] for v in PLANTS if mask & (1 << v))
                            for mask in profile))


def main():
    exceptions = []
    eligible_counts = {}
    score_checks = 0
    for m in (2, 3, 4, 5):
        eligible = 0
        for profile in combinations_with_replacement(range(1, 8), m):
            if not feasible(profile):
                continue
            actions = modifications(profile)
            if not actions:
                continue
            eligible += 1
            scores = []
            for modified in actions.values():
                q = subset_score(modified)
                assert q == neighbor_mask_score(modified)
                score_checks += 1
                assert q[-1] == 1 and q[0] == 0 and q[1] == 0
                assert all(0 <= q[k] <= comb(m, k) for k in range(m+1))
                scores.append(q)
            universal_coefficient_winner = any(all(dominates(q, other)
                                                        for other in scores)
                                               for q in scores)
            if not universal_coefficient_winner:
                exceptions.append((m, profile, frozenset(scores)))
            if m <= 4:
                assert universal_coefficient_winner, (m, profile, scores)
        eligible_counts[m] = eligible
    orbit = {plant_permute(CANONICAL, perm) for perm in permutations(PLANTS)}
    assert eligible_counts == {2: 0, 3: 13, 4: 77, 5: 251}, eligible_counts
    assert len(orbit) == 6
    assert len(exceptions) == 6
    assert {prof for m,prof,_ in exceptions} == orbit
    assert all(m == 5 and set(score_vectors) == EXPECTED_EXCEPTION_SCORES
               for m,prof,score_vectors in exceptions)
    # Each of the remaining vectors is coefficientwise dominated by (0,4,5).
    high = (0, 0, 0, 4, 5, 1)
    low = (0, 0, 1, 3, 3, 1)
    assert all(dominates(high, q) for q in EXPECTED_EXCEPTION_SCORES if q != low)
    assert not dominates(high, low) and not dominates(low, high)
    # Exact difference of the two reliability polynomials:
    # sum_k (low[k]-high[k])*p^k*(1-p)^(5-k) = p^2(1-p)(1-3p).
    import fractions
    for numer, denom in ((1, 7), (1, 3), (2, 3), (4, 5)):
        p = fractions.Fraction(numer, denom)
        difference = sum((low[k] - high[k]) * p**k * (1-p)**(5-k)
                         for k in range(6))
        assert difference == p**2 * (1-p) * (1 - 3*p)
    print('PASS: eligible profiles by pollinator count:', eligible_counts)
    print('PASS: independent coefficient checks:', score_checks)
    print('PASS: 6 exceptions; 1 class under plant relabeling')
    print('PASS: unique switching point p=1/3, with exact gain difference')

if __name__ == '__main__':
    main()
