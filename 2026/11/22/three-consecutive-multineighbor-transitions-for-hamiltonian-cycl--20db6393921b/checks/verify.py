#!/usr/bin/env python3
"""Standalone finite corroboration of the three-stage cyclic two-factor-neighborhood theorem.
Run: python3 checks/verify.py
All computations use Python standard library and exact bit arithmetic.
"""
from itertools import combinations
from math import comb


def graph_neighbors(n):
    """Adjacency sets for K_(n,n) without edges a_i b_i and a_i b_(i+1)."""
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if j not in (i, (i + 1) % n):
                adj[i].add(n + j)
                adj[n + j].add(i)
    return adj


def all_faces(n, m):
    """Independently compute one-shore faces from graph common-neighbor intersection."""
    adj = graph_neighbors(n)
    faces = [[] for _ in range(n + 1)]
    for s in range(1, 1 << n):
        support = [i for i in range(n) if (s >> i) & 1]
        neighbors = set(adj[support[0]])
        for i in support[1:]:
            neighbors.intersection_update(adj[i])
        if len(neighbors) >= m:
            faces[s.bit_count()].append(s)
    # Any mixed nonempty pair has no common neighbor in a simple bipartite graph.
    for i in range(n):
        for j in range(n, 2 * n):
            assert not (adj[i] & adj[j])
    return faces


def gf2_rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            hi = vector.bit_length() - 1
            if hi in pivots:
                vector ^= pivots[hi]
            else:
                pivots[hi] = vector
                break
    return len(pivots)


def betti(faces):
    max_s = max(i for i, a in enumerate(faces) if a)
    boundary_rank = [0] * (max_s + 2)  # boundary_rank[k] = rank(C_(k-1)->C_(k-2))
    for k in range(2, max_s + 1):
        rows = {s: i for i, s in enumerate(faces[k - 1])}
        vectors = []
        for simplex in faces[k]:
            col = 0
            bitset = simplex
            while bitset:
                bit = bitset & -bitset
                bitset -= bit
                col ^= 1 << rows[simplex ^ bit]
            vectors.append(col)
        boundary_rank[k] = gf2_rank(vectors)
    ans = {}
    for k in range(1, max_s + 1):
        rank = len(faces[k]) - boundary_rank[k] - boundary_rank[k + 1]
        if k == 1:
            rank -= 1  # reduced H_0 (all tested complexes connected)
        if rank:
            ans[k - 1] = rank
    return ans


def cycle_chain(n, edges):
    index = {f: i for i, f in enumerate(edges)}
    result = 0
    for i in range(n):
        edge = (1 << i) | (1 << ((i + 1) % n))
        result ^= 1 << index[edge]
    return result


def boundary_columns(triangles, edges):
    index = {f: i for i, f in enumerate(edges)}
    cols = []
    for tri in triangles:
        col = 0
        for i in range(tri.bit_length()):
            if (tri >> i) & 1:
                col ^= 1 << index[tri ^ (1 << i)]
        cols.append(col)
    return cols


def span_rank_plus(cols, extra):
    return gf2_rank(cols + [extra]) - gf2_rank(cols)


def run():
    for n in range(7, 12):
        for t in (3, 4, 5):
            m = n - t
            faces = all_faces(n, m)
            fvector = tuple(len(a) for a in faces[1:] if a)
            if t == 3:
                assert fvector == (n, n)
                expected = {1: 1}
            elif t == 4:
                assert fvector == (n, comb(n, 2), n)
                expected = {1: comb(n, 2) - 2 * n + 1}
            else:
                assert fvector == (n, comb(n, 2), n * (n - 3), n)
                expected = {2: n * (n - 5) // 2 - 1}
                # All n maximal tetrahedra each have a specified unique triangular free face.
                tetra = [set((i + j) % n for j in range(4)) for i in range(n)]
                tetra_sets = {frozenset(s) for s in tetra}
                assert len(tetra_sets) == n
                for i in range(n):
                    special = {(i + j) % n for j in (0, 1, 3)}
                    assert sum(special <= s for s in tetra) == 1
            observed = betti(faces)
            assert observed == expected, (n, t, observed, expected)
            cycle = cycle_chain(n, faces[2])
            columns = boundary_columns(faces[3], faces[2]) if len(faces) > 3 else []
            if t == 4:
                assert span_rank_plus(columns, cycle) == 1
            if t == 5:
                assert span_rank_plus(columns, cycle) == 0
            print(f'n={n} m={m} shore_f={fvector} reduced_F2_betti={observed} checks=OK')
    print('CYCLIC_MULTINEIGHBOR_THREE_STAGE_OK')

if __name__ == '__main__':
    run()
