#!/usr/bin/env python3
"""Reproducibility checks for monomial singular spectra of the twisted baker map."""
import itertools
import math
import random


def derivative(m, branch):
    a = [[0 for _ in range(m)] for _ in range(m)]
    if branch == 0:
        for j in range(m):
            a[j][j] = 2 if j == 0 else 1
    else:
        a[0][m - 1] = -2
        for j in range(1, m):
            a[j][j - 1] = 1
    return a


def multiply(a, b):
    m = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(m))
             for j in range(m)] for i in range(m)]


def count_stretches(m, word):
    # Read from the most recent derivative factor backwards.
    state = 0
    counts = [0] * m
    for b in reversed(word):
        counts[state] += 1
        state = (state + b) % m
    return counts


def matrix_stretches(m, word):
    a = [[int(i == j) for j in range(m)] for i in range(m)]
    for b in word:
        a = multiply(derivative(m, b), a)
    col_squares = [sum(a[i][j] ** 2 for i in range(m)) for j in range(m)]
    assert all(s > 0 and (s & (s - 1)) == 0 for s in col_squares)
    assert all((s.bit_length() - 1) % 2 == 0 for s in col_squares)
    return sorted((s.bit_length() - 1) // 2 for s in col_squares)


def exact_word_checks():
    total = 0
    for m in range(2, 7):
        for n in range(1, 10):
            for word in itertools.product((0, 1), repeat=n):
                expected = sorted(count_stretches(m, word))
                observed = matrix_stretches(m, word)
                assert observed == expected, (m, n, word, observed, expected)
                total += 1
    print('EXACT_MONOMIAL_ALL_BINARY_WORDS_OK', total)


def two_dimensional_binomial_check():
    from math import comb
    for n in range(1, 12):
        counts = [0] * (n + 1)
        for word in itertools.product((0, 1), repeat=n):
            counts[count_stretches(2, word)[0]] += 1
        for k in range(n):
            assert counts[k + 1] == 2 * comb(n - 1, k), (n, k)
        assert counts[0] == 0
    print('TWO_DIMENSIONAL_BINOMIAL_LAW_OK')


def monte_carlo_covariance():
    rng = random.Random(20261106)
    for m in (3, 5):
        n, trials = 1800, 3200
        covariance = [[0.0] * m for _ in range(m)]
        for _ in range(trials):
            counts = [0] * m
            state = 0
            for t in range(n):
                counts[state] += 1
                state = (state + rng.randrange(2)) % m
            d = [(v - n / m) / math.sqrt(n) for v in counts]
            for i in range(m):
                for j in range(m):
                    covariance[i][j] += d[i] * d[j] / trials
        for i in range(m):
            for j in range(m):
                expected = (1.0 if i == j else 0.0) / m - 1.0 / (m * m)
                assert abs(covariance[i][j] - expected) < 0.045, (m, i, j, covariance[i][j], expected)
        print('COVARIANCE_APPROXIMATION_OK', m,
              'variance=', round(covariance[0][0], 5),
              'expected=', round((m-1)/m**2, 5))


if __name__ == '__main__':
    exact_word_checks()
    two_dimensional_binomial_check()
    monte_carlo_covariance()
    print('TWISTED_BAKER_SINGULAR_SPECTRUM_CHECKS_OK')
