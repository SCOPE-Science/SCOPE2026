#!/usr/bin/env python3
"""Independent, finite checks for the two-dimer cyclic avalanche theorem.

Run with Python 3.10+: python verify.py.  Uses only standard library.
The infinite-parameter argument is in RESULT.md, not inferred from these tests.
"""
from itertools import combinations
from collections import defaultdict, Counter


def all_faces(facets):
    out = set()
    for f in facets:
        for r in range(1, len(f) + 1):
            out.update(tuple(sorted(s)) for s in combinations(f, r))
    return out


def key(*args):
    return tuple(sorted(args))


def original(n, d):
    return {key(i % n, (i + 1) % n, (i + d) % n, (i + d + 1) % n)
            for i in range(n)}


def expected(n, d):
    return {key(i % n, (i + 1) % n, (i + d + 1) % n)
            for i in range(n)} | {
            key(i % n, (i + d) % n, (i + d + 1) % n)
            for i in range(n)}


def incidence(faces, face):
    s = set(face)
    return [f for f in faces if len(f) == len(face) + 1 and s.issubset(f)]


def collapse(n, d):
    faces = all_faces(original(n, d))
    assert len([f for f in faces if len(f) == 4]) == n
    # Collapse each tetrahedron along one short-diagonal triangle.
    for i in range(n):
        top = key(i % n, (i + 1) % n, (i + d) % n, (i + d + 1) % n)
        free = key(i % n, (i + 1) % n, (i + d) % n)
        assert top in faces and free in faces
        assert incidence(faces, free) == [top]
        faces.remove(top)
        faces.remove(free)
    # The short diagonal becomes free in its other incident triangle.
    for i in range(n):
        free = key((i + 1) % n, (i + d) % n)
        triangle = key((i + 1) % n, (i + d) % n, (i + d + 1) % n)
        assert free in faces and triangle in faces
        assert incidence(faces, free) == [triangle]
        faces.remove(triangle)
        faces.remove(free)
    assert faces == all_faces(expected(n, d))
    return faces


def orientable_surface(n, d, faces):
    tris = [f for f in faces if len(f) == 3]
    edges = [f for f in faces if len(f) == 2]
    assert len(tris) == 2 * n
    assert len(edges) == 3 * n
    assert len([f for f in faces if len(f) == 1]) == n
    assert n - len(edges) + len(tris) == 0
    edge_signs = defaultdict(list)
    def orient(abc):
        x, y, z = abc
        for u, v in ((x, y), (y, z), (z, x)):
            e = key(u, v)
            edge_signs[e].append(1 if (u, v) == e else -1)
    for i in range(n):
        orient((i, (i + 1) % n, (i + d + 1) % n))
        orient((i, (i + d + 1) % n, (i + d) % n))
    assert set(edge_signs) == set(edges)
    assert all(sorted(v) == [-1, 1] for v in edge_signs.values())
    # Each vertex link must be one connected six-cycle, not several components.
    for v in range(n):
        adjacent = defaultdict(set)
        for t in tris:
            if v in t:
                a, b = [q for q in t if q != v]
                adjacent[a].add(b)
                adjacent[b].add(a)
        assert len(adjacent) == 6
        assert all(len(q) == 2 for q in adjacent.values())
        seen, todo = set(), [next(iter(adjacent))]
        while todo:
            u = todo.pop()
            if u in seen: continue
            seen.add(u)
            todo.extend(adjacent[u] - seen)
        assert len(seen) == 6


def boundary_rank(faces, r):
    upper = sorted(f for f in faces if len(f) == r)
    lower = {f: i for i, f in enumerate(sorted(f for f in faces if len(f) == r - 1))}
    pivot = {}
    for f in upper:
        vec = 0
        for sub in combinations(f, r - 1): vec ^= 1 << lower[sub]
        while vec:
            k = vec.bit_length() - 1
            if k in pivot: vec ^= pivot[k]
            else:
                pivot[k] = vec
                break
    return len(pivot)


def betti_mod2(n, d):
    faces = all_faces(original(n, d))
    cnt = [0] + [sum(len(f) == s for f in faces) for s in range(1, 5)]
    ranks = [0, 0] + [boundary_rank(faces, s) for s in range(2, 5)] + [0]
    return tuple(cnt[s] - ranks[s] - ranks[s + 1] for s in range(1, 5))


def dynamics(n, d):
    state = [int(i in {0, 1, d, d + 1}) for i in range(n)]
    facets = []
    for i in range(n):
        firing = {j for j in range(n) if state[j] >= 1}
        facets.append(tuple(sorted(firing)))
        nxt = [state[j] - int(j in firing) + int((j - 1) % n in firing)
               for j in range(n)]
        state = nxt
    assert state == [int(i in {0, 1, d, d + 1}) for i in range(n)]
    assert set(facets) == original(n, d)
    assert len(set(facets)) == n


def main():
    torus_cases = 0
    boundary_cases = 0
    dynamics_cases = 0
    homology_cases = 0
    for d in range(3, 26):
        n0 = 2 * d + 2
        for n in range(n0, n0 + 26):
            faces = collapse(n, d)
            if n == n0:
                assert len([f for f in faces if len(f) == 2]) == 2 * n + n // 2
                assert n - (2 * n + n // 2) + 2 * n == n // 2
                boundary_cases += 1
            else:
                orientable_surface(n, d, faces)
                torus_cases += 1
            if d <= 9 and n <= 2 * d + 8:
                dynamics(n, d)
                dynamics_cases += 1
            if d <= 9 and n <= 2 * d + 8:
                expected_betti = (1, 2, 1, 0) if n >= n0 + 1 else (1, 1, n // 2, 0)
                assert betti_mod2(n, d) == expected_betti, (n, d, betti_mod2(n, d))
                homology_cases += 1
    print(f'ALL_VERIFY_OK torus_cases={torus_cases} boundary_cases={boundary_cases} '
          f'dynamics_cases={dynamics_cases} homology_cases={homology_cases} '
          f'd_range=3..25 n_range_each=2d+2..2d+27')

if __name__ == '__main__':
    main()
