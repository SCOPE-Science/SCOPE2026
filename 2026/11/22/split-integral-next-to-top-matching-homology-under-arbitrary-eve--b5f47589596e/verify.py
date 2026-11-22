#!/usr/bin/env python3
"""Exact finite checks for an integral matching-complex inclusion theorem.
No third-party dependencies. Run with python verify.py.
"""
from itertools import combinations
from collections import deque, defaultdict


def faces_from_edges(n_vertices, edges):
    """Return nonempty matching faces, represented by edge-index bitmasks."""
    faces = {0}
    for i, (u, v) in enumerate(edges):
        bit = 1 << i
        for face in list(faces):
            used = 0
            for j, (a, b) in enumerate(edges):
                if face & (1 << j):
                    used |= 1 << a | 1 << b
            if not used & (1 << u | 1 << v):
                faces.add(face | bit)
    return faces - {0}


def greedy_match_and_acyclicity(faces, order, n_edges):
    """Match pairs and topologically sort every oriented Hasse edge."""
    unmatched = set(faces)
    pairs = []
    for k in order:
        bit = 1 << k
        for a in sorted(list(unmatched)):
            b = a | bit
            if not (a & bit) and a in unmatched and b in unmatched:
                unmatched.remove(a)
                unmatched.remove(b)
                pairs.append((a, b))
    pair_by_upper = {b: a for a, b in pairs}
    indeg = {f: 0 for f in faces}
    adj = defaultdict(list)
    cover_count = 0
    for high in faces:
        for k in range(n_edges):
            if not high & (1 << k):
                continue
            low = high ^ (1 << k)
            if low == 0:
                continue
            assert low in faces
            source, target = (low, high) if pair_by_upper.get(high) == low else (high, low)
            adj[source].append(target)
            indeg[target] += 1
            cover_count += 1
    q = deque(f for f, d in indeg.items() if d == 0)
    seen = 0
    while q:
        f = q.popleft()
        seen += 1
        for g in adj[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                q.append(g)
    assert seen == len(faces), 'Matching contains a directed cycle'
    critical = {size: sum(f.bit_count() == size for f in unmatched) for size in range(1, 5)}
    return len(pairs), critical, cover_count


def test_cube():
    all_edges = list(combinations(range(8), 2))
    forbidden = {(0, 1), (2, 3), (4, 5), (6, 7)}
    sub_edges = [e for e in all_edges if e not in forbidden]
    sub_faces = faces_from_edges(8, sub_edges)
    full_faces = faces_from_edges(8, all_edges)
    assert len(sub_faces) == 512 and len(full_faces) == 763
    order = [20, 22, 15, 6, 13, 14, 3, 1, 12, 17, 18, 11,
             0, 19, 8, 4, 7, 21, 23, 9, 16, 10, 5, 2]
    p1, critical1, covers1 = greedy_match_and_acyclicity(sub_faces, order, 24)
    p2, critical2, covers2 = greedy_match_and_acyclicity(full_faces, list(range(28)), 28)
    assert critical1 == {1: 1, 2: 0, 3: 79, 4: 0}, critical1
    assert critical2 == {1: 1, 2: 0, 3: 132, 4: 0}, critical2
    assert 2*p1 + sum(critical1.values()) == len(sub_faces)
    assert 2*p2 + sum(critical2.values()) == len(full_faces)
    print('K8 minus a perfect matching: faces', len(sub_faces),
          'pairs', p1, 'critical by size', critical1, 'Hasse covers', covers1)
    print('K8: faces', len(full_faces), 'pairs', p2,
          'critical by size', critical2, 'Hasse covers', covers2)
    print('Cofiber rank from primitive inclusion: ', 132-79)
    # Verify every relative top simplex has a free face outside smaller complex.
    sub_face_sets = {frozenset(sub_edges[i] for i in range(24) if f & 1 << i)
                     for f in sub_faces}
    full_top_faces = [frozenset(all_edges[i] for i in range(28) if f & 1 << i)
                      for f in full_faces if f.bit_count() == 4]
    missing = [face for face in full_top_faces if face not in sub_face_sets]
    assert len(missing) == 45
    for sigma in missing:
        forbidden_in_sigma = next(e for e in sorted(sigma) if e in forbidden)
        # Retain this forbidden edge while dropping a different edge.
        deletion = next(e for e in sorted(sigma) if e != forbidden_in_sigma)
        tau = sigma - {deletion}
        assert forbidden_in_sigma in tau
        assert tau not in sub_face_sets
        assert sum(tau < rho for rho in full_top_faces) == 1
    print('Relative top-face free-pair witnesses:', len(missing), 'PASS')


def test_sharpness():
    c6_edges = [(i, (i+1)%6) if i < 5 else (0,5) for i in range(6)]
    c6_edges = sorted(set(tuple(sorted(e)) for e in c6_edges))
    faces = faces_from_edges(8, c6_edges)
    fvec = [sum(x.bit_count() == i for x in faces) for i in (1,2,3)]
    assert fvec == [6,9,2], fvec
    tri = [f for f in faces if f.bit_count() == 3]
    for t in tri:
        assert any(sum((u & (t^(1<<k))) == (t^(1<<k)) for u in tri) == 1
                   for k in range(6) if t & (1<<k))
    # Verify connectedness of the one-skeleton, and two distinct free triangles.
    adj = {1 << k: set() for k in range(6)}
    for f in faces:
        if f.bit_count() == 2:
            a, b = [1 << k for k in range(6) if f & (1 << k)]
            adj[a].add(b)
            adj[b].add(a)
    reached = set()
    q = [1]
    while q:
        u = q.pop()
        if u in reached: continue
        reached.add(u); q.extend(adj[u]-reached)
    assert len(reached) == 6
    # Collapsing two triangles leaves connected graph with six vertices and seven edges.
    assert fvec[1]-fvec[2]-fvec[0]+1 == 2
    print('C6 plus two isolated graph vertices: (vertices, edges, triangles)', fvec,
          'and reduced H1 rank 2')

if __name__ == '__main__':
    test_cube()
    test_sharpness()
    print('ALL FINITE CHECKS PASS')
