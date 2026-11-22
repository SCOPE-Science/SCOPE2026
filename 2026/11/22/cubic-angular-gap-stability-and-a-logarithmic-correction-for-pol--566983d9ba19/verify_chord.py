"""Numerical checks for the angular-gap perimeter-chord asymptotics.

Run: python verify_chord.py
Requires numpy. The proof in RESULT.md, not this finite computation,
establishes the asymptotics.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def regular_ratio(n, order=48):
    """Independent edge-pair quadrature; same-side term is exact."""
    alpha = math.pi / n
    c, b = math.cos(alpha), math.sin(alpha)
    nodes, ww = leggauss(order)
    x = b * nodes
    wt = ww / 2
    xi, xj = np.meshgrid(x, x, indexing='ij')
    W = np.outer(wt, wt)
    total = 2 * b / 3  # expected same-edge distance
    for j in range(1, n):
        ang = 2 * math.pi * j / n
        co, si = math.cos(ang), math.sin(ang)
        dx = c - (c * co - xj * si)
        dy = xi - (c * si + xj * co)
        total += (W * np.hypot(dx, dy)).sum()
    mean = total / n
    perimeter = 2 * n * b
    return mean / perimeter


def unequal_gap_ratio(n, order=18):
    """Direct pairwise quadrature on all actual polygon sides."""
    k = np.arange(n)
    gaps = 2 * np.pi / n * (1 + 0.35 * np.sin(2 * np.pi * (k + 0.5) / n))
    gaps *= 2 * np.pi / gaps.sum()
    angles = np.r_[0, np.cumsum(gaps)]
    v = np.array([[np.cos(t), np.sin(t)] for t in angles[:-1]])
    e = np.roll(v, -1, axis=0) - v
    lengths = np.linalg.norm(e, axis=1)
    nodes, weights = leggauss(order)
    points = v[:, None, :] + (0.5 * (nodes + 1))[None, :, None] * e[:, None, :]
    w = lengths[:, None] * weights[None, :] / 2
    integral = 0.0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                val = lengths[i] ** 3 / 3
            else:
                diff = points[i, :, None, :] - points[j, None, :, :]
                val = np.sum(w[i, :, None] * w[j, None, :] * np.linalg.norm(diff, axis=2))
            integral += val * (1 if i == j else 2)
    perim = lengths.sum()
    return integral / perim ** 3, gaps


def run():
    print('Regular polygon: n, deficit, n^2*deficit, n^4*(deficit-1/(3n^2)), logarithm-corrected')
    last = None
    for n in (20, 40, 80, 160, 320):
        gap = 2 / math.pi ** 2 - regular_ratio(n)
        rem = n ** 4 * (gap - 1 / (3 * n ** 2))
        corrected = rem + math.pi ** 2 * math.log(n) / 90
        print(n, '%.12g' % gap, '%.8f' % (n*n*gap), '%.8f' % rem, '%.8f' % corrected)
        assert gap > 0
        assert abs(n*n*gap - 1/3) < 0.05
        if last is not None:
            assert abs(corrected-last) < 0.015
        last = corrected
    print('Unequal gaps: n, exact deficit, cubic prediction, relative error')
    for n in (12, 20, 40, 80):
        ratio, gaps = unequal_gap_ratio(n)
        deficit = 2 / math.pi ** 2 - ratio
        leading = np.sum(gaps ** 3) / (24 * math.pi ** 3)
        err = (deficit-leading) / leading
        print(n, '%.12g' % deficit, '%.12g' % leading, '%.8f' % err)
        assert deficit > 0
        assert -0.035 < err < 0.005
    print('PASS: all independent edge-pair quadrature checks')

if __name__ == '__main__':
    run()
