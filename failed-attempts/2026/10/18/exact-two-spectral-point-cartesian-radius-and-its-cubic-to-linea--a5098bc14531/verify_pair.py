"""Finite diagnostics for the two-spectral-point Cartesian-radius formula.
The analytic proof, not these finite tests, establishes the theorem.
"""
import cmath
import math


def formula(z, w):
    a = abs(z)**2
    b = abs(w)**2
    h = abs(a - b) / 2
    c = abs((z.conjugate()*w).imag)
    correction = c - h * math.atan(c/h) if h else c
    return max(a, b)/2 + correction/math.pi


def angular_quadrature(z, w, count=32768):
    summation = 0.0
    for j in range(count):
        angle = 2*math.pi*(j+0.5)/count
        rotation = cmath.exp(-1j*angle)
        summation += max((z*rotation).real**2, (w*rotation).real**2)
    return summation/count


def test():
    pairs = [
        (1+0j, 0+0j), (1+0j, 0.5+0j),
        (1+0j, 0+1j), (1+0j, 0.2j),
        (1+0j, 0.7j), (1+0j, 0.4+0.2j),
        (1+0j, 0.5+0.7j), (2+0j, 1j),
        (0.7+0.4j, 0.2-0.6j),
        (1.2+0.3j, -0.6+0.9j),
        (0.2+0.7j, 0.9-0.3j),
        (1-2j, 1+1j),
    ]
    for z, w in pairs:
        exact = formula(z, w)
        approximate = angular_quadrature(z, w)
        assert abs(exact-approximate)<1e-7*max(1, exact), (z, w, exact, approximate)
    for a in (0.2, 0.5, 0.9):
        levels = [formula(1, a*cmath.exp(1j*t)) for t in (0, 0.2, 0.4, 0.8, math.pi/2)]
        assert all(v < u for v, u in zip(levels,levels[1:])), levels
    for a in (0.2, 0.5, 0.9):
        h = (1-a*a)/2
        for theta in (0.02, 0.01):
            numerical = formula(1, a*cmath.exp(1j*theta))-0.5
            leading = a**3*theta**3/(3*math.pi*h*h)
            assert 0.95 < numerical/leading < 1.05, (a, theta, numerical/leading)
    print('PASS: 12 angular integrals, 3 phase-monotonicity tests, 6 cubic-asymptotic diagnostics')


if __name__ == '__main__':
    test()
