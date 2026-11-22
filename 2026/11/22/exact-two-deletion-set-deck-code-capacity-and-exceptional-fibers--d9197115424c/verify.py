"""Exhaustive certificate: distinct four-pattern decks of six-permutations.

Run: python3 verify.py. Only the Python standard library is required.
Each of the 720 permutations and each of the 15 four-position choices is
examined. Two independent constructions of the 24-bit observation agree.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import prod

N = 6
SIX = list(permutations(range(1, N + 1)))
FOUR = list(permutations(range(1, 5)))
QUADS = list(combinations(range(6), 4))
FOUR_INDEX = {p: i for i, p in enumerate(FOUR)}
EXPECTED = [
    ((1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (2, 1, 3, 5, 4, 6)),
    ((2, 4, 1, 6, 3, 5), (3, 1, 5, 2, 6, 4)),
    ((4, 6, 2, 5, 1, 3), (5, 3, 6, 1, 4, 2)),
    ((5, 6, 4, 2, 3, 1), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2)),
]


def deck_a(word):
    # Enumerate the 15 rank-standardized subsequences directly.
    out = set()
    for indices in QUADS:
        seq = [word[i] for i in indices]
        rank = {a: i + 1 for i, a in enumerate(sorted(seq))}
        out.add(tuple(rank[a] for a in seq))
    return frozenset(out)


def deck_b(word):
    # Independent pattern-containment test: no ranks/sorting of subsequences.
    bits = 0
    for j, pattern in enumerate(FOUR):
        for indices in QUADS:
            if all((word[indices[a]] < word[indices[b]]) ==
                   (pattern[a] < pattern[b])
                   for a in range(4) for b in range(a + 1, 4)):
                bits |= 1 << j
                break
    return bits


def flip_positions(p):
    return p[::-1]


def flip_values(p):
    return tuple(7 - a for a in p)


def inverse(p):
    return tuple(p.index(k) + 1 for k in range(1, 7))


def main():
    assert len(SIX) == 720 and len(FOUR) == 24 and len(QUADS) == 15
    buckets = defaultdict(list)
    for p in SIX:
        a = deck_a(p)
        bits_from_a = sum(1 << FOUR_INDEX[z] for z in a)
        b = deck_b(p)
        assert bits_from_a == b, (p, bits_from_a, b)
        buckets[bits_from_a].append(p)
    multiplicities = Counter(len(v) for v in buckets.values())
    assert multiplicities == {1: 710, 2: 2, 3: 2}, multiplicities
    exceptional = sorted((tuple(sorted(v)) for v in buckets.values() if len(v) > 1))
    assert exceptional == EXPECTED, exceptional
    assert sum(map(len, buckets.values())) == 720
    assert len(buckets) == 714
    assert prod(len(x) for x in buckets.values()) == 36

    # Each involution maps an exceptional fiber to an exceptional fiber.
    for op in (flip_positions, flip_values, inverse):
        for fiber in exceptional:
            assert tuple(sorted(op(p) for p in fiber)) in exceptional
    assert tuple(sorted(map(flip_positions, exceptional[0]))) == exceptional[3]
    assert tuple(sorted(map(flip_positions, exceptional[1]))) == exceptional[2]
    # Every source with at most one descent has a singleton fiber.
    easy = [p for p in SIX if sum(p[i] > p[i + 1] for i in range(5)) <= 1]
    assert len(easy) == 58
    assert all(len(buckets[deck_b(p)]) == 1 for p in easy)
    print('VERIFY_OK sources=720 distinct_decks=714 singleton=710 '
          'doubleton=2 tripleton=2 optimal_dictionaries=36 '
          'one_descent_singletons=58')

if __name__ == '__main__':
    main()
