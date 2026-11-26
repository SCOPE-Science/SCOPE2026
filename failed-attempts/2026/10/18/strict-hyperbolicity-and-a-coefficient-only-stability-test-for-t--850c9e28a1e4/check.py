#!/usr/bin/env python3
"""Reproduce exact three-zone crossing-cycle offset checks.

Optional independent event-driven flight integration uses NumPy and SciPy.
Primary published sample: Pessoa--Ribeiro, arXiv:2106.04638v1, Example 5.
"""
from fractions import Fraction as F
from math import sqrt

cases = {
    5: {'L': (F(4), F(8), F(3, 2)), 'C': (F(0), F(2), F(2, 3)), 'R': (F(4), F(2), F(-4))},
    6: {'L': (F(1), F(1), F(2, 3)), 'C': (F(0), F(2), F(2, 3)), 'R': (F(4), F(2), F(-4))},
    7: {'L': (F(1), F(1), F(3, 5)), 'C': (F(0), F(2), F(1)), 'R': (F(1), F(1), F(-1))},
    8: {'L': (F(4), F(8), F(2)), 'C': (F(2, 5), F(24, 5), F(-9, 5)), 'R': (F(8), F(10), F(-8))},
    9: {'L': (F(-2, 3), F(4, 3), F(-2, 3)), 'C': (F(2, 11), F(120, 11), F(-41, 11)), 'R': (F(-2, 11), F(4, 11), F(1, 5))},
    10: {'L': (F(-2, 3), F(4, 3), F(-2, 3)), 'C': (F(2, 11), F(120, 11), F(-41, 11)), 'R': (F(8), F(10), F(-7))},
}
expected = {5: (F(2, 3), F(31, 24)), 6: (F(2, 3), F(4, 3)),
            7: (F(1), F(9, 5)), 8: (F(-7, 5), F(-1)),
            9: (F(-45, 11), F(-43, 11)),
            10: (F(-51, 11), F(-43, 11))}
for num, zones in cases.items():
    al, bl, alph_l = zones['L']
    ac, bc, alph_c = zones['C']
    ar, br, alph_r = zones['R']
    ell = (al - alph_l) / bl
    r = -(ar + alph_r) / br
    a_offset = ac + alph_c + bc*r
    b_offset = -ac + alph_c + bc*ell
    assert (a_offset, b_offset) == expected[num], (num, a_offset, b_offset)
    assert a_offset < b_offset and a_offset*b_offset > 0
print('Six exact-rational offset/sign checks: PASS')

s = sqrt(1259/235)
a_offset, b_offset = map(float, expected[5])
bc = 2.0
D, E = 31*s/48, s/3
assert abs(a_offset*D - b_offset*E) < 1e-13
mu = ((a_offset - bc*D)*(b_offset + bc*E)
      / ((b_offset - bc*E)*(a_offset + bc*D)))
assert 7.16368 < mu < 7.16370
print('Example 5 exact-formula multiplier:', format(mu, '.13f'))

try:
    import numpy as np
    from scipy.integrate import solve_ivp
except ImportError:
    print('Optional numerical integration skipped (NumPy/SciPy unavailable).')
else:
    params = {
        'R': (4.0, 2.0, -10.0, -4.0, -4.0),
        'C': (0.0, 2.0, -2.0, 2/3, 2/3),
        'L': (4.0, 8.0, -2.5, 1.5, 11/4),
    }
    def advance(point, strip, crossing_x, direction):
        a, b, c, alpha, beta = params[strip]
        def rhs(t, z):
            x, y = z
            return [a*x + b*y + alpha, c*x - a*y + beta]
        def hit(t, z):
            return z[0] - crossing_x
        hit.direction = direction
        hit.terminal = True
        solution = solve_ivp(rhs, (0, 15), point, events=hit,
                             rtol=2e-12, atol=1e-13, max_step=.001)
        assert len(solution.t_events[0]) == 1
        assert solution.t_events[0][0] > 0
        return solution.y_events[0][0]
    def return_y(y):
        z = np.array([1., y])
        for strip, crossing_x, direction in [
                ('R', 1, -1), ('C', -1, -1),
                ('L', -1, 1), ('C', 1, 1)]:
            z = advance(z, strip, crossing_x, direction)
        return z[1]
    fixed = float(D)
    assert abs(return_y(fixed)-fixed) < 2e-9
    eps=1e-6
    slope = (return_y(fixed+eps)-return_y(fixed-eps))/(2*eps)
    assert abs(slope-mu) < 2e-5, (slope,mu)
    print('Independent four-flight return derivative:', format(slope,'.10f'))
    print('Numerical trajectory check: PASS')
