"""Exact-rational consistency checks for demihypercube isotropic formulas.

Run: python check_demicube.py
The optional NumPy/SciPy hull comparison is a finite numerical cross-check.
"""
from fractions import Fraction as F
from math import factorial


def data(d):
    assert isinstance(d, int) and d >= 3
    a = F(2 ** (d - 1), factorial(d))
    b = F((d - 1) * (d - 2), (d + 1) * (d + 2))
    vol = 1 - a
    variance = F(1, 12) - a * b / (6 * vol)
    # Independent simplex-integration expression for variance:
    exc_moment = F(1, 4) - F(1, d + 1) + F(2, (d + 1) * (d + 2))
    independent = (F(1, 12) - a * exc_moment) / vol
    assert variance == independent
    assert a > 0 and vol > 0 and variance > 0
    return a, b, vol, variance


def below(d, threshold):
    _, _, v, s = data(d)
    return (s / threshold) ** d < v ** 2


def above(d, threshold):
    _, _, v, s = data(d)
    return (s / threshold) ** d > v ** 2


def rational_checks():
    expected = {
        3: (F(1, 3), F(1, 20)),
        4: (F(2, 3), F(1, 15)),
        5: (F(13, 15), F(83, 1092)),
        6: (F(43, 45), F(97, 1204)),
        7: (F(311, 315), F(923, 11196)),
    }
    for d, pair in expected.items():
        assert data(d)[2:] == pair, d
    threshold = F(13, 160)
    assert below(5, threshold)
    for d in (3, 4, 6):
        assert above(d, threshold)
    assert data(7)[3] > threshold
    assert above(3, F(1, 12))
    for d in range(4, 161):
        assert below(d, F(1, 12)), d
    for d in range(5, 161):
        a, b, v, s = data(d)
        a1, b1, v1, s1 = data(d + 1)
        assert a1 == a * F(2, d + 1)
        assert (F(1, 12) - s1) / (F(1, 12) - s) == F(2*d, (d - 2)*(d + 3)) * v / v1
        assert s1 > s
        if d >= 7:
            assert s > threshold
    print('DEMICUBE_ISOTROPIC_EXACT_CHECKS_PASSED', 160)


def optional_convex_hull_checks():
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
    except ImportError:
        print('DEMICUBE_CONVEX_HULL_VOLUME_CHECKS_SKIPPED (NumPy/SciPy unavailable)')
        return
    for d in range(3, 7):
        verts = np.array([[float((mask >> i) & 1) for i in range(d)]
                          for mask in range(1 << d) if mask.bit_count() % 2 == 0])
        hull = ConvexHull(verts)
        assert len(hull.vertices) == 2 ** (d-1)
        assert abs(hull.volume - float(data(d)[2])) < 5e-10
    print('DEMICUBE_CONVEX_HULL_VOLUME_CHECKS_PASSED', 4)


if __name__ == '__main__':
    rational_checks()
    optional_convex_hull_checks()
