#!/usr/bin/env python3
"""Reproducible finite diagnostics for polynomial harmonic-Bergman Toeplitz defects.

Python 3 standard library only. These finite tests do not prove the theorem.
"""
import cmath
import math
import random


def toeplitz_monomial_coefficient(j, degree):
    """Coefficient of e_(j+degree) in T_(z^degree)e_j."""
    k = j + degree
    if j >= 0:
        return math.sqrt((j + 1) / (k + 1))
    if k <= 0:
        return math.sqrt((1 - k) / (1 - j))
    return math.sqrt((1 - j) * (k + 1)) / (degree + 1)


def iterated_degree_one(j, degree):
    result = 1.0
    for k in range(j, j + degree):
        result *= toeplitz_monomial_coefficient(k, 1)
    return result


def crossing_coefficient(n, degree):
    if not 1 <= n < degree:
        return 0.0
    return n * (degree - n) / ((degree + 1) * math.sqrt((n + 1) * (degree - n + 1)))


def run():
    count = 0
    # Independent evaluation of the monomial Toeplitz shift and the iterated
    # degree-one shift in both wings and at their connecting interface.
    for degree in range(1, 51):
        for j in range(-70, 71):
            difference = toeplitz_monomial_coefficient(j, degree) - iterated_degree_one(j, degree)
            expected = crossing_coefficient(-j, degree)
            assert math.isclose(difference, expected, abs_tol=1e-12, rel_tol=1e-10), (j, degree)
            count += 1

    rng = random.Random(4102)
    for degree in range(2, 26):
        for trial in range(11):
            coefficients = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(degree + 1)]
            coefficients[degree] = 1.0 + 0.1j
            matrix = []
            for n in range(1, degree):
                matrix.append([coefficients[n + ell] * n * ell / (
                    (n + ell + 1) * math.sqrt((n + 1) * (ell + 1)))
                    if n + ell <= degree else 0j for ell in range(1, degree)])
            assert all(abs(matrix[j][degree - 2 - j]) > 0 for j in range(degree - 1))
            assert all(abs(matrix[i][j] - matrix[j][i]) < 2e-13 for i in range(degree - 1) for j in range(degree - 1))
            assert all(matrix[i][j] == 0 for i in range(degree - 1) for j in range(degree - 1) if i + j + 2 > degree)
            count += 1

    for degree in [10, 30, 100, 1000, 4000]:
        values = [crossing_coefficient(n, degree) for n in range(1, degree)]
        jmax = degree * degree // 4
        exact_max = jmax / ((degree + 1) * math.sqrt(jmax + degree + 1))
        assert math.isclose(max(values), exact_max, rel_tol=1e-14)
        for power in [1, 2, 3, 4]:
            expected = math.gamma(1 + power / 2)**2 / math.gamma(2 + power)
            observed = sum(x ** power for x in values) / degree
            if degree == 4000:
                assert abs(observed - expected) < 0.0015, (power, observed, expected)
            count += 1
    print(f"PASS {count} finite diagnostic checks; four moment comparisons at degree 4000")

if __name__ == "__main__":
    run()
