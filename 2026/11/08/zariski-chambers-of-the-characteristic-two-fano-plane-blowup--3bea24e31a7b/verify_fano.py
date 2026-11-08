#!/usr/bin/env python3
"""Exact chamber-support count for the blowup of the Fano plane points."""
from fractions import Fraction

POINTS = tuple(range(1, 8))
LINES = tuple(range(1, 8))
# Nonzero binary vectors represent projective points and dual lines.
INCIDENCE = [[int((i & j).bit_count() % 2 == 0) for j in LINES]
             for i in POINTS]
assert all(sum(row) == 3 for row in INCIDENCE)
assert all(sum(INCIDENCE[i][j] for i in range(7)) == 3 for j in range(7))
assert all(sum(INCIDENCE[i][j] * INCIDENCE[k][j] for j in range(7)) == 1
           for i in range(7) for k in range(i+1, 7))

# Full curve-intersection matrix E_1,...,E_7,L_1,...,L_7.
Q = [[0] * 14 for _ in range(14)]
for i in range(7):
    Q[i][i] = -1
    Q[i+7][i+7] = -2
    for j in range(7):
        Q[i][7+j] = Q[7+j][i] = INCIDENCE[i][j]


def is_negative_definite(selected):
    """Exact rational symmetric Schur elimination on the negative matrix."""
    size = len(selected)
    matrix = [[Fraction(-Q[u][v]) for v in selected]
              for u in selected]
    for j in range(size):
        pivot = matrix[j][j]
        if pivot <= 0:
            return False
        for i in range(j+1, size):
            for k in range(i, size):
                matrix[k][i] = matrix[i][k] = (
                    matrix[i][k] - matrix[i][j]*matrix[k][j]/pivot
                )
    return True


def is_induced_matching(mask):
    degrees = [0] * 14
    for i in range(7):
        if mask & (1 << i):
            for j in range(7):
                if (mask & (1 << (7+j))) and INCIDENCE[i][j]:
                    degrees[i] += 1
                    degrees[7+j] += 1
    return max(degrees) <= 1


counts = [0] * 15
for mask in range(1 << 14):
    selected = [i for i in range(14) if mask & (1 << i)]
    combinatorial = is_induced_matching(mask)
    algebraic = is_negative_definite(selected)
    assert combinatorial == algebraic, (mask, combinatorial, algebraic)
    if algebraic:
        counts[len(selected)] += 1

expected = [1, 14, 91, 322, 651, 728, 392, 58] + [0] * 7
assert counts == expected, (counts, expected)
assert sum(counts) == 2257
print('FULL_MASKS_TESTED', 1 << 14)
print('ZARISKI_CHAMBER_POLYNOMIAL', counts)
print('TOTAL_CHAMBERS', sum(counts))
print('ALL_CHECKS_PASSED')
