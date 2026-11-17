#!/usr/bin/env python3
"""Independent finite checks for two-clear-geodesic visibility complexes of K_{n,n,n}."""
from itertools import combinations
from collections import defaultdict


def cover_faces(n):
    ground = range(3 * n)
    faces = {()}
    for shore in range(3):
        own = list(range(shore * n, (shore + 1) * n))
        outside = [v for v in ground if v not in own]
        for count in range(n - 1):
            for chosen in combinations(own, count):
                faces.add(chosen)
                for v in outside:
                    faces.add(tuple(sorted(chosen + (v,))))
    return faces


def exhaustive_dual(n):
    """Complement of faces satisfying a direct two-geodesic test in the graph."""
    N = 3 * n
    adjacency = [set(j for j in range(N) if j // n != i // n) for i in range(N)]
    dual = set()
    for absent_mask in range(1 << N):
        present = set(range(N)) - {v for v in range(N) if absent_mask >> v & 1}
        valid = True
        for i in range(3):
            nodes = [u for u in present if u // n == i]
            for u, v in combinations(nodes, 2):
                # In a complete tripartite graph all shortest u-v paths have length two.
                clear_internals = (adjacency[u] & adjacency[v]) - present
                if len(clear_internals) < 2:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            dual.add(tuple(v for v in range(N) if absent_mask >> v & 1))
    return dual


def rank_mod_two(columns):
    pivots = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def reduced_betti_mod_two(faces):
    levels = defaultdict(list)
    for face in faces:
        levels[len(face)-1].append(face)
    ranks = {}
    for dimension in sorted(levels):
        if dimension <= 0:
            continue
        row_index = {face: index for index, face in enumerate(levels[dimension - 1])}
        boundary_columns = []
        for face in levels[dimension]:
            column = 0
            for index in range(len(face)):
                column ^= (1 << row_index[face[:index] + face[index+1:]])
            boundary_columns.append(column)
        ranks[dimension] = rank_mod_two(boundary_columns)
    betti = {d:len(levels[d]) - ranks.get(d,0) - ranks.get(d+1,0)
             for d in levels if d >= 0}
    betti[0] -= 1
    return {degree: count for degree, count in sorted(betti.items()) if count}, \
           tuple(len(levels[d]) for d in range(max(levels) + 1))


def main():
    for n in (5, 6):
        combinatorial_faces = cover_faces(n)
        geodesic_faces = exhaustive_dual(n)
        assert combinatorial_faces == geodesic_faces
        actual, fvector = reduced_betti_mod_two(combinatorial_faces)
        expected = {1:1, 2:3*(n-1)**2, n-2:3*(n-1)*(2*n-1)}
        assert actual == expected, (n, actual, expected)
        print('n={} dual_faces={} fvector={} reduced_F2_betti={} PASS'.format(
            n, len(combinatorial_faces)-1, fvector, sorted(actual.items())))
    print('TRIPARTITE_TWO_PATH_INTEGRAL_HOMOLOGY_FINITE_CHECK_PASS')


if __name__ == '__main__':
    main()
