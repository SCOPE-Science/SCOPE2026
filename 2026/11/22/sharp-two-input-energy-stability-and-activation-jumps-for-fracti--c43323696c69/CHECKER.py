"""Exact rational branch certificates and deterministic numerical checks.

Run with Python 3.9+ using only its standard library.
The all-dimensional result depends on the accompanying proof, not this finite test.
"""
from fractions import Fraction as F
from math import ceil, sqrt
from random import Random


def feasible_k(n, c):
    assert F(1, n) < c < 1
    # For a rational c, avoid floating point rounding at integer thresholds.
    reciprocal = 1 / c
    ceiling = (reciprocal.numerator + reciprocal.denominator - 1) // reciprocal.denominator
    return min(n - 1, ceiling - 1)


def R(n, k, c):
    return (n - k) * (1 + k * c * (n * c - 2))


def squared_constant(n, c):
    K = feasible_k(n, c)
    return max([R(n, k, c) for k in range(1, K + 1)] + ([F(n)] if K >= 2 else []))


def branch(n, k, c):
    assert 1 <= k <= feasible_k(n, c)
    J = [[(F(i == j) if i < k else c) for j in range(n)] for i in range(n)]
    # Matrix of graph edge energy, L = nI - 11^T.
    B = [[sum((F(n if a == b else 0) - 1) * J[a][i] * J[b][j]
              for a in range(n) for b in range(n)) for j in range(n)] for i in range(n)]
    u = [F(1, k) - c if i < k else -c for i in range(n)]
    C = [[F(n) * (F(i == j) - F(1, k)) if i < k and j < k else F(0)
          for j in range(n)] for i in range(n)]
    target = [[C[i][j] + k * (n - k) * u[i] * u[j] for j in range(n)] for i in range(n)]
    assert B == target, (n, k, c)
    assert sum(t * t for t in u) * k * (n - k) == R(n, k, c)
    # A nonconstant input witness has strictly positive coordinates and margin.
    eps = min(F(1, 8), (1 - k * c) / (4 * c * (n - k)), k * c / 4)
    x = [F(1) if i < k else eps for i in range(n)]
    threshold = c * sum(x)
    assert all(x[i] > threshold for i in range(k))
    assert all(x[i] < threshold for i in range(k, n))
    return u, eps


def T(x, c):
    threshold = float(c) * sum(x)
    return [max(t, threshold) for t in x]


def V2(x):
    return sqrt(sum((x[i] - x[j]) ** 2 for i in range(len(x)) for j in range(i + 1, len(x))))


def tests():
    branch_checks = 0
    for n in range(2, 15):
        cs = [F(1, n) + (1 - F(1, n)) * F(a, 23) for a in (1, 3, 7, 11, 15, 21)]
        cs += [F(1, 2), F(2, 3), F(3, 4)]
        for c in sorted(set(z for z in cs if F(1, n) < z < 1)):
            K = feasible_k(n, c)
            vals = []
            for k in range(1, K + 1):
                u, eps = branch(n, k, c)
                vals.append(R(n, k, c))
                branch_checks += 1
            assert squared_constant(n, c) == max(vals + ([F(n)] if K >= 2 else []))
            # The norming local perturbation realizes the predicted branch value.
            for k in range(1, K + 1):
                u, eps = branch(n, k, c)
                v = u if (k == 1 or R(n, k, c) >= n) else [F(int(i == 0) - int(i == 1)) for i in range(n)]
                x = [float(F(1) if i < k else eps) for i in range(n)]
                t = float(eps) * 1e-5
                y = [xi + t * float(vi) for xi, vi in zip(x, v)]
                assert min(y) >= 0
                out = [a - b for a, b in zip(T(x, c), T(y, c))]
                ratio = V2(out) / sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))
                target = sqrt(float(max(R(n, k, c), n if k >= 2 else F(0))))
                assert abs(ratio - target) < 1e-5, (n, k, c, ratio, target)
    random_tests = 0
    rng = Random(20261121)
    for n in range(2, 12):
        for c in [F(1, n) + (1 - F(1, n)) * F(a, 21) for a in (1, 5, 9, 13, 17, 20)]:
            L = sqrt(float(squared_constant(n, c)))
            for _ in range(240):
                x = [rng.uniform(-3, 6) for _ in range(n)]
                y = [rng.uniform(-3, 6) for _ in range(n)]
                dx = sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))
                fx = T([abs(z) for z in x], c)
                fy = T([abs(z) for z in y], c)
                assert V2([a - b for a, b in zip(fx, fy)]) <= (L + 1e-11) * dx
                random_tests += 1
    complex_tests = 0
    for n in (3, 5, 9):
        c = F(1, n) + (1 - F(1, n)) * F(11, 19)
        L = sqrt(float(squared_constant(n, c)))
        for _ in range(500):
            a = [complex(rng.uniform(-2, 3), rng.uniform(-3, 2)) for i in range(n)]
            b = [complex(rng.uniform(-2, 3), rng.uniform(-3, 2)) for i in range(n)]
            da = sqrt(sum(abs(x-y)**2 for x, y in zip(a, b)))
            ta, tb = T([abs(x) for x in a], c), T([abs(x) for x in b], c)
            assert V2([x-y for x, y in zip(ta, tb)]) <= (L+1e-11)*da
            complex_tests += 1
    # Sharp one-sided k=2 feasibility transition at c=1/2.
    for n in range(3, 21):
        boundary = R(n, 1, F(1, 2))
        left = max(F(n), boundary, R(n, 2, F(1, 2)))
        right = squared_constant(n, F(1, 2))
        assert right == boundary
        assert (left == right) == (n == 5)
    print(f"PASS: {branch_checks} exact rational branch identities, "
          f"{random_tests} real and {complex_tests} complex direct pair tests, "
          "all sharp local witnesses and 18 exact boundary tests")


if __name__ == '__main__':
    tests()
