#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse certificate for half-turn fixed
noncrossing forest complexes on regular 2m-gons, 2 <= m <= 6.
Uses only Python standard library. All checks use exact integer data.
"""
import collections
import itertools
import json

EXPECTED = {
    2: ((4, 4), 1),
    3: ((9, 24, 21), 5),
    4: ((16, 78, 160, 120), 23),
    5: ((25, 190, 660, 1100, 715), 109),
    6: ((36, 390, 2000, 5445, 7644, 4368), 524),
}

def crossing(e, f):
    a, b = e
    c, d = f
    if len({a, b, c, d}) != 4:
        return False
    return (a < c < b < d) or (c < a < d < b)

def edge_orbits(m):
    n = 2*m
    edges = {(i, j) for i in range(n) for j in range(i+1, n)}
    result = []
    while edges:
        e = min(edges)
        t = tuple(sorted(((x + m) % n for x in e)))
        o = tuple(sorted({e, t}))
        assert set(o) <= edges
        edges.difference_update(o)
        result.append(o)
    assert len(result) == m*m
    return result

def is_face(subset, orbits, m):
    n = 2*m
    edges = tuple(e for i in subset for e in orbits[i])
    if any(crossing(e, f) for e, f in itertools.combinations(edges, 2)):
        return False
    parent = list(range(n))
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for a, b in edges:
        x, y = find(a), find(b)
        if x == y:
            return False
        parent[x] = y
    return True

def enumerate_faces(orbits, m):
    # The forest/noncrossing condition is hereditary. In increasing orbit
    # order every valid face is therefore generated exactly once.
    faces = {()}
    for v in range(len(orbits)):
        additions = set()
        for f in faces:
            g = f + (v,)
            if is_face(g, orbits, m):
                additions.add(g)
        faces.update(additions)
    assert all(is_face(f, orbits, m) for f in faces)
    return faces

def lexicographic_matching(faces, number_vertices):
    unmatched = set(faces) - {()}
    matching = []
    for v in range(number_vertices):
        # Only unmatched faces are paired, using a fixed total vertex order.
        for f in sorted(unmatched, key=lambda s: (len(s), s)):
            if f not in unmatched or v in f:
                continue
            g = tuple(sorted((*f, v)))
            if g in unmatched:
                unmatched.remove(f)
                unmatched.remove(g)
                matching.append((f, g))
    assert 2*len(matching)+len(unmatched) == len(faces)-1
    return unmatched, matching

def check_acyclic(faces, matching):
    # Orient every unmatched Hasse edge upper -> lower and matched
    # edges lower -> upper. Acyclicity is equivalent to having a
    # topological ordering of this exact finite directed graph.
    nonempty = set(faces) - {()}
    pairdict = {f: g for f, g in matching}
    edges = collections.defaultdict(list)
    indegree = {f: 0 for f in nonempty}
    num_matched_hasse = 0
    for upper in nonempty:
        for v in upper:
            lower = tuple(x for x in upper if x != v)
            if not lower:
                continue
            if pairdict.get(lower) == upper:
                a, b = lower, upper
                num_matched_hasse += 1
            else:
                a, b = upper, lower
            edges[a].append(b)
            indegree[b] += 1
    assert num_matched_hasse == len(matching)
    q = collections.deque(f for f, k in indegree.items() if k == 0)
    processed = 0
    while q:
        f = q.popleft()
        processed += 1
        for g in edges[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    assert processed == len(nonempty), "closed gradient path"
    return processed

def check_independent_counts(orbits, m, fvector):
    # Independent face test, without hereditary face generation.
    if m > 5:
        return "not_run"
    counts = []
    for k in range(1, m+1):
        cnt = sum(is_face(s, orbits, m)
                  for s in itertools.combinations(range(m*m), k))
        counts.append(cnt)
    assert tuple(counts) == fvector
    return "passed"

def main():
    result = []
    for m, (expected_f, expected_wedges) in EXPECTED.items():
        orbits = edge_orbits(m)
        faces = enumerate_faces(orbits, m)
        vector = tuple(sum(len(f) == k for f in faces)
                       for k in range(1, m+1))
        assert vector == expected_f
        assert not any(len(f) > m for f in faces)
        # Every inclusion-maximal face is a top-dimensional simplex.
        fset = set(faces)
        assert all(len(f) == m or any(
            tuple(sorted((*f, v))) in fset for v in range(m*m) if v not in f)
            for f in faces if f)
        unmatched, pairs = lexicographic_matching(faces, m*m)
        dag_vertices = check_acyclic(faces, pairs)
        critical = collections.Counter(len(f)-1 for f in unmatched)
        assert critical == {0: 1, m-1: expected_wedges}
        chi = sum((-1)**d*c for d, c in enumerate(vector))
        assert chi == 1 + (-1)**(m-1)*expected_wedges
        independent = check_independent_counts(orbits, m, vector)
        result.append({
            "polygon_vertices": 2*m,
            "edge_orbits": m*m,
            "f_vector": vector,
            "nonempty_faces": len(faces)-1,
            "matched_pairs": len(pairs),
            "critical_cells": dict(sorted(critical.items())),
            "oriented_hasse_dag_vertices": dag_vertices,
            "acyclic": True,
            "independent_subset_counts": independent,
            "reduced_top_betti_number": expected_wedges,
        })
    print(json.dumps({"checks": "passed", "cases": result},
                     indent=2, sort_keys=True))
if __name__ == '__main__':
    main()
