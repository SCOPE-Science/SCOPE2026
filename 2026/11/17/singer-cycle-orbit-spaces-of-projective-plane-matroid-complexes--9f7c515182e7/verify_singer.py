#!/usr/bin/env python3
"""Independent finite consistency checks for Singer-orbit matroid quotients.
This program tests small prime-power orders; it does not prove the infinite theorem.
No network or third-party packages are used.
"""
from itertools import combinations
from math import comb


def planar_difference_set(q):
    m = q * q + q + 1
    # A small exhaustive construction of a cyclic (m,q+1,1) difference set.
    for tail in combinations(range(1, m), q):
        cand = (0,) + tail
        seen = set()
        for a in cand:
            for b in cand:
                if a != b:
                    seen.add((a - b) % m)
        if len(seen) == m - 1:
            return cand
    raise AssertionError("difference set not found")


def canon_orbit(face, m):
    return min(tuple(sorted((x + k) % m for x in face)) for k in range(m))


def run(q):
    m = q*q + q + 1
    D = planar_difference_set(q)
    lines = {frozenset((d + t) % m for d in D) for t in range(m)}
    assert len(lines) == m
    point_pairs = list(combinations(range(m), 2))
    for x, y in point_pairs:
        assert sum({x, y} <= line for line in lines) == 1
    tris = [x for x in combinations(range(m), 3)
            if not any(set(x) <= line for line in lines)]
    assert len(tris) == comb(m, 3) - m * comb(q+1, 3)
    invariant = {}
    for k in range(1, m):
        invariant[k] = sum(set((a+k) % m for a in T) == set(T)
                           for T in tris)
        if m % 3 == 0 and k in (m//3, 2*m//3):
            assert invariant[k] == m//3
        else:
            assert invariant[k] == 0
    # A directly enumerated group orbit census on nonempty faces.
    n0 = len({canon_orbit((x,), m) for x in range(m)})
    n1 = len({canon_orbit(e, m) for e in point_pairs})
    n2 = len({canon_orbit(t, m) for t in tris})
    assert n0 == 1 and n1 == (m-1)//2
    fixed_count = (m//3 if m % 3 == 0 else 0)
    assert n2 == (len(tris) - fixed_count)//m + (1 if fixed_count else 0)
    # Barycentric-subdivision flag orbit cells: vertices are faces,
    # edges are two-step incidence flags, triangles are full chains.
    # Any positive-dimensional flag has trivial stabilizer.
    sd0 = n0+n1+n2
    sd1 = (2*len(point_pairs) + 6*len(tris))//m
    sd2 = (6*len(tris))//m
    assert (2*len(point_pairs) + 6*len(tris)) % m == 0
    assert 6*len(tris) % m == 0
    quotient_euler = sd0-sd1+sd2
    initial_euler = m - comb(m, 2) + len(tris)
    burnside_euler = (initial_euler + 2*fixed_count)//m
    assert (initial_euler + 2*fixed_count) % m == 0
    assert quotient_euler == burnside_euler
    # Fractions are important in the nonfree case: use exact numerators.
    b2_numerator = (m-1)*(m-5) - 6*comb(q+1,3) + 4*(1 if fixed_count else 0)
    assert b2_numerator % 6 == 0
    b2 = b2_numerator//6
    assert b2 == quotient_euler-1
    d = m//3 if fixed_count else m
    print(f"q={q} m={m} D={D} independent_triangles={len(tris)} "
          f"order3_fixed_triangles={fixed_count} "
          f"sd_orbit_cells=({sd0},{sd1},{sd2}) "
          f"chi={quotient_euler} expected_H2_rank={b2} "
          f"expected_pi1_order={d}")


if __name__ == '__main__':
    for q in (2,3,4,5):
        run(q)
    print('SINGER_PLANE_QUOTIENT_FINITE_CHECK_PASS q=2,3,4,5')
