"""Reproduce finite numerical checks of the three-pulse competing-repair theorem.

Requires Python >=3.10, standard library only. The analytic proof, not
this finite test, establishes the universal claim.
"""
import math
import random


def thresholds(a, b, T):
    L = T / 2
    r0 = (b / a) ** 2 * math.exp(-(b - a) * L)
    r1 = (b / a) * (-math.expm1(-b * T)) / (-math.expm1(-a * T))
    return r0, r1


def ratio(a, b, T, x):
    L = T / 2
    if x == 0:
        return thresholds(a, b, T)[0]
    return (b / a) * math.exp(-(b - a) * L) * math.sinh(b * x) / math.sinh(a * x)


def gain(a, b, T, r, t):
    return r * (math.exp(-a * t) + math.exp(-a * (T - t))) - (math.exp(-b * t) + math.exp(-b * (T - t)))


def maximizers(a, b, T, r):
    r0, r1 = thresholds(a, b, T)
    L = T / 2
    if r <= r0:
        return (L,)
    if r >= r1:
        return (0.0, T)
    lo, hi = 0.0, L
    for _ in range(90):
        mid = (lo + hi) / 2
        if ratio(a, b, T, mid) < r:
            lo = mid
        else:
            hi = mid
    x = (lo + hi) / 2
    return (L - x, L + x)


def check():
    rng = random.Random(651593)
    n = 0
    for _ in range(400):
        a = rng.uniform(0.1, 0.8)
        b = a + rng.uniform(0.15, 1.2)
        T = rng.uniform(1.0, 7.0)
        r0, r1 = thresholds(a, b, T)
        assert 0 < r0 < r1
        n += 1
        # Check the monotonically increasing critical-ratio function.
        xs = [T * j / 160.0 for j in range(81)]
        vals = [ratio(a, b, T, x) for x in xs]
        assert all(vals[j] < vals[j + 1] for j in range(80))
        n += 80
        for r in (r0 * 0.5, r0, (r0 + r1) / 2, r1, r1 * 2):
            times = maximizers(a, b, T, r)
            v = gain(a, b, T, r, times[0])
            for j in range(81):
                t = T * j / 80
                assert v >= gain(a, b, T, r, t) - 4e-12
                n += 1
            if len(times) == 2:
                assert abs(gain(a, b, T, r, times[1]) - v) < 4e-12
                n += 1
    a, b, T, r = .3, 1.5, 6.0, 3.0
    t = maximizers(a, b, T, r)[0]
    assert abs(t - .659782178682854) < 1e-12
    assert abs(gain(a, b, T, r, t) - 2.693680142430604) < 1e-11
    n += 2
    print(f"PASS: {n} deterministic numerical assertions")


if __name__ == '__main__':
    check()
