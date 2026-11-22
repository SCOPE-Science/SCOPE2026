#!/usr/bin/env python3
"""Reproduce exact finite saturated-step counts for one adaptive projected-gradient scheme."""
from fractions import Fraction
from math import exp, hypot, log, log1p, sqrt


def count_exact_parameters(lam, eta, gamma, radius):
    assert min(lam, eta, gamma, radius) > 0
    ratio = lam * eta / (2 * gamma)
    if ratio < 1:
        return 0
    return int(log(ratio) / (0.5 * log1p(4 * radius * radius / (eta * eta)))) + 1


def simulate(lam, eta, gamma, radius):
    # Coordinates (3/5,4/5) make the same projection test genuinely vector-valued.
    direction = (0.6, 0.8)
    x = [radius * u for u in direction]
    s = gamma
    flips = 0
    while True:
        step = eta / s
        z = [(1 - lam * step) * t for t in x]
        norm = hypot(*z)
        if norm > radius:
            z = [radius * t / norm for t in z]
        delta_sq = sum((z[i] - x[i])**2 for i in range(2))
        new_s = s * sqrt(1 + delta_sq / (eta * eta))
        if all(abs(z[i] + x[i]) < 1e-9 for i in range(2)) and abs(hypot(*x) - radius) < 1e-9:
            flips += 1
        else:
            assert hypot(*z) < radius + 1e-8
            assert lam * eta / s < 2 + 1e-10
            x, s = z, new_s
            break
        x, s = z, new_s
        assert flips < 100000
    # Verify the regular regime and a finite, analytical accumulator bound.
    entry_x = hypot(*x)
    if entry_x > 0:
        for _ in range(3000):
            theta = lam * eta / s
            assert 0 < theta < 2
            z = [(1-theta)*t for t in x]
            new_s = hypot(s,lam*hypot(*x))
            assert hypot(*z) <= hypot(*x) + 1e-10
            x,s = z,new_s
    return flips


def exact_boundary_certificates():
    # When (lambda, gamma, radius)=(1,1,1), eta=4, the square of the
    # multiplicative accumulator ratio is 5/4 and the boundary is r^2=4.
    assert Fraction(5,4)**6 <= 4 < Fraction(5,4)**7
    # At eta=8, this same ratio is 17/16 and the boundary is r^2=16.
    assert Fraction(17,16)**45 <= 16 < Fraction(17,16)**46


if __name__ == '__main__':
    exact_boundary_certificates()
    for eta, expected in [(0.1,0),(1,0),(2,1),(4,7),(8,46),(16,269),(32,1423),(64,7102)]:
        calc = count_exact_parameters(1, eta, 1, 1)
        observed = simulate(1, eta, 1, 1)
        assert calc == observed == expected, (eta, calc, observed, expected)
        print(f'eta={eta:g} exact_count={calc} simulated={observed}: PASS')
    # Check another radius, curvature and base denominator, including m=0.
    for lam,eta,gamma,radius in [(2,5,1,0.7),(1.5,10,2,1.7),(3,2,7,0.5)]:
        observed = simulate(lam,eta,gamma,radius)
        predicted = count_exact_parameters(lam,eta,gamma,radius)
        assert observed == predicted, (lam,eta,gamma,radius,observed,predicted)
    print('Exact rational certificates and independent two-dimensional recurrence checks passed.')
