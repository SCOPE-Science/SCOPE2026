#!/usr/bin/env python3
"""Exact rational finite checks of a diagonal annular operator construction."""
from fractions import Fraction

count = 0
for q in (Fraction(1, 10), Fraction(1, 3), Fraction(1, 2),
          Fraction(2, 3), Fraction(9, 10)):
    for N in range(1, 31):
        def d(j):
            return max(Fraction(0), Fraction(1) - Fraction(abs(j - N), N))
        def a(j):
            return (1 + q ** (j + 1)) / (1 + q ** j)
        def b(j):
            return (1 + q ** (j + 2)) / (1 + q ** j)
        def delta(j):
            return d(j + 1) - d(j)
        observed = []
        for j in range(-5, 2 * N + 6):
            assert (1 + q) * a(j) - b(j) == q
            direct = -b(j) * d(j + 2) + (1 + q) * a(j) * d(j + 1) - q * d(j)
            factorized = q * delta(j) - b(j) * delta(j + 1)
            assert direct == factorized
            if j == -1 or j == 2 * N - 1:
                expected = -q / N
            elif 0 <= j <= N - 2:
                expected = (q - b(j)) / N
            elif j == N - 1:
                expected = (q + b(N - 1)) / N
            elif N <= j <= 2 * N - 2:
                expected = (b(j) - q) / N
            else:
                expected = Fraction(0)
            assert direct == expected
            observed.append(abs(direct))
            count += 3
        expected_norm = (q + (1 + q ** (N + 1)) / (1 + q ** (N - 1))) / N
        assert max(observed) == expected_norm
        assert d(N) == 1 and d(0) == d(2 * N) == 0
        assert all(0 <= d(j) <= 1 for j in range(-5, 2 * N + 6))
        for alpha, beta in ((Fraction(1, 4), Fraction(-2, 5)),
                            (Fraction(-3, 7), Fraction(4, 9))):
            for j in (-4, -1, 0, N, 2 * N, 3 * N):
                tj = (alpha + q ** j * beta) / (1 + q ** j)
                assert (1 + q ** j) * tj == alpha + q ** j * beta
                count += 1
        count += 4
print('ANNULAR_TOEPLITZ_TENT_EXACT_OK', count)
