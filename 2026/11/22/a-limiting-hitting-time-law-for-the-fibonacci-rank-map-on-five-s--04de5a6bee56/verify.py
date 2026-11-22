#!/usr/bin/env python3
"""Independent finite checks for rank-map smooth-core hitting times.

The all-size claims rely on the proof, not on these finite computations.
"""
from math import log, ceil


def closed_time(a, b):
    if a == b == 0:
        return 0
    if a == 0:
        return 3 if b == 1 else b - 1
    if b == 0:
        return {1: 4, 2: 2, 3: 2}.get(a, (a - 1) // 2)
    return max((a - 1) // 2, b - 1, int(a == 1))


def exponent_step(a, b):
    u = 0 if a <= 1 else 1 if a == 2 else a - 2
    return (max(u, 2 if b else 0),
            max(int(a > 0), b - 1, 0))


def exponent_time(a, b):
    steps = 0
    while (a, b) not in {(0, 0), (2, 1)}:
        a, b = exponent_step(a, b)
        steps += 1
        assert steps < 1000
    return steps


def direct_rank(n):
    """Compute rank using only F_(j+1)=F_j+F_(j-1) modulo n."""
    if n == 1:
        return 1
    x, y = 0, 1
    for j in range(1, 2 * n + 2):
        x, y = y, (x + y) % n
        if x == 0:
            return j
    raise RuntimeError('rank bound failure')


def direct_time(n):
    steps, cur = 0, n
    while True:
        nxt = direct_rank(cur)
        if nxt == cur:
            return steps, cur
        cur = nxt
        steps += 1
        assert steps < 100


def q_count(L):
    u, v, w = log(2), log(3), log(5)
    if L < 0:
        return 0
    out = 0
    for a in range(int(L / u) + 1):
        for b in range(int((L - a * u) / v) + 1):
            out += int((L - a * u - b * v) / w) + 1
    return out


def limit_cdf(t):
    A, B = 2 * log(2), log(3)
    return (1 - max(1 - A * t, 0) ** 3
            - max(1 - B * t, 0) ** 3
            + max(1 - (A + B) * t, 0) ** 3)


def test():
    for a in range(100):
        for b in range(100):
            assert exponent_time(a, b) == closed_time(a, b), (a, b)
    print('exact exponent recurrence: 10,000 pairs')

    c0 = 0
    for a in range(8):
        for b in range(6):
            for c in range(4):
                n = 2**a * 3**b * 5**c
                steps, reached = direct_time(n)
                assert steps == closed_time(a, b)
                assert reached == (5**c if a == b == 0 else 12 * 5**c)
                c0 += 1
    print('independent modular Fibonacci ranks:', c0, 'triples')

    for L in (15, 30):
        for t in (0.1, 0.25, 0.5, 0.75, 1.0):
            K, J = int(2 * t * L), int(t * L)
            u, v, w = log(2), log(3), log(5)
            direct = sum(1 for a in range(int(L / u) + 1)
                         for b in range(int((L - a * u) / v) + 1)
                         for c in range(int((L - a * u - b * v) / w) + 1)
                         if a <= K and b <= J)
            inclusion = (q_count(L) - q_count(L - u * (K + 1))
                         - q_count(L - v * (J + 1))
                         + q_count(L - u * (K + 1) - v * (J + 1)))
            assert direct == inclusion, (L, t, direct, inclusion)
    print('finite simplex inclusion-exclusion: 10 cases')

    A, B = 2 * log(2), log(3)
    mu = 1 / (4 * A) + 1 / (4 * B) - 1 / (4 * (A + B))
    for L in (15, 30, 60, 120):
        points = []
        for a in range(int(L / log(2)) + 1):
            for b in range(int((L - a * log(2)) / log(3)) + 1):
                c_count = int((L - a * log(2) - b * log(3)) / log(5)) + 1
                points.append((closed_time(a, b), c_count))
        size = sum(v for _, v in points)
        for t in (0.1, 0.25, 0.5, 0.75, 1.0):
            empirical = sum(v for h, v in points if h <= t * L) / size
            assert abs(empirical - limit_cdf(t)) < 0.12
        empirical_mean = sum(h * v for h, v in points) / (size * L)
        assert abs(empirical_mean - mu) < 0.05
        print('log cutoff', L, 'sample size', size,
              'mean/lnX', round(empirical_mean, 8), 'limit', round(mu, 8))
    print('All finite checks passed; asymptotic assertions require proof.')


if __name__ == '__main__':
    test()
