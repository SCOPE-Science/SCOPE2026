#!/usr/bin/env python3
"""Exact exhaustive F_7 census for smooth plane cubic degree-three embeddings.

Only Python's standard library is required.  The mathematical completeness
of the normal forms is supplied in RESULT.md, rather than inferred from code.
"""
from collections import Counter
P = 7
POINTS = ([(x, y, 1) for x in range(P) for y in range(P)] +
          [(1, y, 0) for y in range(P)] + [(0, 1, 0)])
assert len(POINTS) == 57


def normalize(coeff):
    c = [v % P for v in coeff]
    first = next(v for v in c if v)
    inverse = pow(first, -1, P)
    return tuple((inverse * v) % P for v in c)


def form_gradient(a, b, T, x, y, z):
    if T is None:  # L=3O, ordinary Weierstrass plane embedding
        f = y*y*z-x*x*x-a*x*z*z-b*z*z*z
        grad = (-3*x*x-a*z*z, 2*y*z, y*y-2*a*x*z-3*b*z*z)
    else:   # L=2O+T, T=(u,v)
        u, v = T
        f = ((x-u*z)*y*y - 2*v*y*z*z -
             (x*x+u*x*z+(u*u+a)*z*z)*z)
        grad = (y*y-2*x*z-u*z*z,
                2*(x-u*z)*y-2*v*z*z,
                -u*y*y-4*v*y*z-x*x-2*u*x*z-3*(u*u+a)*z*z)
    return f % P, tuple(w % P for w in grad)


def census():
    covers = Counter()
    exceptional = []
    total = 0
    smooth_weierstrass = 0
    curves = Counter()
    for a in range(P):
        for b in range(P):
            if (4*a*a*a+27*b*b) % P == 0:
                continue
            smooth_weierstrass += 1
            elliptic_points = [(u,v) for u in range(P) for v in range(P)
                               if (v*v-u*u*u-a*u-b) % P == 0]
            for T in [None] + elliptic_points:
                total += 1
                tangent_lines = set()
                npoints = 0
                for point in POINTS:
                    f, grad = form_gradient(a,b,T,*point)
                    if f == 0:
                        npoints += 1
                        assert any(grad), (a,b,T,point,'bad rational gradient')
                        tangent_lines.add(normalize(grad))
                assert npoints == len(elliptic_points)+1, (a,b,T,npoints)
                assert len(tangent_lines) == npoints, (a,b,T,'repeated tangent')
                covered = sum(any(sum(c*x for c,x in zip(ell,point)) % P == 0
                                  for ell in tangent_lines) for point in POINTS)
                covers[covered] += 1
                curves[npoints] += 1
                if covered == 57:
                    exceptional.append((a,b,T,npoints))
    return smooth_weierstrass, total, covers, curves, exceptional


if __name__ == '__main__':
    na, total, covers, curves, exceptional = census()
    assert na == 42, na
    assert total == 336, total
    assert covers == Counter({
        21:2,22:1,27:12,29:4,30:15,33:6,36:30,37:28,
        39:7,40:24,42:18,45:35,46:34,47:30,48:33,
        50:25,51:24,57:8}), covers
    expected_T = [(0,1),(0,6),(1,3),(1,4),(2,3),(2,4),(4,3),(4,4)]
    assert sorted(exceptional) == sorted((0,1,T,12) for T in expected_T)
    print('SMOOTH_SHORT_WEIERSTRASS_MODELS',na)
    print('TOTAL_COMPLETE_LINEAR_SERIES_MODELS',total)
    print('COVERED_POINT_HISTOGRAM',sorted(covers.items()))
    print('ONLY_FILLING_MODELS',sorted(exceptional))
    print('F7_TANGENT_FILLING_CUBIC_CENSUS_PASS')
