"""Independent exact finite checks for a longest-run derivative identity.

Usage: python3 verify.py
"""
from fractions import Fraction
from itertools import product
from math import comb, sqrt


def binomial(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def inclusion_exclusion(n, r):
    """Return (P(R_n<r), d/dp P_p(R_n<r) at p=1/2)."""
    p = Fraction(1, 2)
    q = p
    probability = Fraction(1)
    derivative = Fraction(0)
    for k in range(1, n // r + 1):
        a = binomial(n - k * r, k)
        b = binomial(n - k * r, k - 1)
        weight = p ** k * a + p ** (k - 1) * b
        probability += (-1) ** k * q ** (r * k) * weight
        dweight = k * p ** (k - 1) * a
        if k > 1:
            dweight += (k - 1) * p ** (k - 2) * b
        derivative += (-1) ** k * (
            -r * k * q ** (r * k - 1) * weight
            + q ** (r * k) * dweight
        )
    return probability, derivative


def exhaustive(n, r):
    cumulative = Fraction(0)
    derivative = Fraction(0)
    for word in product((0, 1), repeat=n):
        length = maximum = 0
        for bit in word:
            length = length + 1 if bit == 0 else 0
            maximum = max(maximum, length)
        if maximum < r:
            cumulative += Fraction(1, 2 ** n)
            derivative += Fraction(2 * sum(word) - n, 2 ** (n - 1))
    return cumulative, derivative


def exact_covariance(n):
    return -sum(inclusion_exclusion(n, r)[1] for r in range(1, n + 1)) / 4


def dynamic_correlation(n):
    """Float DP on trailing zero-run states for diagnostic reference values."""
    mean = second = total_derivative = 0.0
    # Long-tail error < 1e-8 for these n.
    from math import log2
    cap = min(n, int(log2(n)) + 32)
    for r in range(1, cap + 1):
        probs = [0.0] * r
        slopes = [0.0] * r
        probs[0] = 1.0
        for _ in range(n):
            s, d = sum(probs), sum(slopes)
            new_p = [0.0] * r
            new_d = [0.0] * r
            new_p[0] = 0.5 * s
            new_d[0] = s + 0.5 * d
            for j in range(1, r):
                new_p[j] = 0.5 * probs[j - 1]
                new_d[j] = -probs[j - 1] + 0.5 * slopes[j - 1]
            probs, slopes = new_p, new_d
        tail = 1.0 - sum(probs)
        mean += tail
        second += (2 * r - 1) * tail
        total_derivative += sum(slopes)
    covariance = -total_derivative / 4
    variance = second - mean * mean
    return covariance / (sqrt(n) / 2 * sqrt(variance))


def main():
    cases = 0
    for n in range(1, 10):
        for r in range(1, n + 1):
            assert inclusion_exclusion(n, r) == exhaustive(n, r), (n, r)
            cases += 1
    assert exact_covariance(4) == Fraction(-7, 8)
    for n, target in [(100, -0.441772), (200, -0.361888),
                      (1000, -0.215704)]:
        observed = dynamic_correlation(n)
        assert abs(observed - target) < 3e-6, (n, observed)
    print(f"VERIFY_OK {cases} exact IE/derivative comparisons; 3 published correlations")


if __name__ == "__main__":
    main()
