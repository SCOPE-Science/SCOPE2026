"""Supplementary finite numerical diagnostics for Gaussian multiwindow Gabor frames.

All mathematical universal statements are proved in the accompanying text.
This script does not certify an infinite zero set or a global minimum.
"""
import cmath
import math
from itertools import product


def zak(beta, x, omega, radius=35):
    return sum(math.exp(-beta * (x + k)**2) * cmath.exp(-2j * math.pi * k * omega)
               for k in range(-radius, radius + 1))


def zak_dx(beta, x, omega, radius=35):
    return sum(-2 * beta * (x + k) * math.exp(-beta * (x + k)**2)
               * cmath.exp(-2j * math.pi * k * omega)
               for k in range(-radius, radius + 1))


def energy(beta, points, x, omega):
    return sum(abs(zak(beta, x[0]-a, omega[0]) *
                   zak(beta, x[1]-b, omega[1]))**2 for a, b in points)


def has_coordinate_collision(points):
    return any(len({round(p[i] % 1.0, 12) for p in points}) < len(points)
               for i in range(len(points[0])))


def verify():
    examples = [
        ([(0, 0), (1/3, 1/3), (2/3, 2/3)], False),
        ([(0, 0), (0, 1/3), (1/3, 2/3)], True),
        ([(0, 0, 0), (.25, .25, .25), (.5, .5, .5), (.75, .75, .75)], False),
        ([(0, 0, 0), (0, .25, .25), (.5, .5, .5), (.75, .75, .75)], True),
    ]
    for points, expected in examples:
        assert has_coordinate_collision(points) is expected
    count = 0
    for beta in (.5, 1.0, math.pi, 5.0):
        L = zak(beta, 1/6, .5)
        D = zak_dx(beta, .5, .5)
        q = math.exp(-beta)
        D_product = -2*beta*math.exp(-beta/4)*math.prod(
            (1-q**(2*n))**3 for n in range(1, 80))
        assert abs(D-D_product) < 3e-11
        assert abs(L.imag) < 1e-12 and L.real > 0
        coeff = .5 * (abs(L) * abs(D))**2
        for eps in (.03, .01, .003):
            centers = [(0,0), (eps, 1/3), (1/3, 2/3)]
            # Trial point at which the local quadratic form is minimized.
            val = energy(beta, centers, (.5+eps/2, 1/6), (.5, .5))
            ratio = val/(coeff*eps*eps)
            assert .99 < ratio < 1.01, (beta, eps, ratio)
            count += 1
        print('beta', beta, 'predicted_collision_coefficient', format(coeff, '.13g'))
    print('PASS:', len(examples), 'coordinate classification examples;',
          count, 'quadratic-collision numerical diagnostics; 4 derivative products')


if __name__ == '__main__':
    verify()
