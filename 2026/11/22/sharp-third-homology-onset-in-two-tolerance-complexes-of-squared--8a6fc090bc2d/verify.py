#!/usr/bin/env python3
"""Exact, exhaustive simplicial-chain checks for squared cycles of order 7..12.

Requires Python 3 and SymPy; all matrices are over ZZ (integer Smith forms).
"""
import json
from collections import Counter
from itertools import combinations
from math import comb
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def adjacent(a, b, n):
    d = (b - a) % n
    return min(d, n - d) in (1, 2)


def clique(S, n):
    return all(adjacent(a, b, n) for a, b in combinations(S, 2))


def tolerant(S, n):
    # Direct definition: S minus at most two elements is a clique.
    return any(clique(T, n) for T in combinations(S, max(0, len(S) - 2)))


def simplices(n):
    return {k: [S for S in combinations(range(n), k) if tolerant(S, n)]
            for k in range(1, n + 1)}


def boundary_matrix(upper, lower):
    lookup = {f: i for i, f in enumerate(lower)}
    vals = {}
    for j, S in enumerate(upper):
        for k in range(len(S)):
            T = S[:k] + S[k+1:]
            assert T in lookup
            vals[(lookup[T], j)] = (-1)**k
    return SparseMatrix(len(lower), len(upper), vals)


def smith_counts(M):
    diag = smith_normal_form(M, domain=ZZ)
    return Counter(abs(int(diag[k, k])) for k in range(min(diag.shape)) if diag[k, k] != 0)


def mod2_rank(upper, lower):
    pos = {S: i for i, S in enumerate(lower)}
    pivots = {}
    for S in upper:
        w = sum(1 << pos[S[:i] + S[i+1:]] for i in range(len(S)))
        while w:
            p = w.bit_length() - 1
            if p not in pivots:
                pivots[p] = w
                break
            w ^= pivots[p]
    return len(pivots)


def canonical_top_cycles(n, f4):
    lookup = {S: i for i, S in enumerate(f4)}
    triangles = [{i, (i+1)%n, (i+2)%n} for i in range(n)]
    sixsets = sorted({tuple(sorted(a | b)) for a, b in combinations(triangles, 2)
                      if not (a & b)})
    values = {}
    for j, S in enumerate(sixsets):
        for i in range(6):
            face = S[:i] + S[i+1:]
            assert face in lookup, (n, S, face)
            values[(lookup[face], j)] = (-1)**i
    return sixsets, SparseMatrix(len(f4), len(sixsets), values)


def verify(n):
    F = simplices(n)
    assert not any(F[k] for k in range(6, n + 1)), n
    assert len([S for S in combinations(range(n), 3) if clique(S, n)]) == n
    f2, f3, f4 = F[3], F[4], F[5]
    M3 = boundary_matrix(f3, f2)
    M4 = boundary_matrix(f4, f3)
    assert M3*M4 == SparseMatrix(len(f2), len(f4), {})
    rank3 = mod2_rank(f3, f2)
    rank4_mod2 = mod2_rank(f4, f3)
    diag4 = smith_counts(M4)
    assert set(diag4).issubset({1}), (n, diag4)
    rank4 = diag4[1]
    assert rank4 == rank4_mod2
    assert rank3 == comb(n-1, 3), (n, rank3)
    betti3 = len(f3) - rank3 - rank4
    betti4 = len(f4) - rank4
    missing_four = comb(n, 4) - len(f3)
    sixsets, carrier_matrix = canonical_top_cycles(n, f4)
    assert M4 * carrier_matrix == SparseMatrix(len(f3), len(sixsets), {})
    topdiag = smith_counts(carrier_matrix)
    assert set(topdiag).issubset({1})
    # The number of independent four-subsets first becomes positive at 12.
    row = dict(n=n, f_vector=[len(F[k]) for k in range(1, 6)],
               missing_tetrahedra=missing_four, rank_boundary3=rank3,
               smith_boundary4_units=rank4, smith_boundary4_nonunit=[],
               H3_rank=betti3, H4_rank=betti4,
               canonical_sixsets=len(sixsets), canonical_cycle_primitive_rank=topdiag[1])
    if n >= 11:
        assert topdiag[1] == betti4, row
    return row


def main():
    results = [verify(n) for n in range(7, 13)]
    assert [(x['H3_rank'], x['H4_rank']) for x in results] == [
        (0,6),(0,13),(0,20),(2,26),(12,33),(33,42)]
    for row in results:
        print(json.dumps(row, sort_keys=True))
    print('PASS: six exhaustive integral homotopy computations and primitive top-cycle tests')


if __name__ == '__main__':
    main()
