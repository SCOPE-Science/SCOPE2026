#!/usr/bin/env python3
"""Independent finite checks for length-optimal rank-loss words in edge-collapse monoids.
Public scientific verifier; Python 3 standard library only.
"""
from collections import defaultdict


def alphabet(n, family):
    assert family in ('path', 'cycle')
    assert n >= (1 if family == 'path' else 3)
    edges = [(v, v + 1) for v in range(n - 1)]
    if family == 'cycle':
        edges.append((n - 1, 0))
    return [(a, b) for a, b in edges] + [(b, a) for a, b in edges]


def closed(n, family, m):
    assert 0 <= m < n
    k = n - m
    if family == 'path':
        return (2 ** m) * (k ** m)
    if m == 0:
        return 1
    return (2 ** m) * n * (k ** (m - 1))


def direct(n, family):
    # Counts actual words by expanding functions on vertices; does not assume
    # any forest property or use a subset-only recurrence.
    acts = alphabet(n, family)
    current = {tuple(range(n)): 1}
    out = [1]
    for m in range(1, n):
        nxt = defaultdict(int)
        for f, multiplicity in current.items():
            for a, b in acts:
                g = tuple(b if x == a else x for x in f)
                if len(set(g)) == n - m:
                    nxt[g] += multiplicity
        current = nxt
        out.append(sum(current.values()))
    return out


def rank_subset_dp(n, family):
    # A different computation: retain only the image set of the evolving map.
    # At each transition, check whether it loses one image point.
    acts = alphabet(n, family)
    initial = (1 << n) - 1
    current = {initial: 1}
    out = [1]
    for m in range(1, n):
        nxt = defaultdict(int)
        for mask, multiplicity in current.items():
            for a, b in acts:
                if (mask >> a) & 1 and (mask >> b) & 1:
                    nxt[mask ^ (1 << a)] += multiplicity
        current = nxt
        out.append(sum(current.values()))
    return out


def main():
    direct_cases = 0
    subset_cases = 0
    for family in ('path', 'cycle'):
        for n in (range(1, 7) if family == 'path' else range(3, 7)):
            actual = direct(n, family)
            expected = [closed(n, family, m) for m in range(n)]
            assert actual == expected, (family, n, actual, expected)
            print(f'DIRECT {family} n={n} counts={actual}')
            direct_cases += 1
        for n in (range(1, 13) if family == 'path' else range(3, 13)):
            actual = rank_subset_dp(n, family)
            expected = [closed(n, family, m) for m in range(n)]
            assert actual == expected, (family, n, actual, expected)
            subset_cases += 1
    # Check the rank-by-rank path/cycle ratio exactly for the supported n.
    ratios = 0
    for n in range(3, 13):
        for m in range(1, n):
            k = n - m
            assert closed(n, 'cycle', m) * k == n * closed(n, 'path', m)
            ratios += 1
    print(f'VERIFY_OK direct_cases={direct_cases} subset_cases={subset_cases} ratio_checks={ratios}')


if __name__ == '__main__':
    main()
