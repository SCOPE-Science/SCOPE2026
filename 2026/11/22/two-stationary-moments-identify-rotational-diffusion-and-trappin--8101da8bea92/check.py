"""Reproduce exact moments and global two-snapshot inversion for a trapped active Brownian particle.

Python 3 standard library only; analytic monotonicity is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def active_exact(d, q):
    """Dimensionless athermal stationary moments via an independent generator recurrence."""
    moments = {(0, 0): F(1)}
    for b in range(2, 5, 2):
        moments[0, b] = F(b - 1, b + d - 2) * moments[0, b - 2]
    for a in range(1, 5):
        for b in range(5 - a):
            if (a + b) % 2:
                continue
            inp = a * moments[(a - 1, b + 1)]
            if b >= 2:
                inp += q * b * (b - 1) * moments[(a, b - 2)]
            moments[(a, b)] = inp / (a + q * b * (b + d - 2))
    return moments[(2, 0)], moments[(4, 0)] - 3 * moments[(2, 0)] ** 2


def prediction(d, speed, thermal_D, kappa, rotational_D):
    q = rotational_D / kappa
    x = 1.0 / kappa
    active = (speed * x) ** 2 / (d * (1 + (d - 1) * q))
    variance = thermal_D * x + active
    f = (3 + (4 * d - 1) * q) / ((1 + d * q) * (3 + (d - 1) * q))
    cumulant4 = -6 * active**2 * f / (d + 2)
    return variance, cumulant4


def invert(d, speed, thermal_D, variance, cumulant4):
    assert d >= 2 and speed > 0 and thermal_D >= 0 and variance > 0
    a0 = speed**2 / d
    x0 = 2 * variance / (thermal_D + sqrt(thermal_D**2 + 4 * a0 * variance))
    top = 6 * (variance - thermal_D * x0) ** 2 / (d + 2)
    assert -top < cumulant4 < 0, 'fourth cumulant outside sharp open attainable interval'
    target = -cumulant4

    def at(q):
        a = speed**2 / (d * (1 + (d - 1) * q))
        x = 2 * variance / (thermal_D + sqrt(thermal_D**2 + 4 * a * variance))
        active = variance - thermal_D * x
        f = (3 + (4 * d - 1) * q) / ((1 + d * q) * (3 + (d - 1) * q))
        return 6 * active**2 * f / (d + 2), x

    lo, hi = 0., 1.
    while at(hi)[0] > target:
        hi *= 2
        assert hi < 1e16
    for _ in range(110):
        mid = (lo + hi) / 2
        if at(mid)[0] > target:
            lo = mid
        else:
            hi = mid
    q = (lo + hi) / 2
    _, x = at(q)
    return 1 / x, q / x


def main():
    n = 0
    for d in (2, 3, 4, 5, 9):
        for q in (F(1, 20), F(1, 3), F(1), F(4), F(11)):
            moment2, cum4 = active_exact(d, q)
            m2_expected = 1 / (F(d) * (1 + (d - 1) * q))
            h = (3 + (4 * d - 1) * q) / ((1 + d * q) * (3 + (d - 1) * q))
            k4_expected = -F(6, d + 2) * m2_expected**2 * h
            assert moment2 == m2_expected and cum4 == k4_expected
            n += 2
    for d in (2, 3, 5, 8):
        for speed in (0.7, 1.4):
            for D in (0.0, 0.3, 1.9):
                for kappa in (0.6, 2.1):
                    for Dr in (0.08, 0.7, 3.5):
                        v, k4 = prediction(d, speed, D, kappa, Dr)
                        recovered_k, recovered_r = invert(d, speed, D, v, k4)
                        assert isclose(recovered_k, kappa, rel_tol=2e-9)
                        assert isclose(recovered_r, Dr, rel_tol=2e-9)
                        n += 2
    for d in (2, 5):
        for D in (0., 0.6):
            for q in (0.001, 0.01, 0.1, 1., 10., 100.):
                k = 1.0
                v, k4 = prediction(d, 1, D, k, q * k)
                assert k4 < 0
                n += 1
    print('PASS:', n, 'exact-rational and independent numerical assertions')


if __name__ == '__main__':
    main()
