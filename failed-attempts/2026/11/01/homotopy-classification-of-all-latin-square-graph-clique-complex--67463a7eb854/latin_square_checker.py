#!/usr/bin/env python3
"""Exact finite checks of the Latin-square-graph clique-complex theorem.

Run with Python 3.9+ and no third-party packages. Finite checks supplement,
not replace, the universal topological argument.
"""
from itertools import combinations, permutations
from collections import Counter


def cyclic(n):
    return [[(i + j) % n for j in range(n)] for i in range(n)]


def symmetric_three():
    p = list(permutations(range(3)))
    index = {v: i for i, v in enumerate(p)}
    return [[index[tuple(p[i][p[j][k]] for k in range(3))]
             for j in range(6)] for i in range(6)]


def verify_square(M):
    n = len(M)
    assert all(sorted(row) == list(range(n)) for row in M)
    assert all(sorted(M[i][j] for i in range(n)) == list(range(n))
               for j in range(n))
    verts = [(i, j) for i in range(n) for j in range(n)]
    labels = {v: t for t, v in enumerate(verts)}

    def adjacent(u, v):
        return u != v and (u[0] == v[0] or u[1] == v[1]
                           or M[u[0]][u[1]] == M[v[0]][v[1]])

    # Every extra symbol edge is homotopic through one genuine triangle
    # to a row edge followed by a column edge.
    diag_count = 0
    for u, v in combinations(verts, 2):
        if M[u[0]][u[1]] == M[v[0]][v[1]]:
            assert u[0] != v[0] and u[1] != v[1]
            t = (u[0], v[1])
            assert adjacent(u, t) and adjacent(t, v) and adjacent(u, v)
            diag_count += 1

    # Check the explicit disk filling of every rook rectangle.
    rect_count = 0
    six_disks = 0
    for i, k in combinations(range(n), 2):
        for j, ell in combinations(range(n), 2):
            a, b, c, d = (i, j), (i, ell), (k, ell), (k, j)
            if M[i][ell] == M[k][j]:
                tris = [(a, b, d), (b, c, d)]
            elif M[i][j] == M[k][ell]:
                tris = [(a, b, c), (a, c, d)]
            else:
                s = M[i][ell]
                h = next(z for z in range(n) if M[k][z] == s)
                m = next(z for z in range(n) if M[z][j] == s)
                e, f = (k, h), (m, j)
                assert len({a, b, c, d, e, f}) == 6
                tris = [(a, b, f), (b, f, e), (b, e, c),
                        (c, e, d), (d, e, f), (d, f, a)]
                six_disks += 1
            counts = Counter()
            for tr in tris:
                assert len(set(tr)) == 3
                assert all(adjacent(u, v) for u, v in combinations(tr, 2))
                for edge in combinations(tr, 2):
                    counts[frozenset(edge)] += 1
            assert all(z <= 2 for z in counts.values())
            boundary = {frozenset(z) for z in [(a, b), (b, c),
                                                (c, d), (d, a)]}
            assert {edge for edge, mult in counts.items() if mult == 1} == boundary
            nodes = set(v for tr in tris for v in tr)
            assert len(nodes) - len(counts) + len(tris) == 1
            for v in nodes:
                # Link of an interior vertex must be a connected circle;
                # link of a boundary vertex must be a connected interval.
                link = [frozenset(u for u in tr if u != v)
                        for tr in tris if v in tr]
                neighbors = set(u for edge in link for u in edge)
                degrees = Counter(u for edge in link for u in edge)
                assert all(degrees[u] in (1, 2) for u in neighbors)
                seen = {next(iter(neighbors))}
                frontier = list(seen)
                while frontier:
                    t = frontier.pop()
                    for edge in link:
                        if t in edge:
                            for u in edge:
                                if u not in seen:
                                    seen.add(u)
                                    frontier.append(u)
                assert seen == neighbors
                if v in (a, b, c, d):
                    assert sorted(degrees.values()).count(1) == 2
                else:
                    assert all(degrees[u] == 2 for u in neighbors)
            rect_count += 1

    # Enumerate the *entire* clique complex as maximal line simplices,
    # exceptional triangles, and exceptional intercalate tetrahedra.
    adjacency = [[adjacent(verts[i], verts[j]) for j in range(n * n)]
                 for i in range(n * n)]
    faces = [set() for _ in range(n + 1)]
    for i in range(n):
        for line in [[labels[(i, j)] for j in range(n)],
                     [labels[(j, i)] for j in range(n)],
                     [labels[(r, c)] for r in range(n) for c in range(n)
                      if M[r][c] == i]]:
            assert len(line) == n
            for size in range(1, n + 1):
                faces[size].update(combinations(sorted(line), size))
    for k in (3, 4):
        for t in combinations(range(n * n), k):
            if all(adjacency[u][v] for u, v in combinations(t, 2)):
                faces[k].add(t)
    # Independent Bron--Kerbosch maximal-clique enumeration: ensures that
    # no exceptional faces above dimension three were silently omitted.
    neighbors = [set(j for j in range(n * n) if adjacency[i][j])
                 for i in range(n * n)]
    maximal = []
    def bronk(r, p, x):
        if not p and not x:
            maximal.append(tuple(sorted(r)))
            return
        pivot = max(p | x, key=lambda v: len(p & neighbors[v])) if p or x else None
        for v in list(p - (neighbors[pivot] if pivot is not None else set())):
            bronk(r | {v}, p & neighbors[v], x & neighbors[v])
            p.remove(v)
            x.add(v)
    bronk(set(), set(range(n*n)), set())
    actual = [set() for _ in range(n+1)]
    for maxi in maximal:
        for size in range(1, len(maxi)+1):
            actual[size].update(combinations(maxi, size))
    assert actual == faces, (n, [len(z) for z in actual], [len(z) for z in faces])

    for k in range(2, n + 1):
        for t in faces[k]:
            for sub in combinations(t, k - 1):
                assert sub in faces[k - 1]

    # Exact boundary ranks over F_2 via bit-packed incremental elimination.
    ranks = {}
    for k in range(2, n + 1):
        basis = {}
        row_index = {simplex: t for t, simplex in enumerate(sorted(faces[k - 1]))}
        for t in sorted(faces[k]):
            col = 0
            for sub in combinations(t, k - 1):
                col ^= 1 << row_index[sub]
            while col:
                pivot = col.bit_length() - 1
                if pivot in basis:
                    col ^= basis[pivot]
                else:
                    basis[pivot] = col
                    break
        ranks[k - 1] = len(basis)
    f = [len(faces[i]) for i in range(1, n + 1)]
    rank_d1 = f[0] - 1  # connected: every row meets every column
    betti = {0: f[0] - rank_d1}
    for k in range(1, n):
        betti[k] = f[k] - (rank_d1 if k == 1 else ranks[k]) \
                   - (ranks[k + 1] if k + 1 < n else 0)
    intercalates = 0
    for i, k in combinations(range(n), 2):
        for j, ell in combinations(range(n), 2):
            if M[i][j] == M[k][ell] and M[i][ell] == M[k][j]:
                intercalates += 1
    assert betti[0] == 1
    assert betti[1] == 0
    assert betti[2] == (n - 1)**3 - intercalates
    assert all(betti[k] == 0 for k in range(3, n))
    assert sum((-1)**(k-1) * f[k-1] for k in range(1, n+1)) \
           == 1 + betti[2]
    return (f, ranks, betti, intercalates, diag_count, rect_count, six_disks)


def main():
    for name, M in [("cyclic_5", cyclic(5)),
                    ("cyclic_6", cyclic(6)),
                    ("nonabelian_S3_6", symmetric_three()),
                    ("cyclic_7", cyclic(7))]:
        f, ranks, betti, intercalates, diags, rects, disks = verify_square(M)
        print("{}: f={} boundary_ranks={} H_2_rank={} intercalates={} "
              "symbol_edges={} rook_rectangles={} six_triangle_disks={}".format(
                  name, f, ranks, betti[2], intercalates, diags, rects, disks))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
