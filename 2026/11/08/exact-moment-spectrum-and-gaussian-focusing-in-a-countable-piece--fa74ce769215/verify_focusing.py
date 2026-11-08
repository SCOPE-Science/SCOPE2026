#!/usr/bin/env python3
"""Exact rational consistency tests for dyadic-strip focusing statistics.

No random sampling, external input files, or third-party packages are needed.
The proof for unrestricted time and real moment orders is in RESULT.md.
"""
from fractions import Fraction as F


def step(x):
    if x == 0:
        return F(1, 4)
    d = 1 - x
    j, edge = 1, F(1, 2)
    while edge > d:
        edge /= 2
        j += 1
    return x + F(1, 2 ** (j + 1))


def iterate(x, n):
    for _ in range(n):
        x = step(x)
    return x


def interval_integral(s, n):
    """Integrate x-deficit^s over the first strip, sum over all strips exactly.

    Each of the 2^n dyadic v-cylinders carries a translation branch of T^n.
    The first-strip conditional coordinate is x=(1-v)/2, v uniform [0,1).
    """
    nb = 2 ** n
    sum_integrals = F(0)
    for k in range(nb):
        mid = F(2 * k + 1, 2 * nb)
        x = F(1, 2) - mid / 2
        deficit = 1 - iterate(x, n)
        # Deficit changes by +/- 1/(4 nb) across a half cylinder.
        low, high = deficit - F(1, 4 * nb), deficit + F(1, 4 * nb)
        assert low > 0
        integral = F(2, s + 1) * (high ** (s + 1) - low ** (s + 1))
        sum_integrals += integral
    # Sum first-strip integral over geometrically scaled strips.
    return sum_integrals * F(2 ** s, 2 ** (s + 1) - 1)


def predicted(s, n):
    g0 = F(2 ** (s + 1) - 1, s + 1)
    g1 = (F(3, 2) ** (s + 1) - F(1, 2) ** (s + 1)) / (s + 1)
    g = [g0, g1]
    for t in range(2, n + 1):
        g.append((g[-1] + g[-2]) / 2 ** (s + 1))
    return g[n] / (2 ** (s + 1) - 1)


def j_of(x):
    d, j, edge = 1 - x, 1, F(1, 2)
    while edge > d:
        edge /= 2
        j += 1
    return j


def check_binary_waits(v, count):
    # For binary digits, each 0 leads to a one-step level gain, each 1 to two.
    x, current, clock = F(1, 2) - v / 2, v, 0
    j = 1
    for _ in range(count):
        bit = (2 * current).numerator // (2 * current).denominator
        wait = 1 + bit
        for internal in range(wait - 1):
            x = step(x)
            clock += 1
            assert j_of(x) == j
        x = step(x)
        clock += 1
        j += 1
        assert j_of(x) == j
        current = 2 * current - bit
    return clock


def main():
    checks = 0
    for s in (1, 2, 3, 4):
        for t in range(0, 11):
            assert interval_integral(s, t) == predicted(s, t), (s, t)
            checks += 1
    for k in range(1, 1024, 2):
        v = F(k, 1024)
        check_binary_waits(v, 10)
        checks += 1
    for t in range(2, 12):
        for v in (F(1, 101), F(2, 3), F(13, 17), F(511, 1024)):
            x = iterate(F(1, 2) - v / 2, t)
            assert x >= F(1, 2)
            checks += 1
    assert predicted(1, 0) == F(1, 2)
    assert predicted(1, 1) == F(1, 3)
    assert predicted(1, 2) == F(5, 24)
    checks += 3
    print(f"PASS: {checks} exact-rational checks (finite corroboration, not an infinite proof).")


if __name__ == '__main__':
    main()
