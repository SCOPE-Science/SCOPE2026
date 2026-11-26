"""Exact arithmetic checks for the incidence reduction and conic evaluations."""

from itertools import product
from math import comb


def incidence_profiles():
    profiles = []
    for t, u, v, a, b, g in product(range(1, 8), range(8), range(8),
                                     range(7), range(7), range(7)):
        h, n, s = 7 - t, t - 1, u + v
        if (n + 2*t + 3*s, n + 3*t + 4*s) != (35, 47):
            continue
        if 4*(8 + n) + 3*s < 28 + 10*t:
            continue
        if v > h or 21 - 3*u - v < 0 or 14 - 2*t - 2*v < 0:
            continue
        if 4*(21 - 3*u) + 3*u < 28:
            continue
        if u != a+b+g or a > comb(t, 2) or b+3*g+v > comb(h, 2):
            continue
        if 2*(a+b) > t*h or b > t*(h//2):
            continue
        profiles.append((t, u, v, a, b, g))
    return profiles


def primal_value(a, b, c, x, y, z):
    return (-c*c*x*x - b*b*y*y - a*a*z*z
            + 2*b*c*x*y + 2*a*c*x*z + 2*a*b*y*z)


if __name__ == '__main__':
    profiles = incidence_profiles()
    assert profiles == [
        (1, 5, 6, 0, 3, 2),
        (2, 5, 5, 1, 4, 0),
        (3, 5, 4, 3, 2, 0), (3, 6, 3, 3, 3, 0),
        (4, 5, 3, 5, 0, 0), (4, 6, 2, 5, 1, 0), (4, 6, 2, 6, 0, 0),
    ], profiles
    points = ((1, 1, -1), (1, -1, 1), (-1, 1, 1))
    for a, b, c in product(range(-3, 4), repeat=3):
        v1, v2, v3 = (primal_value(a, b, c, *p) for p in points)
        assert v1 - v2 == 4*c*(b-a)
        assert v1 - v3 == 4*b*(c-a)
        if a == b == c:
            assert v1 == -5*a*a
        if a+b+c == 0:
            assert (v1, v2, v3) == (4*b*c, 4*a*c, 4*a*b)
    print('NEARLY_FREE_REDUCTION_CHECKED', profiles)
