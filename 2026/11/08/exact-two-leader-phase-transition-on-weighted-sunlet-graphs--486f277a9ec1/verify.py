#!/usr/bin/env python3
"""Exact symbolic and matrix checks for two noise-free leaders on weighted sunlet graphs.

Requires Python 3 and SymPy. This finite replay supplements, but does not
replace, the uniform analytic arguments in RESULT.md.
"""
from itertools import combinations
from sympy import Matrix, Rational, symbols, factor, simplify, zeros


def reduced_objective(n, t, pair):
    """Compute trace of a grounded Laplacian inverse directly, with rationals."""
    L = zeros(2 * n)
    for i in range(n):
        for u, v, w in ((i, (i + 1) % n, Rational(1)), (i, i + n, t)):
            L[u, u] += w
            L[v, v] += w
            L[u, v] -= w
            L[v, u] -= w
    followers = [i for i in range(2 * n) if i not in pair]
    return L.extract(followers, followers).inv().trace()


def closed_objective(n, t, pair):
    a, b = pair
    i, j = a % n, b % n
    d = min((i - j) % n, (j - i) % n)
    r = Rational(d * (n - d), n)
    q = r * (2 * n * r + 1) / 6
    if a < n and b < n:
        return n / t + (n * n - 2 * n * r - 2) / 3
    if a >= n and b >= n:
        return (2 * n - 3) / t + Rational(n * n - 1, 3) - (2 * t * q + (n + 1) * r) / (2 + t * r)
    if d == 0:
        return (n - 1) / t + Rational(n * n - 1, 3)
    return (n - 1) / t + Rational(n * n - 1, 3) - (2 * t * q + r) / (1 + t * r)


def theoretical_types(n, t):
    R = Rational((n // 2) * (n - n // 2), n)
    critical = 3 / (1 + 2 * (n - 3) * R)
    if t < critical:
        return {'CL'}
    if t > critical:
        return {'CC'}
    return {'CL', 'CC'}


def case_type(n, pair):
    a, b = pair
    if a < n and b < n:
        return 'CC'
    if a >= n and b >= n:
        return 'LL'
    return 'CL'


def main():
    n, r, t = symbols('n r t', positive=True)
    q = r * (2 * n * r + 1) / 6
    cc = n / t + (n * n - 2 * n * r - 2) / 3
    cl = (n - 1) / t + (n * n - 1) / 3 - (2 * t * q + r) / (1 + t * r)
    ll = (2 * n - 3) / t + (n * n - 1) / 3 - (2 * t * q + (n + 1) * r) / (2 + t * r)
    assert simplify((cl - cc) - (t * (1 + 2 * (n - 3) * r) - 3) / (3 * t * (1 + t * r))) == 0
    positive_poly = (2 * n - 6) * r ** 2 * t ** 2 + r * t ** 2 + (6 * n - 15) * r * t + 6 * n - 12
    assert simplify((ll - cl) - positive_poly / (3 * t * (1 + t * r) * (2 + t * r))) == 0
    print('PASS: two symbolic comparison identities, with positive coefficients for n>=3')

    matrices = 0
    opt_checks = 0
    for N in range(3, 9):
        R = Rational((N // 2) * (N - N // 2), N)
        threshold = 3 / (1 + 2 * (N - 3) * R)
        for T in sorted(set((Rational(1, 4), Rational(2, 3), Rational(1), Rational(5, 2), threshold))):
            results = {}
            for pair in combinations(range(2 * N), 2):
                actual = reduced_objective(N, T, pair)
                predicted = closed_objective(N, T, pair)
                assert actual == predicted, (N, T, pair, actual, predicted)
                results[pair] = actual
                matrices += 1
            optimum = min(results.values())
            winning = [pair for pair, value in results.items() if value == optimum]
            count = 0
            for a, b in winning:
                d = min((a % N - b % N) % N, (b % N - a % N) % N)
                assert d == N // 2
                assert case_type(N, (a, b)) in theoretical_types(N, T)
                count += 1
            expected = (N if N % 2 else N // 2) * ('CC' in theoretical_types(N, T)) + (2 * N if N % 2 else N) * ('CL' in theoretical_types(N, T))
            assert count == expected, (N, T, count, expected)
            opt_checks += 1
    print(f'PASS: {matrices} independently inverted rational grounded matrices and {opt_checks} exhaustive optimizer classifications')


if __name__ == '__main__':
    main()
