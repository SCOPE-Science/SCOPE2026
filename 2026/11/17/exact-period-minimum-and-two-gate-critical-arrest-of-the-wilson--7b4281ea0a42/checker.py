"""Numerical diagnostics for the fixed algebraic cycle in a polynomial Lienard flow.

Uses only Python's standard library. This is diagnostic, not a machine proof of
limits; the mathematical argument is given in RESULT.md.
"""
import math


def critical_u():
    lo, hi = 0.5, 1.0
    for _ in range(90):
        u = (lo + hi) / 2
        r = u * (1 - u)
        if 2 * u - 1 < 2 * r ** 1.5:
            lo = u
        else:
            hi = u
    return (lo + hi) / 2


def measure_period_and_log_multiplier(b, steps=262144):
    """Composite midpoint rule, sufficient to show the numerical trend."""
    h = 2 * math.pi / steps
    total_t = total_log = 0.0
    for j in range(steps):
        t = (j + 0.5) * h
        x = math.cos(t)
        y = math.sin(t)
        u = x * x
        f = 1 + x * y * (u - b)
        assert f > 0
        dt = h / f
        total_t += dt
        total_log += -2 * u * (u - b) * dt
    return total_t, total_log


def main():
    u = critical_u()
    r = u * (1-u)
    bm = u - 1 / math.sqrt(r)
    bp = 1 - bm
    assert abs(2*u-1-2*r**1.5) < 1e-12
    C = 2*math.pi*math.sqrt(2*math.sqrt(r)/(3-8*r))
    qm = -2*u*(u-bm)
    qp = 2*(1-u)*(u-bm)
    T0, L0 = measure_period_and_log_multiplier(0.5)
    Tmin = 16*math.pi/math.sqrt(63)
    assert abs(T0 - Tmin) < 1e-9
    t1, _ = measure_period_and_log_multiplier(0.2)
    t2, _ = measure_period_and_log_multiplier(0.8)
    assert abs(t1-t2) < 1e-9
    assert t1 > Tmin
    print('critical b endpoints:', format(bm, '.13f'), format(bp, '.13f'))
    print('exact center period:', format(Tmin, '.13f'))
    print('predicted period prefactor:', format(C, '.13f'))
    print('predicted log-multiplier prefactors:', format(C*qm, '.13f'), format(C*qp, '.13f'))
    for ep in (0.01, 0.001, 0.0001):
        for b, q in ((bm+ep, qm), (bp-ep, qp)):
            T, logmu = measure_period_and_log_multiplier(b)
            print('epsilon', ep, 'b', format(b, '.9f'),
                  'scaled T', format(math.sqrt(ep)*T, '.8f'),
                  'scaled logmu', format(math.sqrt(ep)*logmu, '.8f'),
                  'target', format(C*q, '.8f'))
    print('WILSON_CIRCLE_DIAGNOSTICS_OK')


if __name__ == '__main__':
    main()
