#!/usr/bin/env python3
"""Reproduce finite face and elementary-collapse checks for pentagonal torus grids.

Only Python standard library is used. The all-n proof is the combinatorial
argument in RESULT.md, not extrapolation from these finite examples.
"""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import json


def vertex(j, a, n):
    return 5 * (j % n) + a % 5


def adjacency(n):
    N = 5 * n
    adj = [set() for _ in range(N)]
    for j in range(n):
        for a in range(5):
            u = vertex(j, a, n)
            for v in (vertex(j + 1, a, n), vertex(j, a + 1, n)):
                adj[u].add(v)
                adj[v].add(u)
    return adj


def short_distance_graph(n):
    adj = adjacency(n)
    dist = []
    for u in range(5 * n):
        q = deque([u]); du = {u: 0}
        while q:
            x = q.popleft()
            if du[x] == 2:
                continue
            for y in adj[x]:
                if y not in du:
                    du[y] = du[x] + 1
                    q.append(y)
        dist.append(du)
    return [set(v for v in d if v != u) for u, d in enumerate(dist)]


def clique_faces(vertices, nbr):
    """Direct all-clique enumeration; no input facet list is trusted."""
    faces = {()}
    def extend(face, candidates):
        for i, v in enumerate(candidates):
            nf = face + (v,)
            faces.add(nf)
            extend(nf, [w for w in candidates[i + 1:] if w in nbr[v]])
    extend((), sorted(vertices))
    return faces


def free_pair(F, smaller, larger):
    small = set(smaller); large = set(larger)
    assert smaller in F and larger in F
    assert len(larger) == len(smaller) + 1 and small < large
    assert all((z == larger) for z in F if len(z) > len(smaller) and small.issubset(z)), (smaller, larger)
    F.remove(smaller)
    F.remove(larger)


def remove_distant_column_edges(F, n):
    pairs = 0
    for j in range(n):
        for a in range(5):
            e = (vertex(j - 1, a, n), vertex(j + 1, a, n))
            mid = vertex(j, a, n)
            others = (vertex(j, a - 1, n), vertex(j, a + 1, n))
            for k in (2, 1, 0):
                for T in combinations(others, k):
                    low = tuple(sorted(e + T))
                    up = tuple(sorted(e + T + (mid,)))
                    free_pair(F, low, up)
                    pairs += 1
    assert pairs == 20 * n
    return pairs


def local_patch(n, j=0):
    neighbors = short_distance_graph(n)
    columns = [vertex(j, a, n) for a in range(5)] + [vertex(j + 1, a, n) for a in range(5)]
    return clique_faces(columns, neighbors)


def octahedral_collapse(F, n):
    """Verify an independent finite collapse certificate and its residual surface."""
    cert = json.loads(Path(__file__).with_name("local_sphere_collapse.json").read_text())
    assert len(cert["elementary_collapse_pairs"]) == 48
    count = 0
    # Relabel the selected two consecutive columns to vertices 0,...,9.
    # In this verifier, the selected patch is columns zero and one.
    remap = {vertex(0, a, n): a for a in range(5)}
    remap.update({vertex(1, a, n): 5 + a for a in range(5)})
    inv = {v: k for k, v in remap.items()}
    for lo, hi in cert["elementary_collapse_pairs"]:
        low = tuple(sorted(inv[x] for x in lo))
        high = tuple(sorted(inv[x] for x in hi))
        free_pair(F, low, high)
        count += 1
    relabeled = {tuple(sorted(remap[x] for x in face)) for face in F}
    assert relabeled == {tuple(face) for face in map(tuple, cert["residual_faces"])}
    nonempty = [s for s in F if s]
    assert Counter(map(len, nonempty)) == {1: 6, 2: 12, 3: 8}
    triangles = [s for s in F if len(s) == 3]
    edges = {s for s in F if len(s) == 2}
    verts = {s[0] for s in F if len(s) == 1}
    edge_degree = Counter(tuple(sorted(e)) for face in triangles for e in combinations(face, 2))
    assert set(edge_degree) == edges
    assert all(edge_degree[e] == 2 for e in edges)
    nonedges = {tuple(sorted(e)) for e in combinations(sorted(verts), 2) if tuple(sorted(e)) not in edges}
    assert len(nonedges) == 3
    assert Counter(x for e in nonedges for x in e) == Counter({v: 1 for v in verts})
    # The eight facets choose one endpoint from each of three opposite pairs.
    assert len(triangles) == 2 ** 3
    assert all(not set(e).issubset(face) for e in nonedges for face in triangles)
    # Check the residual graph is connected, independently of its local links.
    visited = {min(verts)}
    while True:
        fresh = {x for e in edges if any(y in visited for y in e) for x in e} - visited
        if not fresh:
            break
        visited |= fresh
    assert visited == verts
    # Every vertex link is a 4-cycle, not merely a 2-regular disjoint union.
    for v in verts:
        link_edges = [tuple(sorted(set(face) - {v})) for face in triangles if v in face]
        link_verts = set(x for edge in link_edges for x in edge)
        assert len(link_verts) == len(link_edges) == 4
        degree = Counter(x for edge in link_edges for x in edge)
        assert all(degree[x] == 2 for x in link_verts)
        visited = {next(iter(link_verts))}
        while True:
            fresh = {x for edge in link_edges if any(y in visited for y in edge) for x in edge} - visited
            if not fresh:
                break
            visited |= fresh
        assert visited == link_verts
    assert count == 48
    return count


def check(n):
    assert n >= 7
    nbr = short_distance_graph(n)
    F = clique_faces(range(5 * n), nbr)
    face_vector = tuple(sum(len(s) == k for s in F) for k in range(1, 6))
    assert face_vector == tuple(n * x for x in (5, 30, 55, 35, 6)), (n, face_vector)
    full = len(F)
    pairs = remove_distant_column_edges(F, n)
    assert len(F) == 91 * n + 1
    # The remaining faces are precisely those contained in a consecutive pair of columns.
    L = {()}
    for j in range(n):
        cols = {vertex(j, a, n) for a in range(5)} | {vertex(j + 1, a, n) for a in range(5)}
        L.update(f for f in clique_faces(cols, nbr))
    assert F == L
    patch = local_patch(n)
    assert len(patch) == 123
    assert octahedral_collapse(patch, n) == 48
    assert full == 131 * n + 1
    print(f'C5xC{n}: faces={full}, distant-edge-collapse-pairs={pairs}, slabs={n}, local-sphere-collapse-pairs=48: PASS')


if __name__ == '__main__':
    for n in (7, 8, 9, 10, 11, 12):
        check(n)
    print('PENTAGONAL_RECTANGULAR_RIPS2_COLLAPSES_OK')
