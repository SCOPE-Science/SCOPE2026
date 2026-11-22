"""Finite checks for a single-edge fault in cubical graph-metric Rips complexes.

Uses only Python's standard library. Finite checks corroborate, but do not
replace, the all-dimensional proof given in the accompanying manuscript.
"""
from collections import deque
from math import comb


def cube_distances(n, remove_edge):
    total = 1 << n
    adjacent = [[] for _ in range(total)]
    for x in range(total):
        for bit in range(n):
            y = x ^ (1 << bit)
            if remove_edge and {x, y} == {0, 1}:
                continue
            adjacent[x].append(y)
    all_distances = []
    for x in range(total):
        distances = [-1] * total
        distances[x] = 0
        queue = deque([x])
        while queue:
            y = queue.popleft()
            for z in adjacent[y]:
                if distances[z] < 0:
                    distances[z] = distances[y] + 1
                    queue.append(z)
        assert -1 not in distances
        all_distances.append(distances)
    return all_distances


def faces_at_scale(distances, threshold=2):
    total = len(distances)
    adj = [{j for j in range(i + 1, total) if distances[i][j] <= threshold}
           for i in range(total)]
    faces = {}

    def recurse(prefix, choices):
        for i, vertex in enumerate(choices):
            face = prefix + (vertex,)
            faces.setdefault(len(face) - 1, []).append(face)
            recurse(face, [w for w in choices[i + 1:] if w in adj[vertex]])

    recurse((), list(range(total)))
    return faces


def gf2_rank(boundaries):
    pivots = {}
    for col in boundaries:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def homology_bettis(faces):
    ranks = {}
    for dim in sorted(faces):
        if dim == 0:
            continue
        previous = {face: j for j, face in enumerate(faces[dim - 1])}
        columns = []
        for face in faces[dim]:
            col = 0
            for j in range(len(face)):
                boundary = face[:j] + face[j + 1:]
                col ^= 1 << previous[boundary]
            columns.append(col)
        ranks[dim] = gf2_rank(columns)
    return {dim: len(group) - ranks.get(dim, 0) - ranks.get(dim + 1, 0)
            for dim, group in faces.items()}


def intact_c(n):
    return sum((j + 1) * ((1 << (n - 2)) - (1 << (i - 1)))
               for i in range(1, n) for j in range(i))


def check(n):
    d0 = cube_distances(n, False)
    d1 = cube_distances(n, True)
    differences = [(a, b, d0[a][b], d1[a][b])
                   for a in range(1 << n) for b in range(a + 1, 1 << n)
                   if d0[a][b] != d1[a][b]]
    assert differences == [(0, 1, 1, 3)], differences
    m = n - 1
    link_vertices = [1 << i for i in range(1, n)] + [1 | (1 << i) for i in range(1, n)]
    assert len(link_vertices) == 2 * m
    for i in range(len(link_vertices)):
        for j in range(i + 1, len(link_vertices)):
            actual = d0[link_vertices[i]][link_vertices[j]] <= 2
            expected = ((i < m and j < m) or (i >= m and j >= m)
                        or (i < m and j == i + m))
            assert actual == expected
    ranks = []
    counts = []
    for faulty in (False, True):
        faces = faces_at_scale(d1 if faulty else d0)
        betti = homology_bettis(faces)
        expected = intact_c(n) - (n - 2 if faulty else 0)
        assert betti[0] == 1
        assert betti.get(3, 0) == expected
        assert all(v == 0 for k, v in betti.items() if k not in (0, 3))
        ranks.append(expected)
        counts.append(tuple(len(faces.get(k, [])) for k in range(max(faces) + 1)))
    print(f'n={n}, original H3={ranks[0]}, fault H3={ranks[1]}, '
          f'loss={ranks[0]-ranks[1]}, intact f-vector={counts[0]}, '
          f'fault f-vector={counts[1]}')


if __name__ == '__main__':
    for dimension in range(3, 7):
        check(dimension)
    print('All finite metric, link and boundary-rank checks passed (n=3,4,5,6).')
