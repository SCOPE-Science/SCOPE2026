"""Reproduce numerical consistency checks for the critical drift of a partially reactive Brownian reset search."""

import math


def critical_shape(u):
    assert u >= 1.0
    return u - u * math.sqrt((u - 1.0) / (u + 1.0)) - math.log1p(u)


def critical_constants():
    lo, hi = 1.0, 4.0
    assert critical_shape(lo) > 0 > critical_shape(hi)
    for _ in range(115):
        mid = (lo + hi) / 2.0
        if critical_shape(mid) > 0:
            lo = mid
        else:
            hi = mid
    u = (lo + hi) / 2.0
    m = u * math.sqrt((u - 1.0) / (u + 1.0))
    s = 2.0 * u * u / (u + 1.0)
    return u, m, s


def stationarity(s, signed_m, eta):
    m = abs(signed_m)
    u = math.sqrt(m * m + s)
    e = math.exp(u + signed_m)
    return e * ((1.0 + eta * u) -
                s * (1.0 + eta * (u + 1.0)) / (2.0 * u)) - 1.0


def stationary_eta_coefficient(s, signed_m):
    m = abs(signed_m)
    u = math.sqrt(m * m + s)
    return math.exp(u + signed_m) * (u - s * (u + 1.0) / (2.0 * u))


def optimizer(signed_m, eta):
    assert eta > 0
    lo = 1e-10
    hi = max(1.0, abs(signed_m))
    assert stationarity(lo, signed_m, eta) > 0
    while stationarity(hi, signed_m, eta) >= 0:
        hi *= 2.0
        assert hi < 1e5
    for _ in range(85):
        mid = (lo + hi) / 2.0
        if stationarity(mid, signed_m, eta) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def mean_time(s, signed_m, eta):
    m = abs(signed_m)
    u = math.sqrt(m * m + s)
    return math.expm1(u + signed_m) / s + eta * u * math.exp(u + signed_m) / s


def run_checks():
    count = 0
    def check(cond, message):
        nonlocal count
        assert cond, message
        count += 1

    uc, mc, sc = critical_constants()
    check(abs(uc - 1.2949521881887404) < 4e-14, 'critical u')
    check(abs(mc - 0.4642401779264712) < 4e-14, 'critical m')
    check(abs(sc - 1.4613822268936053) < 4e-14, 'critical s')
    check(abs(critical_shape(uc)) < 1e-14, 'root residual')
    check(abs(sc - (uc * uc - mc * mc)) < 1e-14, 'critical relation')

    for eta in [0.0002, 0.02, 0.2, 1.0, 5.0, 100.0, 10000.0]:
        s_star = optimizer(-mc, eta)
        check(abs(s_star - sc) < 3e-9, 'exact reactivity-neutral optimizer')
        check(abs(stationarity(sc, -mc, eta)) < 2e-8, 'stationarity at critical')
        check(abs(stationary_eta_coefficient(sc, -mc)) < 1e-14,
              'zero reactivity sensitivity')
        for factor in [0.4, 0.95, 1.05, 2.0]:
            check(mean_time(sc * factor, -mc, eta) > mean_time(sc, -mc, eta),
                  'strict local/global minimization near critical')

    # k increases iff eta decreases; optimum is increasing in k below the threshold.
    etas = [50.0, 10.0, 1.0, 0.2, 0.02, 0.002]
    for m in [0.0, 0.1, 0.3, mc - 0.02]:
        for side in ([-1, 1] if m else [1]):
            rates = [optimizer(side * m, eta) for eta in etas]
            for a, b in zip(rates, rates[1:]):
                check(a < b - 1e-10, 'low drift: increases with trap strength')
    for m in [mc + 0.02, 0.7, 1.0, 2.0, 5.0]:
        rates = [optimizer(-m, eta) for eta in etas]
        for a, b in zip(rates, rates[1:]):
            check(a > b + 1e-10, 'strong inward drift: decreases with trap strength')
    for m in [0.1, 0.4, mc, 0.7, 1.0, 2.0, 5.0]:
        rates = [optimizer(m, eta) for eta in etas]
        for a, b in zip(rates, rates[1:]):
            check(a < b - 1e-10, 'outward drift: increases with trap strength')

    for eta in [0.02, 0.2, 1.0, 20.0, 200.0]:
        for m in [0.0, 0.1, 0.3, mc, 0.55, 1.0, 2.5]:
            for side in ([-1, 1] if m else [1]):
                signed_m = side * m
                s = optimizer(signed_m, eta)
                check(abs(stationarity(s, signed_m, eta)) <
                      1e-8 * max(1.0, math.exp(math.sqrt(m*m+s)+signed_m)),
                      'stationarity identity')
                for factor in [0.2, 0.8, 1.2, 3.0]:
                    check(mean_time(factor * s, signed_m, eta) >
                          mean_time(s, signed_m, eta),
                          'global candidate tests')
                if m:
                    u = math.sqrt(m * m + s)
                    check((u - 1.0 + eta * (u*u + u - 1.0)) > 0,
                          'strict negative derivative of B at optimizer')
    print('PASS:', count, 'numerical consistency assertions')
    print('critical u = %.15f, inward drift m = %.15f, s = %.15f' % (uc, mc, sc))


if __name__ == '__main__':
    run_checks()
