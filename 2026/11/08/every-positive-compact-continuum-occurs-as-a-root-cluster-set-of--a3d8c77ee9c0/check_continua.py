"""Finite diagnostics for a continuum-realization theorem.

The universal theorem has a separate analytical proof; these finite checks
verify algebraic and finite-dimensional identities, not the limit theorem.
"""
from fractions import Fraction
import math


def gamma(t):
    # A 1-Lipschitz periodic traversal of a square boundary in log coordinates.
    u = t % 8.0
    if u < 2:
        return (-1 + u, -1.0)
    if u < 4:
        return (1.0, -1 + u - 2)
    if u < 6:
        return (1 - (u - 4), 1.0)
    return (-1.0, 1 - (u - 6))


def run():
    tests = 0
    for length in range(1, 30):
        c = [(Fraction((i * 17 + 3) % 41 - 20, i + 7),
              Fraction((i * 19 + 5) % 53 - 26, i + 11))
             for i in range(1, length + 1)]
        b = [c[0]] + [tuple(i * c[i - 1][j] - (i - 1) * c[i - 2][j]
                             for j in range(2)) for i in range(2, length + 1)]
        sums = [Fraction(0), Fraction(0)]
        for i in range(length):
            for j in range(2):
                sums[j] += b[i][j]
                assert sums[j] / (i + 1) == c[i][j]
                tests += 1
    N = 7000
    c = [gamma(math.log(i)) for i in range(1, N + 1)]
    b = [c[0]] + [tuple(i * c[i - 1][j] - (i - 1) * c[i - 2][j]
                         for j in range(2)) for i in range(2, N + 1)]
    B = 2.000000001
    for i in range(N):
        assert all(abs(b[i][j]) <= B for j in range(2))
        tests += 1
    prefix = [[0.0, 0.0]]
    for v in b:
        prefix.append([prefix[-1][j] + v[j] for j in range(2)])
    for n in [20, 50, 101, 257, 1024, 4096]:
        for k in range(1, 12):
            for j in range(2):
                base = prefix[n][j] / n
                shifted = (prefix[n + k - 1][j] - prefix[k - 1][j]) / n
                assert abs(base - c[n - 1][j]) < 1e-11
                assert abs(shifted - base) < 2 * B * (k - 1) / n + 1e-11
                # Positive-root eigenvalue equals the geometric mean.
                assert abs(math.exp(shifted) -
                           math.exp((prefix[n + k - 1][j] - prefix[k - 1][j]) / n)) < 1e-12
                tests += 3
    print(f"PASS: {tests} finite identity and bound assertions")


if __name__ == '__main__':
    run()
