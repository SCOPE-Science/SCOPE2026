#!/usr/bin/env python3
"""Exact finite checks for the general-position complex of a ladder graph."""
from itertools import combinations
from math import comb


def distance(u, v):
    return abs(u[0] - v[0]) + (u[1] != v[1])


def is_gp(face):
    for a, b, c in combinations(face, 3):
        dab, dac, dbc = distance(a, b), distance(a, c), distance(b, c)
        if dab + dbc == dac or dab + dac == dbc or dac + dbc == dab:
            return False
    return True


def vertex_list(n):
    return [(i, row) for i in range(n) for row in (0, 1)]


def predicted_triangles(n):
    return {tuple(sorted(((i, row), (j, 1-row), (k, row))))
            for i, j, k in combinations(range(n), 3) for row in (0, 1)}


def rank_mod_p(n, p):
    verts = vertex_list(n)
    edges = list(combinations(verts, 2))
    indexed = {edge: index for index, edge in enumerate(edges)}
    pivots = {}
    triangles = predicted_triangles(n)
    for triangle in sorted(triangles):
        row = {indexed[edge]: (1 if j % 2 == 0 else -1) % p
               for j, edge in enumerate(combinations(triangle, 2))}
        while row:
            first = min(row)
            if first not in pivots:
                mult = pow(row[first], -1, p)
                pivots[first] = {k: (v*mult) % p for k, v in row.items() if v % p}
                break
            mult = row[first]
            for k, v in pivots[first].items():
                row[k] = (row.get(k, 0) - mult*v) % p
                if not row[k]:
                    row.pop(k)
    return len(pivots)


def expected_rank(n):
    if n == 2: return 0
    if n == 3: return 2
    return 2*n*(n-3)


def main():
    total_subsets = 0
    for n in range(2, 9):
        verts = vertex_list(n)
        expected = predicted_triangles(n)
        actual = set()
        three_count = 0
        for size in range(len(verts)+1):
            for subset in combinations(verts, size):
                total_subsets += 1
                valid = is_gp(subset)
                if valid and size > 3:
                    raise AssertionError(('higher face', n, subset))
                if valid and size == 3:
                    actual.add(subset)
                    three_count += 1
        assert actual == expected, ('triangles', n, len(actual), len(expected))
        assert three_count == 2*comb(n,3), (n,three_count)
    checks = 0
    for n in range(2, 14):
        for p in (2, 3, 101):
            rank = rank_mod_p(n, p)
            assert rank == expected_rank(n), (n, p, rank, expected_rank(n))
            E, V, T = comb(2*n, 2), 2*n, 2*comb(n,3)
            h1, h2 = E-V+1-rank, T-rank
            e1, e2 = ({2:3,3:8}.get(n,3*n+1),
                      0 if n<=5 else n*(n-4)*(n-5)//3)
            assert (h1,h2) == (e1,e2), (n,p,h1,h2,e1,e2)
            checks += 1
    print('VERIFY_OK full_subset_orders=2..8 examined_subsets=%d face_description=PASS'
          ' homology_orders=2..13 prime_fields=2,3,101 rank_checks=%d'
          ' exact_betti=PASS first_h2_order=6' % (total_subsets,checks))


if __name__ == '__main__':
    main()
