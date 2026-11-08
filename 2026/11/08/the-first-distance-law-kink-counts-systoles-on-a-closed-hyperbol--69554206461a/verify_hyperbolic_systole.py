"""Numerical checks of universal hyperbolic-lens and systolic orbital asymptotics.

Run: python3 verify_hyperbolic_systole.py
Uses only Python standard library. Numerical checks are not an exhaustive proof.
"""
import math


def gauss_legendre(n):
    pts = []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(15):
            p0, p1 = 1.0, x
            for j in range(2, n + 1):
                p0, p1 = p1, ((2 * j - 1) * x * p1 - (j - 1) * p0) / j
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 2e-15:
                break
        pts.append((x, 2.0 / ((1 - x * x) * dp * dp)))
    return pts


NODES = gauss_legendre(80)


def integrate(f, a, b):
    if b <= a:
        return 0.0
    scale, center = (b - a) / 2, (a + b) / 2
    return scale * sum(w * f(center + scale * x) for x, w in NODES)


def lens_angle(r, d):
    if d >= 2 * r:
        return 0.0
    if d <= 0:
        return 2 * math.pi * (math.cosh(r) - 1)
    a = math.acos(min(1.0, math.tanh(d / 2) / math.tanh(r)))
    b = math.acos(min(1.0, math.sinh(d / 2) / math.sinh(r)))
    return 4 * (math.cosh(r) * a - b)


def lens_slice(r, d):
    if d >= 2 * r:
        return 0.0
    ymax = math.acosh(math.cosh(r) / math.cosh(d / 2))
    return 4 * integrate(
        lambda y: math.cosh(y) * max(
            0., math.acosh(max(1., math.cosh(r) / math.cosh(y))) - d / 2
        ), 0, ymax
    )


def collar(ell, eps, lens=lens_angle):
    s = math.sinh(ell / 2)
    r = ell / 2 + eps
    tmax = math.acosh(math.sinh(r) / s)
    return 2 * ell * integrate(
        lambda t: math.cosh(t) * lens(r, 2 * math.asinh(s * math.cosh(t))),
        0, tmax
    )


def run():
    cases = [(0.3, 0.29), (1., 1.5), (1., 0.2), (2., 3.4), (3., 5.5)]
    for r, d in cases:
        a, b = lens_angle(r, d), lens_slice(r, d)
        assert abs(a-b) < 2e-8 * max(1., a), (r, d, a, b)
    for ell in (0.5, 2., 4.):
        for eps in (0.01, 0.005):
            a = collar(ell, eps)
            assert a > 0
            predicted = 2 * math.pi * ell * eps * eps
            assert abs(a / predicted - 1) < 3.0 * eps / min(ell, 1.0) + .004
        r1 = collar(ell, 0.01) / (ell * 0.01**2)
        r2 = collar(ell, 0.005) / (ell * 0.005**2)
        extrap = 2 * r2 - r1
        assert abs(extrap - 2 * math.pi) < 0.009, (ell, r1, r2, extrap)
        # Independent angular lens and Fermi-slice quadrature agree in a collar.
        q1, q2 = collar(ell, 0.025), collar(ell, 0.025, lens_slice)
        assert abs(q1 - q2) < 4e-7 * max(1., q1), (ell, q1, q2)
        print('ell=%.2f normalized=%.9f extrapolated=%.9f' % (ell, r2, extrap))
    # The one-sided quadratic coefficient corresponds to a jump of twice its magnitude.
    area, ell, count = 4 * math.pi, 1., 3
    c = 2 * math.pi * count * ell / area**2
    jump = -4 * math.pi * count * ell / area**2
    assert abs(jump + 2*c) < 1e-14
    print('HYPERBOLIC_SYSTOLE_CHECK_OK lenses=%d collar_lengths=3' % len(cases))


if __name__ == '__main__':
    run()
