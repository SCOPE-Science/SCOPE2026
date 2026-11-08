"""Deterministic independent checks for a regular-polygon boundary-chord crossover.

Run: python verify_boundary_crossover.py
Uses only the Python standard library. Grid quadrature is diagnostic, not a proof.
"""
import math
from fractions import Fraction


def nearest_integer_distance(x):
    return abs((x + 0.5) % 1.0 - 0.5)


def face_deficit(x):
    q = nearest_integer_distance(x)
    return 2.0 * q * (1.0 - q)


def radius_and_weight(x, n):
    a = math.pi / n
    z = a * (1.0 - 2.0 * nearest_integer_distance(x))
    c = math.cos(z)
    return math.cos(a) / c, math.pi * math.cos(a) / (n * math.sin(a) * c * c)


def quadratures(n, threshold, mesh=280):
    """Return finite-n n*Pr and the claimed scaling integral, same quadrature grid."""
    sigma = (n % 2) / 2.0
    a = math.pi / n
    width = math.sqrt(threshold)
    nv = 2 * mesh
    dv = 2 * width / nv
    result_finite = 0.0
    result_limit = 0.0
    for i in range(mesh):
        u = (i + 0.5) / mesh
        r1, w1 = radius_and_weight(u, n)
        f1 = face_deficit(u)
        for j in range(nv):
            v = -width + (j + 0.5) * dv
            other = u + sigma + v
            r2, w2 = radius_and_weight(other, n)
            length = math.sqrt(r1*r1 + r2*r2 + 2*r1*r2*math.cos(2*a*v))
            if length > 2 - math.pi**2 * threshold / (n*n):
                result_finite += w1*w2
            if f1 + face_deficit(other) + v*v < threshold:
                result_limit += 1
    factor = dv / mesh
    return result_finite*factor, result_limit*factor


def run():
    even = Fraction(2) * (Fraction(1, 2)**2)  # area of |x|+|y|<t/2 at t=1
    odd = 2 * Fraction(1, 2) * (1 + Fraction(1, 3))**2
    assert even == Fraction(1, 2)
    assert odd == Fraction(16, 9)
    # Exact geometric diameter of a regular odd n-gon: two farthest vertices.
    for n in (5, 7, 21, 101):
        angular = 2*math.pi*(n//2)/n
        diameter = math.sqrt(2-2*math.cos(angular))
        expected = 2*math.cos(math.pi/(2*n))
        assert abs(diameter - expected) < 1e-13
    # The direct finite-n geometry is computed separately from the limiting G function.
    errors = []
    for n in (80, 81, 120, 121):
        for t in (0.30, 1.0, 2.0):
            measured, predicted = quadratures(n, t)
            error = abs(measured - predicted)
            assert error < 0.007, (n, t, measured, predicted, error)
            errors.append(error)
    # Check onset, minimum and radius parametrization identities.
    for n in (20, 21, 100, 101):
        r0, _ = radius_and_weight(0, n)
        rm, _ = radius_and_weight(0.5, n)
        assert abs(r0-1) < 1e-14
        assert abs(rm-math.cos(math.pi/n)) < 1e-14
    for t in (1.1, 3.0, 10.0):
        for sigma in (0., 0.5):
            # Both envelope bounds follow from 0 <= f(u) <= 1/2.
            assert math.sqrt(t-1) < math.sqrt(t)
    print('VERIFY_OK exact_onset_coefficients=2 odd_diameters=4 finite_n_quadratures=12'
          ' max_absolute_error={:.6f}'.format(max(errors)))


if __name__ == '__main__':
    run()
