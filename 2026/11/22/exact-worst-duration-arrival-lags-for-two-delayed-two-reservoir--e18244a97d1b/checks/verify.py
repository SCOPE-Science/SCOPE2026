"""Independent numerical and exact-rational checks for a two-pulse threshold-duration theorem.

Run with Python 3 standard library; no external dependencies.
The continuous-parameter theorem is proved in RESULT.md, not by these tests.
"""
from fractions import Fraction as F
from math import exp, e
import random


def lower_upper_exp(x, n=60):
    """Rational enclosure exp(x), x>=0, using a geometric bound on the tail."""
    x = F(x)
    assert 0 <= x < n + 2
    term, partial = F(1), F(1)
    for k in range(1, n + 1):
        term *= x / k
        partial += term
    next_term = term * x / (n + 1)
    return partial, partial + next_term / (1 - x / (n + 2))


def enclose_f(x):
    x = F(x)
    lo, hi = lower_upper_exp(x)
    return x / hi, x / lo


def f(t):
    return t * exp(-t) if t >= 0.0 else 0.0


def bisect_decreasing(target, start=1.0):
    lo, hi = start, max(start + 1.0, 2.0)
    while f(hi) >= target:
        hi *= 2.0
    for _ in range(90):
        m = (lo + hi) / 2.0
        if f(m) > target:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2.0


def bisect_increasing(target):
    lo, hi = 0.0, 1.0
    for _ in range(90):
        m = (lo + hi) / 2.0
        if f(m) < target:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2.0


def K(d):
    z = exp(-d)
    return (1.0 + z) * exp(d * z / (1.0 + z))


def c(d):
    return d / (1.0 + exp(-d))


def width(level):
    if level >= 1.0 / e:
        return 0.0
    return bisect_decreasing(level) - bisect_increasing(level)


def T_formula(level, delay):
    if level >= 2.0 / e:
        return 0.0
    kd = K(delay)
    if level >= 1.0 / e:
        return width(level / kd)
    a, b = bisect_increasing(level), bisect_decreasing(level)
    if delay < a:
        return width(level / kd)
    if delay > b:
        return b - a + width(level / kd)
    return c(delay) + bisect_decreasing(level / kd) - a


def time_above_direct(level, delay):
    """Numerical independent crossing integrator on shape-monotonic intervals."""
    upper = max(36.0, delay + 36.0)
    def q(t):
        return f(t) + f(t - delay) - level
    knots = sorted(set([0.0, min(delay, 1.0), delay, c(delay) + 1.0, upper]))
    roots = []
    for x, y in zip(knots, knots[1:]):
        if q(x) * q(y) < 0:
            lo, hi = x, y
            for _ in range(60):
                mid = (lo + hi) / 2.0
                if q(lo) * q(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            roots.append((lo + hi) / 2.0)
    endpoints = sorted([0.0, *roots, upper])
    return sum(y - x for x, y in zip(endpoints, endpoints[1:])
               if q((x + y) / 2.0) > 0)


def main():
    # A mathematical certificate, not a numerical approximation: all inequalities
    # use Fraction bounds for exp at rational arguments.
    h = F(1, 4)
    assert enclose_f(F(357, 1000))[1] < h
    assert enclose_f(F(358, 1000))[0] > h
    assert enclose_f(F(2153, 1000))[0] > h
    assert enclose_f(F(2154, 1000))[1] < h
    # At t=4.65, delayed discharge with b in (2.153,2.154)
    # exceeds 1/4 on its strictly decreasing final branch.
    assert enclose_f(F(465, 100))[0] + enclose_f(F(2497, 1000))[0] > h
    assert enclose_f(F(33, 10))[1] < h / 2
    # Therefore delayed duration > 4.65-0.358 = 4.292,
    # and synchronous duration < 3.3, an exact strict comparison.
    a = bisect_increasing(.25)
    b = bisect_decreasing(.25)
    sync, delayed = T_formula(.25, 0.0), T_formula(.25, b)
    assert abs(a - .3574029561813889) < 1e-12
    assert abs(b - 2.15329236411035) < 1e-12
    assert abs(sync - 3.117264331438979) < 1e-10
    assert abs(delayed - 4.293100050524549) < 1e-10
    assert delayed > sync * 1.37

    rng = random.Random(902031)
    worst_error = 0.0
    for _ in range(1100):
        level = rng.uniform(.015, .733)
        delay = rng.uniform(0.0, 12.0)
        error = abs(T_formula(level, delay) - time_above_direct(level, delay))
        worst_error = max(worst_error, error)
        assert error < 2e-8, (level, delay, error)
    for level in [.03, .06, .125, .2, .25, .32, .36, .365]:
        b = bisect_decreasing(level)
        global_value = max(T_formula(level, 0), T_formula(level, b))
        for j in range(1001):
            delay = 5.0 * b * j / 1000.0
            assert T_formula(level, delay) <= global_value + 2e-10
    for level in [.368, .4, .5, .6, .7]:
        optimum = T_formula(level, 0)
        for delay in [.01, .1, 1, 3, 10, 20]:
            assert T_formula(level, delay) < optimum
    print("VERIFY_OK rational_exponential_certificate=PASS randomized_crossings=1100"
          " grid_dominance=8008 subpeak_cases=30 max_abs_error=%.3g" % worst_error)


if __name__ == '__main__':
    main()
