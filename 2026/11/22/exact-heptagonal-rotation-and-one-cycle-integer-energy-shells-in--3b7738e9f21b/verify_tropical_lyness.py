"""Exact checks for the two-season tropical Lyness rotation theorem.

This program uses rational arithmetic throughout, except for SymPy in the
optional symbolic consistency check of the classical rational first integral.
It does not turn finite samples into a proof of any infinite assertion.
"""
from fractions import Fraction as Q
from math import gcd


def step(x, y):
    z = max(0, y) - x
    return (z, max(1, z) - y)


def invariant(x, y):
    return max(x + 1, 0) + max(y, 1) + max(x, y + 1, 1) - x - y


def vertices(h):
    assert h > 3
    return [(1, 3-h), (h-1, 1), (h-1, h-2), (-1, h-2),
            (2-h, 1), (2-h, 0), (-1, 3-h)]


def arc_length(p, q):
    return max(abs(q[0]-p[0]), abs(q[1]-p[1]))


def coordinate(h, point):
    polygon = vertices(h)
    offset = 0
    for j in range(7):
        p = polygon[j]
        r = polygon[(j+1)%7]
        dx, dy = r[0]-p[0], r[1]-p[1]
        t = Q(point[0]-p[0], dx) if dx else Q(point[1]-p[1], dy)
        if 0 <= t <= 1 and point == (p[0]+t*dx, p[1]+t*dy):
            return offset + t*arc_length(p, r)
        offset += arc_length(p, r)
    raise AssertionError(f'not on the polygon boundary: {point}')


def sample_boundary_test():
    levels = [Q(10, 3), Q(7,2), Q(11,3), Q(4), Q(9,2), Q(17,3), Q(13,2), Q(10), Q(53,3)]
    samples = [Q(0), Q(1,7), Q(1,3), Q(1,2), Q(3,5), Q(6,7), Q(1)]
    num = 0
    for h in levels:
        poly = vertices(h)
        L = 5*h-8
        delta = 3*h-5
        assert sum(arc_length(poly[j], poly[(j+1)%7]) for j in range(7)) == L
        twice_area = sum(poly[j][0]*poly[(j+1)%7][1] - poly[j][1]*poly[(j+1)%7][0]
                         for j in range(7))
        assert twice_area == 5*h*h-16*h+8
        for j in range(7):
            p, r = poly[j], poly[(j+1)%7]
            for t in samples:
                pt = (p[0]+t*(r[0]-p[0]), p[1]+t*(r[1]-p[1]))
                q = step(*pt)
                assert invariant(*pt) == h and invariant(*q) == h
                assert (coordinate(h, q) - coordinate(h, pt) - delta) % L == 0
                num += 1
    return num


def integer_shell_test(max_k=200):
    assert max_k >= 4
    for k in range(4, max_k+1):
        assert gcd(3*k-5, 5*k-8) == 1
        poly = vertices(k)
        boundary = set()
        for j in range(7):
            p, r = poly[j], poly[(j+1)%7]
            length = int(arc_length(p, r))
            ux = (r[0]-p[0])//length
            uy = (r[1]-p[1])//length
            for i in range(length):
                pt = (p[0]+i*ux, p[1]+i*uy)
                assert invariant(*pt) == k
                boundary.add(pt)
        assert len(boundary) == 5*k-8
        for pt in boundary:
            assert step(*pt) in boundary
            assert (coordinate(k, step(*pt))-coordinate(k, pt) - (3*k-5)) % (5*k-8) == 0
        # Even the largest boundary is one orbit, not merely a union of orbits.
        p = poly[0]
        seen = set()
        for _ in range(5*k-8):
            assert p not in seen
            seen.add(p)
            p = step(*p)
        assert p == poly[0] and seen == boundary
    base = {(x,y) for x in range(-3,4) for y in range(-3,4) if invariant(x,y) == 3}
    assert base == {(-1,0), (-1,1), (0,0), (0,1), (1,0), (1,1), (2,1)}
    p = (0,0)
    seen = set()
    for _ in range(7):
        assert p not in seen
        seen.add(p)
        p = step(*p)
    assert p == (0,0) and seen == base
    return max_k-2


def symbolic_rational_limit_check():
    import sympy as sp
    x, y, a, b, h = sp.symbols('x y a b h', positive=True)
    z = (a+y)/x
    w = (b+z)/y
    inv = lambda X,Y: (b*X+a)*(a*Y+b)*(a*X+b*Y+a*b)/(X*Y)
    assert sp.factor(inv(z, w)-inv(x,y)) == 0
    rho = (3*h-5)/(5*h-8)
    area = (5*h*h-16*h+8)/2
    assert sp.factor(sp.diff(rho,h) - 1/(5*h-8)**2) == 0
    assert sp.factor(sp.diff(rho,h)/(sp.diff(area,h)/(2*sp.pi))
                     - 2*sp.pi/(5*h-8)**3) == 0


if __name__ == '__main__':
    count = sample_boundary_test()
    levels = integer_shell_test(200)
    symbolic_rational_limit_check()
    print(f'BOUNDARY_EXACT={count} rational sample points; integer shells k=3..200={levels}')
    print('RATIONAL_FIRST_INTEGRAL=exact identity; AREA_TWIST=exact identities')
    print('VERIFY_OK')
