#!/usr/bin/env python3
"""Exact checks for sparse Walsh cancellation of derangement matchings.

No external dependencies. Run: python3 check_derangement_first_zero.py
"""
from itertools import combinations, permutations
from math import comb


def derangements(n):
    return [p for p in permutations(range(n)) if all(p[i] != i for i in range(n))]


def signed_permanent(n, flipped_edges):
    """Independent subset DP, signs -1 on flipped allowed positions."""
    flipped = set(flipped_edges)
    dp = {0: 1}
    for row in range(n):
        ndp = {}
        for mask, value in dp.items():
            for col in range(n):
                if col == row or mask & (1 << col):
                    continue
                new_mask = mask | (1 << col)
                factor = -1 if (row, col) in flipped else 1
                ndp[new_mask] = ndp.get(new_mask, 0) + factor * value
        dp = ndp
    return dp.get((1 << n) - 1, 0)


def layer_check(n, max_k):
    """Independent permutation enumeration for all sparse sign sets."""
    ps = derangements(n)
    E = [(i, j) for i in range(n) for j in range(n) if i != j]
    emap = {edge: index for index, edge in enumerate(E)}
    match_masks = [sum(1 << emap[(i, p[i])] for i in range(n)) for p in ps]
    D = len(ps)
    expected_D = signed_permanent(n, ())
    assert D == expected_D
    checks = 0
    for k in range(max_k + 1):
        zeros = 0
        minimizers = 0
        for indices in combinations(range(len(E)), k):
            mask = sum(1 << c for c in indices)
            signed_sum = sum(1 - 2 * ((mask & p).bit_count() % 2) for p in match_masks)
            assert signed_sum * (n - 1) >= D * (n - 1 - 2 * k)
            is_star = (k <= 1 or
                       len({E[i][0] for i in indices}) == 1 or
                       len({E[i][1] for i in indices}) == 1)
            is_min = signed_sum * (n - 1) == D * (n - 1 - 2 * k)
            if n >= 4:
                assert is_min == is_star, (n, k, indices, signed_sum)
            elif k <= 1:
                assert is_min
            minimizers += is_min
            zeros += signed_sum == 0
            checks += 1
        if n >= 4 and 2 <= k <= n - 1:
            assert minimizers == 2 * n * comb(n - 1, k)
        if n >= 3 and n % 2 and k < (n - 1) // 2:
            assert zeros == 0
        if n >= 3 and n % 2 and k == (n - 1) // 2:
            goal = n * (n - 1) if n == 3 else 2 * n * comb(n - 1, k)
            assert zeros == goal, (n, k, zeros, goal)
        if n % 2 == 0:
            assert zeros == 0
    return checks, D


def main():
    checks = 0
    for n in range(2, 17):
        D = signed_permanent(n, ())
        assert D > 0
        assert (D % 2 == 1) == (n % 2 == 0)
        for k in range(n):
            if n % 2 or k in (0, 1, n - 1):
                edge_set = {(0, j) for j in range(1, k + 1)}
                value = signed_permanent(n, edge_set)
                assert (n - 1) * value == D * (n - 1 - 2 * k)
                checks += 1
        if n % 2:
            k = (n - 1) // 2
            assert signed_permanent(n, {(0, j) for j in range(1, k + 1)}) == 0
    for n, bound in [(3, 1), (4, 3), (5, 4), (6, 3), (7, 3)]:
        c, D = layer_check(n, bound)
        checks += c
        print('exhaustive n=%d, D=%d, k=0..%d, sets=%d' % (n, D, bound, c))
    for n in (3, 4, 5, 6, 7):
        E = [(i, j) for i in range(n) for j in range(n) if i != j]
        test_sets = [[], E[:1], E[:2], E[-min(3, len(E)):]]
        for s in test_sets:
            direct = sum((-1)**sum((i, p[i]) in s for i in range(n))
                         for p in derangements(n))
            assert direct == signed_permanent(n, s)
            checks += 1
    print('DERANGEMENT_SPARSE_WALSH_PASS; exact assertions/groups:', checks)


if __name__ == '__main__':
    main()
