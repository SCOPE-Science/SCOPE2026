"""Reproduce modal-crossing comparisons in a one-delay heat forecast.

Standard library only. This is numerical corroboration, not a substitute for the
proof that works for all dimensions and sufficiently large decay lags.
"""
import math


def data(dimension, lag, burn_in):
    eigen = [2.0 - 2.0 * math.cos(math.pi * j / (dimension + 1))
             for j in range(1, dimension + 1)]
    crossing = [4 * (dimension - j) + 0.5 for j in range(1, dimension)]
    gamma = [0.0]
    for j in range(dimension - 1):
        gamma.append(gamma[-1] + (eigen[j + 1] - eigen[j]) * crossing[j])
    levels = [gamma[j] - burn_in * eigen[j] for j in range(dimension)]
    maximum = max(levels)
    weights = [math.exp(2 * lag * (level - maximum)) for level in levels]
    relative_factors = [math.exp(-lag * (e - eigen[0])) for e in eigen]
    numerator = math.fsum(weights[i] * weights[j] *
                          (relative_factors[i] - relative_factors[j]) ** 2
                          for i in range(dimension) for j in range(i + 1, dimension))
    denominator = (math.fsum(weights) *
                   math.fsum(w * r * r for w, r in zip(weights, relative_factors)))
    return math.sqrt(numerator / denominator), eigen, gamma, crossing


def verify():
    comparisons = 0
    for n in range(2, 9):
        for lag in (10, 30):
            for j in range(1, n):
                s = 4 * (n - j)
                before = data(n, lag, s - 1)[0]
                at = data(n, lag, s)[0]
                after = data(n, lag, s + 1)[0]
                assert 0 <= before < at <= 1 + 1e-12
                assert 0 <= after < at <= 1 + 1e-12
                comparisons += 2
        # Exact crossing schedule and adjacent-mode log-amplitude ordering.
        rr, eigen, gamma, crossing = data(n, 10, 0)
        for j in range(n - 1):
            assert abs((gamma[j + 1] - gamma[j]) -
                       (eigen[j + 1] - eigen[j]) * crossing[j]) < 1e-11
            comparisons += 1
    # Compare the pairwise variance identity with the direct projective formula
    # where there is no catastrophic cancellation.
    for n in range(2, 9):
        for s in range(1, 4 * n):
            lag = 1.0
            r, eigen, gamma, _ = data(n, lag, s)
            z = [math.exp(lag * (gamma[j] - eigen[j] * s)) for j in range(n)]
            z1 = [z[j] * math.exp(-lag * eigen[j]) for j in range(n)]
            inner = math.fsum(a * b for a, b in zip(z, z1))
            cos2 = inner * inner / (math.fsum(a * a for a in z) *
                                    math.fsum(a * a for a in z1))
            assert abs((1 - cos2) - r * r) < 5e-12
            comparisons += 1
    print(f'VERIFY_OK {comparisons} checks (dimensions 2..8)')


if __name__ == '__main__':
    verify()
