"""Standalone exact verifier for four-run binary 3-deck reconstruction.

Only uses Python's standard library. All word classes are generated from positive
run compositions; deck counts are computed by subsequence dynamic programming.
Finite tests are evidence supporting, not replacing, the algebraic proof.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def words(n):
    for r in range(1, min(4, n) + 1):
        for cuts in combinations(range(1, n), r - 1):
            endpoints = (0, *cuts, n)
            for first in ('0', '1'):
                yield ''.join(str((int(first) + j) % 2) *
                              (endpoints[j + 1] - endpoints[j]) for j in range(r))


def deck(w, max_length):
    counts = {'': 1}
    for letter in w:
        for pattern, multiplicity in list(counts.items()):
            if len(pattern) < max_length:
                extended = pattern + letter
                counts[extended] = counts.get(extended, 0) + multiplicity
    return tuple(counts.get(''.join(p), 0)
                 for length in range(1, max_length + 1)
                 for p in product('01', repeat=length))


def runs(w):
    entries = []
    for ch in w:
        if entries and entries[-1][0] == ch:
            entries[-1][1] += 1
        else:
            entries.append([ch, 1])
    return entries


def fair_zero_start(w):
    r = runs(w)
    if len(r) != 4 or w[0] != '0':
        return False
    a, b, c, d = (z[1] for z in r)
    return 2 * b * c == (a + c) * (b + d)


def arithmetic_classes(n):
    total = 0
    for A in range(2, n - 1):
        B = n - A
        for b in range(1, B):
            if (A * B) % (2 * b) == 0:
                c = (A * B) // (2 * b)
                if 1 <= c < A:
                    total += 1
    return total


def test_n(n, include_four):
    fibres = defaultdict(list)
    for w in words(n):
        fibres[deck(w, 3)].append(w)
    collisions = [grp for grp in fibres.values() if len(grp) > 1]
    assert all(len(grp) == 2 for grp in collisions), ('triple fibre', n)
    for grp in collisions:
        assert grp[0] == grp[1][::-1], (n, grp)
        w = next(v for v in grp if v[0] == '0')
        assert fair_zero_start(w), (n, grp)
    t = 2 * sum(comb(n - 1, j) for j in range(min(3, n - 1) + 1))
    assert sum(map(len, fibres.values())) == t
    assert len(collisions) == arithmetic_classes(n), (n, len(collisions))
    assert len(fibres) == t - arithmetic_classes(n)
    if include_four:
        seen = set()
        for w in words(n):
            sig = deck(w, 4)
            assert sig not in seen, ('four-deck collision', n, w)
            seen.add(sig)
    return len(collisions), len(fibres)


def main():
    for n in range(1, 29):
        test_n(n, include_four=(n <= 24))
    assert test_n(7, True)[0] == 2
    assert deck('0110001', 3) == deck('1000110', 3)
    assert deck('0110001', 4) != deck('1000110', 4)
    for n in range(29, 301):
        assert 0 <= arithmetic_classes(n) < 2 * sum(
            comb(n - 1, j) for j in range(4))
    print('PASS: all words of length 1..28 having at most four runs')
    print('PASS: independent 4-decks for lengths 1..24')
    print('PASS: divisor-class checks at lengths 1..300')
    print('PASS: sharp 7-letter collision witness')


if __name__ == '__main__':
    main()
