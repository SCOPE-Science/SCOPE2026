#!/usr/bin/env python3
"""Finite diagnostics for a sharp planar harmonic Bergman kernel bound."""
import cmath
import math

count = 0

def check(value, message):
    global count
    assert value, message
    count += 1

for beta in (0.1, 0.5, 1.0, 1.1, 1.25, 1.5, 2.0, 3.0, 5.0, 9.0, 20.0):
    def kernel(t):
        return 2 * ((1 - t) ** (-beta)).real - 1
    for j in range(1, 13):
        radius = j / 13
        floor = 2 / (1 + radius) ** beta - 1
        if beta * radius <= 1:
            for k in range(21):
                angle = math.pi * k / 20
                actual = kernel(radius * cmath.exp(1j * angle))
                check(actual + 1e-12 >= floor,
                      ('angular inequality', beta, radius, angle, actual, floor))
    if beta <= 1:
        for k in range(1, 20):
            radius = k / 20
            check(kernel(-radius) > 0, ('no real kernel zero', beta, radius))
        continue
    rho = 2 ** (1 / beta) - 1
    check(0 < beta * rho < 1, ('strict angular regime', beta))
    check(abs(kernel(-rho)) < 1e-12, ('sharp zero', beta))
    check(kernel(-rho * (1 - 1e-4)) > 0, ('strict positivity', beta))
    check(kernel(-rho * (1 + 1e-4)) < 0, ('negative side', beta))
    for fraction in (1e-6, 1e-7, 1e-8):
        r = rho + fraction * (1 / beta - rho)
        # bisection for the single zero in the upper semicircle
        lo, hi = 0.0, math.pi
        for _ in range(65):
            mid = (lo + hi) / 2
            if kernel(r * cmath.exp(1j * (math.pi - mid))) < 0:
                lo = mid
            else:
                hi = mid
        delta = (lo + hi) / 2
        predicted = math.sqrt(2 * (1 + rho) / (rho * (1 - beta * rho)) * (r - rho))
        check(abs(delta / predicted - 1) < 0.01,
              ('onset coefficient', beta, fraction, delta, predicted))
print('PASS:', count, 'finite diagnostic checks; exact theorem uses symbolic proof')
