"""Independent numerical checks for the two-patch marine-reserve threshold law.

Uses only Python's standard library. Numerical checks supplement, never
replace, the analytic matrix-spectral proof in RESULT.md.
"""
from math import exp, sqrt, log, isclose


def survival(c, m, q, E, R, T):
    """Closed-form two-patch survival for unit initial total mass."""
    h = q * E
    D = sqrt((h - m) ** 2 + 4 * m * h * R)
    w = (1.0 + (m + h * (2 * R - 1)) / D) / 2.0
    slow = -c - (h + m - D) / 2.0
    fast = -c - (h + m + D) / 2.0
    return w * exp(slow * T) + (1 - w) * exp(fast * T)


def survival_series(c, m, q, E, R, T, terms=70):
    """Matrix exponential via independent Taylor summation."""
    h = q * E
    a = -c - h - m * R
    b = m * (1 - R)
    d = m * R
    e = -c - m * (1 - R)
    v0, v1 = 1 - R, R
    total = v0 + v1
    for k in range(1, terms):
        v0, v1 = T * (a * v0 + b * v1) / k, T * (d * v0 + e * v1) / k
        total += v0 + v1
    return total


def reserve_limit(c, m, R, T):
    return R * exp(-(c + m * (1 - R)) * T)


def reserve_critical(c, m, r, T):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if r * reserve_limit(c, m, mid, T) > 1.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def effort_critical(c, m, q, r, R, T):
    target = 1.0 / r
    lo, hi = 0.0, 1.0
    for _ in range(80):
        if survival(c, m, q, hi, R, T) <= target:
            break
        hi *= 2
    else:
        raise AssertionError("finite effort cutoff not bracketed")
    for _ in range(100):
        mid = (lo + hi) / 2
        if survival(c, m, q, mid, R, T) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def coefficient(c, m, q, r, T):
    Rc = reserve_critical(c, m, r, T)
    return m * Rc * (1 - Rc) * (2 + m * Rc * T) / (q * (1 + m * Rc * T))


def run():
    checks = 0
    for c in (0.1, 0.4, 0.9):
        for m in (0.3, 1.1):
            for q in (0.5, 1.2):
                for R in (0.2, 0.5, 0.83):
                    for E in (0.0, 0.2, 0.8, 1.5, 3.0):
                        for T in (0.2, 0.7):
                            exact = survival(c, m, q, E, R, T)
                            series = survival_series(c, m, q, E, R, T)
                            assert isclose(exact, series, rel_tol=2e-11, abs_tol=2e-11), (exact, series)
                            checks += 1
    for c, m, q, T, r in ((1, 1, .7, .5, 2), (.2, 1.3, .7, .8, 2), (.3, .7, 1.2, .6, 2.1)):
        Rc = reserve_critical(c, m, r, T)
        assert 0 < Rc < 1 and abs(r * reserve_limit(c, m, Rc, T) - 1) < 2e-15
        checks += 1
        B = coefficient(c, m, q, r, T)
        assert B > 0
        prev_err = 1e5
        for gap in (.04, .02, .01, .005, .002, .001):
            R = Rc - gap
            assert R > 0
            E = effort_critical(c, m, q, r, R, T)
            assert E > 0 and abs(r * survival(c, m, q, E, R, T) - 1) < 2e-13
            err = abs(E * gap - B)
            assert err < prev_err
            prev_err = err
            checks += 3
        assert prev_err < .02 * B, (prev_err, B)
        checks += 1
        # First-order asymptotic of survival at fixed protected fraction.
        R = .4
        F_inf = reserve_limit(c, m, R, T)
        C = exp(-(c + m * (1 - R)) * T) * m * R * (1 - R) * (2 + m * R * T)
        errors = []
        for h in (300., 600., 1200., 2400.):
            F = survival(c, m, 1., h, R, T)
            errors.append(abs(h * (F - F_inf) - C))
            checks += 1
        assert errors[-1] < errors[0] / 6.0, errors
        checks += 1
    print(f"PASS: {checks} supplementary exact-formula, matrix-series, and asymptotic checks")
    print("Example: c=1, m=1, q=0.7, r=2, T=0.5")
    c,m,q,T,r=1.,1.,.7,.5,2.
    Rc=reserve_critical(c,m,r,T)
    B=coefficient(c,m,q,r,T)
    print(f"Critical reserve fraction: {Rc:.12f}")
    print(f"Inverse-distance coefficient: {B:.12f}")
    for gap in (.02,.01,.005,.001):
        E=effort_critical(c,m,q,r,Rc-gap,T)
        print(f"gap={gap:.4f}, effort cap={E:.9f}, gap-times-cap={gap*E:.9f}")

if __name__ == "__main__":
    run()
