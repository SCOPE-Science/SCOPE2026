#!/usr/bin/env python3
"""Exact finite certificate for the volume spectrum of a regular truncated octahedron.

Run: python3 verify.py  (Python standard library only).
All arithmetic is integral; no floating-point comparisons occur.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import isqrt
from fractions import Fraction
from pathlib import Path
import csv

EXPECTED = {
    0:846, 2:552, 4:1728, 6:1152, 8:1332, 10:456,
    12:1872, 14:360, 16:654, 18:408, 20:480, 22:72,
    24:468, 26:48, 28:144, 30:24, 32:30,
}
MAX_ORBITS = {
    (12, 12, 12, 12, 16, 16): 6,
    (10, 12, 12, 14, 14, 16): 24,
}
SECOND_ORBITS = {(10, 10, 12, 14, 14, 18): 24}


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def det_of_quad(quad):
    v0, v1, v2, v3 = quad
    return abs(det3(tuple(v1[j]-v0[j] for j in range(3)),
                    tuple(v2[j]-v0[j] for j in range(3)),
                    tuple(v3[j]-v0[j] for j in range(3))))


def distances(quad):
    return tuple(sorted(sum((u[j]-v[j])**2 for j in range(3))
                        for u, v in combinations(quad, 2)))


def get_vertices():
    return tuple(sorted({p for a, b in product((-1, 1), repeat=2)
                         for p in permutations((0, a, 2*b))}))


def direct_spectrum(vertices):
    table = Counter()
    for subset in combinations(vertices, 4):
        table[det_of_quad(subset)] += 1
    assert dict(table) == EXPECTED
    assert sum(table.values()) == 10626
    return table


def symmetry_orbit_check(vertices):
    """Separate orbit dissection by all 48 signed coordinate permutations."""
    look = {v:i for i,v in enumerate(vertices)}
    transformations = []
    for perm in permutations(range(3)):
        for signs in product((-1,1), repeat=3):
            t = tuple(look[tuple(signs[j]*v[perm[j]] for j in range(3))]
                      for v in vertices)
            assert sorted(t)==list(range(24))
            transformations.append(t)
    assert len(set(transformations)) == 48
    covered = set()
    by_orbit = Counter()
    high = Counter()
    second = Counter()
    orbit_count = 0
    for subset in combinations(range(24), 4):
        if subset in covered:
            continue
        orbit = {tuple(sorted(t[i] for i in subset)) for t in transformations}
        assert not covered.intersection(orbit)
        covered.update(orbit)
        orbit_count += 1
        selected = tuple(vertices[i] for i in subset)
        magnitude = det_of_quad(selected)
        for member in orbit:
            assert det_of_quad(tuple(vertices[i] for i in member)) == magnitude
        by_orbit[magnitude] += len(orbit)
        if magnitude in (30,32):
            signature = distances(selected)
            for member in orbit:
                assert distances(tuple(vertices[i] for i in member)) == signature
            (high if magnitude==32 else second)[signature] += len(orbit)
    assert len(covered) == 10626
    assert orbit_count == 265
    assert dict(by_orbit) == EXPECTED
    assert dict(high) == MAX_ORBITS
    assert dict(second) == SECOND_ORBITS
    return orbit_count


def gram4_spectrum():
    """Independent 4-dimensional permutohedron presentation and Gram determinants.

    The 24 distinct permutations of (1,2,3,4) lie in the affine
    hyperplane of coordinate sum 10. Their orthogonal Hadamard images
    are exactly signed permutations of (0,1,2).
    """
    four = tuple(permutations((1,2,3,4)))
    images = {}
    for p in four:
        a,b,c,d = p
        image2 = (a+b-c-d, a-b+c-d, a-b-c+d)
        assert all(z%2==0 for z in image2)
        images[p] = tuple(z//2 for z in image2)
    assert set(images.values()) == set(get_vertices())
    assert len(set(images.values())) == 24
    count = Counter()
    for points in combinations(four,4):
        base=points[0]
        diff=tuple(tuple(p[j]-base[j] for j in range(4)) for p in points[1:])
        g=tuple(tuple(sum(diff[i][j]*diff[k][j] for j in range(4))
                      for k in range(3)) for i in range(3))
        dsquared=det3(*g)
        assert dsquared>=0
        d=isqrt(dsquared)
        assert d*d==dsquared
        count[d]+=1
    assert dict(count)==EXPECTED
    return count


def main():
    vertices=get_vertices()
    assert len(vertices)==24
    assert all(sum(abs(z) for z in v)==3 and max(map(abs,v))==2 for v in vertices)
    direct_spectrum(vertices)
    csvpath=Path(__file__).with_name('SPECTRUM.csv')
    with csvpath.open(encoding='utf-8', newline='') as fp:
        rows=list(csv.DictReader(fp))
    assert len(rows)==17
    for row in rows:
        d=int(row['absolute_determinant'])
        assert d in EXPECTED
        assert Fraction(row['tetrahedron_volume'])==Fraction(d,6)
        assert int(row['multiplicity'])==EXPECTED[d]
        indices=tuple(map(int,row['vertex_indices_0_based'].split()))
        assert len(indices)==4 and tuple(sorted(set(indices)))==indices
        assert all(0<=i<24 for i in indices)
        assert det_of_quad(tuple(vertices[i] for i in indices))==d
    assert set(int(x['absolute_determinant']) for x in rows)==set(EXPECTED)
    n_orbits=symmetry_orbit_check(vertices)
    gram4_spectrum()
    assert sum(EXPECTED.values())==10626
    assert sorted(EXPECTED) == list(range(0,33,2))
    print('TRUNCATED_OCTAHEDRON_TETRAHEDRAL_SPECTRUM_PASS',
          'quadruples=10626 levels=17 octahedral_orbits='+str(n_orbits),
          'max_orbits=6+24 second_orbit=24')


if __name__=='__main__':
    main()
