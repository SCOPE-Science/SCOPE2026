#!/usr/bin/env python3
"""Finite diagnostics for the Sturmian-decorated renewal pressure theorem.

No external packages or data. These checks are finite only. The all-parameter
and small-activity conclusions are established analytically in RESULT.md.
"""
import bisect
import math

ALPHA = (3.0 - math.sqrt(5.0)) / 2.0
LIMIT = 7000


def factor_profile(alpha, limit):
    """(length, fractional n*alpha, heavy factor count), via rotation cells."""
    dividers = [0.0]
    yield (0, 0.0, 0)
    for n in range(1, limit + 1):
        boundary = (-n * alpha) % 1.0
        position = bisect.bisect_left(dividers, boundary)
        dividers.insert(position, boundary)
        # The heavy-count cells start with this newly inserted boundary.
        heavy = len(dividers) - position
        yield n, (n * alpha) % 1.0, heavy


def check_direct_factors(alpha, profile):
    length = 12000
    digits = [math.floor((i + 1) * alpha) - math.floor(i * alpha)
              for i in range(length)]
    for n, theta, heavy in profile[:13]:
        if n == 0:
            assert heavy == 0
            continue
        words = {tuple(digits[i:i+n]) for i in range(length - n + 1)}
        assert len(words) == n+1, (n, len(words))
        assert all(sum(u) in (math.floor(n*alpha), math.floor(n*alpha)+1)
                   for u in words)
        actual_heavy = sum(sum(u) == math.floor(n*alpha)+1 for u in words)
        assert actual_heavy == heavy, (n, actual_heavy, heavy)
    print('direct Sturmian factor tests: 12 lengths passed')


def coefficient(t, profile):
    return [(n+1-r)*math.exp(-t*theta)+r*math.exp(t*(1-theta))
            for n, theta, r in profile]


def deviation_coefficient(t, profile):
    return [-theta*(n+1-r)*math.exp(-t*theta) +
            (1-theta)*r*math.exp(t*(1-theta))
            for n, theta, r in profile]


def exponential_moments(coeff, delta):
    terms = [v * math.exp(-delta*n) for n, v in enumerate(coeff)]
    return math.fsum(terms), math.fsum(n*v for n,v in enumerate(terms))


def solve_delta(activity, t, alpha, coeff):
    def residual(delta):
        z, _ = exponential_moments(coeff, delta)
        return activity * math.exp(-alpha*t-delta)*z-1
    lo, hi = 1e-5, 1.0
    assert residual(lo) > 0 and residual(hi) < 0
    for _ in range(70):
        mid = (lo+hi)/2
        if residual(mid) > 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def hyperbolic_ratio(t):
    return 1.0 if t == 0.0 else 2*math.sinh(t/2)/t


def log_i_derivative(t):
    return 0.0 if t == 0.0 else math.cosh(t/2)/math.sinh(t/2)-2/t


def main():
    profile = list(factor_profile(ALPHA, LIMIT))
    check_direct_factors(ALPHA, profile)
    tests=0
    for t in (-1.0, 0.0, 1.3):
        coeff = coefficient(t, profile)
        dc = deviation_coefficient(t, profile)
        predicted = math.exp(-ALPHA*t/2)*hyperbolic_ratio(t)
        for activity in (1e-3,1e-4):
            delta = solve_delta(activity, t, ALPHA, coeff)
            scaled = delta/math.sqrt(activity)
            assert abs(scaled/predicted - 1.0) < 0.008, (t, activity, scaled, predicted)
            z, zn = exponential_moments(coeff, delta)
            marker = 1.0/(1.0 + zn/z)
            predicted_marker = predicted*math.sqrt(activity)/2
            assert abs(marker/predicted_marker - 1.0) < 0.008
            centered = math.fsum(v*math.exp(-delta*n) for n,v in enumerate(dc))/z
            color = ALPHA*(1-marker)+marker*centered
            assert abs((color-ALPHA)/marker -
                       (log_i_derivative(t)-ALPHA)) < 0.008
            if t == 0.0:
                exact_pressure=2*math.asinh(math.sqrt(activity)/2)
                exact_marker=math.sqrt(activity)/math.sqrt(4+activity)
                assert abs(delta-exact_pressure)<1e-10
                assert abs(marker-exact_marker)<1e-8
            tests += 1
            print(f't={t:+.1f} activity={activity:.4g} '
                  f'pressure-excess/sqrt(activity)={scaled:.9f} '
                  f'limit={predicted:.9f} '
                  f'marker={marker:.9f} '
                  f'centered-color/marker={(color-ALPHA)/marker:.9f}')
    print('finite pressure/composition diagnostics:', tests, 'passed')

if __name__ == '__main__':
    main()
