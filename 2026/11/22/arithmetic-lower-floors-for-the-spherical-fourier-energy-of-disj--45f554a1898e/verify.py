#!/usr/bin/env python3
"""Independent finite sanity checks for the accompanying analytical theorem.

Only standard-library Python is required; tests do not certify the limiting theorem.
"""
from math import cos, sin, pi, sqrt, gcd


def analytic_two_ball_floor(p, q, d):
    assert p >= 1 and q >= 1 and gcd(p, q) == 1 and d >= 2
    return ((p - q) * (d + 3)) % 4 != 0


def modular_two_ball_floor(p, q, d):
    # The only possible difference between two bits in (9) is their parity.
    # Integer equality is tested after multiplication by eight.
    alpha8 = (p - q) * (d + 3)
    common_zero = any((alpha8 + 4 * (p * a - q * b)) % 8 == 0
                      for a in (0, 1) for b in (0, 1))
    return not common_zero


count = 0
for d in range(2, 25):
    for p in range(1, 26):
        for q in range(1, 26):
            if gcd(p, q) == 1:
                assert analytic_two_ball_floor(p, q, d) == modular_two_ball_floor(p, q, d)
                count += 1
print('Congruence checks:', count)

# The planar 1:2 formula is an exact stationary-point expression;
# a grid comparison here detects transcription or normalization mistakes.
M2 = (2367 + 129 * sqrt(129)) / 2048
floor_exact = 1.5 - sqrt(M2)
assert 0 < floor_exact < 0.14
N = 250_000
floor_grid = min(1.5 - 0.5*sin(2*pi*k/N) - sin(4*pi*k/N)
                 for k in range(N))
assert abs(floor_exact - floor_grid) < 2e-8, (floor_exact, floor_grid)
print('Planar 1:2 coefficient before radius/pi^2:', format(floor_exact, '.17g'))

# Exact d=3 ball amplitudes and spherical cross factor; this is not an
# asymptotic substitution. The two balls have radii 1 and 2, center distance 4.
def amp3(r, R):
    z = 2*pi*r*R
    return r/(pi*R**2) * (sin(z)/z - cos(z))


def energy3(R):
    a = amp3(1, R)
    b = amp3(2, R)
    k = 2*pi*R*4
    return a*a + b*b + 2*a*b*sin(k)/k

for R in (2.37, 8.13, 20.41, 100.73, 1000.57):
    target = (cos(2*pi*R - pi)**2 + 4*cos(4*pi*R - pi)**2)/pi**2
    actual = R**4*energy3(R)
    assert abs(actual-target) < 1/R, (R, actual, target)
    assert actual >= 0
print('Dimension-three closed-form Bessel checks: 5')
print('All finite checks passed; the continuous-frequency proof is analytic.')
