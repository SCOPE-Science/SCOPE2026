#!/usr/bin/env python3
"""Finite checks for dimensionalities of two-row rectangular-band monoids.

The universal theorem is proved independently; this script checks every
partition through four columns, plus exact finite automorphism orbits.
Standard Python library only.
"""
import itertools
from functools import lru_cache
from math import comb


def partitions(size):
    labels = [0] * size

    def extend(index, largest):
        if index == size:
            yield tuple(labels)
        else:
            for val in range(largest + 2):
                labels[index] = val
                yield from extend(index + 1, max(largest, val))

    yield from extend(1, 0)


def blocks_of(labels):
    blocks = {}
    for cell, color in enumerate(labels):
        blocks.setdefault(color, set()).add(cell)
    return list(blocks.values())


def is_dimensionality(n, labels):
    groups = blocks_of(labels)
    group_of = {}
    for group in groups:
        for cell in group:
            group_of[cell] = group
    for a in groups:
        rows = {cell // n for cell in a}
        for b in groups:
            columns = {cell % n for cell in b}
            rectangle = {i * n + j for i in rows for j in columns}
            if any(not group_of[cell].issubset(rectangle) for cell in rectangle):
                return False
    return True


def predicted_form(n, labels):
    top, bottom = labels[:n], labels[n:]
    topcolors, bottomcolors = set(top), set(bottom)
    if topcolors.isdisjoint(bottomcolors):
        return 'separated' if all((top[i] == top[j]) == (bottom[i] == bottom[j])
                                  for i in range(n) for j in range(n)) else None
    if topcolors != bottomcolors:
        return None
    column_palettes = [frozenset((top[j], bottom[j])) for j in range(n)]
    for color in set(labels):
        containing = {column_palettes[j] for j in range(n)
                      if color in column_palettes[j]}
        if len(containing) != 1:
            return None
    return 'mixed'


@lru_cache(None)
def stirling(n, k):
    if n == 0:
        return int(k == 0)
    return stirling(n - 1, k - 1) + k * stirling(n - 1, k) if k > 0 else 0


def bell(n):
    return sum(stirling(n, k) for k in range(n + 1))


@lru_cache(None)
def weighted_bell(n):
    if n == 0:
        return 1
    return sum(comb(n - 1, size - 1) *
               (1 + (comb(size, size // 2) // 2 if size % 2 == 0 else 0)) *
               weighted_bell(n - size) for size in range(1, n + 1))


def normalize(labels):
    name, out = {}, []
    for x in labels:
        if x not in name:
            name[x] = len(name)
        out.append(name[x])
    return tuple(out)


def partition_join(first, second):
    size = len(first)
    parent = list(range(size))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for relation in (first, second):
        seen = {}
        for i, color in enumerate(relation):
            if color in seen:
                parent[root(i)] = root(seen[color])
            else:
                seen[color] = i
    return normalize([root(i) for i in range(size)])


def cycle_partition(permutation):
    parent = list(range(len(permutation)))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for i, j in enumerate(permutation):
        parent[root(i)] = root(j)
    return normalize([root(i) for i in range(len(permutation))])


def all_subgroup_orbit_partitions(n):
    generators = set()
    for column_perm in itertools.permutations(range(n)):
        for flip in (0, 1):
            image = [(row ^ flip) * n + column_perm[j]
                     for row in range(2) for j in range(n)]
            generators.add(cycle_partition(image))
    accepted = {tuple(range(2 * n))}
    while True:
        expanded = accepted | {partition_join(a, b) for a in accepted
                               for b in generators}
        if expanded == accepted:
            return accepted
        accepted = expanded


def check():
    for n in range(1, 6):
        valid = set()
        separated = mixed = 0
        for labels in partitions(2 * n):
            finite = is_dimensionality(n, labels)
            form = predicted_form(n, labels)
            assert finite == (form is not None), (n, labels, finite, form)
            if finite:
                valid.add(labels)
                if form == 'separated':
                    separated += 1
                else:
                    mixed += 1
        expected_mixed = sum(stirling(n, k) * 2 ** (n - k)
                             for k in range(1, n + 1))
        assert separated == bell(n)
        assert mixed == expected_mixed
        orbit = all_subgroup_orbit_partitions(n)
        assert orbit.issubset(valid)
        assert len(orbit) == bell(n) + weighted_bell(n)
        assert len(valid) == bell(n) + expected_mixed
        print('n=%d D=%d O=%d nonorbit=%d congruences=%d'
              % (n, len(valid), len(orbit), len(valid - orbit), 2 * bell(n)))

    n = 3
    # Three classes on the seven-element monoid, with the identity separate.
    x = {0, 1, 5}  # (0,1),(0,2),(1,3), zero-based columns
    labels = tuple(0 if i in x else 1 for i in range(2 * n))
    assert is_dimensionality(n, labels)
    assert labels not in all_subgroup_orbit_partitions(n)
    assert sum(i // n == 0 for i in x) == 2
    assert sum(i // n == 1 for i in x) == 1
    # The square of its block sum has coefficients 2 and 1 across rows:
    assert (2, 1) == (len([i for i in x if i // n == 0]),
                      len([i for i in x if i // n == 1]))
    assert bell(5) + sum(stirling(5, k) * 2 ** (5-k)
                         for k in range(1, 6)) == 309
    print('RECTANGULAR_BAND_DIMENSIONALITIES_OK')


if __name__ == '__main__':
    check()
