"""Independent finite-step return calculation for an axis-memory nearest-neighbor walk.

Pure Python 3 standard library; execute: python check_return.py
Finite computations corroborate the stated asymptotics; the proof is analytic.
"""
import math


def probability(n, q):
    assert n >= 2 and n % 2 == 0 and -1 < q < 1
    p = (1.0 + q) / 2.0
    fx, fy = [0.0] * (n + 1), [0.0] * (n + 1)
    fx[1], fy[0] = 0.5, 0.5
    for step in range(2, n + 1):
        nx, ny = [0.0] * (n + 1), [0.0] * (n + 1)
        for j in range(step):
            nx[j + 1] = p * fx[j] + (1.0 - p) * fy[j]
            ny[j] = (1.0 - p) * fx[j] + p * fy[j]
        fx, fy = nx, ny
    # P(symmetric one-dimensional k-step walk = 0), evaluated stably.
    def central(k):
        if k % 2:
            return 0.0
        return math.exp(math.lgamma(k + 1) - 2 * math.lgamma(k / 2 + 1) - k * math.log(2))
    return sum((fx[j] + fy[j]) * central(j) * central(n - j) for j in range(0, n + 1, 2))


def first(q):
    return (3.0 * q - 1.0) / (4.0 * (1.0 - q))


def second(q):
    return (25.0 * q * q + 2.0 * q + 1.0) / (32.0 * (1.0 - q) ** 2)


def run():
    tests = 0
    for m in (1, 2, 4, 8, 30, 200):
        q = 0.0
        expected = (math.comb(2 * m, m) / (4.0 ** m)) ** 2
        actual = probability(2 * m, q)
        assert abs(actual - expected) < 2e-11, (m, actual, expected)
        tests += 1
    for q in (-0.6, -0.2, 0.0, 1.0 / 3.0, 0.6):
        # The asymptotic error has order m^-3; the n=800 comparison is
        # deliberately coarse and is only a consistency check, not a proof.
        m = 400
        actual = math.pi * m * probability(2 * m, q)
        model = 1.0 + first(q) / m + second(q) / (m * m)
        assert abs(actual - model) < 0.000012, (q, actual, model)
        tests += 1
    q = 1.0 / 3.0
    for m in (160, 300, 500):
        estimate = m * m * (math.pi * m * probability(2 * m, q) - 1.0)
        assert abs(estimate - 5.0 / 16.0) < 0.009, (m, estimate)
        tests += 1
    assert abs(first(1.0 / 3.0)) < 1e-14
    assert abs(second(1.0 / 3.0) - 5.0 / 16.0) < 1e-14
    tests += 2
    print(f"PASS: {tests} finite-time/asymptotic consistency checks")


if __name__ == '__main__':
    run()
