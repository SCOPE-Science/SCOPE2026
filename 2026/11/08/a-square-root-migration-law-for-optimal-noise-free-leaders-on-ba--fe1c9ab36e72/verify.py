"""Exact validation for balanced split-graph grounded-Laplacian leader placement.

Uses standard-library exact rationals; no external dependencies.
The finite checks corroborate but do not prove the all-n limit theorem.
"""
from fractions import Fraction
from itertools import combinations


def value_formula(n, k, a):
    assert n >= 2 and 1 <= k < n and 0 <= a <= k
    u, v = n - a, n - k + a
    d = n * k + a * v
    return (Fraction(u - 1, 2 * n) + Fraction(v - 1, n)
            + Fraction(2 * n + a, d))


def trace_inverse(matrix):
    m = len(matrix)
    if m == 0:
        return Fraction(0)
    a = [[Fraction(matrix[i][j]) for j in range(m)]
         + [Fraction(int(i == j)) for j in range(m)] for i in range(m)]
    for i in range(m):
        pivot = next(j for j in range(i, m) if a[j][i])
        a[i], a[pivot] = a[pivot], a[i]
        t = a[i][i]
        a[i] = [v / t for v in a[i]]
        for j in range(m):
            if j == i:
                continue
            f = a[j][i]
            if f:
                a[j] = [a[j][h] - f * a[i][h] for h in range(2 * m)]
    return sum(a[i][m + i] for i in range(m))


def laplacian(n):
    N = 2 * n
    L = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            connected = i < n or j < n
            if connected:
                L[i][j] = L[j][i] = -1
                L[i][i] += 1
                L[j][j] += 1
    return L


def run():
    tests = 0
    for n in range(2, 6):
        L = laplacian(n)
        for k in range(1, n):
            for leaders in combinations(range(2*n), k):
                a = sum(i < n for i in leaders)
                follow = [i for i in range(2*n) if i not in leaders]
                block = [[L[i][j] for j in follow] for i in follow]
                observed = trace_inverse(block)
                expected = value_formula(n, k, a)
                assert observed == expected, (n, k, leaders, observed, expected)
                tests += 1
    for k, best_a, best_value in [(4,4,Fraction(8,5)), (7,0,Fraction(381,280))]:
        vals = [value_formula(20,k,a) for a in range(k+1)]
        assert min(vals) == best_value
        assert [a for a,v in enumerate(vals) if v==min(vals)] == [best_a]
    print('PASS:', tests, 'independent rational inversions and two unique optimal-placement witnesses')

if __name__ == '__main__':
    run()
