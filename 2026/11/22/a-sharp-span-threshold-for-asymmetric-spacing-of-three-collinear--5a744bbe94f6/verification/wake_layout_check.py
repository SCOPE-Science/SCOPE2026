#!/usr/bin/env python3
"""Reproducible finite diagnostics for a three-turbine linear-superposition wake model.

Analytical proof of the all-parameter theorem is in RESULT.md. This checker
is supplementary and does not establish universal assertions by sampling.
"""
from fractions import Fraction as F
from math import isfinite
from random import Random


def h(t, k):
    return (1 + k * t) ** -2


def P(x, L, d, k):
    return 1 + (1 - d * h(x, k)) ** 3 + (1 - d * h(L, k) - d * h(L - x, k)) ** 3


def A(x, L, d, k):
    return 2 * k * (1 + k * x) ** -3 * (1 - d * h(x, k)) ** 2


def B(x, L, d, k):
    return 2 * k * (1 + k * (L - x)) ** -3 * (1 - d * h(L, k) - d * h(L - x, k)) ** 2


def D(x, L, d, k):
    return A(x, L, d, k) - B(x, L, d, k)


def bisect(f, a, b, eps=2e-13):
    fa, fb = f(a), f(b)
    assert fa >= 0 and fb <= 0, (a, b, fa, fb)
    for _ in range(100):
        m = (a + b) / 2
        if f(m) > 0:
            a = m
        else:
            b = m
        if b - a < eps:
            break
    return (a + b) / 2


def critical_span(d, k, minimum):
    lower = 2 * minimum
    upper = max(1, 2 * minimum + 1)
    while D(upper - minimum, upper, d, k) >= 0:
        upper = 2 * upper + 1
    return bisect(lambda L: D(L - minimum, L, d, k), lower, upper)


def max_location(L, d, k, minimum):
    assert L > 2 * minimum
    upper = L - minimum
    if D(upper, L, d, k) >= 0:
        return upper
    return bisect(lambda x: D(x, L, d, k), L / 2, upper)


def main():
    count = 0
    for d in (F(1, 20), F(1, 10), F(1, 5), F(29, 100)):
        for k in (F(1, 2), F(1), F(2)):
            for minimum in (F(0), F(1, 2), F(1)):
                for extra in (F(1, 10), F(1, 2), F(1), F(4), F(10)):
                    L = 2 * minimum + extra
                    xx = [minimum + (L - 2 * minimum) * F(i, 20) for i in range(21)]
                    assert all(1 - d * h(L, k) - d * h(L - x, k) > 0 for x in xx)
                    count += 1
                    aa = [A(x, L, d, k) for x in xx]
                    bb = [B(x, L, d, k) for x in xx]
                    assert all(aa[i] > aa[i + 1] for i in range(20))
                    assert all(bb[i] < bb[i + 1] for i in range(20))
                    count += 40
                    assert D(L / 2, L, d, k) > 0
                    count += 1
                    # Exact rational direct finite-difference *sign* test at midpoints.
                    for i in range(20):
                        lo, hi = xx[i], xx[i + 1]
                        x = (lo + hi) / 2
                        left, right = P(x - F(1, 1000000), L, d, k), P(x + F(1, 1000000), L, d, k)
                        if D(x, L, d, k) > F(1, 100000):
                            assert right > left
                            count += 1
                        if D(x, L, d, k) < -F(1, 100000):
                            assert right < left
                            count += 1
    rng = Random(20261119)
    for j in range(450):
        d = rng.uniform(.005, .299)
        k = rng.uniform(.1, 3.5)
        minimum = rng.uniform(0, 2)
        Lcrit = critical_span(d, k, minimum)
        assert Lcrit > 2 * minimum
        count += 1
        for factor in (.5, .99, 1.01, 2.0, 10.0):
            L = 2 * minimum + (Lcrit - 2 * minimum) * factor
            x = max_location(L, d, k, minimum)
            assert L / 2 < x <= L - minimum + 1e-11
            count += 1
            if factor <= 1:
                assert abs(x - (L - minimum)) < 1e-9
                count += 1
            else:
                assert x < L - minimum
                assert abs(D(x, L, d, k)) < 2e-9
                count += 2
            values = [P(minimum + (L - 2 * minimum) * i / 200, L, d, k) for i in range(201)]
            assert P(x, L, d, k) >= max(values) - 2e-12
            count += 1
    # Highly stable large-span asymptotics, far above threshold.
    for L in (20, 50, 100, 500):
        for d in (.05, .15, .25):
            x = max_location(L, d, 1, .2)
            ratio = (x - L / 2) / (d / (6 * L))
            assert abs(ratio - 1) < .018
            count += 1
    # Published fixed parameter numerical benchmark.
    lc = critical_span(.2, 1, .5)
    assert abs(lc - 1.0617970425831182) < 1e-10
    x = max_location(3, .2, 1, .5)
    assert abs(x - 1.5113339039885152) < 1e-10
    count += 2
    print('Finite checks passed:', count)
    print('critical L for d=0.2, k=1, min_gap=0.5:', format(lc, '.13f'))
    print('optimal middle position at L=3:', format(x, '.13f'))
    print('power gain over midpoint at L=3:', format(P(x, 3, .2, 1) - P(1.5, 3, .2, 1), '.12g'))


if __name__ == '__main__':
    main()
