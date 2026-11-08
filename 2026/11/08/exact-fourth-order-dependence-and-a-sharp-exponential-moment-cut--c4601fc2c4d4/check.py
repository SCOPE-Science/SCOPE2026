#!/usr/bin/env python3
"""Exact-rational checks of stationary fourth moments in coordinate-sampled Gaussian recursions."""
from fractions import Fraction as Q
from itertools import combinations
from math import exp, log


def check():
    checked = 0
    # Coefficients are enumerated from the actual uniformly sampled coordinate.
    # These numerical identities supplement, not replace, the infinite proof.
    for d in (2, 3, 4, 7):
        for a in (Q(1), Q(3, 2), Q(5, 4)):
            for step_numerator in (1, 2, 3, 4, 5, 7):
                h = Q(step_numerator, 4 * d * a)
                c = 1 - d * a * h
                assert -1 < c < 1
                beta = 1 - d * a * h / 2
                v = 2 * h * beta
                one = Q(1)
                m2 = one / a
                m4 = 3 * m2 * m2 * (1 + Q(d - 1, d) * (1 - c*c) / (1 + c*c))
                m22 = m2 * m2 * (1 - (1 - c*c) / (2*d))
                choices = tuple(range(d))
                for i in choices:
                    e2 = sum((c if j == i else one)**2 for j in choices) / d
                    e4 = sum((c if j == i else one)**4 for j in choices) / d
                    assert m2 == e2 * m2 + v
                    assert m4 == e4 * m4 + 6 * e2 * v * m2 + 3 * v*v
                    assert (m4 / m2**2 - 3) == 3 * Q(d - 1, d) * (1 - c*c)/(1+c*c)
                    checked += 3
                for i, j in combinations(choices, 2):
                    # Simultaneously scaling two coordinates only when one chosen.
                    e22 = sum((c if k == i else one)**2 *
                              (c if k == j else one)**2 for k in choices) / d
                    ei2 = sum((c if k == i else one)**2 for k in choices) / d
                    ej2 = sum((c if k == j else one)**2 for k in choices) / d
                    assert m22 == e22 * m22 + v * (ei2+ej2) * m2 + v*v
                    assert m22-m2*m2 == -(1-c*c) / (2*d*a*a)
                    checked += 2
                if step_numerator == 4:
                    assert c == 0 and v == Q(1, d*a)
                    # Age K is geometric with success probability 1/d.
                    mean_steps = Q(d)
                    squared_steps = Q(d*(2*d-1))
                    assert m2 == v*mean_steps
                    assert m4 == 3*v*v*squared_steps
                    assert m22-m2*m2 == -Q(1,2*d*a*a)
                    checked += 3
    # Geometric series check for the exact MGF at a reset step.
    d, a, t = 2, 1, Q(1, 2)
    z = float(t*t) / (2*d*a)
    ratio = (1-1/d)*exp(z)
    expected = exp(z)/(d-(d-1)*exp(z))
    partial = sum((1/d)*((1-1/d)**k)*exp((k+1)*z) for k in range(100))
    assert abs(expected-partial) < 1e-12 and ratio < 1
    assert abs((2*(log(2))**0.5)**2 - 4*log(2)) < 1e-12
    checked += 2
    print(f"PASS {checked} exact-rational and independent finite-series checks")


if __name__ == '__main__':
    check()
