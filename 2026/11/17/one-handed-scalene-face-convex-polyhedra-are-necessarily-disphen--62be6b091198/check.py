#!/usr/bin/env python3
"""Finite oriented-edge incidence checks for triangular polyhedra.

These checks test small examples only. The all-dimensional/face-count
rigidity statement follows from the separate geometric argument.
"""
from itertools import combinations


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def oriented_triangular_facets(vertices):
    result = []
    for i, j, k in combinations(range(len(vertices)), 3):
        normal = cross(sub(vertices[j], vertices[i]),
                       sub(vertices[k], vertices[i]))
        if dot(normal, normal) == 0:
            continue
        signs = [dot(normal, sub(v, vertices[i]))
                 for n, v in enumerate(vertices) if n not in (i, j, k)]
        if all(s < 0 for s in signs):
            result.append((i, j, k))
        elif all(s > 0 for s in signs):
            result.append((i, k, j))
    return sorted(result)


def edge(i, j):
    return tuple(sorted((i, j)))


def oriented_face_edges(f):
    a, b, c = f
    return (edge(a, b), edge(b, c), edge(c, a))


CYCLIC = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
REVERSE = ((0, 2, 1), (2, 1, 0), (1, 0, 2))


def compatible_labelings(faces):
    """Enumerate globally consistent edge 3-colorings with every face 012."""
    labeled = []
    assignments = {}

    def walk(t):
        if t == len(faces):
            labeled.append(assignments.copy())
            return
        tri = oriented_face_edges(faces[t])
        for colors in CYCLIC:
            if any(e in assignments and assignments[e] != c
                   for e, c in zip(tri, colors)):
                continue
            new = [(e, c) for e, c in zip(tri, colors) if e not in assignments]
            assignments.update(new)
            walk(t + 1)
            for e, _ in new:
                del assignments[e]

    walk(0)
    return labeled


def main():
    tetra = [(1, 2, 3), (1, -2, -3), (-1, 2, -3), (-1, -2, 3)]
    octa = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
            (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    ft = oriented_triangular_facets(tetra)
    fo = oriented_triangular_facets(octa)
    assert len(ft) == 4 and len(fo) == 8
    squared_lengths = {edge(i, j): dot(sub(tetra[i], tetra[j]),
                                      sub(tetra[i], tetra[j]))
                       for i, j in combinations(range(4), 2)}
    values = sorted(set(squared_lengths.values()))
    assert len(values) == 3
    actual = {e: values.index(v) for e, v in squared_lengths.items()}
    words = [tuple(actual[e] for e in oriented_face_edges(f)) for f in ft]
    assert all(w in CYCLIC for w in words) or all(w in REVERSE for w in words)
    assert len(compatible_labelings(ft)) == 3
    assert len(compatible_labelings(fo)) == 0
    print('PASS: disphenoid has four uniformly handed faces')
    print('PASS: tetrahedral triangulation admits three oriented edge-colorings')
    print('PASS: octahedral triangulation admits zero oriented edge-colorings')
    print('These finite checks do not establish the general convex rigidity theorem.')


if __name__ == '__main__':
    main()
