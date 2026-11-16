#!/usr/bin/env python3
"""Finite numerical consistency checks for a quadratic-Gaussian Gabor obstruction.
The analytic proof of existence, uniqueness, and non-frame property is in RESULT.md.
No finite computation is used to certify infinite quantifiers.
"""
import math


def phi(u):
    """u times the logarithmic derivative of Jacobi theta_4, via its product."""
    assert u > 0
    v = 0.0
    for j in range(1, 5000):
        x = 2 * j * u
        y = (2 * j - 1) * u
        if y > 745:
            break
        v += 0 if x > 745 else x / math.expm1(x)
        v += 2 * y / math.expm1(y)
        if j > 5 and y > 38:
            break
    return v


def u_for(gamma, c):
    target = gamma * c
    lo, hi = 1.0e-6, 100.0
    assert phi(lo) > target and phi(hi) < target
    for _ in range(90):
        mid = (lo + hi) / 2
        if phi(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def theta_c(u):
    return phi(u) / u


def alternating_fiber(u, d, x, K=140):
    return sum((-1)**k * ((x-k)**2 + d) * math.exp(-u*(x-k)**2)
               for k in range(-K, K+1))


def main():
    tests = 0
    critical = u_for(1, 1)
    assert 1.645014968675 < critical < 1.645014968677
    tests += 1
    for u in [0.09, 0.25, 0.5, 1.0, critical, 1.7, 2.5, 4.0, 9.0]:
        for h in [1.01, 1.10, 1.5]:
            assert phi(u) > phi(u*h)
            tests += 1
    for gamma, c in [(0.5, 0.3), (1, 0.1), (1, 1), (1, 2),
                     (math.pi, 1), (1.6, 4), (0.2, 100), (2, 100)]:
        u = u_for(gamma, c)
        b = math.sqrt(gamma/u)
        d = c*b*b
        assert b > 0
        assert abs(phi(u)-gamma*c) < 2e-9*max(1,gamma*c)
        assert abs(d-theta_c(u)) < 2e-8*max(1,d)
        tests += 3
        for j in range(-10,11):
            resid = alternating_fiber(u, d, j/2)
            base = sum(((j/2-k)**2+d)*math.exp(-u*(j/2-k)**2)
                       for k in range(-140,141))
            assert abs(resid) < 2e-9*max(1,base), (gamma,c,u,j,resid)
            tests += 1
        # Exact radial curvature formula used in the proof.
        for t in [0, 0.01, 0.1, 0.5, 1, 2, 5]:
            curvature = 2*(c-t*t)/(c+t*t)**2-2*gamma
            assert curvature <= 2/c-2*gamma + 1e-12
            tests += 1
    print('PASS: %d finite consistency assertions' % tests)
    print('critical dimensionless Gaussian exponent u_0 = %.15f' % critical)
    print('Example: gamma=1,c=2 -> unique half-density frequency step b=%.15f' %
          math.sqrt(1/u_for(1,2)))

if __name__ == '__main__':
    main()
