"""Exact verification of the distance-three geodesic spectrum for sparse-paving matroid base polytopes.
Requires only Python 3 standard library; all arithmetic is integer.
"""
from itertools import combinations
from collections import Counter


def main():
    vertices = [sum(1 << i for i in c) for c in combinations(range(6), 3)]
    A, B = sum(1 << i for i in (0, 1, 2)), sum(1 << i for i in (3, 4, 5))
    assert len(vertices) == 20 and A in vertices and B in vertices
    interior = [u for u in vertices if u != A and u != B]
    assert len(interior) == 18
    adjacent = {u: {v for v in vertices if (u ^ v).bit_count() == 2} for u in vertices}
    # Exhaustively range over every stable subset of the 18 eligible forbidden vertices.
    histogram = Counter()
    stable_count = 0
    max_missing = 0
    max_patterns = set()
    for mask in range(1 << 18):
        forbidden = {interior[i] for i in range(18) if (mask >> i) & 1}
        if any((u ^ v).bit_count() == 2 for u, v in combinations(forbidden, 2)):
            continue
        stable_count += 1
        s = len(forbidden)
        survivors = set(vertices) - forbidden
        # Independently count length-three paths in the actual induced one-skeleton.
        length3 = sum(1 for c in adjacent[A] & survivors
                      for d in adjacent[c] & adjacent[B] & survivors)
        assert length3 == 36 - 4 * s
        # No length shorter than 3 can connect the disjoint endpoint bases.
        assert B not in adjacent[A]
        assert not (adjacent[A] & adjacent[B])
        histogram[length3] += 1
        if s > max_missing:
            max_missing = s
            max_patterns = {frozenset(forbidden)}
        elif s == max_missing:
            max_patterns.add(frozenset(forbidden))
    expected = {36: 1, 32: 18, 28: 81, 24: 84, 20: 18}
    assert stable_count == 202, (stable_count, histogram)
    assert dict(histogram) == expected, histogram
    assert max_missing == 4 and len(max_patterns) == 18
    # Check each sharp four-deletion pattern is a rook rectangle across the two layers.
    layer1 = [u for u in interior if (A ^ u).bit_count() == 2]
    layer2 = [u for u in interior if (B ^ u).bit_count() == 2]
    assert len(layer1) == len(layer2) == 9
    for S in max_patterns:
        assert len(S & set(layer1)) == len(S & set(layer2)) == 2
    print('SPARSE_PAVING_THREE_EXCHANGE_PASS stable_sets=202 '
          'spectrum=' + ','.join(f'{x}:{expected[x]}' for x in sorted(expected)) +
          ' sharp_patterns=18')


if __name__ == '__main__':
    main()
