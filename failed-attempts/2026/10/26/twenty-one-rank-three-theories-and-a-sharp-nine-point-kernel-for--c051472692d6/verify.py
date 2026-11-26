#!/usr/bin/env python3
"""Exact rank-three FO theory profile for finite nonempty equivalence relations.

No external packages. Run: python3 verify.py
"""
from functools import lru_cache
from itertools import product

Q = 3


def canonical_partitions():
    structures = []
    for counts in product(range(Q + 1), repeat=Q):
        if not any(counts):
            continue
        sizes = tuple(size for size, many in enumerate(counts, 1)
                      for _ in range(many))
        block_of = tuple(block for block, size in enumerate(sizes)
                         for _ in range(size))
        structures.append((counts, block_of))
    return structures


def atomic(tup, blocks):
    return tuple((tup[i] == tup[j],
                  blocks[tup[i]] == blocks[tup[j]])
                 for i in range(len(tup)) for j in range(i + 1, len(tup)))


def rank_types(structures):
    """Bottom-up Hintikka recursion with three total available pebbles."""
    # (structure index, tuple) maps to an integer naming its current type.
    prev = {}
    pool = {}
    for i, (_, blocks) in enumerate(structures):
        for tup in product(range(len(blocks)), repeat=Q):
            key = atomic(tup, blocks)
            if key not in pool:
                pool[key] = len(pool)
            prev[i, tup] = pool[key]
    level_counts = [len(pool)]
    for arity in (2, 1, 0):
        next_types = {}
        pool = {}
        for i, (_, blocks) in enumerate(structures):
            for tup in product(range(len(blocks)), repeat=arity):
                possible = frozenset(prev[i, tup + (v,)]
                                     for v in range(len(blocks)))
                # Explicit atomic data makes induction valid for every vocabulary.
                key = (atomic(tup, blocks), possible)
                if key not in pool:
                    pool[key] = len(pool)
                next_types[i, tup] = pool[key]
        prev = next_types
        level_counts.append(len(pool))
    return {i: prev[i, ()] for i in range(len(structures))}, level_counts


@lru_cache(maxsize=None)
def duplicator_wins(i, j, left, right, moves):
    """Independent direct three-move game; not based on type identifiers."""
    A, B = STRUCTURES[i][1], STRUCTURES[j][1]
    if atomic(left, A) != atomic(right, B):
        return False
    if moves == 0:
        return True
    for a in range(len(A)):
        if not any(duplicator_wins(i, j, left + (a,), right + (b,),
                                   moves - 1) for b in range(len(B))):
            return False
    for b in range(len(B)):
        if not any(duplicator_wins(i, j, left + (a,), right + (b,),
                                   moves - 1) for a in range(len(A))):
            return False
    return True


STRUCTURES = canonical_partitions()


def main():
    types, levels = rank_types(STRUCTURES)
    groups = {}
    for index, name in types.items():
        groups.setdefault(name, []).append(index)
    assert len(STRUCTURES) == 63
    assert levels == [12, 16, 18, 21], levels
    assert len(groups) == 21
    mins = []
    for group in groups.values():
        size = lambda i: len(STRUCTURES[i][1])
        best_size = min(map(size, group))
        best = [i for i in group if size(i) == best_size]
        assert len(best) == 1, best
        mins.append(best[0])
    representatives = sorted(STRUCTURES[i][0] for i in mins)
    expected = [
        (0, 0, 1), (0, 0, 2), (0, 0, 3),
        (0, 1, 0), (0, 1, 1), (0, 2, 0), (0, 2, 1), (0, 3, 0),
        (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 2, 0),
        (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 2, 0),
        (3, 0, 0)]
    assert representatives == expected
    assert max(len(STRUCTURES[i][1]) for i in mins) == 9
    assert sum(len(STRUCTURES[i][1]) for i in mins) == 103
    for ix, i in enumerate(mins):
        for j in mins[ix + 1:]:
            assert not duplicator_wins(i, j, (), (), Q), (i, j)
    for group in groups.values():
        representative = next(i for i in mins if i in group)
        for j in group:
            assert duplicator_wins(representative, j, (), (), Q), (representative, j)
    print('CANONICAL_PARTITIONS=63')
    print('HINTIKKA_TYPE_COUNTS=12,16,18,21')
    print('SENTENCE_THEORIES=21')
    print('UNIQUE_MINIMAL_REPRESENTATIVES=21')
    print('SHARP_MAXIMUM_MINIMAL_ORDER=9')
    print('TOTAL_MINIMAL_REPRESENTATIVE_ORDER=103')
    print('DIRECT_EF_DISTINCT_PAIRS=210')
    print('DIRECT_EF_MEMBERSHIP_CHECKS=63')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
