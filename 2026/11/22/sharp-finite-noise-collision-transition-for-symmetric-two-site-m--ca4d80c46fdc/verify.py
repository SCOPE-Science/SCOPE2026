"""Supplementary numerical consistency checks for two-site Matern-3/2 quadrature.

Standard-library Python 3; finite checks are not a proof of continuum optimality.
"""
from math import exp, sqrt, sinh, cosh, isclose

E = exp(-0.5)
ETA_CRIT = 8 * sqrt(exp(1)) - 12
PRIOR = 8 / exp(1) - 2


def kernel(r):
    r = abs(r)
    return (1 + r) * exp(-r)


def mean(s):
    return 4 - 2 * E * (2.5 * cosh(s) - s * sinh(s))


def u(s):
    if s == 0:
        return E
    return 2 * E * (1.5 * sinh(s) / s - cosh(s))


def c(s):
    return (1 + 2 * s) * exp(-2 * s)


def threshold(s):
    return 2 * exp(-2 * s) * mean(s) / u(s) - 1 - c(s)


def reduction(s, eta):
    return 2 * mean(s) ** 2 / (1 + eta + c(s))


def direct_gain(x, y, eta):
    m1, m2, r = mean(x - 0.5), mean(y - 0.5), kernel(x - y)
    a = 1 + eta
    return (a * (m1*m1 + m2*m2) - 2*r*m1*m2) / (a*a-r*r)


def bisect_root(eta):
    lo, hi = 0.0, 0.5
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if threshold(mid) > eta:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def simpson_mean(s, steps=4000):
    # Independent integral formula from the integrated closed form.
    t = 0.5 + s
    dx = 1 / steps
    total = kernel(t) + kernel(1 - t)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * kernel(t - j * dx)
    return total * dx / 3


def main():
    assert isclose(threshold(0), ETA_CRIT, rel_tol=1e-12)
    assert isclose(threshold(0.5), (1 + 2*exp(1) - exp(2))/(exp(1)*(exp(1)-2)), rel_tol=1e-12)
    assert threshold(0.5) < 0 < ETA_CRIT
    for j in range(1, 1000):
        s = j / 2000
        assert u(s) > 0
        assert threshold(s) > threshold(s + 1/2000)
        assert mean(s) > 0
        assert abs(mean(s) - simpson_mean(s)) < 1e-8
    for eta in (0.02, 0.1, 0.2, 0.5, 1.0, ETA_CRIT, 1.5, 5.0):
        s_star = bisect_root(eta) if eta < ETA_CRIT else 0
        best = reduction(s_star, eta)
        assert isclose(best, direct_gain(0.5 - s_star, 0.5 + s_star, eta), abs_tol=2e-13)
        for j in range(1001):
            s = j / 2000
            assert reduction(s, eta) <= best + 2e-12
    print('PASS: 999 integrated-mean, positivity and threshold-monotonicity checks')
    print('PASS: symmetric global grid comparisons for 8 noise levels')
    print('PASS: direct 2x2 Gram inversion and endpoint formulas')
    print('eta_crit=%.15f, noise=0.1 optimal separation=%.12f' % (ETA_CRIT, 2*bisect_root(0.1)))
    print('independently audited: no; finite tests do not establish the analytical theorem')


if __name__ == '__main__':
    main()
