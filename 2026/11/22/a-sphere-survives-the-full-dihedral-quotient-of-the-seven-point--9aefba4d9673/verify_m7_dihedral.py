#!/usr/bin/env python3
"""Reproducible cell-collapse verification for a seven-label matching complex."""
from collections import Counter, defaultdict
from itertools import combinations

P = 7
EDGES = tuple(combinations(range(P), 2))
EDGE_ID = {edge: i for i, edge in enumerate(EDGES)}


def edge_transform(edge_id, translation, reflection):
    a, b = EDGES[edge_id]
    return EDGE_ID[tuple(sorted(((reflection * a + translation) % P,
                                 (reflection * b + translation) % P)))]


def disjoint(face):
    labels = [vertex for edge_id in face for vertex in EDGES[edge_id]]
    return len(labels) == len(set(labels))


FACES = {r: tuple(face for face in combinations(range(len(EDGES)), r)
                  if disjoint(face)) for r in (1, 2, 3)}
FACE_SET = {r: set(faces) for r, faces in FACES.items()}
GROUP = tuple((t, s) for s in (1, -1) for t in range(P))


def transformed(face, element):
    t, s = element
    return tuple(sorted(edge_transform(edge_id, t, s) for edge_id in face))


def canonical(chain):
    return min(tuple(transformed(face, element) for face in chain)
               for element in GROUP)


def build_chains():
    zero = [(face,) for r in (1, 2, 3) for face in FACES[r]]
    one = []
    two = []
    for small, large in ((1, 2), (1, 3), (2, 3)):
        one.extend((a, b) for a in FACES[small] for b in FACES[large]
                   if set(a).issubset(b))
    for c in FACES[3]:
        for b in combinations(c, 2):
            for a in b:
                two.append(((a,), b, c))
    return (zero, one, two)


def quotient_cells(chains):
    return tuple(tuple(sorted({canonical(c) for c in cells})) for cells in chains)


def connected(vertices, edges, endpoints):
    adjacency = {v: set() for v in vertices}
    for e in edges:
        a, b = endpoints[e]
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        v = todo.pop()
        for w in adjacency[v] - seen:
            seen.add(w)
            todo.append(w)
    return seen == set(vertices)


def certify():
    assert [len(FACES[r]) for r in (1, 2, 3)] == [21, 105, 105]
    original = build_chains()
    assert [len(c) for c in original] == [231, 840, 630]
    quotient = quotient_cells(original)
    assert [len(c) for c in quotient] == [26, 72, 48]
    idmap = [{cell: i for i, cell in enumerate(cells)} for cells in quotient]
    ends = {}
    for e, chain in enumerate(quotient[1]):
        a, b = (idmap[0][canonical((face,))] for face in chain)
        assert a != b
        ends[e] = (a, b)
    sides = {}
    for f, chain in enumerate(quotient[2]):
        edge_ids = tuple(idmap[1][canonical(chain[:i] + chain[i+1:])]
                         for i in range(3))
        assert len(set(edge_ids)) == 3
        sides[f] = frozenset(edge_ids)
        tri_vertices = set(v for e in edge_ids for v in ends[e])
        assert len(tri_vertices) == 3
    assert connected(set(range(26)), set(range(72)), ends)
    # Equivariant cross-check: all reflections fix 19/24/6 ordered chains.
    for dimension, cells in enumerate(original):
        nfix = sum(tuple(transformed(face, (0, -1)) for face in chain) == chain
                   for chain in cells)
        assert nfix == (19, 24, 6)[dimension]

    vertices = set(range(26))
    edges = set(range(72))
    triangles = set(range(48))
    collapse_pairs = []
    while True:
        frequencies = defaultdict(list)
        for f in triangles:
            for e in sides[f]:
                assert e in edges
                frequencies[e].append(f)
        available_2 = [(e, incident[0]) for e, incident in frequencies.items()
                       if len(incident) == 1]
        if available_2:
            e, f = min(available_2)
            edges.remove(e)
            triangles.remove(f)
            collapse_pairs.append((2, e, f))
            continue
        incident_edges = defaultdict(list)
        for e in edges:
            a, b = ends[e]
            assert a in vertices and b in vertices
            incident_edges[a].append(e)
            incident_edges[b].append(e)
        available_1 = [(v, inc[0]) for v, inc in incident_edges.items()
                       if len(inc) == 1]
        if available_1:
            v, e = min(available_1)
            vertices.remove(v)
            edges.remove(e)
            collapse_pairs.append((1, v, e))
            continue
        break
    assert Counter(d for d, _, _ in collapse_pairs) == {2: 18, 1: 9}
    expected_pairs = [
        (2, 3, 2), (2, 9, 7), (2, 15, 0), (2, 0, 1),
        (2, 1, 13), (2, 2, 5), (2, 19, 24), (2, 21, 45),
        (2, 40, 27), (2, 45, 17), (2, 31, 26), (2, 39, 25),
        (2, 34, 19), (2, 46, 40), (2, 58, 35), (2, 59, 36),
        (2, 56, 34), (2, 57, 38),
        (1, 1, 16), (1, 2, 26), (1, 3, 38), (1, 9, 69),
        (1, 16, 50), (1, 20, 49), (1, 18, 64),
        (1, 23, 68), (1, 24, 71),
    ]
    assert collapse_pairs == expected_pairs
    assert (len(vertices), len(edges), len(triangles)) == (17, 45, 30)
    assert connected(vertices, edges, ends)
    edge_degrees = Counter(e for f in triangles for e in sides[f])
    assert set(edge_degrees) == edges
    assert all(edge_degrees[e] == 2 for e in edges)
    # Link graph at vertex v: vertices are incident original edges;
    # each remaining triangle contributes a link edge between the two sides
    # meeting at v. Multiple link edges are retained (2-gon links occur).
    link_lengths = Counter()
    for v in vertices:
        linked_vertices = {e for e in edges if v in ends[e]}
        link_edges = []
        for f in triangles:
            inc = [e for e in sides[f] if v in ends[e]]
            if inc:
                assert len(inc) == 2
                link_edges.append(tuple(inc))
        assert len(link_edges) == len(linked_vertices)
        degrees = Counter(x for pair in link_edges for x in pair)
        assert set(degrees) == linked_vertices
        assert all(degrees[x] == 2 for x in linked_vertices)
        adjacency = defaultdict(set)
        for a, b in link_edges:
            assert a != b
            adjacency[a].add(b)
            adjacency[b].add(a)
        seen = {next(iter(linked_vertices))}
        stack = list(seen)
        while stack:
            for x in adjacency[stack.pop()] - seen:
                seen.add(x)
                stack.append(x)
        assert seen == linked_vertices
        link_lengths[len(linked_vertices)] += 1
    assert link_lengths == {2: 3, 4: 6, 6: 5, 10: 3}
    assert len(vertices) - len(edges) + len(triangles) == 2
    print('M7_D7_QUOTIENT_COLLAPSES_TO_SPHERE_OK')
    print('matching_faces=21,105,105; barycentric_cells=231,840,630')
    print('quotient_cells=26,72,48; collapses=(2,18),(1,9)')
    print('sphere_cells=17,45,30; link_sizes=' + repr(dict(sorted(link_lengths.items()))))
    return True


if __name__ == '__main__':
    certify()
