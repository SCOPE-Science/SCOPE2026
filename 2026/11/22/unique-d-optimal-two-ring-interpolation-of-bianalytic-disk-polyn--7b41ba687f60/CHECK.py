"""Reproducible finite checks for a two-ring bianalytic interpolation identity.

The all-degree conclusions rely on the analytic block-factorization and
strict concavity arguments; these finite calculations are diagnostics.
Requires only Python 3 standard library.
"""
import cmath
import math


def complex_determinant(matrix):
    n = len(matrix)
    a = [list(map(complex, row)) for row in matrix]
    determinant = complex(1.0)
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(a[i][j]))
        assert abs(a[k][j]) > 1e-14
        if k != j:
            a[j], a[k] = a[k], a[j]
            determinant *= -1
        pivot = a[j][j]
        determinant *= pivot
        for i in range(j + 1, n):
            scale = a[i][j] / pivot
            for h in range(j + 1, n):
                a[i][h] -= scale * a[j][h]
            a[i][j] = 0j
    return determinant


def direct_gram_determinant(n, r, s, phase):
    count = n + 1
    roots = [r * cmath.exp(2j * math.pi * k / count) for k in range(count)]
    roots += [s * cmath.exp(1j * (phase + 2 * math.pi * k / count)) for k in range(count)]
    matrix = [[z ** j for j in range(count)] +
              [z.conjugate() * z ** j for j in range(count)] for z in roots]
    return abs(complex_determinant(matrix)) ** 2


def exact_block_formula(n, r, s, phase):
    count = n + 1
    return (count ** (2 * count) * (r * s) ** (n * (n - 1) + 2) *
            (s * s - r * r) ** (2 * n) *
            abs(s ** (n - 1) * cmath.exp(1j * count * phase) - r ** (n - 1)) ** 2)


def stationary_equation(n, t):
    a = (n * (n - 1) + 2) / 2
    b = (n - 1) / 2
    y = t ** b
    return a - 2 * n * t / (1 - t) + (n - 1) * y / (1 + y)


def optimum_t(n):
    lower, upper = 0.0, 1.0
    for _ in range(150):
        mid = (lower + upper) / 2
        if stationary_equation(n, mid) > 0:
            lower = mid
        else:
            upper = mid
    return (lower + upper) / 2


def run():
    checks = 0
    for n in range(1, 9):
        for k in range(12):
            r = 0.13 + 0.021 * k
            s = 0.73 + 0.012 * k
            phase = 0.07 + 0.17 * k
            x = direct_gram_determinant(n, r, s, phase)
            y = exact_block_formula(n, r, s, phase)
            assert abs(x / y - 1) < 4e-8, (n, k, x, y)
            checks += 1
        t = optimum_t(n)
        eps = 1e-7
        assert stationary_equation(n, t - eps) > 0
        assert stationary_equation(n, t + eps) < 0
        checks += 2
        best_phase = math.pi / (n + 1)
        r = math.sqrt(t)
        optimal = exact_block_formula(n, r, 1, best_phase)
        assert optimal >= exact_block_formula(n, r, 1, 0)
        assert optimal > exact_block_formula(n, r * 0.9999, 1, best_phase)
        assert optimal > exact_block_formula(n, r * 1.0001, 1, best_phase)
        checks += 3
        print('degree', n, 'optimal squared radius', f'{t:.12f}')
    assert abs(optimum_t(1) - 1/3) < 1e-13
    checks += 1
    for n in (50, 100, 500, 1000):
        t = optimum_t(n)
        assert abs(n * (1 - t) - 4) < 15 / n
        checks += 1
    print('PASS:', checks, 'finite tests; infinite proofs are analytic.')


if __name__ == '__main__':
    run()
