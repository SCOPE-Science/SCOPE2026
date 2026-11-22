"""Exact finite checks for the outer-sphere contact theorem on total-matching polytopes.

Run: python3 check.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from math import factorial


def state_dist(p, q, k, side, s):
    """Squared Euclidean distance from the proposed M-orbit barycenter.

    A total matching has k selected edges and s selected vertices, all from one
    bipartition class; side is 'L' (size p) or 'R' (size q).
    """
    d = q - p
    base = F(d * d + p, q)
    edge = 1 - F(2, q)
    vert = F(1) if side == 'L' else F(p - d, q)
    return base + k * edge + s * vert


def orbit_radius(p, q):
    return F(p * (2 * q - p - 1), q)


def check_orbit_centroid(p, q):
    # Enumerate the injective assignments of p distinct L elements into B.
    injections = list(permutations(range(q), p))
    n = len(injections)
    by_b = [0] * q
    by_edge = [[0] * q for _ in range(p)]
    for match in injections:
        occupied = set(match)
        for j in range(q):
            by_b[j] += j not in occupied
        for i, j in enumerate(match):
            by_edge[i][j] += 1
    d = q - p
    assert all(F(x, n) == F(d, q) for x in by_b)
    assert all(F(x, n) == F(1, q) for row in by_edge for x in row)
    assert n == factorial(q) // factorial(q - p)


def check_states(p, q):
    d = q - p
    center_radius = orbit_radius(p, q)
    max_rad = F(-1)
    contact = []
    for k in range(p + 1):
        for side, cap in [('L', p - k), ('R', q - k)]:
            for s in range(cap + 1):
                dist = state_dist(p, q, k, side, s)
                if dist > max_rad:
                    max_rad = dist
                    contact = [(k, side, s)]
                elif dist == max_rad:
                    contact.append((k, side, s))
    screening = d * (p - d) >= 2 * p
    assert (max_rad == center_radius) == screening, (p, q)
    if screening:
        assert (p, 'R', q - p) in contact
        others = set(contact) - {(p, 'R', q - p)}
        # At k=p, L-side with s=0 is not a distinct matching type from R-side s=0.
        assert others == ({(0, 'L', p)} if d * (p-d) == 2*p else set()), (p, q, others)


def main():
    for p in range(1, 41):
        for q in range(p + 1, 3 * p + 8):
            check_states(p, q)
    for p in range(1, 5):
        for q in range(p, min(7, p+4)):
            check_orbit_centroid(p, q)
    ties = [(p, d) for p in range(1, 200) for d in range(1, p+1)
            if d * (p-d) == 2*p]
    assert ties == [(8, 4), (9, 3), (9, 6)], ties
    positive = [(p, d) for p in range(1, 50) for d in range(1, p+2)
                if d * (p-d) > 2*p]
    assert all((p == 9 and d in (4, 5)) or
               (p >= 10 and 3 <= d <= p-3) for p, d in positive)
    for p in range(10, 50):
        assert all((p, d) in positive for d in range(3, p-2))
    print('TOTAL_MATCHING_OUTER_SPHERE_EXACT_PASS',
          'state_grids=1680_plus', 'ties=3', 'centroid_injections_checked')

if __name__ == '__main__':
    main()
