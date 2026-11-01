#!/usr/bin/env python3
"""Exact finite sanity check for the Cartan determinant used in RESULT.md.
The all-parameter theorem is proved by the recurrence in RESULT.md; this script
only checks the recurrence's matrix values for n=2,...,32.
"""

def det_bareiss(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot_value
    return sign * a[n - 1][n - 1]

for n in range(2, 33):
    k = n - 1
    gram = [[2 if i == j else -1 if abs(i-j) == 1 else 0 for j in range(k)] for i in range(k)]
    assert det_bareiss(gram) == n, (n, det_bareiss(gram))
print("CARTAN_DETERMINANTS_OK n=2..32")
