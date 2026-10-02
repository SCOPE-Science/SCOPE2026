"""Reproduce the two scalar constants in the Möbius-shrinker area profile."""
from math import sinh, cosh, exp, sqrt


def bisect(f, lo, hi, steps=100):
    flo = f(lo)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if flo * fm <= 0.0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def radius(a):
    return sqrt((3.0 * cosh(2.0 * a) - 1.0) / 2.0)


def ratio(a):
    return sqrt(2.0) * (3.0 * sinh(2.0 * a) + 2.0 * a) / (3.0 * cosh(2.0 * a) - 1.0)


a_star = bisect(lambda a: 3.0 * a * sinh(2.0 * a) - 4.0, 0.0, 2.0)
a_cross = bisect(lambda a: 2.0 * a + 1.0 - 3.0 * exp(-2.0 * a), 0.0, 2.0)

print(f"a_star={a_star:.13f}")
print(f"R_star={radius(a_star):.13f}")
print(f"ratio_max={ratio(a_star):.13f}")
print(f"a_cross={a_cross:.13f}")
print(f"R_cross={radius(a_cross):.13f}")
