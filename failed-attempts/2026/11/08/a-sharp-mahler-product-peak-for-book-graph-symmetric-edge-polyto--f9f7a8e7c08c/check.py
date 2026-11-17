#!/usr/bin/env python3
"""Reproduce book-graph symmetric edge polytope volume-product tests.

Optional dependencies for convex-hull checks: numpy and scipy. Exact rational
identities and positivity tests require only the Python standard library.
"""
from fractions import Fraction as F
from math import factorial


def predicted_primal(m):
    return F(2**m * (m + 2), factorial(m + 1))


def predicted_polar(m):
    return F(2 * (2**(m + 1) - 1), m + 1)


def predicted_ratio(m):
    return F(m + 2, m + 1) * (1 - F(1, 2**(m + 1)))


def difference(m):
    return predicted_ratio(m+1) - predicted_ratio(m)


def bareiss(A):
    """Exact determinant for a square integer matrix via fraction-free elimination."""
    A = [list(map(int, row)) for row in A]
    n = len(A)
    if n == 1:
        return A[0][0]
    sign = 1
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            i = next((i for i in range(k+1, n) if A[i][k]), None)
            if i is None:
                return 0
            A[k], A[i] = A[i], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = A[i][j]*pivot - A[i][k]*A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
            A[i][k] = 0
        prev = pivot
    return sign * A[-1][-1]


def geom_checks(max_m=4):
    import numpy as np
    from scipy.spatial import ConvexHull, HalfspaceIntersection

    for m in range(1,max_m+1):
        d = m+1
        primal = []
        for j in range(d):
            w = [0]*d
            w[j] = 1
            primal += [w, [-x for x in w]]
        for j in range(1,d):
            w = [0]*d
            w[0],w[j] = 1,-1
            primal += [w, [-x for x in w]]
        hrep = np.asarray([[*v,-1.] for v in primal],dtype=float)
        polar_float = HalfspaceIntersection(hrep, np.zeros(d)).intersections
        polar = np.rint(polar_float).astype(int)
        assert np.max(np.abs(polar_float-polar)) < 1e-7
        assert all(int(np.dot(polar, np.asarray(v,dtype=int)).max()) <= 1 for v in primal)

        for name, V, expectation in [
            ('primal',primal,predicted_primal(m)),
            ('polar', polar.tolist(), predicted_polar(m))
        ]:
            hull = ConvexHull(np.asarray(V,dtype=float))
            # Origin is interior; cones over the Qhull facet triangulation
            # have disjoint interiors. Every determinant below is exact.
            exact = F(sum(abs(bareiss([V[int(k)] for k in facet]))
                              for facet in hull.simplices), factorial(d))
            assert exact == expectation, (name,m,exact,expectation)
        print('exact hull cones',m,'primal',predicted_primal(m),
              'polar',predicted_polar(m),'normalized ratio',predicted_ratio(m))


def main():
    for m in range(1,200):
        R=predicted_ratio(m)
        assert R > 1
        assert (predicted_primal(m)*predicted_polar(m) /
                F(4**(m+1),factorial(m+1))) == R
        analytical_delta = F(m*m+4*m+5,2**m) - 4
        analytical_delta /= 4*(m+1)*(m+2)
        assert difference(m) == analytical_delta
        assert (difference(m)>0) == (m in (1,2))
        assert (difference(m)<0) == (m>=3)
    assert predicted_ratio(3) == F(75,64)
    # The strict sign for all remaining m follows by induction:
    # 2^(m+2)>m^2+4m+5 at m=3, and the gap increases at each step.
    # The first 199 exact tests are a regression check, not that proof.
    print('EXACT_RATIONAL_IDENTITIES_AND_SIGN_TESTS_PASSED')
    geom_checks()
    print('BOOK_GRAPH_MAHLER_CHECKS_PASSED')


if __name__ == '__main__':
    main()
