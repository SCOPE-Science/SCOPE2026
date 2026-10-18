"""Finite tests for neighborhood complexes of odd folded hypercubes.
The accompanying mathematical proof is uniform in every odd dimension.
"""
from collections import Counter
from itertools import combinations
from math import comb


def neighborhoods(n):
    assert n >= 3 and n % 2
    N = 1 << (n - 1)
    antipodal = N - 1
    return [frozenset([v ^ (1 << j) for j in range(n - 1)] +
                      [v ^ antipodal]) for v in range(N)]


def face_masks(facets):
    all_faces = {0}
    for facet in facets:
        bits = [1 << v for v in sorted(facet)]
        subsets = [0]
        for bit in bits:
            subsets += [mask | bit for mask in subsets]
        all_faces.update(subsets)
    return all_faces


def collapse_check(n, facets, all_faces):
    """Check that the stated elementary-collapse list removes every >2-face."""
    living = set(all_faces)
    pairs = 0
    for facet in facets:
        vertices = sorted(facet)
        t = vertices[0]
        base = vertices[1:]
        local_subsets = [0]
        for v in vertices:
            local_subsets += [mask | (1 << v) for mask in local_subsets]
        for k in range(n - 1, 2, -1):
            for vv in combinations(base, k):
                small = sum(1 << v for v in vv)
                large = small | (1 << t)
                assert small in living and large in living, (n, small, large)
                # Any simplex with >=3 vertices is in exactly one facet.
                # Thus all cofaces of 'small' must be among local_subsets.
                actual = [s for s in local_subsets if s in living and s & small == small]
                assert set(actual) == {small, large}, (n, k, actual)
                living.remove(small)
                living.remove(large)
                pairs += 1
    assert all(m.bit_count() <= 3 for m in living)
    assert len(living) + 2 * pairs == len(all_faces)
    return pairs, sum(m.bit_count() == 3 for m in living)


def verify(n):
    facets = neighborhoods(n)
    N = len(facets)
    assert len(set(facets)) == N
    assert all(len(f) == n for f in facets)
    for u, v in combinations(range(N), 2):
        assert len(facets[u] & facets[v]) in (0, 2)
    masks = face_masks(facets)
    observed = Counter(m.bit_count() - 1 for m in masks)
    expected = {-1: 1, 0: N, 1: N * comb(n, 2) // 2}
    expected.update({k - 1: N * comb(n, k) for k in range(3, n + 1)})
    assert dict(observed) == expected, (n, observed, expected)
    chi = sum((-1) ** i * count for i, count in observed.items() if i >= 0)
    assert chi == 2 ** (n - 3) * (n * n - 5 * n + 8)
    multiplicity = chi - 1
    result = f'n={n} vertices={N} simplices={len(masks)-1} chi={chi} wedge_S2={multiplicity}'
    if n <= 7:
        matched_pairs, triangles_left = collapse_check(n, facets, masks)
        result += f' elementary_collapse_pairs={matched_pairs} remaining_triangles={triangles_left}'
    print(result)


if __name__ == '__main__':
    for dimension in (3, 5, 7, 9):
        verify(dimension)
    print('VERIFIED finite structural checks (not a substitute for the uniform proof)')
