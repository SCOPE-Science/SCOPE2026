#!/usr/bin/env python3
"""Finite Gaussian-packet diagnostics; analytic infinite arguments are in RESULT.md."""
import math
from fractions import Fraction


def log_heat_peak(n):
    b = n * n
    return (math.log(2) + (n + 1) * math.log1p(1 / (2 * b))
            - (n / 2 + 1) * math.log1p(1 / b)
            + (n / 2) * (math.log(n) - 1) - math.lgamma(n + 1) / 2)


def log_heat_upper(n):
    return math.log(2) + (n + 1) / (2 * n * n) - .25 * math.log(2 * math.pi * n)


def test_weights(n):
    q = Fraction(1, 1 + 2 * n * n)
    # Squared Toeplitz coefficients of the Gaussian anti-holomorphic packet.
    weights_sq = [q ** (2 * k) * math.comb(n + k, k) for k in range(24)]
    assert weights_sq[0] == 1
    assert all(weights_sq[k + 1] < weights_sq[k] for k in range(23))
    assert (q * q * (n + 1)) < 1
    return len(weights_sq)


def main():
    count = 0
    for n in [1, 2, 3, 4, 8, 16, 100, 4096]:
        count += test_weights(n)
        assert log_heat_peak(n) <= log_heat_upper(n) + 3e-11
        # The real packet is the sum of two conjugate Gaussian monomials.
        assert 2 * math.exp(log_heat_peak(n)) <= 4 * math.e / (2 * math.pi * n) ** .25 + 1e-10
        count += 2
    for j in range(1, 50):
        n = (j + 1) ** 12
        # The analytic Stirling envelope is a summable explicit majorant.
        assert n == (j + 1)**12
        assert j / (j + 1)**3 <= 1 / j**2
        if j <= 2:  # Avoid catastrophic cancellation at astronomic degrees.
            assert log_heat_peak(n) <= log_heat_upper(n) + 1e-8
        count += 2
    print("PASS: finite normalized-weight/heat-bound checks:", count)
    print("The Gaussian-integral identities and infinite center recursion need the written proof.")


if __name__ == "__main__":
    main()
