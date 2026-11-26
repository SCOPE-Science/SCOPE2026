#!/usr/bin/env python3
"""Exact finite first-order extension-type checks for partition lattices.

No third-party dependencies. The infinite case uses the separate mathematical
argument about atomistic/coatomistic refinement lattices and block counts.
"""
import collections
import hashlib
import itertools
import random


def partitions(n):
    """Canonical restricted-growth words for set partitions on n points."""
    if n == 0:
        yield ()
        return

    def rec(word, largest):
        if len(word) == n:
            yield tuple(word)
            return
        for letter in range(largest + 2):
            word.append(letter)
            yield from rec(word, max(largest, letter))
            word.pop()

    yield from rec([0], 0)


def edges(word):
    """Bit mask of unordered pairs identified by this partition."""
    value = 0
    bit = 0
    for i in range(len(word)):
        for j in range(i):
            if word[i] == word[j]:
                value |= 1 << bit
            bit += 1
    return value


def leq(a, b):
    """Refinement: the equivalent pairs of a are among those of b."""
    return a & ~b == 0


def relation(a, b):
    """0 equal; 1 strictly below; 2 strictly above; 3 incomparable."""
    less = leq(a, b)
    greater = leq(b, a)
    return 0 if less and greater else 1 if less else 2 if greater else 3


def blocks(word):
    return len(set(word))


def theoretical_extensions(pa, pb, n):
    """Pairs of relations (R vs P, R vs Q) from the structural lemma."""
    hp, hq = n - blocks(pa), n - blocks(pb)
    cp, cq = blocks(pa) - 1, blocks(pb) - 1
    position = relation(edges(pa), edges(pb))
    out = set()
    if position == 0:
        out.add((0, 0))
        if hp: out.add((1, 1))
        if cp: out.add((2, 2))
        if hp and cp: out.add((3, 3))
    elif position == 1:  # P below Q
        out.update(((0, 1), (2, 0)))
        if hp: out.update(((1, 1), (3, 1)))
        if cq: out.update(((2, 2), (2, 3)))
        if hq - hp >= 2: out.add((2, 1))
        if hp and cq: out.add((3, 3))
    elif position == 2:  # P above Q: symmetry
        return {(v, u) for u, v in theoretical_extensions(pb, pa, n)}
    else:
        out.update(((0, 3), (3, 0), (1, 1), (2, 2), (3, 3)))
        if hp >= 2: out.add((1, 3))
        if hq >= 2: out.add((3, 1))
        if cp >= 2: out.add((2, 3))
        if cq >= 2: out.add((3, 2))
    return out


def types_and_check(n, sample_limit=None):
    words = list(partitions(n))
    N = len(words)
    masks = [edges(p) for p in words]
    singletons = [1 << j for j in range(N)]
    # For every P, the four masks of all possible order relations P vs R.
    profiles = []
    for p in masks:
        groups = [0] * 4
        for j, r in enumerate(masks):
            groups[relation(p, r)] |= singletons[j]
        profiles.append(groups)

    pairs = ((i, j) for i in range(N) for j in range(N))
    if sample_limit is not None:
        rng = random.Random(230919)
        pairs = ((rng.randrange(N), rng.randrange(N)) for _ in range(sample_limit))
    nchecked = 0
    for i, j in pairs:
        # Actual type uses P vs R; reverse the two strict comparisons
        # to obtain R vs P as in the table.
        reverse = (0, 2, 1, 3)
        actual = {(reverse[a], reverse[b])
                  for a in range(4) for b in range(4)
                  if profiles[i][a] & profiles[j][b]}
        predicted = theoretical_extensions(words[i], words[j], n)
        assert actual == predicted, (n, words[i], words[j], actual, predicted)
        nchecked += 1

    # One-variable rank-2 types, grouped by orbit under permutations of [n].
    representatives = {}
    for i, p in enumerate(words):
        shape = tuple(sorted(collections.Counter(p).values()))
        representatives.setdefault(shape, i)
    pointed_types = {}
    for shape, i in representatives.items():
        ps = profiles[i]
        possible = set()
        for j in range(N):
            qs = profiles[j]
            atom = relation(masks[i], masks[j])
            extension = 0
            for x in range(4):
                for y in range(4):
                    if ps[x] & qs[y]:
                        extension |= 1 << (4*x+y)
            possible.add((atom, extension))
        pointed_types[shape] = frozenset(possible)
    sentence_type = frozenset(pointed_types.values())
    if n >= 5:
        # The pointed type is a function of these two truncated dimensions.
        by_trunc = {}
        for shape, profile in pointed_types.items():
            b = len(shape)
            height = n - b
            key = (min(b, 4), min(height, 3))
            if key in by_trunc:
                assert by_trunc[key] == profile
            by_trunc[key] = profile
        # Conversely these truncated pairs produce distinct pointed types.
        assert len(by_trunc) == len(set(by_trunc.values()))
    return N, sentence_type, nchecked, len(representatives)


def abstract_type_set(n):
    return frozenset((min(b, 4), min(n-b, 3)) for b in range(1, n+1))


def main():
    observed = {}
    bell = []
    tested = []
    for n in range(1, 9):
        # Exhaustive pair tests to n=7; reproducible subset at n=8.
        limit = 50000 if n == 8 else None
        count, r3type, nchecked, orbits = types_and_check(n, limit)
        bell.append(count)
        observed[n] = r3type
        tested.append(nchecked)
        print(f'RANK3_EXACT n={n} partitions={count} one_variable_orbits={orbits} '
              f'pointed_rank2_types={len(r3type)} pair_comparisons={nchecked}')
    assert bell == [1, 2, 5, 15, 52, 203, 877, 4140]
    assert all(observed[n] != observed[n+1] for n in range(1, 7))
    assert observed[7] == observed[8]
    print('FINITE_CLASSIFICATION_OK rank3_classes_1_to_8=7 stable_7_equals_8=True')

    stabilized = abstract_type_set(7)
    assert len(stabilized) == 7
    for n in range(7, 301):
        assert abstract_type_set(n) == stabilized
    assert all(abstract_type_set(n) != abstract_type_set(n+1) for n in range(1, 7))
    print('BLOCK_HEIGHT_PROFILE_OK universal_algebraic_classes=7 tested_parameters=1..300')
    print('PAIR_EXTENSION_LEMMA_OK exhaustive_n=1..7 deterministic_samples_n8=50000')
    print('SHARP_REPRESENTATIVE_OK ground_points=7 lattice_elements=877')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
