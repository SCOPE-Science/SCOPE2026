#!/usr/bin/env python3
"""Supplementary exact rational finite checks of a Steinhaus modulus identity.

This program verifies sample configurations only; the infinite statement
is proved in RESULT.md.  All rational arithmetic is exact.
"""
from fractions import Fraction as F
from itertools import product


def qnorm(v):
    return max(abs(v[0]), abs(v[1]))


def profile(d, a):
    return min(d, max(F(0), 2*a+d/2-1))


def sup_exact(x, y, a):
    """Maximize piecewise-affine absolute difference over a square exactly.

    Its break lines are all sign-switch and dominant-coordinate boundaries
    of the two max-absolute-value functions, plus the square boundaries.
    Their intersections include every vertex of every affine cell.
    """
    if not a:
        return abs(qnorm(x)-qnorm(y))
    lines = [(F(1), F(0), v) for v in (-a, a)]
    lines += [(F(0), F(1), v) for v in (-a, a)]
    for v in (x, y):
        lines += [(F(1), F(0), -v[0]), (F(0), F(1), -v[1])]
        for s in (-1, 1):
            lines.append((F(1), F(s), -v[0]-s*v[1]))
    vertices = set()
    for i, (a1, b1, c1) in enumerate(lines):
        for a2, b2, c2 in lines[i+1:]:
            det = a1*b2-a2*b1
            if not det:
                continue
            z1 = (c1*b2-c2*b1)/det
            z2 = (a1*c2-a2*c1)/det
            if max(abs(z1), abs(z2)) <= a:
                vertices.add((z1, z2))
    def val(z):
        return abs(qnorm((x[0]+z[0], x[1]+z[1]))-
                   qnorm((y[0]+z[0], y[1]+z[1])))
    return max(map(val, vertices))


def test():
    count = 0
    coords = [F(n, 4) for n in range(-4, 5)]
    # Each boundary pair on the unit square, all possible relative facets.
    boundary = [(u,v) for u,v in product(coords, repeat=2) if qnorm((u,v)) == 1]
    radii = [F(0), F(1,8), F(1,4), F(3,8), F(1,2),
             F(5,8), F(3,4), F(1), F(5,4)]
    for x in boundary:
        for y in boundary:
            d = qnorm((x[0]-y[0], x[1]-y[1]))
            if not d:
                continue
            for a in radii:
                q = sup_exact(x,y,a)
                assert q >= profile(d,a), (x,y,d,a,q)
                assert q <= d, (x,y,d,a,q)
                count += 2
    for d in [F(n,8) for n in range(1,17)]:
        x=(F(1),d/2)
        y=(F(1),-d/2)
        for a in radii + [F(7,8), F(9,8), F(3,2), F(2)]:
            q = sup_exact(x,y,a)
            assert q == profile(d,a), (d,a,q,profile(d,a))
            count += 1
    # Unit sphere under a linear real isometry to the two-atom ell_1 plane.
    for u,v in product(coords, repeat=2):
        assert (abs((u+v)/2)+abs((u-v)/2)) == max(abs(u),abs(v))
        count+=1
    return count

if __name__ == '__main__':
    n=test()
    print('STEINHAUS_SQUARE_EXACT_RATIONAL_DIAGNOSTIC_OK', n)
