#!/usr/bin/env python3
"""Finite cross-checks for the cycle-packing skeleton theorem.

Only finite cases are tested: the unrestricted theorem rests on the
block-concatenation argument in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations, permutations
import random


def cycle_type(p):
    n = len(p)
    seen = set()
    lengths = []
    for i in range(n):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def capacity(partition):
    return sum(x // 2 for x in partition)


def extend_word(word, partition):
    """Build a cycle-type-prescribed permutation containing word as subsequence."""
    n = sum(partition)
    word = tuple(word)
    k = len(word)
    assert len(set(word)) == k and all(0 <= x < n for x in word)
    assert k <= capacity(partition)
    spare = [i for i in range(n) if i not in word]
    positions = spare[:k]  # Increasing, each outside the prescribed values
    singleton = spare[k:]
    pair_list = list(zip(positions, word))
    ans = [None] * n
    used = 0
    si = 0
    for ell in partition:
        pair_count = min(ell // 2, len(pair_list) - used)
        vertices = []
        for pos, val in pair_list[used:used + pair_count]:
            vertices.extend([pos, val])
        used += pair_count
        single_count = ell - 2 * pair_count
        vertices.extend(singleton[si:si + single_count])
        si += single_count
        assert len(vertices) == ell and len(set(vertices)) == ell
        for z in range(ell):
            ans[vertices[z]] = vertices[(z + 1) % ell]
    assert used == k and si == len(singleton)
    assert set(ans) == set(range(n))
    assert cycle_type(ans) == tuple(sorted(partition, reverse=True))
    assert tuple(ans[pos] for pos in positions) == word
    return tuple(ans)


def exhaustive_skeleton(n):
    words_by_type = defaultdict(set)
    for p in permutations(range(n)):
        part = cycle_type(p)
        c = capacity(part)
        if c == 0:
            continue
        for indices in combinations(range(n), c):
            words_by_type[part].add(tuple(p[i] for i in indices))
    for part, words in words_by_type.items():
        c = capacity(part)
        expected = 1
        for i in range(n-c+1, n+1):
            expected *= i
        assert len(words) == expected, (n, part, len(words), expected)
        for w in words:
            p = extend_word(w, part)
            assert len(p) == n
    print('PASS exhaustive conjugacy classes', 'n=', n, 'classes=', len(words_by_type))


def test_12():
    rng = random.Random(20261121)
    partitions = [(6, 4, 2), (5, 3, 2, 1, 1), (2,) * 6,
                  (11, 1), (3,) * 4, (4, 4, 4), (1,) * 12]
    count = 0
    for part in partitions:
        c = capacity(part)
        for k in range(c + 1):
            for _ in range(120):
                word = rng.sample(range(12), k)
                extend_word(word, part)
                count += 1
    print('PASS constructive tests', 'n=', 12, 'cases=', count)


def test_sharpness():
    for m in range(1, 7):
        n = 2*m
        part = (2,) * m
        increasing = tuple(range(m + 1))
        for p in permutations(range(n)) if n <= 8 else ():
            if cycle_type(p) != part:
                continue
            # No increasing subword of length m+1 in any FPF involution.
            assert not any(tuple(p[i] for i in idx) == increasing
                           for idx in combinations(range(n), m + 1))
        extend_word(tuple(range(m)), part)
        print('PASS sharp threshold for fixed-point-free involutions', 'n=', n,
              'full through length=', m, 'missing increasing length=', m+1)


if __name__ == '__main__':
    for n in range(2, 9):
        exhaustive_skeleton(n)
    test_12()
    test_sharpness()
    print('ALL TESTS PASS; unrestricted theorem is proven separately')
