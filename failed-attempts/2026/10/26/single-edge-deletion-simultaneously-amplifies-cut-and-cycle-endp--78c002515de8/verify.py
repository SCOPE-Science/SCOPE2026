"""Exact rational, dependency-free verification for a single-edge-deleted Boolean cube.

Run: python3 verify.py . No network, stochastic inputs, or third-party packages.
The all-dimension theorem is analytic; finite computations check the key identities.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def oriented_edges(n):
    return [(x, i) for x in range(1 << n) for i in range(n)
            if ((x >> i) & 1) == 0]


def dot(n, a, b):
    x, i = a
    y, j = b
    z = x ^ y
    total = F(0)
    for mask in range(1, 1 << n):
        if (mask >> i) & 1 and (mask >> j) & 1:
            total += F(-1 if (mask & z).bit_count() % 2 else 1,
                       mask.bit_count())
    return F(2, 1 << n) * total


def inverse(M):
    N = len(M)
    A = [[F(M[i][j]) for j in range(N)] + [F(i == j) for j in range(N)]
         for i in range(N)]
    for p in range(N):
        k = next(k for k in range(p, N) if A[k][p] != 0)
        A[p], A[k] = A[k], A[p]
        d = A[p][p]
        A[p] = [x / d for x in A[p]]
        for k in range(N):
            if k == p or not A[k][p]:
                continue
            d = A[k][p]
            A[k] = [x - d * y for x, y in zip(A[k], A[p])]
    return [a[N:] for a in A]


def grounded_transfer(n, edge_list):
    N = 1 << n
    L = [[0] * (N - 1) for _ in range(N - 1)]
    for x, i in edge_list:
        y = x ^ (1 << i)
        for a in (x, y):
            if a:
                L[a - 1][a - 1] += 1
        if x and y:
            L[x - 1][y - 1] -= 1
            L[y - 1][x - 1] -= 1
    M = inverse(L)
    out = []
    for x, i in edge_list:
        y = x ^ (1 << i)
        def val(a, b):
            return F(0) if not a or not b else M[a - 1][b - 1]
        out.append([val(x, u) - val(x, u ^ (1 << j))
                    - val(y, u) + val(y, u ^ (1 << j))
                    for u, j in edge_list])
    return out


def check(n, independent=False):
    E = oriented_edges(n)
    assert E[0] == (0, 0)
    E1 = E[1:]
    m = len(E)
    R = dot(n, E[0], E[0])
    a = dot(n, E[0], (2, 0))
    assert R == F(2, n) * (1 - F(1, 2 ** n))
    assert a == F(2, n * (n - 1)) * (1 - F(n + 1, 2 ** n))
    assert F(0) < a <= 1 - R
    C = F(n + 1, 2)
    base_flow = [dot(n, g, E[0]) for g in E]
    assert sum(abs(x) for x in base_flow) == C
    assert sum(abs(x) for x, (u, j) in zip(base_flow, E) if j == 0) == 1
    for j in range(1, n):
        assert sum(abs(x) for x, (u, i) in zip(base_flow, E) if i == j) == F(1, 2)
    # Differentiate the potential of the damaged electrical network via a rank-one update.
    Q = [[dot(n, f, g) + dot(n, f, E[0]) * dot(n, E[0], g) / (1 - R)
          for g in E1] for f in E1]
    assert all(Q[i][j] == Q[j][i] for i in range(len(E1)) for j in range(len(E1)))
    if independent:
        other = grounded_transfer(n, E1)
        assert Q == other, (n, 'grounded inverse mismatch')
    rows_C = [sum(abs(Q[i][j]) for i in range(len(E1))) for j in range(len(E1))]
    rows_P = [sum(abs(F(i == j) - Q[i][j]) for i in range(len(E1)))
              for j in range(len(E1))]
    adjacent = E1.index((2, 0))
    gain_C = F(n - 3, 2) * a / (1 - R)
    gain_P = gain_C - 2 * a * a / (1 - R)
    assert rows_C[adjacent] == C + gain_C
    assert rows_P[adjacent] == C + 1 - 2 * R + gain_P
    if n == 2:
        assert max(rows_C) == 1 and max(rows_P) == 0
    if n == 3:
        assert max(rows_C) == 2 and max(rows_P) == F(71, 40)
        assert sorted(set(rows_C)) == [F(9, 5), F(15, 8), F(39, 20), F(2)]
    if n >= 4:
        assert gain_C > 0 and gain_P > 0
    return m, len(E1), max(rows_C), max(rows_P), gain_C, gain_P


if __name__ == '__main__':
    total = 0
    for n in (2, 3, 4, 5):
        m, cols, q, p, dq, dp = check(n, independent=True)
        total += cols
        print('dimension', n, 'edges', m, 'Q_after', q, 'P_after', p,
              'adjacent_gain_Q', dq, 'adjacent_gain_P', dp)
    print('EDGE_DELETED_CUBE_EXACT_OK dimensions=4 independent_grounded_columns=' + str(total))
