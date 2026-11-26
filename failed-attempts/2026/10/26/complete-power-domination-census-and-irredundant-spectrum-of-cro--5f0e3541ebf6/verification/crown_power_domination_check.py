#!/usr/bin/env python3
"""Exhaustive checks for the power-domination census of labeled crown graphs.

Requires Python 3.8+ only. The tested definition is independent of the
classification and uses the original domination-then-forcing dynamics.
"""
from collections import Counter
from math import comb


def adjacencies(n):
    neighbors = [0] * (2 * n)
    for i in range(n):
        for j in range(n):
            if i != j:
                neighbors[i] |= 1 << (n + j)
                neighbors[n + j] |= 1 << i
    return neighbors


def is_power_dominating(mask, neighbors):
    all_bits = (1 << len(neighbors)) - 1
    seen = mask
    chosen = mask
    while chosen:
        bit = chosen & -chosen
        chosen -= bit
        seen |= neighbors[bit.bit_length() - 1]
    while seen != all_bits:
        unseen = all_bits & ~seen
        new = 0
        scanned = seen
        while scanned:
            bit = scanned & -scanned
            scanned -= bit
            white_neighbors = neighbors[bit.bit_length() - 1] & unseen
            if white_neighbors and not (white_neighbors & (white_neighbors - 1)):
                new |= white_neighbors
        if not new:
            break
        seen |= new
    return seen == all_bits


def verify(n):
    neighbors = adjacencies(n)
    size = 1 << (2 * n)
    half = (1 << n) - 1
    flags = [False] * size
    got_all = Counter()
    got_min = Counter()
    for mask in range(size):
        a = (mask & half).bit_count()
        b = (mask >> n).bit_count()
        direct = is_power_dominating(mask, neighbors)
        flags[mask] = direct
        predicted = (a > 0 and b > 0) or (a == 0 and b >= n - 2) or (b == 0 and a >= n - 2)
        assert direct == predicted, (n, mask, a, b, direct, predicted)
        if direct:
            got_all[(a, b)] += 1
    for mask in range(size):
        if not flags[mask]:
            continue
        chosen = mask
        minimal = True
        while chosen:
            bit = chosen & -chosen
            chosen -= bit
            if flags[mask ^ bit]:
                minimal = False
                break
        if minimal:
            a = (mask & half).bit_count()
            b = (mask >> n).bit_count()
            got_min[(a, b)] += 1
    expected_all = Counter()
    for a in range(n + 1):
        for b in range(n + 1):
            if (a > 0 and b > 0) or (a == 0 and b >= n - 2) or (b == 0 and a >= n - 2):
                expected_all[(a, b)] = comb(n, a) * comb(n, b)
    expected_min = Counter({(1, 1): n * n, (n - 2, 0): comb(n, 2), (0, n - 2): comb(n, 2)})
    assert got_all == expected_all, (n, got_all - expected_all, expected_all - got_all)
    assert got_min == expected_min, (n, got_min - expected_min, expected_min - got_min)
    assert sum(got_all.values()) == 4 ** n - 2 ** (n + 1) + n * n + n + 3
    print('PASS n={} subsets={} all={} minimal={}'.format(
        n, size, sum(got_all.values()), sum(got_min.values())))


def main():
    for n in range(4, 9):
        verify(n)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
