#!/usr/bin/env python3
"""Reproducible arithmetic checks for the half-logistic Archimedean extension."""
import math
from fractions import Fraction


def q_value(alpha, theta):
    r = math.exp(theta)
    return (r-1)/(r+alpha)


def psi(u, alpha, theta):
    r = math.exp(theta)
    x = math.exp(theta*u)
    return (r+alpha)*(x-1)/((r-1)*(x+alpha))


def inverse_psi(v, alpha, theta):
    q = q_value(alpha, theta)
    return math.log((1+alpha*q*v)/(1-q*v))/theta


def h(t, alpha, theta):
    return inverse_psi(math.exp(-t), alpha, theta)


def w(k, alpha, theta):
    q = q_value(alpha, theta)
    return q**k*(1+(-1)**(k+1)*alpha**k)/(k*theta)


def check():
    # Inversion and boundaries for a wide parameter range.
    for alpha, theta in [(0.1, 0.2), (0.4, math.log(3)),
                         (1, math.log(3)), (2, 0.5), (100, math.log(3))]:
        assert abs(h(0, alpha, theta)-1) < 1e-12
        for u in [0.05, 0.2, 0.5, 0.9]:
            v = psi(u, alpha, theta)
            assert abs(inverse_psi(v, alpha, theta)-u) < 2e-12
        for t in [0.1, 1, 2, 4]:
            assert abs(psi(h(t, alpha, theta), alpha, theta)-math.exp(-t)) < 3e-12

    # For alpha <= 1, the explicit frailty weights are nonnegative and sum to 1.
    for alpha, theta in [(0.2, 0.7), (0.5, math.log(3)), (1, 1.2)]:
        ws = [w(k, alpha, theta) for k in range(1, 401)]
        assert min(ws) >= -1e-15
        assert abs(sum(ws)-1) < 1e-12
        for t in [0, 0.2, 1, 2]:
            assert abs(sum(wk*math.exp(-(k+1)*t) for k, wk in enumerate(ws))-
                       h(t, alpha, theta)) < 2e-12
    assert all(w(k, 1, 1.2) == 0.0 for k in range(2, 16, 2))
    assert all(w(k, 0.5, 0.7) > 0 for k in range(1, 9))

    # The first negative coefficient is exactly w_2 when alpha>1.
    for alpha, theta in [(1.01, 0.1), (2, 1), (100, math.log(3))]:
        q = q_value(alpha, theta)
        assert w(2, alpha, theta) < 0
        assert abs(w(2, alpha, theta) - q*q*(1-alpha*alpha)/(2*theta)) < 1e-12
        # At large t, the signed Laplace series converges absolutely.
        t = max(3, math.log(alpha*q)+3)
        series = sum(w(k, alpha, theta)*math.exp(-k*t) for k in range(1, 61))
        assert abs(series-h(t, alpha, theta)) < 2e-13

    # Rational certificate: (alpha, exp(theta)) = (100,3) fails 3-monotonicity.
    q = Fraction(2, 103)
    a = 100*q
    d3 = q*(1+q)/(1-q)**3 + a*(1-a)/(1+a)**3
    assert d3 == Fraction(21630, 101**3) - Fraction(1998200, 303**3)
    assert d3 < 0  # Equals theta * (-1)^3 h'''(0): violates h''' <= 0.
    print('PASS: inversion, nonnegative and normalized weights, series, negative coefficient, 3D obstruction')
    print('Exact rational theta*(-1)^3*h3(0):', d3)


if __name__ == '__main__':
    check()
