"""Independent low-dimensional convex-hull diagnostics for a cube--simplex Cayley body.

Dependencies: Python >=3.9, NumPy, SciPy.  Tests do not prove all-dimensional
facet completeness or limiting boundary-area statements; those require the proof.
"""
from itertools import combinations, product
from math import factorial, isclose, sqrt
import numpy as np
from scipy.spatial import ConvexHull


def vertices(n):
    lower = [list(bits) + [0] for bits in product((0, 1), repeat=n)]
    upper = [[0]*n + [1]]
    upper += [[int(i == j) for i in range(n)] + [1] for j in range(n)]
    return np.asarray(lower + upper, dtype=float)


def predicted_hyperplanes(n):
    # Outward unit normal and normalized right-hand-side constant.
    cs = []
    cs.append((np.array([0.]*n + [-1.]), 0., 'bottom'))
    cs.append((np.array([0.]*n + [1.]), 1., 'top'))
    for i in range(n):
        c = np.zeros(n + 1); c[i] = -1
        cs.append((c, 0., 'lower'))
    for k in range(1, n+1):
        for s in combinations(range(n), k):
            c = np.zeros(n + 1)
            for i in s: c[i] = 1
            c[-1] = k - 1
            cs.append((c, float(k), 'upper_' + str(k)))
    return [(c/np.linalg.norm(c), rhs/np.linalg.norm(c), label)
            for c, rhs, label in cs]


def exact_volume(n):
    return sum(1/factorial(k) for k in range(n+1))/(n+1)


def exact_area(n):
    return (1 + 1/factorial(n)
            + sum(1/factorial(k) for k in range(n))
            + sum(sqrt(k*k-k+1)/factorial(k) for k in range(1, n+1)))


def test():
    for n in range(1, 7):
        p = vertices(n)
        h = ConvexHull(p)
        expected = predicted_hyperplanes(n)
        hit = set()
        for equation in h.equations:
            normal, constant = equation[:-1], -equation[-1]
            matches = [i for i, (c, rhs, _) in enumerate(expected)
                       if np.linalg.norm(normal-c) < 2.e-8 and abs(constant-rhs) < 2.e-8]
            assert len(matches) == 1, (n, equation, matches)
            hit.add(matches[0])
        assert len(hit) == len(expected), (n, len(hit), len(expected))
        assert len(expected) == (1 << n) + n + 1
        assert isclose(h.volume, exact_volume(n), rel_tol=2.e-10, abs_tol=1.e-10)
        assert isclose(h.area, exact_area(n), rel_tol=2.e-10, abs_tol=1.e-10)
        # Exact symbolic relation for the volume's normalized lattice count.
        assert isclose(factorial(n+1) * exact_volume(n),
                       sum(factorial(n)//factorial(k) for k in range(n+1)),
                       rel_tol=1.e-13)
        print(f'n={n} dimension={n+1} vertices={len(p)} facets={len(hit)} '
              f'volume={h.volume:.12g} boundary_area={h.area:.12g}')
    print('CAYLEY_CUBE_SIMPLEX_HULL_FACET_AREA_PASS')

if __name__ == '__main__':
    test()
