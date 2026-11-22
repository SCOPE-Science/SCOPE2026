"""Numerical diagnostics for the near-minimum width laws of two orthogonal disks.

Run with Python 3 and NumPy/SciPy:
    python checks/width_tail_checker.py

Finite quadrature is used only to cross-check the analytic limit statements.
"""
import math
import numpy as np
from scipy.special import roots_legendre

SQ2 = math.sqrt(2.0)


def width_from_support(u, delta):
    x, y, z = u
    a = math.hypot(x, y)
    b = math.hypot(y, z)
    return max(a - delta * y / 2, b + delta * y / 2) + max(a + delta * y / 2, b - delta * y / 2)


def width_folded(y, q, delta):
    a = np.sqrt((1 + y*y + q)/2)
    b = np.sqrt((1 + y*y - q)/2)
    return a + b + np.maximum(a-b, delta*y)


def profile(lam):
    u = 2 * SQ2 / (SQ2 * (math.sqrt(lam*lam + 2*SQ2) + lam))  # cancellation-free
    # Equivalent to (sqrt(lam^2 + 2sqrt(2)) - lam)/sqrt(2)
    return 2 / math.pi * (SQ2*u - u**3/3)


def folded_quadrature(delta, eps, n=520):
    """Deterministic Gauss integration of folded coordinates near the minimum."""
    nodes, weights = roots_legendre(n)
    y_limit = min(1, 1.6 * (eps / delta if delta else math.sqrt(SQ2*eps)))
    q_limit = min(1, 1.6 * SQ2 * eps)
    ys = (nodes + 1) * y_limit / 2
    yws = weights * y_limit / 2
    qs = (nodes + 1) * q_limit / 2
    qws = weights * q_limit / 2
    p = 0.
    for y, dy in zip(ys, yws):
        permitted = qs < 1 - y*y
        selected = permitted & (width_folded(y, qs, delta) < SQ2 + eps)
        den = np.sqrt((1-y*y)**2 - qs[selected]**2)
        p += dy * (2 / math.pi) * np.dot(qws[selected], 1/den)
    return p


def run():
    checks = 0
    rng = np.random.default_rng(325981)
    for delta in (0., 0.02, 0.5, 1., 2., 8.):
        for _ in range(100):
            u = rng.standard_normal(3)
            u /= np.linalg.norm(u)
            x, y, z = u
            w1 = width_from_support(u, delta)
            w2 = width_folded(abs(y), abs(x*x-z*z), delta)
            assert abs(w1-w2) < 1e-12
            assert SQ2 - 1e-12 <= w1 <= 2 + delta + 1e-12
            checks += 2
        for x in (-1, 1):
            for z in (-1, 1):
                assert abs(width_from_support([x/SQ2, 0, z/SQ2], delta)-SQ2) < 1e-12
                checks += 1
        for sign in (-1, 1):
            assert abs(width_from_support([0, sign, 0], delta)-(2+delta)) < 1e-12
            checks += 1
    assert abs(profile(0) - 4*2**.75/(3*math.pi)) < 1e-14
    checks += 1
    vals = [profile(v) for v in (0,.2,1,2,10,100)]
    assert all(a>b for a,b in zip(vals, vals[1:]))
    assert abs(profile(500)*500/(2*SQ2/math.pi)-1) < 1e-5
    checks += 2
    for delta in (0., .5, 1., 2.):
        eps = .001
        expected = profile(0)*eps**1.5 if delta == 0 else (2*SQ2/(math.pi*delta))*eps**2
        actual = folded_quadrature(delta,eps,n=600)
        assert abs(actual/expected-1) < .015, (delta, actual/expected)
        checks += 1
    for lam in (0., .5, 1., 2., 4.):
        eps = .002
        actual = folded_quadrature(lam*math.sqrt(eps),eps,n=560)
        expected = profile(lam)*eps**1.5
        assert abs(actual/expected-1) < .025, (lam,actual/expected)
        checks += 1
    print(f"WIDTH_TAIL_CHECKS_OK {checks}")

if __name__ == '__main__':
    run()
