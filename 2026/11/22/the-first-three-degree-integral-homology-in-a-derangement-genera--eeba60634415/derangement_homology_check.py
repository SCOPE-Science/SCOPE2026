#!/usr/bin/env python3
"""Exact integral homology certificate for derangement-generated word complexes.

Uses only the Python standard library. All matrices have integer entries.
A unit pivot is a unimodular Smith reduction, so successful reduction to a
zero residual matrix proves all nonzero Smith factors are one.
"""
from collections import defaultdict
from itertools import combinations, permutations


def faces(n):
    derangements = [p for p in permutations(range(1, n + 1))
                    if all(x != i for i, x in enumerate(p, 1))]
    levels = []
    for k in range(1, n + 1):
        levels.append(sorted({tuple(p[i] for i in indices)
                              for p in derangements
                              for indices in combinations(range(n), k)}))
    return derangements, levels


def columns(levels, k):
    # Boundary C_k -> C_(k-1); k>=1, with 0-based cell degrees.
    indices = {word: i for i, word in enumerate(levels[k - 1])}
    return [{indices[word[:j] + word[j+1:]]: (-1) ** j
             for j in range(k + 1)} for word in levels[k]]


def check_square_zero(levels):
    for k in range(2, len(levels)):
        lower = columns(levels, k-1)
        upper = columns(levels, k)
        for col in upper:
            total = defaultdict(int)
            for i, coefficient in col.items():
                for j, second in lower[i].items():
                    total[j] += coefficient * second
            assert all(x == 0 for x in total.values()), (k, col)


def integral_unit_rank(matrix):
    # Integer Gauss--Jordan elimination using only +/-1 pivots.
    # Choosing a pivot a=+/-1, we replace every other matrix entry
    # B_ij by B_ij-B_i,pivotCol * a * B_pivotRow,j. This is an integral
    # unimodular equivalence and splits off a 1x1 block [a].
    C = {j: column.copy() for j, column in enumerate(matrix)}
    R = defaultdict(dict)
    for j, column in C.items():
        for i, value in column.items():
            assert isinstance(value, int) and value != 0
            R[i][j] = value
    rank = 0
    while True:
        best = None
        best_cost = None
        for i in sorted(R):
            row = R[i]
            for j in sorted(row):
                a = row[j]
                if abs(a) == 1:
                    cost = (len(row)-1)*(len(C[j])-1)
                    key = (cost, i, j)
                    if best_cost is None or key < best_cost:
                        best = (i, j, a)
                        best_cost = key
                    if cost == 0:
                        break
            if best_cost is not None and best_cost[0] == 0:
                break
        if best is None:
            break
        i, j, a = best
        row = R[i].copy()
        col = C[j].copy()
        for other_i, coefficient in col.items():
            if other_i == i:
                continue
            other_row = R[other_i]
            for other_j, row_coefficient in row.items():
                if other_j == j:
                    continue
                new = other_row.get(other_j, 0)-coefficient*a*row_coefficient
                if new:
                    other_row[other_j] = new
                    C[other_j][other_i] = new
                else:
                    other_row.pop(other_j, None)
                    C[other_j].pop(other_i, None)
        for other_i in col:
            R[other_i].pop(j, None)
        for other_j in row:
            C[other_j].pop(i, None)
        del R[i]
        del C[j]
        rank += 1
    assert not any(C.values()), 'Unit reduction left a nonzero block'
    return rank


def modular_rank(matrix, prime):
    # Independent finite-field implementation for crosschecking rank.
    pivots = {}
    for original in matrix:
        c = {i: value % prime for i, value in original.items()
             if value % prime}
        while c:
            i = max(c)
            if i not in pivots:
                inv = pow(c[i], -1, prime)
                pivots[i] = {j: v*inv % prime for j, v in c.items()}
                break
            factor = c[i]
            for j, v in pivots[i].items():
                new = (c.get(j, 0)-factor*v) % prime
                if new:
                    c[j] = new
                else:
                    c.pop(j, None)
    return len(pivots)


def run(n):
    generators, levels = faces(n)
    check_square_zero(levels)
    ranks = [0]
    for k in range(1, n):
        matrix = columns(levels, k)
        exact = integral_unit_rank(matrix)
        assert exact == modular_rank(matrix, 2)
        assert exact == modular_rank(matrix, 3)
        assert exact == modular_rank(matrix, 101)
        ranks.append(exact)
    ranks.append(0)
    counts = [len(x) for x in levels]
    reduced_betti = [counts[k]-ranks[k]-ranks[k+1]-(1 if k == 0 else 0)
                     for k in range(n)]
    assert all(x >= 0 for x in reduced_betti)
    assert sum((-1)**k*counts[k] for k in range(n))-1 == \
        sum((-1)**k*reduced_betti[k] for k in range(n))
    return len(generators), counts, ranks[1:-1], reduced_betti


if __name__ == '__main__':
    expected = {
        2: ([2,1], [1], [0,0]),
        3: ([3,5,2], [2,2], [0,1,0]),
        4: ([4,12,20,9], [3,9,8], [0,0,3,1]),
        5: ([5,20,59,97,44], [4,16,43,41], [0,0,0,13,3]),
        6: ([6,30,120,351,574,265], [5,25,95,255,245], [0,0,0,1,74,20]),
    }
    for n in range(2,7):
        generators, counts, ranks, betti = run(n)
        assert (counts, ranks, betti) == expected[n], n
        print(f'n={n} derangements={generators} C_counts={counts} boundary_ranks={ranks} reduced_integral_betti={betti}')
    print('PASS: exact unit-Smith reductions, boundary squares, modular ranks, Euler identities, and first three-degree threshold')
