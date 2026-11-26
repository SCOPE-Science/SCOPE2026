#!/usr/bin/env python3
"""Independent numerical and algebraic checks for positive occupation of a reset telegraph particle.
Run: python3 check.py. All checks use Python's standard library.
These finite tests support rather than establish the general analytical statements.
"""
import math
import random
from fractions import Fraction


def effective_rate(r, alpha):
    return r * (r + 2 * alpha) / (2 * (r + alpha))


def free_transform(s, theta, alpha):
    assert s > max(0.0, theta)
    p, q = s - theta, s
    dp, dq = math.sqrt(p * (p + 2 * alpha)), math.sqrt(q * (q + 2 * alpha))
    return (dp + dq) / (q * dp + p * dq)


def matching_transform(s, theta, alpha):
    assert alpha > 0
    p, q = s - theta, s
    dp, dq = math.sqrt(p * (p + 2 * alpha)), math.sqrt(q * (q + 2 * alpha))
    aq = (q + alpha - dq) / alpha
    bp = (p + alpha + dp) / alpha
    delta = 1 / p - 1 / q
    a = delta * (bp - 1) / (bp - aq)
    return 1 / q + (1 + aq) * a / 2


def scgf(theta, r, alpha):
    R = effective_rate(r, alpha)
    return (theta - 2 * R + math.hypot(theta, 2 * R)) / 2


def test_polynomial_identity():
    # Exact rational identity: L^2*p*(p+2alpha) - (L-theta)^2*q*(q+2alpha)
    # equals 2*theta*(alpha+r) times the claimed quadratic in L.
    for j in range(256):
        l = Fraction(j - 121, 17)
        k = Fraction((j * 23) % 47 - 23, 11)
        r = Fraction((j * 7) % 29 + 1, 9)
        a = Fraction((j * 13) % 37, 10)
        q = l + r
        p = q - k
        lhs = l*l*p*(p+2*a) - (l-k)*(l-k)*q*(q+2*a)
        rhs = 2*k*((a+r)*l*l+(r*(2*a+r)-(a+r)*k)*l-r*(2*a+r)*k/Fraction(2))
        assert lhs == rhs, (j, lhs, rhs)
    return 256


def test_resolvents():
    n = 0
    for alpha in (0.01, 0.2, 1.0, 4.5):
        for theta in (-3., -0.6, -0.07, 0.01, 0.2, 4.0):
            for margin in (0.11, 0.8, 7.4):
                s = max(0., theta) + margin
                v = free_transform(s, theta, alpha)
                w = matching_transform(s, theta, alpha)
                assert abs(v-w) < 2e-10 * max(1, abs(v))
                n += 1
    return n


def test_roots():
    n = 0
    for alpha in (0.0, 0.001, 0.08, 0.5, 2., 100.):
        for r in (0.2, 0.7, 1.7, 6.0):
            for theta in (-9., -1., -.08, 0.0, .03, .3, 4., 9.):
                lam = scgf(theta, r, alpha)
                assert lam + r > max(0., theta)
                assert abs(r*free_transform(lam+r, theta, alpha)-1.) < 2e-10
                R = effective_rate(r, alpha)
                assert abs(lam*lam+(2*R-theta)*lam-R*theta)<1e-9
                n += 1
    return n


def simulate(n, duration, r, alpha, seed):
    rng = random.Random(seed)
    values = []
    for _ in range(n):
        t, x, occ = 0., 0., 0.
        direction = 1 if rng.random() < .5 else -1
        while t < duration:
            dt = -math.log1p(-rng.random()) / (r+alpha)
            if t + dt >= duration:
                dt = duration-t
                event = 0
            else:
                event = 1 if rng.random() < r/(r+alpha) else 2
            nx = x + direction * dt  # v=1 is without loss for a sign occupation.
            if x >= 0 and nx >= 0:
                occ += dt
            elif x >= 0 and nx < 0:
                occ += x
            elif x < 0 and nx >= 0:
                occ += nx
            t += dt
            x = nx
            if event == 1:
                x = 0.
                direction = 1 if rng.random() < .5 else -1
            elif event == 2:
                direction = -direction
        values.append(occ)
    avg = sum(values)/n
    var = sum((x-avg)**2 for x in values)/n/duration
    return avg, var


def test_mc():
    out = []
    for idx, alpha in enumerate((0., .5, 2.)):
        duration = 100.
        avg, var = simulate(6000, duration, 1., alpha, 9103+idx)
        target = 1/(4*effective_rate(1,alpha))
        assert abs(avg-duration/2) < 1.6
        assert abs(var-target) < .07
        out.append((alpha, round(avg,5), round(var,5), round(target,5)))
    return out


if __name__ == '__main__':
    print('Exact polynomial cases:', test_polynomial_identity())
    print('Direct matched-ODE resolvent comparisons:', test_resolvents())
    print('Nonlinear renewal-root comparisons:', test_roots())
    print('Monte Carlo: alpha, mean occupation, variance/time, asymptotic theory:')
    for x in test_mc():
        print(' ', *x)
    print('PASS; finite checks are not an infinite proof.')
