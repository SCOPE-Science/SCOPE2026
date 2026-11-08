#!/usr/bin/env python3
"""Exhaustive exact checker for the Hesse pencil chamber-support polynomial.

Requires only Python 3 standard library. The two enumerations use different
criteria: local incidence obstructions and exact positive-definite matrices.
"""
from collections import Counter
from fractions import Fraction

POINTS = [(a, b) for a in range(3) for b in range(3)]
LINES = []
for slope in range(4):
    for value in range(3):
        subset = 0
        for index, (a, b) in enumerate(POINTS):
            coordinate = (a, b, (b-a) % 3, (a+b) % 3)[slope]
            if coordinate == value:
                subset |= 1 << index
        LINES.append(subset)
assert len(set(LINES)) == 12
assert all(v.bit_count() == 3 for v in LINES)
assert all(sum(bool(v & (1 << i)) for v in LINES) == 4 for i in range(9))

# Full intersection matrix, ordered as nine exceptional sections E_p followed
# by twelve components L_i of the four reducible fibers of type I_3.
# Store minus the intersection form, for positive-definiteness testing.
Q = [[0] * 21 for _ in range(21)]
for i in range(21):
    Q[i][i] = 1 if i < 9 else 2
    for j in range(i):
        if i < 9 and j < 9:
            entry = 0
        elif i >= 9 and j >= 9:
            entry = -int((i - 9) // 3 == (j - 9) // 3)
        else:
            section = i if i < 9 else j
            line = (i if i >= 9 else j) - 9
            entry = -int(bool(LINES[line] & (1 << section)))
        Q[i][j] = Q[j][i] = entry


def positive_definite(subset):
    """Exact rational Schur elimination, no floats or eigenvalue tolerances."""
    n = len(subset)
    mat = [[Fraction(Q[subset[i]][subset[j]]) for j in range(n)]
           for i in range(n)]
    for j in range(n):
        pivot = mat[j][j]
        if pivot <= 0:
            return False
        for k in range(j + 1, n):
            for h in range(k, n):
                mat[h][k] = mat[k][h] = (
                    mat[h][k] - mat[k][j] * mat[h][j] / pivot
                )
    return True


def graph_ok(section_mask, line_mask):
    """Criterion from the four affine A_2 triangles and (-1)-section stars."""
    chosen = [j for j in range(12) if (line_mask >> j) & 1]
    for fiber in range(4):
        local = [j for j in range(3*fiber, 3*fiber+3)
                 if (line_mask >> j) & 1]
        if len(local) == 3:
            return False
        if len(local) == 2 and (
            section_mask & (LINES[local[0]] | LINES[local[1]])
        ).bit_count() >= 2:
            return False
    if any((section_mask & LINES[j]).bit_count() >= 2 for j in chosen):
        return False
    if any(sum(bool(LINES[j] & (1 << i)) for j in chosen) >= 2
           for i in range(9) if (section_mask >> i) & 1):
        return False
    return True


def count_by_graph():
    result = Counter()
    visited = 0
    for line_mask in range(1 << 12):
        for section_mask in range(1 << 9):
            visited += 1
            if graph_ok(section_mask, line_mask):
                result[section_mask.bit_count()+line_mask.bit_count()] += 1
    assert visited == 1 << 21
    return result


def count_by_exact_matrix():
    # Independent backtracking using nothing from graph_ok. Every negative
    # definite principal submatrix appears exactly once because every one
    # of its principal submatrices is negative definite.
    result = Counter({0: 1})
    candidate_checks = 0

    def explore(selected, last):
        nonlocal candidate_checks
        for nxt in range(last + 1, 21):
            candidate = selected + (nxt,)
            candidate_checks += 1
            if positive_definite(candidate):
                result[len(candidate)] += 1
                explore(candidate, nxt)

    explore((), -1)
    return result, candidate_checks


def main():
    graph = count_by_graph()
    matrix, checks = count_by_exact_matrix()
    assert graph == matrix, (graph, matrix)
    expected = [1, 21, 210, 1236, 4497, 10308,
                14772, 12612, 5634, 874]
    assert [graph[k] for k in range(10)] == expected
    assert not any(k > 9 for k in graph)
    assert sum(expected) == 50165
    print('Incidence graph: 9 points, 12 lines, four parallel classes')
    print('Subsets checked by graph criterion:', 1 << 21)
    print('Exact positive-definiteness candidate tests:', checks)
    print('Coefficients, including nef chamber:', expected)
    print('Largest support size:', max(graph))
    print('Chambers in largest support size:', graph[max(graph)])
    print('Total Zariski chambers:', sum(graph.values()))
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
