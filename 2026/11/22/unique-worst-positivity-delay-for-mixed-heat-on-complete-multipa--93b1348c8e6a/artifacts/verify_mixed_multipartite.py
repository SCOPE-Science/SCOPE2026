#!/usr/bin/env python3
"""Independent numerical checks for mixed Laplacian/bi-Laplacian positivity on multipartite graphs.
Standard-library Python 3, no external packages required.
The universal assertions are proved analytically; these finite tests are consistency checks.
"""
import math


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matrix_exponential(a):
    n = len(a)
    norm = max(sum(abs(z) for z in row) for row in a)
    levels = max(0, math.ceil(math.log2(norm / 0.2))) if norm else 0
    b = [[x * (2.0 ** -levels) for x in row] for row in a]
    ident = [[float(i == j) for j in range(n)] for i in range(n)]
    total = [row[:] for row in ident]
    term = [row[:] for row in ident]
    for k in range(1, 75):
        product = matmul(term, b)
        term = [[x / k for x in row] for row in product]
        for i in range(n):
            for j in range(n):
                total[i][j] += term[i][j]
        if max(abs(z) for row in term for z in row) < 5e-17:
            break
    else:
        raise AssertionError('Taylor expansion did not converge')
    for _ in range(levels):
        total = matmul(total, total)
    return total


def F(p, x):
    # Equals (1 - average_{0<u<x} 1/(1+p(expm1(u))))/p.
    if x == 0:
        return 0.
    q = 1. - p
    h = -math.log1p(q * math.expm1(-x)) / (q * x)
    return (1. - h) / p


def root(p, kappa):
    lo, hi = 0., 1.
    while F(p, hi) < kappa:
        hi *= 2.
    for _ in range(100):
        mid = (lo + hi) / 2.
        if F(p, mid) < kappa:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.


def cutoff(parts, eta):
    n = sum(parts)
    m = max(parts)
    if m == 1:
        return 0.
    p = m / n
    kappa = eta * n / (1 + eta * n)
    return root(p, kappa) / (n * (1 + eta * n))


def optimal(parts):
    n = sum(parts)
    p = max(parts) / n
    q = 1. - p
    xstar = math.log1p(1 / q)
    kappa = F(p, xstar)
    eta = kappa / (n * (1 - kappa))
    horizon = (1 - kappa) * xstar / n
    closed = ((1 + q) / q * math.log1p(q) + q / p * math.log(q)) / n
    assert abs(horizon - closed) < 3e-13
    return eta, horizon


def laplacian(parts):
    n = sum(parts)
    labels = [i for i, size in enumerate(parts) for _ in range(size)]
    a = [[0.] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and labels[i] != labels[j]:
                a[i][j] = -1.
                a[i][i] += 1.
    return a, labels


def predicted_entry(i, j, labels, parts, n, eta, t):
    rate_n = n * (1 + eta * n)
    z = math.exp(-rate_n * t)
    if labels[i] != labels[j]:
        return (1 - z) / n
    size = parts[labels[i]]
    d = n - size
    y = math.exp(-d * (1 + eta * d) * t)
    if i != j:
        return 1 / n + d / (size * n) * z - y / size
    return 1 / n + d / (size * n) * z + (1 - 1 / size) * y


def run():
    designs = [[2,1], [2,2], [3,1], [3,2], [4,1], [3,3], [2,2,1],
               [2,1,1,1], [2,2,2], [3,2,1], [4,3], [5,1], [4,2,1],
               [2,2,1,1,1], [3,3,2], [5,2,2], [2,3,4], [7,1],
               [3,1,1,1,1,1], [2,2,2,2], [2,2,2,1,1], [2,1,1,1,1,1,1]]
    checks = 0
    for parts in designs:
        n = sum(parts)
        L, labels = laplacian(parts)
        L2 = matmul(L, L)
        for eta in (0.05, 0.2, 0.8, 3.):
            T = cutoff(parts, eta)
            for c in (0.20, 0.75, 1., 1.3, 2.):
                t = c * T
                a = [[-t * (L[i][j] + eta * L2[i][j]) for j in range(n)] for i in range(n)]
                E = matrix_exponential(a)
                for i in range(n):
                    assert abs(sum(E[i]) - 1.) < 2e-10
                    for j in range(n):
                        pr = predicted_entry(i, j, labels, parts, n, eta, t)
                        assert abs(E[i][j] - pr) < 2e-10, (parts, eta, t, i, j, E[i][j], pr)
                        if i != j and labels[i] == labels[j] and parts[labels[i]] == max(parts):
                            if c < 1:
                                assert E[i][j] < -1e-13, (parts, eta, c, i, j, E[i][j])
                            if c > 1:
                                assert E[i][j] > 1e-13
                        if c >= 1.:
                            assert E[i][j] > -2e-10
                        checks += 1
    optimizations = 0
    for n in range(3, 35):
        prev = -1.
        for m in range(max(2, (n + 1) // 2), n):
            p = m / n
            eta, H = optimal([m, n - m])
            assert H > prev + 1e-12
            prev = H
            for multiplier in (0.4, 0.75, 1.3, 2.5):
                test = cutoff([m, n - m], eta * multiplier)
                # This design may have largest part n-m. Test p>=1/2 only.
                if m >= n-m:
                    assert H > test + 1e-13, (n, m, eta, H, test)
                optimizations += 1
    # Direct check of universal weak-coupling and large-coupling limits.
    limit_tests = 0
    for parts in ([2, 1], [2, 2], [3, 2, 1], [5, 3, 2]):
        n = sum(parts)
        for eta in (1e-5, 5e-6):
            assert abs(cutoff(parts, eta) / (2 * eta) - 1) < 1e-3
            limit_tests += 1
        p = max(parts) / n
        pure = root(p, 1.) / (n * n)
        for eta in (1e4, 5e4):
            assert abs(eta * cutoff(parts, eta) / pure - 1) < 1e-3
            limit_tests += 1
    print('VERIFY_OK matrix-entry-comparisons=%d parameter-checks=%d limit-tests=%d' % (checks, optimizations, limit_tests))


if __name__ == '__main__':
    run()
