"""Independent finite checks for the minimal zero-forcing classification.

Usage: python3 verify.py
All vertex subsets are tested directly by ordinary zero forcing.
"""
from itertools import combinations
from collections import Counter
import random


def graph_neighborhoods(m):
    # Vertices 0,1 form an edge, vertex 2 is isolated within that triple.
    # Vertices 3,...,m+2 form a path; every cross edge is present.
    n = m + 3
    nbr = [0] * n
    def edge(u, v):
        nbr[u] |= 1 << v
        nbr[v] |= 1 << u
    edge(0, 1)
    for u in range(3):
        for v in range(3, n):
            edge(u, v)
    for v in range(3, n-1):
        edge(v, v+1)
    return nbr


def directly_forces_all(seed, nbr):
    full = (1 << len(nbr)) - 1
    white = full & ~seed
    while white:
        forced = 0
        for v, neighbors in enumerate(nbr):
            if not ((white >> v) & 1):
                white_neighbors = neighbors & white
                if white_neighbors and not (white_neighbors & (white_neighbors - 1)):
                    forced |= white_neighbors
        if forced == 0:
            return False
        white &= ~forced
    return True


def structural_criterion(seed, m):
    a = seed & 7
    b = (seed >> 3) & ((1 << m) - 1)
    count = a.bit_count()
    if count == 0:
        return False
    if count == 1:
        return a in (1, 2) and b == (1 << m) - 1
    if count == 2:
        # A blue path vertex must have all of its path neighbors blue.
        for i in range(m):
            if not (b >> i) & 1:
                continue
            left_blue = (i == 0) or ((b >> (i-1)) & 1)
            right_blue = (i == m-1) or ((b >> (i+1)) & 1)
            if left_blue and right_blue:
                return True
        return False
    # All three core vertices are initially blue.
    return bool(b & (1 | (1 << (m-1)))) or bool(b & (b >> 1))


def expected_minimal_seeds(m):
    full_b = ((1 << m) - 1) << 3
    result = set()
    for a in (3, 5, 6):
        for pair in ((0, 1), (m-2, m-1)):
            result.add(a | sum(1 << (3+i) for i in pair))
        for i in range(1, m-3):
            result.add(a | sum(1 << (3+j) for j in (i, i+1, i+2)))
    for i in (0, m-1):
        result.add(7 | (1 << (3+i)))
    for i in range(1, m-2):
        result.add(7 | (1 << (3+i)) | (1 << (3+i+1)))
    for a in (1, 2):
        result.add(a | full_b)
    return result


def check_all_subsets(m):
    nbr = graph_neighborhoods(m)
    total = 1 << (m+3)
    direct = bytearray(total)
    for s in range(total):
        d = directly_forces_all(s, nbr)
        assert d == structural_criterion(s, m), ('criterion', m, s, d)
        direct[s] = d
    actual = set()
    for s in range(total):
        if direct[s] and all(not direct[s ^ (1 << i)] for i in range(m+3) if (s >> i) & 1):
            actual.add(s)
    expected = expected_minimal_seeds(m)
    assert actual == expected, ('minimal-family', m, sorted(actual ^ expected)[:10])
    spectrum = Counter(s.bit_count() for s in actual)
    target = Counter()
    target[4] += 8
    target[5] += 4*m - 15
    target[m+1] += 2
    assert spectrum == target, (m, spectrum, target)
    print('EXHAUSTIVE_ALL_SUBSETS_AND_MINIMAL_CLASSIFICATION_PASS', m, total, len(actual), sorted(spectrum.items()))


def independent_large_sample():
    rng = random.Random(620241)
    for m in (20, 35, 60, 100):
        nbr = graph_neighborhoods(m)
        for _ in range(1000):
            s = 0
            for j in range(m+3):
                if rng.random() < rng.choice((0.04, 0.12, 0.5, 0.93)):
                    s |= 1 << j
            assert directly_forces_all(s, nbr) == structural_criterion(s, m)
        print('LARGE_RANDOM_FORCING_CRITERION_PASS', m, 1000)

if __name__ == '__main__':
    for m in range(4, 15):
        check_all_subsets(m)
    independent_large_sample()
    print('VERIFY_OK')
