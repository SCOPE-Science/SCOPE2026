"""Supplementary deterministic checks for a sinusoidal moving-depth interval.

Run: python verification.py
The theorem is analytical; discrete and numerical tests are not a proof.
"""
from math import sin, cos, pi, sqrt, isfinite
from random import Random


def speed(A, h, phi, omega=1.0):
    """None for infeasible; otherwise sharp physical speed."""
    alpha = phi / 2.0
    h0 = 2.0 * A * sin(alpha)
    if h < h0 - 1.0e-12 * A:
        return None
    if h >= 2.0 * A:
        return 0.0
    if abs(h - h0) <= 1.0e-12 * A:
        return omega * A * cos(alpha)
    left, right = alpha, pi / 2.0
    for _ in range(90):
        x = (left + right) / 2.0
        G = 2.0 * A * (sin(x) - (x - alpha) * cos(x))
        if G < h:
            left = x
        else:
            right = x
    return omega * A * cos((left + right) / 2.0)


def sup_quotient(A, h, phi):
    """Independent search in separation using golden section, not root solver."""
    alpha = phi / 2.0
    def f(d):
        return (2.0 * A * sin(alpha + d / 2.0) - h) / d
    lo, hi = 1.0e-9, pi
    invphi = (sqrt(5.0) - 1.0) / 2.0
    x1, x2 = hi - invphi * (hi - lo), lo + invphi * (hi - lo)
    for _ in range(115):
        if f(x1) < f(x2):
            lo = x1
            x1 = x2
            x2 = lo + invphi * (hi - lo)
        else:
            hi = x2
            x2 = x1
            x1 = hi - invphi * (hi - lo)
    return max(0.0, f((lo + hi) / 2.0))


def circle_gap(u, v):
    d = abs((u - v + pi) % (2.0 * pi) - pi)
    return d


def check():
    checks = 0
    rng = Random(20241117)
    for _ in range(1500):
        A = 10.0 ** rng.uniform(-1.5, 1.5)
        phi = rng.uniform(0.0, 2.85)
        h0 = 2.0 * A * sin(phi / 2.0)
        h = h0 + (2.0 * A - h0) * rng.uniform(0.015, 0.985)
        omega = 10.0 ** rng.uniform(-1, 1)
        predicted = speed(A, h, phi, omega)
        optimized = omega * sup_quotient(A, h, phi)
        assert isfinite(predicted)
        assert abs(predicted - optimized) <= 2e-7 * (1.0 + abs(predicted))
        checks += 2
        # Check the necessary pair inequalities on a randomized phase pair.
        t, s = rng.uniform(0, 2 * pi), rng.uniform(0, 2 * pi)
        lower = A * sin(t)
        upper = h + A * sin(s + phi)
        assert lower - upper <= predicted / omega * circle_gap(t, s) + 1.0e-9 * A
        checks += 1
    for phi in (0.0, 0.2, 1.0, 2.1, 2.9, pi):
        A = 3.0
        h0 = 2.0 * A * sin(phi / 2.0)
        assert speed(A, h0, phi) is not None
        assert abs(speed(A, h0, phi) - A * cos(phi / 2.0)) < 1e-10
        assert speed(A, 2.0 * A, phi) == 0.0
        if h0 > 0.0:
            assert speed(A, h0 - 1.0e-5, phi) is None
        checks += 4
    for phi in (0.4, 1.3, 2.2):
        A = 1.0
        h0 = 2.0 * sin(phi / 2.0)
        v0 = cos(phi / 2.0)
        for eps in (1e-5, 1e-6, 1e-7):
            change = v0 - speed(A, h0 + eps, phi)
            approx = sqrt(sin(phi / 2.0) * eps)
            assert abs(change / approx - 1.0) < 0.006
            checks += 1
    for eps in (1e-5, 1e-6, 1e-7):
        change = 1.0 - speed(1.0, eps, 0.0)
        approx = 0.5 * (1.5 * eps) ** (2.0 / 3.0)
        assert abs(change / approx - 1.0) < 0.006
        checks += 1
    for phi in (0.0, 0.6, 1.6, 2.6):
        eps = 1e-6
        delta = speed(1.0, 2.0-eps, phi)
        assert abs(delta / (eps / (pi-phi)) - 1.0) < 1e-5
        checks += 1
    A, phi, h, omega = 1.0, pi/3.0, 1.5, pi/12.0
    assert abs(speed(A,h,phi,omega)-0.07202108385338497)<1e-12
    checks += 1
    print(f"PASSED {checks} deterministic supplementary assertions")

if __name__ == '__main__':
    check()
