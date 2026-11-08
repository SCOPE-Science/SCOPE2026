"""Checks for affine least-squares quadrature weight-positivity analysis.

Python 3 standard library only. The probabilistic large-deviation result is
proved analytically in RESULT.md, not by these finite computations.
"""
from fractions import Fraction
from itertools import product
from math import erf, exp, log, pi, sqrt
from random import Random


def simpson(f, lo, hi, intervals=10000):
    assert intervals % 2 == 0
    h = (hi - lo) / intervals
    total = f(lo) + f(hi)
    for i in range(1, intervals):
        total += (4 if i % 2 else 2) * f(lo + i * h)
    return total * h / 3


def weights_exact(xs):
    m = len(xs)
    S = sum(xs)
    Q = sum(x*x for x in xs)
    D = m*Q - S*S
    if D == 0:
        return None
    return [(Q-S*x)/D for x in xs]


def event_bad(xs):
    S = sum(xs)
    Q = sum(x*x for x in xs)
    if S > 0:
        return Q < S*max(xs)
    if S < 0:
        return Q < S*min(xs)
    return False


def test_exact_linear_systems():
    vals = [Fraction(k, 7) for k in (-7, -5, -3, -1, 1, 2, 4, 7)]
    num = 0
    for m in (2, 3, 4):
        for xs in product(vals, repeat=m):
            w = weights_exact(xs)
            if w is None:
                continue
            assert sum(w) == 1
            assert sum(x*y for x, y in zip(xs, w)) == 0
            assert (min(w) < 0) == event_bad(xs)
            num += 1
    return num


def h(t):
    return (sqrt(1+4*t*(1-t))-1)/2


def mgf_erf(t):
    return exp(t/4) * sqrt(pi) * (erf(3*sqrt(t)/2)+erf(sqrt(t)/2))/(4*sqrt(t))


def mgf_integral(t):
    return simpson(lambda x: 0.5*exp(-t*(x*x-x)), -1, 1, 12000)


def mgf_derivative(t):
    return simpson(lambda x: -0.5*(x*x-x)*exp(-t*(x*x-x)), -1, 1, 12000)


def test_exact_three_nodes():
    analytic_integral = pi/8 - 1/4
    assert abs(simpson(h, 0, 1, 12000)-analytic_integral) < 1e-10
    bad_three = (2+pi)/16
    assert abs(bad_three-(1/4+3/4*(2/3)*analytic_integral)) < 1e-12
    rng = Random(38179)
    trials = 210000
    observed = sum(event_bad([rng.uniform(-1, 1) for _ in range(3)]) for _ in range(trials))/trials
    assert abs(observed-bad_three) < 0.006
    return bad_three, observed


def test_exponential_rate():
    for t in (0.1, 0.3, 1, 1.2, 1.5, 4, 7):
        assert abs(mgf_erf(t)-mgf_integral(t)) < 2e-10
    lo, hi = 0.0, 5.0
    assert mgf_derivative(lo) < 0 < mgf_derivative(hi)
    for _ in range(70):
        mid=(lo+hi)/2
        if mgf_derivative(mid)<0:lo=mid
        else:hi=mid
    lam=(lo+hi)/2
    exponent=-log(mgf_erf(lam))
    assert abs(lam-1.26316444) < 3e-7
    assert abs(exponent-0.1727614506) < 2e-8
    for delta in (0.03, 0.1, 0.2):
        # Positive mean and a strict negative region for Y_delta.
        y=lambda x:x*x-(1-delta)*x
        assert simpson(lambda x:y(x)/2, -1, 1) > 0
        assert y((1-delta)/2) < 0
    return lam, exponent


if __name__ == '__main__':
    cases = test_exact_linear_systems()
    p, empirical = test_exact_three_nodes()
    lam, rate = test_exponential_rate()
    print('EXACT_RATIONAL_CASES', cases)
    print('P3_BAD', format(p, '.12f'), 'MONTE_CARLO', format(empirical, '.6f'))
    print('LAMBDA_STAR', format(lam, '.12f'))
    print('EXPONENTIAL_RATE', format(rate, '.12f'))
    print('VERIFY_OK')
