#!/usr/bin/env python3
"""Exact finite witness and assay-ratio checks for paired detection alias."""
from collections import Counter
from fractions import Fraction
from itertools import permutations


def rate_law(pairs, ratio=Fraction(1)):
    return (Counter(a for a, b in pairs), Counter(b for a, b in pairs),
            Counter(Fraction(a) + ratio * b for a, b in pairs))


def classify(a, b, ratio=Fraction(1)):
    candidates = {}
    for order in permutations(b):
        pairs = tuple(zip(a, order))
        fingerprint = tuple(sorted(rate_law(pairs, ratio)[2].items()))
        candidates.setdefault(fingerprint, []).append(pairs)
    return candidates


def test():
    checks = 0
    a = (6, 2, 4)
    b = (1, 3, 5)
    first = tuple(zip(a, b))
    second = tuple(zip(a, (3, 5, 1)))
    assert first != second
    checks += 1
    assert rate_law(first) == rate_law(second)
    checks += 1
    assert rate_law(first)[2] == Counter({Fraction(5): 1, Fraction(7): 1, Fraction(9): 1})
    checks += 1
    assert sum(a < z for a, z in first) == 2
    assert sum(a < z for a, z in second) == 1
    checks += 2
    ratio = Fraction(3, 2)
    assert rate_law(first, ratio) != rate_law(second, ratio)
    checks += 1
    every_pair_sum = [Fraction(x) + ratio * y for x in a for y in b]
    assert len(set(every_pair_sum)) == 9
    checks += 1
    groups = classify(a, b)
    assert any(first in options and second in options for options in groups.values())
    checks += 1
    assert all(len(options) == 1 for options in classify(a, b, ratio).values())
    checks += 1
    # Exact finite checks supplement (not replace) the symbolic two-class proof.
    for a0 in range(1, 11):
        for a1 in range(a0 + 1, 12):
            for b0 in range(1, 11):
                for b1 in range(b0 + 1, 12):
                    groupings = classify((a0, a1), (b0, b1))
                    assert len(groupings) == 2
                    assert all(len(g) == 1 for g in groupings.values())
                    checks += 2
    # Derive the forbidden finite ratio set by exact divisions.
    forbidden = {Fraction(abs(x - y), abs(u - v))
                 for x in a for y in a if x != y
                 for u in b for v in b if u != v}
    assert forbidden == {Fraction(1, 2), Fraction(1), Fraction(2)}
    assert ratio not in forbidden
    checks += 2
    print(f"PASS: {checks} exact assertions; witness equal on diagonal; 3/2 ratio separates all candidate pairs")


if __name__ == '__main__':
    test()
