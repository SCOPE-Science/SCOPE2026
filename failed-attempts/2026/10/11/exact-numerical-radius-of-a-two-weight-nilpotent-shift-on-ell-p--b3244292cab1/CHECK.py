"""Independent numerical diagnostics for a three-coordinate Banach numerical radius.

This script samples the original variational quotient; its samples are not a
mathematical proof of global optimality. The proof is supplied in RESULT.md.
"""
import math
import random


def radius(p, a, b):
    if not (p > 1 and a > 0 and b > 0):
        raise ValueError("requires p>1 and positive weights")
    r = b / a
    power = p - 1.0
    log_coeff = ((p - 2.0) / power) * math.log(power) + (p / power) * math.log(r)
    def logterms(z):
        x = power * z
        y = log_coeff + z
        m = max(x, y)
        return m + math.log(math.exp(x - m) + math.exp(y - m))
    target = math.log(power)
    lo, hi = -10.0, 10.0
    while logterms(lo) >= target:
        lo *= 2.0
    while logterms(hi) <= target:
        hi *= 2.0
    for _ in range(210):
        mid = 0.5 * (lo + hi)
        if logterms(mid) < target:
            lo = mid
        else:
            hi = mid
    z = 0.5 * (lo + hi)
    log_A = (power / p) * z
    log_C = (math.log(b / (power * a)) + log_A) / power
    A, C = math.exp(log_A), math.exp(log_C)
    val = (power / p) * a / A
    return val, A, C


def quotient(p, a, b, A, B, C):
    return (a * A ** (p - 1.0) * B + b * B ** (p - 1.0) * C) / (A ** p + B ** p + C ** p)


def test():
    rng = random.Random(42118)
    cases = [(2., 1., 1.), (4., 1., 1.), (3., 2., 1.),
             (1.5, 1., 3.), (10., 2., 1.), (1.2, 1., 2.)]
    for p, a, b in cases:
        val, A, C = radius(p, a, b)
        assert abs(quotient(p, a, b, A, 1., C) - val) <= 3e-13 * max(1., val)
        for _ in range(10000):
            xs = [math.exp(rng.uniform(-14., 14.)) for i in range(3)]
            xs = [t / max(xs) for t in xs]
            sampled = quotient(p, a, b, *xs)
            assert sampled <= val * (1. + 1.e-12), (p, a, b, sampled, val)
        print("case", p, a, b, "radius", format(val, '.15g'))
    for a, b in [(1., 1.), (2., 1.), (1., 4.)]:
        r, _, _ = radius(2., a, b)
        assert abs(r - math.hypot(a, b) / 2) <= 2e-14
    for p in [1.5, 2., 3., 4., 10.]:
        for a, b in [(1., 1.), (2., 1.), (1., 2.)]:
            q = p / (p - 1.)
            r1, _, _ = radius(p, a, b)
            r2, _, _ = radius(q, b, a)
            assert abs(r1 - r2) <= 2e-11 * max(r1, r2), (p, a, b, r1, r2)
    print("Diagnostics completed: 60,000 direct quotient samples, 3 Hilbert checks, 15 duality checks.")


if __name__ == '__main__':
    test()
