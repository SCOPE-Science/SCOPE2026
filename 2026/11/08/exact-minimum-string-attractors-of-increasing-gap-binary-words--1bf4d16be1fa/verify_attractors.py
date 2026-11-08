#!/usr/bin/env python3
"""Reproduce finite checks for the increasing-gap string-attractor theorem.

No third-party dependencies. The infinite theorem is established by the
mathematical proof; these are exhaustive small-instance cross-checks.
"""
from itertools import combinations


def make_word(gaps):
    return '1' + ''.join('0' * g + '1' for g in gaps)


def claimed_positions(gaps):
    k = len(gaps)
    markers = [0]
    for g in gaps:
        markers.append(markers[-1] + g + 1)
    chosen = {markers[j] for j in range(1, k + 1, 2)}
    # For odd k use first zero in last gap; for even k use last zero.
    chosen.add(markers[-2] + 1 if k % 2 else markers[-1] - 1)
    return chosen


def distinct_factor_coverage(word, indices):
    """Independently scan all intervals and compare covered/factor sets."""
    seen = set()
    covered = set()
    n = len(word)
    for a in range(n):
        for b in range(a + 1, n + 1):
            factor = word[a:b]
            seen.add(factor)
            if any(a <= p < b for p in indices):
                covered.add(factor)
    return len(seen), seen == covered, seen - covered


def min_attractor_exact(word):
    """Exact small hitting-set search on distinct-factor coverage masks."""
    n = len(word)
    factor_masks = {}
    for a in range(n):
        for b in range(a + 1, n + 1):
            factor_masks[word[a:b]] = factor_masks.get(word[a:b], 0) | (((1 << (b - a)) - 1) << a)
    # A factor is hit if chosen positions intersect its union-of-occurrence mask.
    masks = tuple(set(factor_masks.values()))
    # Small-instance exhaustive search, no LP solver or heuristic inference.
    for r in range(1, n + 1):
        for candidate in combinations(range(n), r):
            selected = sum(1 << p for p in candidate)
            if all(selected & mask for mask in masks):
                return r
    raise AssertionError('a full set must attract')


def main():
    count_vectors = 0
    factor_cells = 0
    for k in range(1, 7):
        for gaps in combinations(range(1, 10), k):
            w = make_word(gaps)
            positions = claimed_positions(gaps)
            target = (k + 1) // 2 + 1
            assert len(positions) == target, (gaps, positions, target)
            cells, ok, missing = distinct_factor_coverage(w, positions)
            assert ok, (gaps, positions, list(missing)[:5])
            count_vectors += 1
            factor_cells += cells
    print('Exhaustive gap-vector upper checks:', count_vectors,
          'distinct-factor cells:', factor_cells)

    exact_checks = 0
    for gaps in [(1,), (2,), (1, 2), (1, 3), (2, 3), (2, 4),
                 (1, 2, 3), (1, 2, 4), (1, 3, 5), (1, 2, 3, 4),
                 (1, 2, 3, 4, 5)]:
        actual = min_attractor_exact(make_word(gaps))
        expected = (len(gaps) + 1) // 2 + 1
        assert actual == expected, (gaps, actual, expected)
        exact_checks += 1
    print('Exact minimum hitting-set checks:', exact_checks)

    for k in range(1, 20):
        gaps = [j * 3 + j // 3 for j in range(1, k + 1)]
        if len(set(gaps)) != k:
            raise AssertionError('gaps not increasing')
        w = make_word(gaps)
        _, ok, missing = distinct_factor_coverage(w, claimed_positions(gaps))
        assert ok, (k, list(missing)[:3])
    print('Large-parameter explicit-cover checks:', 19)
    print('PASS')


if __name__ == '__main__':
    main()
