"""Exact simplex-cell integration checks for barycentric simplex truncations.

Run: python check_truncation.py
Needs scipy, numpy and sympy. Hull triangulations select cells; all
cell volumes and all polynomial integrals are evaluated with rationals.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
import numpy as np
from scipy.spatial import ConvexHull
from sympy import Matrix, Rational, symbols, factor


def integrate_by_cone(d, t):
    """Independently integrate each boundary-simplex cone to the centroid."""
    points = set()
    for i in range(d + 1):
        for j in range(d + 1):
            if i != j:
                x = [Q(0)] * (d + 1)
                x[i], x[j] = 1 - t, t
                points.add(tuple(x))
    vertices = sorted(points)
    hull = ConvexHull(np.array([[float(x) for x in v[:d]] for v in vertices]))
    center = tuple([Q(1, d + 1)] * (d + 1))
    volume = Q(0)
    moment_integral = Q(0)
    for face in hull.simplices:
        nodes = [center] + [vertices[k] for k in face]
        matrix = Matrix([
            [Rational(nodes[i][j].numerator, nodes[i][j].denominator)
             - Rational(nodes[0][j].numerator, nodes[0][j].denominator)
             for i in range(1, d + 1)]
            for j in range(d)
        ])
        determinant = abs(matrix.det())
        cell_volume = Q(int(determinant.p), int(determinant.q)) / factorial(d)
        volume += cell_volume
        deviations = [[v[j] - center[j] for j in range(d + 1)] for v in nodes]
        diagonal = sum(z*z for row in deviations for z in row)
        offdiag = sum(sum(row[j] for row in deviations)**2 for j in range(d + 1))
        second_moment = (diagonal + offdiag) / ((d + 1)*(d + 2))
        moment_integral += cell_volume*second_moment
    return volume, moment_integral/volume, len(hull.simplices)


def closed_forms(d, t):
    B = (d + 1)*t**d
    A = t*t + (d + 2)*(1 - t)**2
    volume = (1 - B)/factorial(d)  # first d barycentric coordinates
    trace = Q(d, (d + 1)*(d + 2)) * (1 - B*A)/(1 - B)
    return volume, trace


def check():
    tests = 0
    cells = 0
    for d in (2, 3, 4):
        for t in (Q(1,5), Q(1,3), Q(2,5), Q(1,2)):
            observed_v, observed_j, c = integrate_by_cone(d, t)
            expected_v, expected_j = closed_forms(d, t)
            assert (observed_v, observed_j) == (expected_v, expected_j), (d, t)
            cells += c
            tests += 1
    z = symbols('z')
    cases = {
        2: (z-1)*(2*z-1)*(3*z-1),
        3: 2*(z-1)*(z+1)*(2*z-1)**2,
        4: (z-1)*(10*z**4-7*z+3),
    }
    for d, target in cases.items():
        S = 1-d + 2*(d+1)*z-(d+3)*z*z-2*(d+1)*z**d*(1-z)
        assert factor(S-target) == 0
    assert closed_forms(2, Q(1,3))[0] == Q(1,3)
    print('SIMPLEX_TRUNCATION_EXACT_CHECKS_PASSED',tests,cells,3)

if __name__ == '__main__':
    check()
