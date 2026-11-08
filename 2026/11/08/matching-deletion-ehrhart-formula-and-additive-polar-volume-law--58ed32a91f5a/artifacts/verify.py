#!/usr/bin/env python3
"""Independent finite checks for matching-relaxed finite-metric Lipschitz polytopes.

Uses brute-force rooted integer potentials, halfspace intersections, and
integer generating-series transformations, none as a substitute for the proof.
Requires Python 3; SciPy only for the optional numerical-volume test.
"""
from itertools import combinations, product
from math import comb, factorial, isclose, sqrt


def eulerian_poly(r):
    p = [1]
    for j in range(1, r + 1):
        if j == 1:
            continue
        q = [0] * (len(p) + 1)
        n = j - 1
        for a, c in enumerate(p):
            q[a] += c
            q[a + 1] += n * c
            if a:
                q[a] += a * c
                q[a + 1] -= a * c
        p = q
    return p


def get_poly(n, matching):
    x = eulerian_poly(n)
    y = eulerian_poly(n - 2)
    for i, c in enumerate(y):
        x[i + 1] += 2 * len(matching) * c
    return x


def count_brute(n, matching, scale):
    omit = {tuple(sorted(ab)) for ab in matching}
    es = [(i, j) for i in range(n) for j in range(i + 1, n)
          if (i, j) not in omit]
    result = 0
    for t in product(range(-2 * scale, 2 * scale + 1), repeat=n - 1):
        a = (*t, 0)
        if all(abs(a[i] - a[j]) <= scale for i, j in es):
            result += 1
    return result


def closed(n, k, m):
    return (m + 1)**n - m**n + 2*k*sum(h**(n-2) for h in range(1,m+1))


def ehrhart_from_poly(n, h, m):
    d = n - 1
    return sum(c*comb(m + d - i, d) for i, c in enumerate(h)
               if m + d - i >= d)


def volume_check(n, matching, weights):
    try:
        import numpy as np
        from scipy.spatial import HalfspaceIntersection, ConvexHull
    except ImportError:
        return None
    omit = {tuple(sorted(ab)): w for ab, w in zip(matching, weights)}
    constraints = []
    for i, j in combinations(range(n), 2):
        w = omit.get((i, j), 1.)
        row = [0.] * (n - 1)
        if i < n - 1:
            row[i] += 1.
        if j < n - 1:
            row[j] -= 1.
        constraints.append([*row, -w])
        constraints.append([*(-r for r in row), -w])
    a = np.array(constraints)
    verts = HalfspaceIntersection(a, np.zeros(n - 1)).intersections
    vol = ConvexHull(verts).volume
    expected = n + 2 * sum((1 - (2 - w)**(n-1))/(n-1) for w in weights)
    assert isclose(vol, expected, rel_tol=3e-8, abs_tol=3e-8), (n, matching, weights, vol, expected)
    return len(verts)


def main():
    counts = volumes = profiles = 0
    for n in range(4, 8):
        for k in range(2, n//2 + 1):
            matching = [(2*i, 2*i + 1) for i in range(k)]
            poly = get_poly(n, matching)
            assert len(poly) == n
            assert poly == poly[::-1]
            assert sum(poly) == factorial(n-1)*(n + 2*k/(n-1))
            for m in range(0, 4 if n<=6 else 3):
                target = closed(n, k, m)
                assert ehrhart_from_poly(n, poly, m) == target
                actual = count_brute(n, matching, m)
                assert actual == target, (n,k,m,actual,target)
                counts += 1
            profiles += 1
            if n <= 6:
                for ws in ([2.0]*k, [1.25 + 0.2*(i%3) for i in range(k)]):
                    v = volume_check(n, matching, ws)
                    if v is not None: volumes += 1
    # The single-relaxation boundary validates the additive base component.
    for n in range(3, 7):
        matching = [(0,1)]
        for m in range(3):
            assert count_brute(n, matching, m) == closed(n, 1, m)
            counts += 1
    print('MATCHING_LIPSCHITZ_EHRHART_CHECKS_PASSED',
          'integer_profiles='+str(counts), 'hstar_profiles='+str(profiles),
          'independent_hulls='+str(volumes))

if __name__ == '__main__':
    main()
