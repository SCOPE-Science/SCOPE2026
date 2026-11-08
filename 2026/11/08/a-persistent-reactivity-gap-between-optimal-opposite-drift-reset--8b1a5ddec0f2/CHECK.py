#!/usr/bin/env python3
"""Independent arithmetic and differentiation checks for the paired-drift optimum theorem.

No special Python packages or external files are required.
The infinite-parameter theorem relies on the written proof, not these finite checks.
"""
import math


def stationarity(u, p, b, sign):
    """Stable log-derivative stationarity expression (positive means increasing mean)."""
    if not (u > 0 and p > 0 and b > 0 and sign in (-1, 1)):
        raise ValueError("positive u,p,b and signed drift required")
    a = b + p + u
    return (1 + 1 / a) - (1 / u + 1 / (2 * p + u)) * (1 - b * math.exp(-u - (1 + sign) * p) / a)


def optimal_u(p, b, sign):
    lo, hi = 1e-13, 8.0
    assert stationarity(lo, p, b, sign) < 0
    while stationarity(hi, p, b, sign) <= 0:
        hi *= 2
    for _ in range(120):
        mid = (lo + hi) / 2
        if stationarity(mid, p, b, sign) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def optimal_r(p, b, sign):
    u = optimal_u(p, b, sign)
    return u * (u + 2 * p)


def mean_scaled(u, p, b, sign):
    return math.expm1((1 + sign) * p + u) / (u * (u + 2 * p)) + math.exp((1 + sign) * p + u) * (p + u) / (b * u * (u + 2 * p))


def derivative_numerator(u, p, b, sign):
    f = math.exp((1 + sign) * p + u)
    q = f * (1 + (p + u) / b) - 1
    qp = f * (1 + (p + u + 1) / b)
    d = u * (u + 2 * p)
    return d * qp - (2 * u + 2 * p) * q


def coeff(n, p, b, sign):
    const = math.exp((1 + sign) * p)
    return const * (1 + (p + n) / b) / math.factorial(n) - (1 if n == 0 else 0)


def series_h(u, p, b, sign, n=45):
    # Coefficient identity for D q' - D' q; truncate only in test.
    cs = [coeff(j, p, b, sign) for j in range(n + 2)]
    return sum((j - 2) * cs[j] * u ** (j + 1) + 2 * p * (j - 1) * cs[j] * u ** j for j in range(n + 1))


def run():
    tests = 0
    for b in (0.03, 0.2, 1.0, 2.0, 7.0, 30.0):
        for p in (0.005, 0.03, 0.1, 0.5, 1.0, 3.0, 10.0, 100.0, 1000.0):
            low, high = [optimal_u(p, b, sign) for sign in (-1, 1)]
            assert 0 < low < high
            tests += 1
            for sign, u in ((-1, low), (1, high)):
                assert abs(stationarity(u, p, b, sign)) < 2e-12
                assert stationarity(u * 0.99, p, b, sign) < 0
                assert stationarity(u * 1.01, p, b, sign) > 0
                tests += 3
                if p <= 10:
                    assert mean_scaled(u, p, b, sign) < mean_scaled(0.98*u, p, b, sign)
                    assert mean_scaled(u, p, b, sign) < mean_scaled(1.02*u, p, b, sign)
                    tests += 2
    for p, b in ((.3, .8), (1, 3), (.1, 4), (2, .7)):
        for sign in (-1, 1):
            for u in (.05, .5, 1.2, 2.5):
                exact = derivative_numerator(u, p, b, sign)
                approx = series_h(u, p, b, sign)
                assert abs(exact - approx) < 1e-9 * max(1, abs(exact))
                tests += 1
    # Strong-drift coefficient and the nonvanishing opposite-drift gap.
    for b in (.2, 1.0, 2.0, 5.0):
        p = 4000.0
        um = optimal_u(p, b, -1)
        up = optimal_u(p, b, 1)
        approx_um = 1 - (.5 + b / math.e) / p
        approx_up = 1 - .5 / p
        assert abs(p * (um - approx_um)) < 0.05
        assert abs(p * (up - approx_up)) < 0.05
        rm, rp = (um * (um + 2*p), up * (up + 2*p))
        assert abs((rp - rm) - 2*b/math.e) < (2*b/math.e + 1) * 0.005
        tests += 3
    print(f"PASS {tests} deterministic numerical and coefficient checks")
    print('Example D=L=1, k=2, v=6:')
    for sign in (-1, 1):
        print('  drift sign',sign, 'optimal r=',format(optimal_r(3, 1, sign), '.12f'))
    print('Asymptotic dimensional rate gap k/(e L) =', format(2/math.e, '.12f'))


if __name__ == '__main__':
    run()
