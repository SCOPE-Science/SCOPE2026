"""Standalone numerical cross-checks for circular maximal-minimal spacing.

Run with: python3 check.py
All probability limits require the analytical argument in RESULT.md;
these finite checks do not establish an infinite-sample limit.
"""
import itertools
import math
import random


def min_cyclic_gap(points):
    v = sorted(x % 1.0 for x in points)
    gaps = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    gaps.append(1.0 + v[0] - v[-1])
    return min(gaps)


def j3_numeric(a, k, steps=4096):
    total = 0.0
    for i in range(steps):
        u = (i + 0.5) / steps
        product = 1.0
        for j in range(3):
            product *= 1.0 + a * math.cos(2 * math.pi * k * (u + j / 3))
        total += product
    return total / steps


def main():
    checks = 0
    a = 0.4
    for k in range(1, 16):
        expected = 1 + 1.5 * a * a if k % 3 == 0 else 1 - 0.75 * a * a
        actual = j3_numeric(a, k)
        assert abs(actual - expected) < 2e-12, (k, actual, expected)
        checks += 1

    # Cyclic and permutation symmetry, and deterministic event/count equivalence.
    nodes = [0 / 19, 1 / 19, 4 / 19, 7 / 19, 11 / 19, 15 / 19]
    for m in (2, 3, 4, 5):
        for eps in (0.01, 0.04):
            values = [min_cyclic_gap(s) for s in itertools.combinations(nodes, m)]
            wc = sum(t >= 1 / m - eps for t in values)
            best = max(values)
            assert (wc > 0) == (1 / m - best <= eps + 1e-14)
            checks += 1
            for s in itertools.combinations(nodes, m):
                v0 = min_cyclic_gap(s)
                assert abs(v0 - min_cyclic_gap([(x + 0.223) % 1 for x in s])) < 1e-12
                checks += 1

    # Numerical Dirichlet-simplex volume calibration for one m-tuple.
    rng = random.Random(524801)
    trials = 130000
    for m, eps in ((2, 0.14), (3, 0.095), (4, 0.078)):
        successes = 0
        for _ in range(trials):
            sample = [rng.random() for i in range(m)]
            successes += min_cyclic_gap(sample) >= 1 / m - eps
        empirical = successes / trials
        exact = (m * eps) ** (m - 1)
        # Five standard deviations plus a conservative numerical margin.
        allowed = 5.0 * math.sqrt(exact * (1 - exact) / trials) + 0.001
        assert abs(empirical - exact) < allowed, (m, empirical, exact, allowed)
        checks += 1
        print('m={}, epsilon={:.3f}: empirical={:.6f}, exact={:.6f}'.format(
            m, eps, empirical, exact))

    for m in range(2, 8):
        for n in range(m, 35):
            eps = 0.2 * n ** (-m / (m - 1))
            expectation = math.comb(n, m) * (m * eps) ** (m - 1)
            asymptotic = (m ** (m - 1) / math.factorial(m)) * 0.2 ** (m - 1)
            assert expectation > 0
            assert expectation <= asymptotic * (1 + 1e-11)
            checks += 1

    print('PASS: {} deterministic assertions, plus {} seeded Bernoulli trials'.format(
        checks, 3 * trials))

if __name__ == '__main__':
    main()
