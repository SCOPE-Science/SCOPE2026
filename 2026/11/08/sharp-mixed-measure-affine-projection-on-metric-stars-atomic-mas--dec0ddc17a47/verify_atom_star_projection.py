"""Exact-rational checks for a continuous affine projector on an atomic metric star.

Uses only Python's standard library. Run: python verify_atom_star_projection.py
"""
from fractions import Fraction as Q
from itertools import product


def inverse(matrix):
    n = len(matrix)
    a = [[Q(x) for x in row] + [Q(int(i == j)) for j in range(n)]
         for i, row in enumerate(matrix)]
    for k in range(n):
        piv = next(i for i in range(k, n) if a[i][k] != 0)
        a[k], a[piv] = a[piv], a[k]
        d = a[k][k]
        a[k] = [x / d for x in a[k]]
        for i in range(n):
            if i != k:
                c = a[i][k]
                a[i] = [x - c * y for x, y in zip(a[i], a[k])]
    return [row[n:] for row in a]


def absolute_affine_integral(a, b):
    """Integral from 0 to 1 of the absolute affine interpolant of a and b."""
    if a * b >= 0:
        return (abs(a) + abs(b)) / 2
    return (a * a + b * b) / (2 * (abs(a) + abs(b)))


def exact_norms(masses, atom):
    n = len(masses)
    m = [[Q(0) for j in range(n + 1)] for i in range(n + 1)]
    m[0][0] = atom + sum(masses) / 3
    for i, mass in enumerate(masses, 1):
        m[0][i] = m[i][0] = mass / 6
        m[i][i] = mass / 3
    inv = inverse(m)
    vals = []
    for v in range(n + 1):
        val = atom * abs(inv[v][0])
        for j, mass in enumerate(masses, 1):
            val += mass * absolute_affine_integral(inv[v][0], inv[v][j])
        vals.append(val)
    return vals


def predicted(masses, atom):
    total = sum(masses)
    z = 1 + 4 * atom / total
    root = 1 + Q(2, 3) / z
    leaf = [2 + 1 / (3 * z) - 4 * (m / total) / (3 * (z + m / total))
            for m in masses]
    return [root] + leaf


def run():
    cases = 0
    for n in (2, 3, 4, 5):
        for ints in product((1, 2, 4), repeat=n):
            masses = list(map(Q, ints))
            for atom in (Q(0), Q(1, 3), Q(3), Q(11)):
                actual = exact_norms(masses, atom)
                expected = predicted(masses, atom)
                assert actual == expected, (masses, atom, actual, expected)
                assert max(actual) == max(expected[1:])
                assert {i for i, v in enumerate(actual) if v == max(actual)} == {
                    i + 1 for i, m in enumerate(masses) if m == min(masses)}
                cases += 1
    print('INDEPENDENT_EXACT_MASS_MATRIX_AND_KERNEL_NORMS_OK', cases)
    transitions = 0
    for m in (Q(1, 7), Q(1, 4), Q(2, 7), Q(1, 3), Q(2, 5)):
        for u in (Q(0), Q(1, 40), Q(1, 5), Q(2), Q(200)):
            z = 1 + 4*u
            delta = 1 / (3*z) - 4*m / (3*(z+m))
            assert (delta > 0) == (z*(1-4*m)+m > 0)
            assert (delta == 0) == (z*(1-4*m)+m == 0)
            transitions += 1
    print('EXACT_PHASE_SIGN_IDENTITY_OK', transitions)
    for masses, atom in [([Q(1),Q(2)], Q(0)), ([Q(1),Q(4)], Q(1)), ([Q(2),Q(3),Q(5)], Q(7))]:
        total = sum(masses)
        z = 1+4*atom/total
        r = min(masses)/total
        limiting = 2 + 1/(3*z)
        old = max(exact_norms(masses, atom))
        assert limiting - old == 4*r/(3*(z+r))
    print('EXACT_COLLAPSING_BRANCH_JUMP_IDENTITY_OK 3')
    print('ALL_ATOMIC_STAR_LINEAR_SPLINE_CHECKS_OK')

if __name__ == '__main__':
    run()
