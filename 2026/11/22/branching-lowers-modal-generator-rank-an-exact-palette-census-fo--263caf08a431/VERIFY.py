#!/usr/bin/env python3
"""Finite checks for generating predicates on reflexive modal bouquets."""
from collections import Counter
from itertools import product
from math import comb, factorial


def falling(x, n):
    if n < 0 or x < n or x < 0:
        return 0
    p = 1
    for j in range(n):
        p *= x - j
    return p


def predicted_count(r, sizes, q):
    if len(sizes) == 1:
        s = sizes[0]
        return falling(q, s) * (falling(q, r) - falling(s, r))
    counts = Counter(sizes)
    result = falling(q, r)
    for s, m in counts.items():
        result *= falling(comb(q, s) if s <= q else 0, m) * factorial(s)**m
    return result


def predicted_generating(r, sizes, colors):
    root = set(colors[:r])
    if len(root) != r:
        return False
    palettes = []
    offset = r
    for s in sizes:
        palette = set(colors[offset:offset+s])
        if len(palette) != s:
            return False
        palettes.append(palette)
        offset += s
    if len(sizes) == 1:
        return not root.issubset(palettes[0])
    return len({frozenset(t) for t in palettes}) == len(palettes)


def frame(r, sizes):
    n = r + sum(sizes)
    successors = []
    for v in range(r):
        successors.append(tuple(range(n)))
    offset = r
    for s in sizes:
        for v in range(s):
            successors.append(tuple(range(offset, offset+s)))
        offset += s
    return successors


def bisimulation_discrete(successors, colors):
    n = len(colors)
    current = tuple(colors)
    while True:
        signatures = tuple((current[v], frozenset(current[w] for w in successors[v])) for v in range(n))
        keys = sorted(set(signatures), key=repr)
        nxt = tuple(keys.index(sig) for sig in signatures)
        if len(set(nxt)) == len(set(current)):
            return len(set(nxt)) == n
        current = nxt


def direct_algebra_discrete(successors, colors, k):
    n = len(colors)
    universe = (1 << n) - 1
    known = {0, universe}
    for bit in range(k):
        known.add(sum((1 << v) for v in range(n) if (colors[v] >> bit) & 1))
    while True:
        old = len(known)
        values = list(known)
        for x in values:
            known.add(universe ^ x)
            d = 0
            for v in range(n):
                if any(x & (1 << w) for w in successors[v]):
                    d |= 1 << v
            known.add(d)
        values = list(known)
        for x in values:
            for y in values:
                known.add(x & y)
        if len(known) == old:
            return len(known) == 1 << n


def run():
    cases = valuations = compared = direct = 0
    for r in (1, 2, 3):
        for sizes in ((1,), (2,), (3,), (1,1), (1,2), (2,1), (2,2),
                      (1,1,1), (2,1,1), (1,2,1), (1,1,2), (2,2,1), (2,2,2)):
            n = r + sum(sizes)
            for k in (0, 1, 2):
                q = 1 << k
                if q**n > 100000:
                    continue
                successors = frame(r, sizes)
                total = 0
                for colors in product(range(q), repeat=n):
                    predicted = predicted_generating(r, sizes, colors)
                    by_bisim = bisimulation_discrete(successors, colors)
                    assert predicted == by_bisim, (r, sizes, k, colors)
                    total += int(by_bisim)
                    valuations += 1
                    if n <= 5 and (valuations % 37 == 0 or predicted):
                        by_algebra = direct_algebra_discrete(successors, colors, k)
                        assert predicted == by_algebra, (r, sizes, k, colors, 'algebra')
                        direct += 1
                expected = predicted_count(r, sizes, q)
                assert total == expected, (r, sizes, q, total, expected)
                cases += 1
                compared += total
    # Strict generator-rank drop after adding a second terminal cluster.
    assert predicted_count(1, [2], 2) == 0
    assert predicted_count(1, [2], 4) > 0
    assert predicted_count(1, [2,1], 2) > 0
    print('VERIFY_OK cases=%d exhaustive_labelings=%d generating_labelings=%d direct_algebra_checks=%d' %
          (cases, valuations, compared, direct))

if __name__ == '__main__':
    run()
