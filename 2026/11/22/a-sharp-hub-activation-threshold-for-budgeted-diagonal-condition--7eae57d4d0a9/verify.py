"""Reproducible exact-arithmetic and independent full-matrix tests for vertex budgets on stars.

Run: python3 verify.py (requires only the Python standard library).
The universal theorem is proved algebraically in RESULT.md; these checks test its identities.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def candidate(m, a, budget):
    k = a * (m + 1) + 2 * m + budget
    free = (budget + m - 1 - F(2 * m * (m - 1), 1) / k) / (m + 1)
    return min(budget / m, free)


def ratio_squared(m, a, budget, x):
    h = 2 * a + m + 1 + budget - (m - 1) * x
    d = m - 1 + budget - (m + 1) * x
    return (d * d + 4 * m) / (h * h)


def eigenvalues_symmetric(mat):
    n = len(mat)
    a = [list(map(float, row)) for row in mat]
    for _ in range(60 * n * n):
        p, q = 0, 1
        mx = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                v = abs(a[i][j])
                if v > mx:
                    mx, p, q = v, i, j
        if mx < 1e-12:
            return sorted(a[i][i] for i in range(n))
        tau = (a[q][q] - a[p][p]) / (2 * a[p][q])
        t = (1 if tau >= 0 else -1) / (abs(tau) + sqrt(1 + tau * tau))
        c = 1 / sqrt(1 + t * t)
        s = t * c
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = app - t * apq
        a[q][q] = aqq + t * apq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                kp, kq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * kp - s * kq
                a[k][q] = a[q][k] = s * kp + c * kq
    raise AssertionError('Jacobi eigensolver did not converge')


def star(m, a, y, leaves):
    n = m + 1
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    matrix[0][0] = float(a + m + y)
    for i, amount in enumerate(leaves, 1):
        matrix[i][i] = float(a + 1 + amount)
        matrix[i][0] = matrix[0][i] = -1.0
    return matrix


def condition(matrix):
    ev = eigenvalues_symmetric(matrix)
    assert ev[0] > 0
    return ev[-1] / ev[0]


def check():
    count = 0
    rng = Random(2026)
    for m in range(2, 10):
        for a in [F(1, 9), F(1, 2), F(1), F(3), F(8)]:
            for budget in [F(0), F(1, 8), F(1), F(2), F(6), F(25)]:
                opt = candidate(m, a, budget)
                assert F(0) <= opt <= budget / m
                k = a * (m + 1) + 2 * m + budget
                free = (budget + m - 1 - 2 * m * (m - 1) / k) / (m + 1)
                # Derivative of the squared relative spectral gap at a rational test site.
                for j in range(1, 17):
                    x = budget * F(j, 17 * m)
                    h = 2 * a + m + 1 + budget - (m - 1) * x
                    d = m - 1 + budget - (m + 1) * x
                    derivative = (-2 * (m + 1) * d * h + 2 * (m - 1) * (d * d + 4 * m)) / h**3
                    expected = 4 * (m + 1) * k * (x - free) / h**3
                    assert derivative == expected
                    assert ratio_squared(m, a, budget, opt) <= ratio_squared(m, a, budget, x)
                    count += 2
                y = budget - m * opt
                eig = eigenvalues_symmetric(star(m, a, y, [opt] * m))
                h = float(2 * a + m + 1 + budget - (m - 1) * opt)
                d = float(m - 1 + budget - (m + 1) * opt)
                s = sqrt(d * d + 4 * m)
                assert abs(eig[0] - (h - s) / 2) < 2e-8
                assert abs(eig[-1] - (h + s) / 2) < 2e-8
                count += 2
                if budget > 0:
                    # Independently vary leaves and hub while preserving the total budget.
                    for _ in range(4):
                        shares = [rng.random() for i in range(m + 1)]
                        total = sum(shares)
                        dloads = [float(budget) * v / total for v in shares]
                        c = condition(star(m, a, dloads[0], dloads[1:]))
                        best = condition(star(m, a, y, [opt] * m))
                        assert c >= best - 1e-8, (m, a, budget, c, best)
                        count += 1
    # Boundary and exact benchmark.
    assert candidate(2, F(1), F(1)) == F(1, 2)
    assert candidate(2, F(1), F(2)) == F(23, 27)
    count += 2
    print('All', count, 'exact-rational and full-matrix checks passed.')


if __name__ == '__main__':
    check()
