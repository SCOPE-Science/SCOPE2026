#!/usr/bin/env python3
"""Exact finite simplicial verification of an NM_3 homotopy calculation.

Python 3 standard library only. Independent face constructions, exhaustive
Morse matching, complete directed Hasse-graph acyclicity test.
"""
from collections import Counter, deque
from itertools import combinations


def mk_edges():
    n = 8
    edges = {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}
    edges |= {(i, i + n) for i in range(n)}
    edges |= {(min(n + i, n + (i + 3) % n), max(n + i, n + (i + 3) % n))
              for i in range(n)}
    return tuple(sorted(edges))


def build_via_forbidden_triples(edges):
    """Complete enumeration via forbidden three-edge matchings, not vertex covers."""
    m = len(edges)
    by_index = [[] for _ in range(m)]
    forbidden = []
    for a, b, c in combinations(range(m), 3):
        if len(set(edges[a] + edges[b] + edges[c])) == 6:
            t = (1 << a) | (1 << b) | (1 << c)
            forbidden.append(t)
            by_index[a].append(t)
            by_index[b].append(t)
            by_index[c].append(t)
    faces = {0}

    def extend(mask, next_index):
        for j in range(next_index, m):
            child = mask | (1 << j)
            if any(child & t == t for t in by_index[j]):
                continue
            assert child not in faces
            faces.add(child)
            extend(child, j + 1)
    extend(0, 0)
    return faces, forbidden


def build_via_vertex_covers(edges):
    """Independent enumeration of faces using two-vertex cover simplices."""
    incident = [0] * 16
    for j, (u, v) in enumerate(edges):
        incident[u] |= 1 << j
        incident[v] |= 1 << j
    faces = {0}
    for u, v in combinations(range(16), 2):
        mask = incident[u] | incident[v]
        sub = mask
        while sub:
            faces.add(sub)
            sub = (sub - 1) & mask
    return faces


def matching(faces, m):
    """Sequential element matching (increasing edge index)."""
    remaining = set(faces)
    pairs = []
    for index in range(m):
        bit = 1 << index
        for lower in sorted(remaining):
            upper = lower | bit
            if not lower & bit and upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                pairs.append((lower, upper))
    return pairs, remaining


def check_acyclic(faces, pairs, augmented):
    """Topologically sort all cover relations, reversing matched pairs."""
    vertices = set(faces) if augmented else set(faces) - {0}
    pairs = [(a, b) for a, b in pairs if a and b] if not augmented else pairs
    partner = dict(pairs)
    assert len(pairs) == len(set(a for a, _ in pairs))
    assert len(pairs) == len(set(b for _, b in pairs))
    arcs = {s: [] for s in vertices}
    indegree = {s: 0 for s in vertices}
    cover_count = 0
    for upper in vertices:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if lower not in vertices:
                continue
            cover_count += 1
            if partner.get(lower) == upper:
                source, target = lower, upper
            else:
                source, target = upper, lower
            arcs[source].append(target)
            indegree[target] += 1
    queue = deque(s for s in vertices if indegree[s] == 0)
    visited = 0
    while queue:
        cur = queue.popleft()
        visited += 1
        for nxt in arcs[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    assert visited == len(vertices), (visited, len(vertices))
    return cover_count


def main():
    edges = mk_edges()
    assert len(edges) == 24
    degree = Counter(x for e in edges for x in e)
    assert sorted(degree) == list(range(16))
    assert set(degree.values()) == {3}
    # Explicit bipartition: outer i has color i mod 2; inner i has opposite color.
    color = {i: i % 2 for i in range(8)}
    color.update({i + 8: 1 - (i % 2) for i in range(8)})
    assert all(color[u] != color[v] for u, v in edges)
    forbidden_faces, triples = build_via_forbidden_triples(edges)
    cover_faces = build_via_vertex_covers(edges)
    assert forbidden_faces == cover_faces
    assert len(triples) == 1096
    assert len(forbidden_faces) == 3149
    f = Counter(face.bit_count() - 1 for face in forbidden_faces)
    assert [f[d] for d in range(-1, 6)] == [1, 24, 276, 928, 1224, 600, 96]
    # Every forbidden triple is truly a minimal non-face.
    assert all(t not in forbidden_faces for t in triples)
    pairs, critical_augmented = matching(forbidden_faces, 24)
    assert len(pairs) == 1552
    assert len(critical_augmented) == 45
    assert {s.bit_count() - 1 for s in critical_augmented} == {3}
    assert sum(1 for a, b in pairs if a == 0) == 1
    covers_aug = check_acyclic(forbidden_faces, pairs, True)
    covers_nonaug = check_acyclic(forbidden_faces, pairs, False)
    assert covers_aug == 11832
    assert covers_nonaug == 11808
    crit_nonaug = set(critical_augmented)
    for lower, upper in pairs:
        if lower == 0:
            crit_nonaug.add(upper)
    assert Counter(s.bit_count() - 1 for s in crit_nonaug) == {0: 1, 3: 45}
    chi = sum((-1)**d * f[d] for d in range(6))
    assert chi == -44
    print('GRAPH_VERTICES=16 GRAPH_EDGES=24 BIPARTITE=YES DEGREE=3')
    print('THREE_EDGE_MATCHING_MINIMAL_NONFACES=1096')
    print('INDEPENDENT_FACE_METHODS=FORBIDDEN_TRIPLES,VERTEX_COVERS AGREE=YES')
    print('AUGMENTED_FACES=3149 FVECTOR=24,276,928,1224,600,96')
    print('MORSE_PAIRS_AUGMENTED=1552 CRITICAL_AUGMENTED_DIM3=45')
    print('DIRECTED_HASSE_COVERS_AUGMENTED=11832 ACYCLIC=YES')
    print('DIRECTED_HASSE_COVERS_NONAUGMENTED=11808 ACYCLIC=YES')
    print('CRITICAL_NONAUGMENTED=ONE_DIM0_AND_45_DIM3')
    print('EULER_CHARACTERISTIC=-44 WEDGE_SPHERES_DIM3=45')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
