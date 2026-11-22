"""Numerical diagnostics for the optimal two-hop cyclic Kemeny design.

Only Python's standard library is used. Finite checks support, but do not
replace, the analytical proof of global optimality and asymptotics.
"""
import math


def spectral(n, eps):
    return sum(1.0 / (eps * (1.0 - math.cos(2 * math.pi * k / n))
                     + (1.0 - eps) * (1.0 - math.cos(4 * math.pi * k / n)))
               for k in range(1, n))


def closed(n, eps):
    a = 4.0 - 3.0 * eps
    delta = math.sqrt(eps * a)
    r = 2.0 * (1.0 - eps) / (2.0 - eps + delta)
    h = (-r) ** n
    return ((n * n - 1) / (6.0 * a)
            + 2.0 * (1.0 - eps) / a
            * (n / delta * (1.0 + h) / (1.0 - h) - 1.0 / a))


def grad(n, eps):
    return sum((1.0 - math.cos(4 * math.pi * k / n)
                - (1.0 - math.cos(2 * math.pi * k / n)))
               / (eps * (1 - math.cos(2 * math.pi * k / n))
                  + (1 - eps) * (1 - math.cos(4 * math.pi * k / n))) ** 2
               for k in range(1, n))


def optimum(n):
    lo, hi = 1e-13, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if grad(n, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def inverse_trace(matrix):
    """Gauss-Jordan inversion of a real positive definite matrix."""
    n = len(matrix)
    a = [list(row) + [float(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = max(range(i, n), key=lambda k: abs(a[k][i]))
        a[i], a[pivot] = a[pivot], a[i]
        d = a[i][i]
        assert abs(d) > 1e-12
        a[i] = [v / d for v in a[i]]
        for j in range(n):
            if j != i:
                d = a[j][i]
                a[j] = [v - d * w for v, w in zip(a[j], a[i])]
    return sum(a[i][n + i] for i in range(n))


def matrix_trace(n, eps):
    # L + J/n has eigenvalue 1 on the constant vector and the
    # nonzero eigenvalues of I-P on the orthogonal complement.
    a, b = eps / 2.0, (1.0 - eps) / 2.0
    mat = [[float(i == j) + 1 / n for j in range(n)] for i in range(n)]
    for i in range(n):
        for step, w in [(1, a), (2, b)]:
            for sign in (-1, 1):
                j = (i + sign * step) % n
                mat[i][j] -= w
    return inverse_trace(mat) - 1.0


def main():
    count = 0
    for n in range(5, 101):
        e = optimum(n)
        assert 0 < e < 1
        count += 1
        assert abs(grad(n, e)) <= max(1e-6, n * n * 1e-11)
        count += 1
        assert abs(grad(n, 1.0) - (n - 1) * (n - 3) / 2) < 2e-8 * n * n
        count += 1
        for x in (0.05, 0.2, 0.5, 0.9, e):
            assert abs(spectral(n, x) / closed(n, x) - 1) < 5e-11
            count += 1
        for x in (max(1e-5, e * .8), min(.999, e * 1.2)):
            assert spectral(n, x) > spectral(n, e) - 1e-9
            count += 1
        if n <= 18:
            assert abs(matrix_trace(n, e) / spectral(n, e) - 1) < 1e-9
            count += 1
    for n in (400, 800, 1600, 3200, 6400, 12800):
        e = optimum(n)
        x = n ** (2 / 3) * e
        assert abs(x / 4 ** (2 / 3) - 1) < 0.2
        count += 1
        # Predicted asymptotic first correction, with relative errors shrinking.
        asympt = 3 / (8 * 4 ** (1 / 3))
        ratio = (closed(n, e) - n * n / 24) / n ** (4 / 3) / asympt
        assert abs(ratio - 1) < 0.15
        count += 1
    print(f"PASS {count} finite diagnostics")
    print("Large-n (n, n^(2/3) eps, correction ratio):")
    for n in (800, 3200, 12800):
        e = optimum(n)
        print(n, round(n ** (2 / 3) * e, 9),
              round((closed(n, e) - n*n/24)/n**(4/3)/(3/(8*4**(1/3))), 9))


if __name__ == '__main__':
    main()
