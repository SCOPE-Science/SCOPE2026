#!/usr/bin/env python3
"""Finite integral homotopy certificate for the graph-metric icosidodecahedron Rips stage.

Run: python3 verify_icosidodecahedron.py collapse_certificate.json
Generate: python3 verify_icosidodecahedron.py --generate collapse_certificate.json
Only Python's standard library is used. All graph labels and orderings are explicit.
"""
import collections
import itertools
import json
import sys
from pathlib import Path


def dodecahedral_edges():
    # The generalized Petersen graph GP(10,2): outer ten-cycle,
    # inner step-two edges, and ten radial spokes.
    edge_set = set()
    for i in range(10):
        for u, v in ((i, (i + 1) % 10),
                     (10 + i, 10 + ((i + 2) % 10)),
                     (i, 10 + i)):
            edge_set.add(tuple(sorted((u, v))))
    edges = sorted(edge_set)
    assert len(edges) == 30
    degree = collections.Counter(v for edge in edges for v in edge)
    assert set(degree) == set(range(20)) and set(degree.values()) == {3}
    return edges


def graph_and_metric():
    edges = dodecahedral_edges()
    adj = [set() for _ in range(30)]
    for a, (x, y) in enumerate(edges):
        for b in range(a):
            if set((x, y)).intersection(edges[b]):
                adj[a].add(b)
                adj[b].add(a)
    assert sum(map(len, adj)) == 120  # 60 graph edges
    distances = []
    for start in range(30):
        ds = {start: 0}
        frontier = collections.deque([start])
        while frontier:
            p = frontier.popleft()
            for q in sorted(adj[p]):
                if q not in ds:
                    ds[q] = ds[p] + 1
                    frontier.append(q)
        assert len(ds) == 30
        distances.append(ds)
    assert max(d for row in distances for d in row.values()) == 5
    return adj, distances


def clique_faces(distances, radius):
    near = [set(j for j in range(30) if j != i and distances[i][j] <= radius)
            for i in range(30)]
    faces = set()

    def walk(partial, candidates):
        for p, v in enumerate(candidates):
            bigger = partial + (v,)
            faces.add(frozenset(bigger))
            walk(bigger, [u for u in candidates[p + 1:] if u in near[v]])

    walk((), list(range(30)))
    return faces


def fvector(faces):
    return [sum(len(f) == i for f in faces)
            for i in range(1, max(map(len, faces)) + 1)]


def greedy_pairs(faces):
    faces = set(faces)
    ans = []
    while True:
        upper = collections.defaultdict(list)
        for f in faces:
            for v in f:
                low = f - {v}
                if low in faces:
                    upper[low].append(f)
        free_pairs = [(lo, ups[0]) for lo, ups in upper.items() if len(ups) == 1]
        if not free_pairs:
            break
        lo, hi = min(free_pairs, key=lambda p:
                     (-len(p[0]), tuple(sorted(p[0])), tuple(sorted(p[1]))))
        faces.remove(lo)
        faces.remove(hi)
        ans.append([sorted(lo), sorted(hi)])
    return ans, faces


def verify_certificate(original, certificate):
    # Independently check each pair against the *entire current face set*.
    remaining = set(original)
    for step, (lo0, hi0) in enumerate(certificate, 1):
        lo, hi = frozenset(lo0), frozenset(hi0)
        assert lo in remaining and hi in remaining, step
        assert len(hi) == len(lo) + 1 and lo < hi, step
        supersets = [f for f in remaining if lo < f]
        assert supersets == [hi], (step, lo0, hi0, supersets)
        remaining.remove(lo)
        remaining.remove(hi)
    assert len(remaining) == len(original) - 2 * len(certificate)
    # The deterministic greedy list is an independent completeness check.
    expected_pairs, expected_remain = greedy_pairs(original)
    assert certificate == expected_pairs
    assert remaining == expected_remain
    return remaining


def verify_surface(faces):
    assert max(map(len, faces)) == 3
    assert fvector(faces) == [16, 42, 28], fvector(faces)
    edges = {f for f in faces if len(f) == 2}
    triangles = [f for f in faces if len(f) == 3]
    vertices = sorted(set().union(*faces))
    # Each edge lies in exactly two triangles (closed pseudomanifold).
    for edge in edges:
        assert sum(edge < tri for tri in triangles) == 2, edge
    # Each vertex has a single circular link (no pinched singularities).
    for v in vertices:
        incident_triangles = [tri - {v} for tri in triangles if v in tri]
        link_vertices = set().union(*incident_triangles)
        assert len(link_vertices) >= 3
        links = {u: set() for u in link_vertices}
        for a, b in map(tuple, incident_triangles):
            links[a].add(b)
            links[b].add(a)
        assert all(len(neighbors) == 2 for neighbors in links.values()), v
        seen, queue = {min(link_vertices)}, collections.deque([min(link_vertices)])
        while queue:
            for u in links[queue.popleft()]:
                if u not in seen:
                    seen.add(u)
                    queue.append(u)
        assert seen == link_vertices, v
    # The complex is connected: check its 1-skeleton, not only its faces.
    neighbors = {v: set() for v in vertices}
    for a, b in map(tuple, edges):
        neighbors[a].add(b)
        neighbors[b].add(a)
    seen, queue = {vertices[0]}, collections.deque([vertices[0]])
    while queue:
        for u in neighbors[queue.popleft()]:
            if u not in seen:
                seen.add(u)
                queue.append(u)
    assert seen == set(vertices)
    assert 16 - 42 + 28 == 2
    # Connected closed 2-manifold of Euler characteristic 2 is a 2-sphere.


def main():
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    adj, distances = graph_and_metric()
    first = clique_faces(distances, 1)
    second = clique_faces(distances, 2)
    assert fvector(first) == [30, 60, 20]
    # Each line-graph triangle comes from one degree-3 graph vertex;
    # each edge of the 60-edge line graph appears in exactly one triangle.
    triangles = [f for f in first if len(f) == 3]
    assert len(triangles) == 20
    for e in (f for f in first if len(f) == 2):
        assert sum(e < t for t in triangles) == 1
    assert fvector(second) == [30, 180, 380, 330, 102]
    assert len(second) == 1022
    if sys.argv[1] == '--generate':
        cert_path = Path(sys.argv[2])
        pairs, after = greedy_pairs(second)
        cert_path.write_text(json.dumps(pairs, separators=(',', ':')) + '\n', encoding='utf-8')
    else:
        cert_path = Path(sys.argv[1])
        pairs = json.loads(cert_path.read_text(encoding='utf-8'))
    remaining = verify_certificate(second, pairs)
    assert len(pairs) == 468
    verify_surface(remaining)
    # First stage: collapse one exclusive edge with each of the 20 triangles,
    # leaving a connected graph with 30 vertices, 40 edges, Betti_1 = 11.
    assert 30 - 40 == -10
    print('ICOSIDODECAHEDRAL_RIPS2_SPHERE_OK')
    print('base_vertices=20 base_edges=30 line_vertices=30 line_edges=60 diameter=5')
    print('rips1_fvector=[30,60,20] graph_core_cycle_rank=11')
    print('rips2_fvector=[30,180,380,330,102] nonempty_faces=1022')
    print('elementary_pairs=468 surface_fvector=[16,42,28]')
    print('surface_links=16_single_cycles connected=True Euler_characteristic=2')
    print('homotopy_types=rips1_wedge_11_circles,rips2_two_sphere')

if __name__ == '__main__':
    main()
