#!/usr/bin/env python3
"""Exact shattering and facet-orbit certificate for five-label betweenness queries.

Requires only Python 3 standard library. Execute from any working directory.
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import csv


def queries(n):
    """(middle, smaller endpoint, larger endpoint), in canonical index order."""
    return [(middle, ends[0], ends[1])
            for tri in combinations(range(n), 3)
            for middle in tri
            for ends in [tuple(v for v in tri if v != middle)]]


def trace_from_positions(order, Q):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    return sum(1 << j for j, (m, a, b) in enumerate(Q)
               if (pos[a] < pos[m] < pos[b] or pos[b] < pos[m] < pos[a]))


def trace_from_inversions(order, Q):
    """A second predicate: middle means disagreement of endpoint comparisons."""
    greater = {(x, y): i > j for i, x in enumerate(order)
               for j, y in enumerate(order) if x != y}
    return sum(1 << j for j, (m, a, b) in enumerate(Q)
               if greater[(m, a)] != greater[(m, b)])


def recursive_orders(n):
    levels = [()]
    for v in range(n):
        levels = [p[:i] + (v,) + p[i:]
                  for p in levels for i in range(len(p) + 1)]
    return levels


def signature(S, C, k):
    ix = tuple(i for i in range(S.bit_length()) if S & (1 << i))
    assert len(ix) == k
    seen = set()
    for c in C:
        sig = 0
        for j, i in enumerate(ix):
            sig |= ((c >> i) & 1) << j
        seen.add(sig)
        if len(seen) == (1 << k):
            return True
    return False


def direct_complex(n):
    Q = queries(n)
    orders = list(permutations(range(n)))
    recursive = recursive_orders(n)
    assert sorted(orders) == sorted(recursive)
    A = {trace_from_positions(p, Q) for p in orders}
    B = {trace_from_inversions(p, Q) for p in recursive}
    assert A == B
    concepts = tuple(sorted(A))
    assert len(concepts) * 2 == len(orders) if n >= 2 else len(concepts) == 1
    max_k = min(len(Q), len(concepts).bit_length() - 1)
    faces = {}
    for k in range(max_k + 1):
        accepted = set()
        for ix in combinations(range(len(Q)), k):
            S = sum(1 << i for i in ix)
            if signature(S, concepts, k):
                accepted.add(S)
        faces[k] = accepted
    return Q, concepts, faces


def facets_of(faces):
    K = max(faces)
    # If a face has no immediate shattered extension it has no larger extension.
    return {(k, s) for k, supports in faces.items() for s in supports
            if k == K or not any((s | (1 << i)) in faces[k + 1]
                                  for i in range(30)
                                  if not s & (1 << i))}


def check_orbit_certificate(Q, C, faces, facets):
    header = ('size', 'orbit_size', 'query_indices', 'trace_count')
    rows = list(csv.DictReader(
        (Path(__file__).parent / 'facet_orbits.tsv').open(encoding='utf-8'),
        delimiter='\t'))
    assert len(rows) == 25
    for row in rows:
        assert tuple(row) == header
    lookup = {q: i for i, q in enumerate(Q)}
    transformations = []
    for p in permutations(range(5)):
        idx = []
        for m, a, b in Q:
            x, y = sorted((p[a], p[b]))
            idx.append(lookup[(p[m], x, y)])
        transformations.append(tuple(idx))
    all_facets = set()
    for row in rows:
        k = int(row['size'])
        ix = tuple(int(i) for i in row['query_indices'].split(','))
        assert len(ix) == k and len(set(ix)) == k
        S = sum(1 << i for i in ix)
        assert signature(S, C, k)
        assert (k, S) in facets
        transformed = {
            sum(1 << idx[i] for i in ix) for idx in transformations}
        assert len(transformed) == int(row['orbit_size'])
        assert int(row['trace_count']) == (1 << k)
        assert not all_facets.intersection({(k, t) for t in transformed})
        all_facets.update((k, t) for t in transformed)
    assert all_facets == facets
    # Independent reconstruction of every face from the complete facet orbits.
    faces_from_facets = {k: set() for k in faces}
    for size, S in all_facets:
        ix = [j for j in range(len(Q)) if S & (1 << j)]
        for k in range(size + 1):
            for sub in combinations(ix, k):
                faces_from_facets[k].add(sum(1 << i for i in sub))
    assert faces_from_facets == faces
    return len(rows), Counter(k for k, _ in all_facets)


def check_explicit_witness(Q):
    ix = (4, 7, 10, 13)
    assert [Q[i] for i in ix] == [(1, 0, 3), (1, 0, 4),
                                   (2, 0, 3), (2, 0, 4)]
    file = Path(__file__).parent / 'witness_4.tsv'
    rows = list(csv.DictReader(file.open(encoding='utf-8'), delimiter='\t'))
    assert len(rows) == 16
    got = set()
    for r in rows:
        order = tuple(map(int, r['order'].split(',')))
        assert set(order) == set(range(5))
        full = trace_from_positions(order, Q)
        bits = ''.join(str((full >> i) & 1) for i in reversed(ix))
        assert bits == r['answer_bits']
        got.add(bits)
    assert got == {f'{x:04b}' for x in range(16)}


def main():
    expected = {
        3: [1, 3],
        4: [1, 12, 54, 0],
        5: [1, 30, 405, 2700, 510, 0],
    }
    for n in (3, 4, 5):
        Q, C, faces = direct_complex(n)
        got = [len(faces.get(i, set())) for i in range(len(expected[n]))]
        assert got == expected[n], (n, got)
        if n == 5:
            assert len(Q) == 30 and len(C) == 60
            check_explicit_witness(Q)
            facets = facets_of(faces)
            assert Counter(k for k, _ in facets) == {3: 1530, 4: 510}
            n_orbits, facet_counts = check_orbit_certificate(
                Q, C, faces, facets)
            assert n_orbits == 25 and facet_counts == {3: 1530, 4: 510}
    print('BETWEENNESS5_PASS: 30 queries, 60 concepts, '
          'face counts 1,30,405,2700,510; '
          'facets 1530+510; 25 facet orbits; '
          'all 142506 five-query supports excluded')


if __name__ == '__main__':
    main()
