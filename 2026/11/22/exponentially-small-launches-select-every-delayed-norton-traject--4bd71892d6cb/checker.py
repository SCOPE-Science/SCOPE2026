"""Reproducible finite-parameter checks for the finite-sphere departure law.

Uses Python's standard library only. These checks sample parameters; the general
continuum and singular-limit statements are proved analytically in RESULT.md.
"""
from math import asin, exp, log, sin, cos, sqrt, pi, isfinite


def geometry(a, rho, r, c=1.0, g=1.0):
    w = r ** (1.0 / a)
    z = (c / g) * w
    assert 0.0 < z < 0.5
    h = a / (a + 1.0) * (c / g) * w ** (a + 1.0)
    h += rho * z * z / (1.0 + sqrt(1.0 - z * z))
    q = r + rho * asin(z)
    kappa = (c / (a * g)) * w ** (1.0 - a) / sqrt(1.0 - z * z)
    return q, h, kappa


def flight_time(a, rho, T, epsilon=0.01, c=1.0, g=1.0, n=12000):
    """Numerically integrate the exact finite-radius flight time.

    Logarithmic substitution resolves the exponentially thin inner-velocity layer.
    """
    b = (rho * c / g) ** (a / (a - 1.0))
    wb = b ** (1.0 / a)
    eta = exp(-T * sqrt(g / rho))
    speed = b * sqrt(g / rho) * eta
    lo = log(eta) - 28.0
    hi = log(epsilon ** (1.0 / a) / wb)
    assert lo < hi
    def f(u):
        w = wb * exp(u)
        z = (c / g) * w
        qw = a * w ** (a - 1.0) + rho * (c / g) / sqrt(1.0 - z * z)
        h = a / (a + 1.0) * (c / g) * w ** (a + 1.0)
        h += rho * z * z / (1.0 + sqrt(1.0 - z * z))
        return w * qw / sqrt(speed * speed + 2 * g * h)
    d = (hi - lo) / n
    sm = f(lo) + f(hi)
    for j in range(1, n):
        sm += (4.0 if j % 2 else 2.0) * f(lo + d * j)
    return sm * d / 3.0


def point_time(a, epsilon=0.01, c=1.0):
    return 2 * a / (a - 1) * sqrt((a + 1) / (2 * a * c)) * epsilon ** ((a - 1) / (2 * a))


def run():
    assertions = 0
    for a in (1.5, 2.0, 3.0):
        for T in (0.0, 0.3):
            previous = None
            for rho in (0.01, 0.002, 0.0004):
                b = rho ** (a / (a - 1.0))
                assert b / rho < 0.6
                assertions += 1
                t = flight_time(a, rho, T)
                error = abs(t - point_time(a) - T)
                assert isfinite(t) and t > 0
                assertions += 1
                assert error <= 4.5 * sqrt(rho)
                assertions += 1
                if previous is not None:
                    assert error < previous
                    assertions += 1
                previous = error
                # Exact geometry and positivity of normal reaction at sample points.
                v = b / sqrt(rho) * exp(-T / sqrt(rho))
                for fraction in (0.01, 0.1, 1.0):
                    r = 0.01 * fraction
                    q, dh, kappa = geometry(a, rho, r)
                    z = r ** (1 / a)
                    qprime = 1 + rho * kappa
                    # A second expression for q', from direct q differentiation.
                    alt = 1 + rho / (a * r ** (1 - 1 / a) * sqrt(1 - z * z))
                    assert abs(qprime - alt) < 1e-12 * (1 + abs(qprime))
                    assertions += 1
                    normal_per_mass = sqrt(1 - z * z) - (v * v + 2 * dh) * kappa / qprime
                    assert normal_per_mass > 0.5
                    assertions += 1
    print(f'PASS: {assertions} finite-parameter assertions; independent proof in RESULT.md')


if __name__ == '__main__':
    run()
