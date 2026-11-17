"""Exact-rational reproducibility checks for two grounded leaders on wheel graphs.
No external dependencies; run with Python 3.9+.
"""
from fractions import Fraction as F
from itertools import combinations


def inverse(A):
    n = len(A)
    if n == 0:
        return []
    X = [[F(v) for v in row] + [F(i == j) for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        p = next((j for j in range(i, n) if X[j][i]), None)
        assert p is not None, 'singular grounded matrix'
        X[i], X[p] = X[p], X[i]
        q = X[i][i]
        X[i] = [v / q for v in X[i]]
        for j in range(n):
            if j != i and X[j][i]:
                q = X[j][i]
                X[j] = [a - q * b for a, b in zip(X[j], X[i])]
    return [row[n:] for row in X]


def trace_inverse(A):
    B = inverse(A)
    return sum((B[i][i] for i in range(len(B))), F(0))


def wheel_laplacian(m):
    n = m + 1
    L = [[0] * n for _ in range(n)]
    edges = [(0, j) for j in range(1, n)]
    edges += [(j + 1, (j + 1) % m + 1) for j in range(m)]
    for a, b in edges:
        L[a][a] += 1
        L[b][b] += 1
        L[a][b] -= 1
        L[b][a] -= 1
    return L


def grounded_value(m, leaders):
    L = wheel_laplacian(m)
    keep = [i for i in range(m + 1) if i not in leaders]
    return trace_inverse([[L[i][j] for j in keep] for i in keep])


def path_data(l):
    T = [[3 if i == j else -1 if abs(i - j) == 1 else 0
          for j in range(l)] for i in range(l)]
    B = inverse(T)
    z = [sum(row, F(0)) for row in B]
    h = sum((B[i][i] for i in range(l)), F(0))
    f = sum(z, F(0))
    g = sum((q * q for q in z), F(0))
    return h, f, g


def schur_value(m, d):
    a, b = d - 1, m - d - 1
    h1, f1, g1 = path_data(a)
    h2, f2, g2 = path_data(b)
    return h1 + h2 + (1 + g1 + g2) / (m - f1 - f2)


def run():
    checks = 0
    table = {}
    for m in range(4, 9):
        hub = grounded_value(m, (0, 1))
        others = {d: grounded_value(m, (1, 1 + d))
                  for d in range(1, m // 2 + 1)}
        table[m] = (str(hub), {str(k): str(v) for k, v in others.items()})
        if m <= 6:
            assert min(others.values()) < hub
            assert [d for d, v in others.items() if v == min(others.values())] == [m // 2]
        else:
            assert hub < min(others.values())
        checks += len(others) + 1

    # All vertex pairs, not only symmetry representatives, and exact inverse traces.
    for m in range(4, 11):
        vals = {leaders: grounded_value(m, leaders)
                for leaders in combinations(range(m + 1), 2)}
        minval = min(vals.values())
        winners = [leaders for leaders, v in vals.items() if v == minval]
        if m <= 6:
            wanted = [leaders for leaders in vals
                      if 0 not in leaders and
                      min((leaders[1] - leaders[0]) % m,
                          (leaders[0] - leaders[1]) % m) == m // 2]
            # Rim labels are 1,...,m; distance is unchanged by the common +1.
        else:
            wanted = [leaders for leaders in vals if 0 in leaders]
        assert set(winners) == set(wanted), (m, winners, wanted)
        checks += len(vals)

    for m in range(4, 19):
        hub = grounded_value(m, (0, 1))
        assert hub == path_data(m - 1)[0]
        checks += 1
        for d in range(1, m // 2 + 1):
            assert schur_value(m, d) == grounded_value(m, (1, 1 + d))
            checks += 1

    # The scalar inequalities required for all m >= 9 are exact in Q(sqrt(5)).
    import math
    c = 2 * math.sqrt(5)
    left9 = (1 + (9 - c)**2 / 7) / c
    right = 6 / 5 - 1 / math.sqrt(5)
    assert left9 > right
    assert 61*61*5 > 132*132 # exact positivity of (61 sqrt(5)-132)/35
    print('PASS: exact-rational checks =', checks)
    print('Small-case table:', table)
    print('Analytic large-case boundary witness 61 sqrt(5) > 132: PASS')


if __name__ == '__main__':
    run()
