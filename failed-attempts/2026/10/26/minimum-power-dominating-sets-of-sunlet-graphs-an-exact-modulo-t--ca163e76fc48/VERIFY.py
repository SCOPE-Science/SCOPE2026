#!/usr/bin/env python3
"""Reproduce finite checks of the exact minimum-power-domination census of sunlets.

A size-minimal set is tested in the *actual* 2n-vertex graph, using an
iterated monotone observation operator. Independently, a local cyclic-gap
classifier predicts which core/leaf lifts should be feasible.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def neighbours(n):
    return [(1 << ((i - 1) % n)) | (1 << ((i + 1) % n)) |
            (1 << (n + i)) for i in range(n)] + [1 << i for i in range(n)]


def power_dominates(mask, neigh):
    total = len(neigh)
    all_bits = (1 << total) - 1
    seen = mask
    for v in range(total):
        if (mask >> v) & 1:
            seen |= neigh[v]
    while seen != all_bits:
        next_seen = seen
        for v in range(total):
            if (seen >> v) & 1:
                remaining = neigh[v] & ~seen
                if remaining and (remaining & (remaining - 1)) == 0:
                    next_seen |= remaining
        if next_seen == seen:
            return False
        seen = next_seen
    return True


def expected(n):
    if n % 3 == 0:
        return 3
    if n % 3 == 2:
        return 3 * n
    if n == 4:
        return 22
    return n * (3 * n + 1) // 2


def dominates_cycle(n, T):
    covered = set(T)
    for i in T:
        covered.add((i - 1) % n)
        covered.add((i + 1) % n)
    return len(covered) == n


def gap_predicate(n, T, leaf_positions):
    k = len(T)
    gaps = [((T[(j + 1) % k] - T[j]) % n or n) for j in range(k)]
    assert sum(gaps) == n and all(1 <= d <= 3 for d in gaps)
    deficits = [3 - d for d in gaps]
    leaf = set(leaf_positions)
    if sum(deficits) == 0:
        return not leaf
    if sum(deficits) == 1:
        j = gaps.index(2)
        return leaf.issubset({T[j], T[(j + 1) % k]}) and len(leaf) <= 1
    assert sum(deficits) == 2
    if 1 in gaps:
        j = gaps.index(1)
        return leaf.issubset({T[j], T[(j + 1) % k]})
    # Exactly two length-two gaps.
    js = [j for j, d in enumerate(gaps) if d == 2]
    assert len(js) == 2
    incident = set()
    for j in js:
        incident.update((T[j], T[(j + 1) % k]))
    if not leaf.issubset(incident):
        return False
    if k == 2:
        return len(leaf) <= 1
    if len(incident) == 3:
        return leaf != incident
    assert len(incident) == 4
    for j in js:
        if {T[j], T[(j + 1) % k]}.issubset(leaf):
            return False
    return True


def direct_count(n):
    k = (n + 2) // 3
    neigh = neighbours(n)
    counts = Counter()
    for positions in combinations(range(2 * n), k):
        mask = sum(1 << v for v in positions)
        if power_dominates(mask, neigh):
            counts[sum(v >= n for v in positions)] += 1
    return counts


def compare_classifier(n):
    k = (n + 2) // 3
    neigh = neighbours(n)
    count = 0
    for T in combinations(range(n), k):
        if not dominates_cycle(n, T):
            continue
        for leaf_flags in product((0, 1), repeat=k):
            leaf = [t for t, f in zip(T, leaf_flags) if f]
            positions = [(n + t if flag else t) for t, flag in zip(T, leaf_flags)]
            mask = sum(1 << v for v in positions)
            observed = power_dominates(mask, neigh)
            predicted = gap_predicate(n, T, leaf)
            assert observed == predicted, (n, T, leaf, observed, predicted)
            count += observed
    return count


def main():
    rows = []
    for n in range(3, 16):
        c = direct_count(n)
        assert sum(c.values()) == expected(n), (n, c, expected(n))
        rows.append((n, sum(c.values()), dict(c)))
    for n in range(3, 14):
        assert compare_classifier(n) == expected(n), n
    # In particular the two exceptional-cycle transitions are exercised.
    assert expected(4) == 22 and expected(7) == 77
    for n, total, profile in rows:
        print(f"n={n:2d}  minimum_sets={total:4d}  leaf_choice_profile={profile}")
    print("PASS: direct graph propagation for n=3..15; independent gap classifier for n=3..13")


if __name__ == '__main__':
    main()
