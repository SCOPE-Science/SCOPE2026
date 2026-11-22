#!/usr/bin/env python3
"""Complete finite-field incidence certificate for optimal tangent covers.

Uses only Python's standard library. All projective points and vertex triples
are traversed without sampling; the classification theorem for minimal
blocking sets of PG(2,11) is an external mathematical input.
"""
from collections import Counter
from itertools import combinations, permutations, product

P = 11
SQUARES = frozenset({1, 3, 4, 5, 9})
NON_SQUARES = frozenset({2, 6, 7, 8, 10})


def norm(v):
    for v0 in v:
        if v0 % P:
            inv = pow(v0, -1, P)
            return tuple((inv * z) % P for z in v)
    raise ValueError("zero projective vector")


def det(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            +a[1]*(b[2]*c[0]-b[0]*c[2])
            +a[2]*(b[0]*c[1]-b[1]*c[0])) % P


def frame(a, b, c, x, y, z):
    return norm(tuple((x*a[i] + y*b[i] + z*c[i]) % P for i in range(3)))


def all_points():
    return sorted({norm((x, y, 1)) for x, y in product(range(P), repeat=2)}
                  | {norm((x, 1, 0)) for x in range(P)} | {(1, 0, 0)})


def tangent_points(projective_points):
    contact = [q for q in projective_points
               if all(q) and sum(q) % P != 0 and len(set(q)) > 1]
    tangents = set()
    for q in contact:
        s_inv = pow(sum(q) % P, -1, P)
        coeff = tuple((3*s_inv-pow(x, -1, P)) % P for x in q)
        tangents.add(norm(coeff))
    assert len(contact) == 90 and len(tangents) == 72
    return sorted(tangents)


def line_histogram(lines, projective_points):
    return Counter(sum((a*x+b*y+c*z) % P == 0 for a,b,c in lines)
                   for x,y,z in projective_points)


def permutations_of_cover(cover):
    return {tuple(sorted(norm(tuple(v[i] for i in pi)) for v in cover))
            for pi in permutations(range(3))}


def classify():
    pts = all_points()
    assert len(pts) == 133
    T = tangent_points(pts)
    tset = frozenset(T)
    assert line_histogram(T, pts) == {1:3, 4:6, 5:30, 6:25, 7:24, 8:42, 11:3}
    assert max(line_histogram(T, pts)) == 11  # no full dual line

    solutions = set()
    triple_count, noncollinear_count = 0, 0
    for a,b,c in combinations(T, 3):
        triple_count += 1
        if det(a,b,c) == 0:
            continue
        noncollinear_count += 1
        # Full projective triangle has 5 nonvertex points on each open side.
        # Any minimum nontrivial blocking set of PG(2,11) is such a triangle.
        side_x = {sgn: tuple(frame(a,b,c,0,1,u) for u in vals)
                  for sgn,vals in ((1,SQUARES),(-1,NON_SQUARES))}
        side_y = {sgn: tuple(frame(a,b,c,1,0,v) for v in vals)
                  for sgn,vals in ((1,SQUARES),(-1,NON_SQUARES))}
        side_z = {sgn: tuple(frame(a,b,c,1,w,0) for w in vals)
                  for sgn,vals in ((1,SQUARES),(-1,NON_SQUARES))}
        for sx,sy in product((1,-1), repeat=2):
            sz = -sx*sy # collinearity v+uw=0 forces this coset
            cover = tuple(sorted((a,b,c)+side_x[sx]+side_y[sy]+side_z[sz]))
            if len(set(cover)) == 18 and set(cover) <= tset:
                solutions.add(cover)
    assert triple_count == 59640, triple_count
    assert len(solutions) == 6, len(solutions)
    histogram = {1:90,2:15,3:25,7:3}
    for cover in solutions:
        assert line_histogram(cover,pts) == histogram
    base = sorted(solutions)[0]
    assert permutations_of_cover(base) == solutions
    assert len(permutations_of_cover(base)) == 6
    print("SIX_OPTIMAL_TANGENT_COVERS_VERIFIED", len(solutions),
          "S3_ORBIT", len(permutations_of_cover(base)),
          "TRIPLES", triple_count, "NONCOLLINEAR", noncollinear_count)
    print("BASE_LINE_COEFFICIENTS", repr(list(base)))
    return solutions

if __name__ == '__main__':
    classify()
