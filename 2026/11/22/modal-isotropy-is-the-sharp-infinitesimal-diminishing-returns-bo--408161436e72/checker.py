"""Exact-arithmetic checks for the diagonal LQR actuator interaction theorem.

Standard-library only; the analytic proof in RESULT.md covers all parameters.
"""
from fractions import Fraction as F
from random import Random


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(*matrices):
    return [[sum(m[i][j] for m in matrices) for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def diag(items):
    return [[items[i] if i == j else F(0) for j in range(len(items))]
            for i in range(len(items))]


def outer(u):
    return [[x * y for y in u] for x in u]


def derivative_trace(lambdas, u, v):
    n = len(lambdas)
    p = [F(1, 2) / z for z in lambdas]
    p0 = diag(p)
    U = outer(u)
    V = outer(v)
    pt = [[-p[i] * p[j] * U[i][j] / (lambdas[i] + lambdas[j])
           for j in range(n)] for i in range(n)]
    ps = [[-p[i] * p[j] * V[i][j] / (lambdas[i] + lambdas[j])
           for j in range(n)] for i in range(n)]
    rhs = add(matmul(matmul(pt, V), p0),
              matmul(matmul(p0, V), pt),
              matmul(matmul(ps, U), p0),
              matmul(matmul(p0, U), ps))
    pts = [[-rhs[i][j] / (lambdas[i] + lambdas[j])
            for j in range(n)] for i in range(n)]
    return sum(pts[i][i] for i in range(n))


def closed_form(lambdas, u, v):
    n = len(lambdas)
    w = [u[i] * v[i] for i in range(n)]
    return sum(F(lambdas[i] ** 2 + lambdas[j] ** 2,
                 8 * lambdas[i] ** 3 * lambdas[j] ** 3 *
                 (lambdas[i] + lambdas[j])) * w[i] * w[j]
               for i in range(n) for j in range(n))


def run():
    tests = 0
    rng = Random(3404)
    for n in range(1, 7):
        for _ in range(150):
            lam = [F(rng.randint(1, 8), rng.randint(1, 4)) for _ in range(n)]
            u = [F(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(n)]
            v = [F(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(n)]
            assert derivative_trace(lam, u, v) == closed_form(lam, u, v)
            tests += 1
            r = F(rng.randint(1, 8), rng.randint(1, 4))
            assert closed_form([r] * n, u, v) == (
                sum(u[i] * v[i] for i in range(n)) ** 2 / (8 * r ** 5))
            tests += 1
    assert closed_form([F(1), F(2)], [F(1), F(1)], [F(1), F(-4)]) == F(-1, 48)
    tests += 1
    for a in range(1, 12):
        for b in range(1, 12):
            ai, bj = F(a), F(b)
            diag1 = F(1, 8 * ai ** 5)
            diag2 = F(1, 8 * bj ** 5)
            cross = F(ai ** 2 + bj ** 2,
                      8 * ai ** 3 * bj ** 3 * (ai + bj))
            expected = -((ai - bj) ** 2 * (ai ** 2 + ai * bj + bj ** 2)
                         / (64 * ai ** 6 * bj ** 6 * (ai + bj) ** 2))
            assert diag1 * diag2 - cross ** 2 == expected
            assert (diag1 * diag2 - cross ** 2 < 0) == (a != b)
            tests += 2
    print(f"PASS: {tests} exact rational assertions")


if __name__ == '__main__':
    run()
