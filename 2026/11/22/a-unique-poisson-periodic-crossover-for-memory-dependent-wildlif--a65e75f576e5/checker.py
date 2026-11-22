#!/usr/bin/env python3
"""Independent arithmetic checks for a two-cadence habituation theorem.

This program tests formulas and example values; the proof of uniqueness
and the claims over continuous parameter ranges are in RESULT.md.
Only the Python standard library is required.
"""
import math
import random


def j_series(k):
    # Integral_0^k (1-exp(-u))/u du, via its absolutely convergent series.
    term = k
    total = term
    for n in range(2, 151):
        term *= -k * (n - 1) / (n * n)
        total += term
        if abs(term) < 1e-16 * max(1.0, abs(total)):
            break
    return total


def j_integral(k):
    # Independent numerical quadrature by composite Simpson.
    count = 4096
    step = k / count
    def f(u):
        return -math.expm1(-u) / u if u else 1.0
    z = f(0.0) + f(k)
    for i in range(1, count):
        z += (4 if i % 2 else 2) * f(i * step)
    return z * step / 3


def bern(y):
    if y > 650:
        return 0.0
    return y / math.expm1(y)


def threshold_y(k):
    target = j_integral(k) / k
    lo, hi = 0.0, 50.0
    for _ in range(150):
        mid = (lo + hi) / 2.0
        if bern(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def exp_periodic(k, g, rate):
    z = g / rate
    if z > 650:
        return 1.0
    return math.exp(-k / math.expm1(z))


def exp_poisson(k, g, rate):
    return math.exp(-rate * j_integral(k) / g)


def bisect(f, lo, hi):
    fl = f(lo)
    assert fl * f(hi) < 0
    for _ in range(120):
        mid = (lo + hi) / 2
        fm = f(mid)
        if fl * fm > 0:
            lo, fl = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def empirical_laplace(k, g, rate, samples=14000):
    # Stationary pre-arrival Poisson history, truncated at 30 memory lifetimes.
    rng = random.Random(250710 + int(1e4 * rate))
    maximum_age = 30.0 / g
    total = 0.0
    for _ in range(samples):
        age, memory = 0.0, 0.0
        while True:
            age += rng.expovariate(rate)
            if age > maximum_age:
                break
            memory += math.exp(-g * age)
        total += math.exp(-k * memory)
    return total / samples


def main():
    checks = 0
    for k in (0.02, 0.1, 0.3, 1.0, 2.5, 4.0, 8.0):
        a, b = j_series(k), j_integral(k)
        assert abs(a - b) < 1e-10, (k, a, b)
        assert 0 < b < k
        checks += 2

    rng = random.Random(81923)
    last_rate = None
    for k in (0.02, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0):
        crit = 1 / threshold_y(k)
        if last_rate is not None:
            assert crit < last_rate
        last_rate = crit
        checks += 1
    for _ in range(300):
        k = 10 ** rng.uniform(-1.6, 0.85)
        g = 10 ** rng.uniform(-1, 1)
        rate_cross = g / threshold_y(k)
        assert 0 < rate_cross < math.inf
        ep_l = exp_poisson(k, g, rate_cross * 0.35)
        er_l = exp_periodic(k, g, rate_cross * 0.35)
        ep_h = exp_poisson(k, g, rate_cross * 3.0)
        er_h = exp_periodic(k, g, rate_cross * 3.0)
        assert ep_l < er_l, (k, g, rate_cross, ep_l, er_l)
        assert ep_h > er_h, (k, g, rate_cross, ep_h, er_h)
        assert abs(exp_poisson(k,g,rate_cross)-exp_periodic(k,g,rate_cross)) < 1e-12
        checks += 4

    k = g = 1.0
    J = j_integral(k)
    cross = g / threshold_y(k)
    assert abs(J - 0.7965995992970532) < 1e-12
    assert abs(cross - 2.279008229726589) < 2e-10
    checks += 2
    a,b = 0.01,0.5
    for rate, expected_pois, expected_periodic in (
        (0.5, 0.17286517345090152, 0.21877910774117448),
        (5.0, 0.09657425936480699, 0.0773137556356564),
    ):
        rp = rate * (a + b * exp_poisson(k,g,rate))
        rr = rate * (a + b * exp_periodic(k,g,rate))
        assert abs(rp - expected_pois) < 1e-12
        assert abs(rr - expected_periodic) < 1e-12
        checks += 2
    # The positive response floor changes the stationary rate derivative only.
    def derivative_x(x, ratio):
        return ratio + (1.0-x)*math.exp(-x)
    ratio = a / b
    assert ratio < math.exp(-2)
    x1 = bisect(lambda x:derivative_x(x,ratio),1,2)
    x2 = bisect(lambda x:derivative_x(x,ratio),2,12)
    assert abs(x1-1.057588370364254) < 1e-11
    assert abs(x2-5.391751018178341) < 1e-11
    assert derivative_x(.5,ratio)>0>derivative_x(3,ratio)
    assert derivative_x(10,ratio)>0
    for ratio2 in (math.exp(-2),.2,1.,5.):
        assert all(derivative_x(i/100,ratio2) >= -1e-14 for i in range(1,2501))
    checks += 7

    # Empirical stochastic history is an independent simulation check.
    for rate in (0.5, 5.0):
        simulated = empirical_laplace(k,g,rate)
        expected = exp_poisson(k,g,rate)
        assert abs(simulated - expected) < 0.015, (simulated,expected)
        checks += 1
    print('PASS: %d deterministic assertions plus 28,000 Monte Carlo histories' % checks)
    print('J(1)=%.15f; unique crossing rate at k=g=1: %.12f' % (J,cross))
    print('Poisson rate stationary extrema, example: %.12f %.12f' % (x1/J,x2/J))


if __name__ == '__main__':
    main()
