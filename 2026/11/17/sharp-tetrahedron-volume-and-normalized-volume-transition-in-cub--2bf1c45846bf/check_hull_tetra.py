"""Exact all-parameter tetrahedral determinant certificate for cube--octahedron hulls.

Run with Python 3 and its standard library.  Each determinant is a degree-at-most-
three integer polynomial in the positive axis length h.  Bernstein coefficients
certify all signed determinant inequalities for the full real interval [1,3].
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb

# A vector coordinate is represented by (constant coefficient, coefficient of h).
verts = []
for axis in range(3):
    for sign in (-1, 1):
        row = [(0, 0)] * 3
        row[axis] = (0, sign)
        verts.append(tuple(row))
for signs in product((-1, 1), repeat=3):
    verts.append(tuple((s, 0) for s in signs))
assert len(verts) == 14


def poly_mult3(a, b, c):
    out = [0] * 4
    for i in range(2):
        for j in range(2):
            for k in range(2):
                out[i + j + k] += a[i] * b[j] * c[k]
    return tuple(out)


def determinant(I):
    base = verts[I[0]]
    mat = [[(verts[I[i]][j][0] - base[j][0],
             verts[I[i]][j][1] - base[j][1]) for j in range(3)]
           for i in (1, 2, 3)]
    out = [0] * 4
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        sign = -1 if inversions % 2 else 1
        term = poly_mult3(*[mat[i][p[i]] for i in range(3)])
        out = [a + sign * b for a, b in zip(out, term)]
    return tuple(out)


# Type k = number of axial vertices among the four points.
# These are sharp absolute-determinant envelopes on the full interval [1,3].
upper = {
    0: (16, 0, 0, 0),
    1: (4, 4, 0, 0),
    2: (0, 4, 2, 0),
    3: (0, 0, 3, 1),
    4: (0, 0, 0, 2),
}


def bernstein_coefficients_on_1_3(poly):
    """Degree-3 Bernstein coefficients of poly(1+2s), 0 <= s <= 1."""
    power = [sum(poly[k] * comb(k, j) * (2 ** j)
                 for k in range(j, 4)) for j in range(4)]
    return [sum((Fraction(power[j] * comb(i, j), comb(3, j))
                 for j in range(i + 1)), Fraction(0))
            for i in range(4)]


tight = {k: [] for k in range(5)}
bytype = {k: 0 for k in range(5)}
checked = 0
for quad in combinations(range(14), 4):
    k = sum(j < 6 for j in quad)
    bytype[k] += 1
    p = determinant(quad)
    for sign in (-1, 1):
        gap = tuple(u + sign * v for u, v in zip(upper[k], p))
        coeffs = bernstein_coefficients_on_1_3(gap)
        assert all(v >= 0 for v in coeffs), (quad, sign, gap, coeffs)
        checked += len(coeffs)
    if p == upper[k] or p == tuple(-u for u in upper[k]):
        tight[k].append(quad)

assert sum(bytype.values()) == 1001
assert checked == 8008
assert [len(tight[k]) for k in range(5)] == [2, 48, 12, 8, 12]

# Explicit geometry and rigidity of the globally maximizing configurations.
expected_cube = set()
for parity in (-1, 1):
    expected_cube.add(tuple(j for j in range(6, 14)
                            if verts[j][0][0] * verts[j][1][0] * verts[j][2][0] == parity))
assert set(tight[0]) == expected_cube
expected_mixed = set()
for eps in product((-1, 1), repeat=3):
    axes = [next(j for j in range(6)
                 if verts[j][axis] == (0, eps[axis]) and
                 all(verts[j][other] == (0, 0) for other in range(3) if other != axis))
            for axis in range(3)]
    corner = next(j for j in range(6, 14)
                  if tuple(verts[j][axis][0] for axis in range(3)) == tuple(-z for z in eps))
    expected_mixed.add(tuple(sorted(axes + [corner])))
assert set(tight[3]) == expected_mixed
maximizing = tight[0] + tight[3]
assert all(len(set(a).intersection(b)) <= 2
           for a, b in combinations(maximizing, 2))

print('CUBE_OCTAHEDRON_HULL_TETRAHEDRA_EXACT_PASS',
      'vertex_quadruples=1001',
      'bernstein_nonnegative=8008',
      'class_tight_counts=2,48,12,8,12',
      'cube_maxima=2',
      'axis_corner_maxima=8',
      'three_vertex_overlap_pairs=0')
