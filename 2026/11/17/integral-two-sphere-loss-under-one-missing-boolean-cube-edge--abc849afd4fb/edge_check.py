"""Direct finite checks of open-neighborhood complexes after a cube edge deletion.

Run with Python 3: python check_edge_puncture.py
This enumerates finite simplicial faces and computes binary boundary ranks;
it does not replace the all-dimensional integral homotopy argument.
"""
from itertools import combinations
from math import comb


def boundary_rank(columns):
    pivots = {}
    for column in columns:
        x = column
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def complex_faces(n, parity, remove_edge):
    faces = [set() for _ in range(n + 1)]
    for center in range(1 << n):
        if center.bit_count() % 2 == parity:
            continue
        verts = [center ^ (1 << j) for j in range(n)]
        if remove_edge and center in (0, 1):
            verts.remove(1 if center == 0 else 0)
        verts.sort()
        for size in range(1, len(verts) + 1):
            faces[size].update(combinations(verts, size))
    return faces


def betti_0_1_2(faces):
    vertices = sorted(faces[1])
    edges = sorted(faces[2])
    triangles = sorted(faces[3])
    tetrahedra = sorted(faces[4]) if len(faces) > 4 else []
    i0 = {v: i for i, v in enumerate(vertices)}
    i1 = {e: i for i, e in enumerate(edges)}
    i2 = {t: i for i, t in enumerate(triangles)}
    r1 = boundary_rank(sum(1 << i0[(v,)] for v in edge) for edge in edges)
    r2 = boundary_rank(sum(1 << i1[e] for e in combinations(t, 2)) for t in triangles)
    r3 = boundary_rank(sum(1 << i2[t] for t in combinations(tet, 3)) for tet in tetrahedra)
    return (len(vertices) - r1, len(edges) - r1 - r2, len(triangles) - r2 - r3)


def expected_sphere_count(n):
    return (1 << (n-3)) * (n * n - 5 * n + 8) - 1 - (n - 2)


def main():
    total = 0
    for n in range(3, 9):
        expected = expected_sphere_count(n)
        values = []
        for parity in (0, 1):
            face_sets = complex_faces(n, parity, True)
            counts = [len(s) for s in face_sets]
            assert counts[1] == (1 << (n-1))
            assert counts[2] == (1 << (n-2)) * comb(n, 2)
            for k in range(3, n + 1):
                assert counts[k] == ((1 << (n-1)) - 1) * comb(n, k) + comb(n-1, k)
            assert sum((-1)**(k-1) * counts[k] for k in range(1, n+1)) - 1 == expected
            b0, b1, b2 = betti_0_1_2(face_sets)
            assert (b0, b1, b2) == (1, 0, expected), (n, parity, b0, b1, b2)
            values.append((b0, b1, b2))
            total += sum(counts[1:])
        # Translation by the deleted edge maps the parity sheets simplicially.
        for k in range(1, n+1):
            ev = complex_faces(n, 0, True)[k]
            odd = complex_faces(n, 1, True)[k]
            assert {tuple(sorted(v ^ 1 for v in face)) for face in ev} == odd
        print(f"n={n} each parity: b0=1 b1=0 b2={expected}; face counts and parity symmetry PASS")
    print(f"PASS: 12 parity components, {total} nonempty faces, direct mod-2 boundary computations")


if __name__ == '__main__':
    main()
