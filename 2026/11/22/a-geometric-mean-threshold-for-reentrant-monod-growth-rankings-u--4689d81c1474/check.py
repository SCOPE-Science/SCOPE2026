"""Exact-arithmetic tests for two-level Monod growth-rank transitions.

Run using Python 3: python check.py
The theorem in RESULT.md is proved analytically, not by these tests.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt


def mean_growth(m, k, v):
    return (m * (m + k) - v) / ((m + k) ** 2 - v)


def ratio(m, k1, k2, v):
    return mean_growth(m, k1, v) / mean_growth(m, k2, v)


def log_ratio_derivative(m, k1, k2, v):
    a1, b1 = m * (m + k1), (m + k1) ** 2
    a2, b2 = m * (m + k2), (m + k2) ** 2
    w1, w2 = k1 * (m + k1), k2 * (m + k2)
    return w2 / ((a2 - v) * (b2 - v)) - w1 / ((a1 - v) * (b1 - v))


def h_ratio(m, k1, k2, v):
    a1, b1 = m * (m + k1), (m + k1) ** 2
    a2, b2 = m * (m + k2), (m + k2) ** 2
    return ((a2 - v) * (b2 - v)) / ((a1 - v) * (b1 - v))


def witness(v):
    return mean_growth(Q(1), Q(1, 5), v) - Q(17, 10) * mean_growth(Q(1), Q(1), v)


def run():
    count = 0
    for j in range(101):
        v = Q(j, 100)
        target = -(175*v*v - 162*v + 24) / (10*(v-4)*(25*v-36))
        assert witness(v) == target
        count += 1
    assert witness(Q(0)) == -Q(1, 60)
    assert witness(Q(1)) == -Q(37, 330)
    assert witness(Q(1, 2)) > 0
    count += 3
    # The roots are (81 +- sqrt(2361))/175. 48^2 < 2361 < 49^2,
    # giving 0 < first root < second root < 1 without floating point.
    assert 48**2 < 2361 < 49**2
    assert (81+49) < 175 and (81-49) > 0
    count += 2
    rng = Random(207507)
    for _ in range(1800):
        m = Q(rng.randint(1, 18), rng.randint(1, 9))
        k1 = Q(rng.randint(1, 15), rng.randint(1, 13))
        k2 = k1 + Q(rng.randint(1, 15), rng.randint(1, 13))
        v1 = m*m*Q(rng.randint(0, 40), 100)
        v2 = m*m*Q(rng.randint(60, 100), 100)
        # Exact average of Monod's two instantaneous responses.
        # When v is a square, this equality can be tested rationally.
        d = m*Q(rng.randint(0, 9), 10)
        v = d*d
        assert mean_growth(m, k1, v) == ((m-d)/(k1+m-d) + (m+d)/(k1+m+d))/2
        count += 1
        # The crossing-control ratio is strictly increasing.
        assert h_ratio(m, k1, k2, v1) < h_ratio(m, k1, k2, v2)
        count += 1
        # The relative response has strictly negative end derivative.
        assert log_ratio_derivative(m, k1, k2, m*m) < 0
        count += 1
        # The initial derivative has the exact geometric-mean sign.
        sign = log_ratio_derivative(m, k1, k2, Q(0))
        assert (sign > 0) == (m*m > k1*k2)
        assert (sign == 0) == (m*m == k1*k2)
        count += 2
        # At full amplitude the relative response is lower than at zero.
        assert ratio(m, k1, k2, m*m) < ratio(m, k1, k2, Q(0))
        count += 1
    print(f"PASS: {count} exact-rational assertions")

if __name__ == '__main__':
    run()
