"""Finite reproducibility checks for a theorem on ordinary wheel edge polytopes.

Runs independently of the proof, using a linear-programming solver.
Finite checks do not establish the universal assertions.
Dependencies: Python 3.10+, numpy, scipy.
"""
from math import sqrt
import numpy as np
from scipy.optimize import linprog


def independent_masks(m):
    return [mask for mask in range(1, 1 << m)
            if not any((mask >> i) & 1 and (mask >> ((i + 1) % m)) & 1
                       for i in range(m))]


def halfspaces(m):
    u = sqrt(m / (m + 1))
    A, b, names = [], [], []
    for i in range(m):
        row = np.zeros(m + 1)
        row[i] = -1
        row[-1] = u
        A.append(row)
        b.append(0)
        names.append(('coordinate', i))
    row = np.zeros(m + 1)
    row[:m] = -1
    row[-1] = u
    A.append(row)
    b.append(-1)
    names.append(('lower_total',))
    for mask in independent_masks(m):
        j = mask.bit_count()
        row = np.zeros(m + 1)
        for i in range(m):
            row[i] = (mask >> i) & 1
        row[-1] = sqrt(j - j * j / (m + 1))
        A.append(row)
        b.append(1)
        names.append(('independent', mask))
    if m % 2:
        row = np.ones(m + 1)
        row[-1] = u
        A.append(row)
        b.append(2)
        names.append(('upper_total',))
    return np.array(A), np.array(b), names


def check(m):
    u = sqrt(m / (m + 1))
    k = m // 2
    v = sqrt(k * (m + 1 - k) / (m + 1))
    A, b, names = halfspaces(m)
    c = np.zeros(m + 1)
    c[-1] = -1
    solve = linprog(c, A_ub=A, b_ub=b,
                    bounds=[(None, None)] * m + [(0, None)], method='highs')
    assert solve.success, (m, solve.message)
    if m == 4:
        rho = 1 / (u + 2 * v)
        s = (u + v) / (4 * v + 2 * u)
    else:
        rho = 1 / (k * u + v)
        s = u / (k * u + v)
    assert abs(solve.x[-1] - rho) < 2e-8, (m, solve.x[-1], rho)
    center = np.full(m, s)
    gaps = b - A @ np.r_[center, rho]
    assert gaps.min() > -2e-9, (m, gaps.min())
    tight = [name for gap, name in zip(gaps, names) if abs(gap) < 2e-8]
    kmax = 2 if m % 2 == 0 else m
    if m == 4:
        assert len(tight) == 3, tight
        assert ('lower_total',) in tight
        assert sum(name[0] == 'independent' for name in tight) == 2
        # Opposite pair sums fixed; independent variations in each pair.
        lo = rho * u
        for first, second in ((lo, lo), (2*s-lo, lo), (lo, 2*s-lo),
                              (2*s-lo, 2*s-lo)):
            candidate = np.array([first, second, 2*s-first, 2*s-second])
            assert (b - A @ np.r_[candidate, rho]).min() > -2e-9
    elif m == 3:
        assert len(tight) == 8, tight
    else:
        assert len(tight) == m + kmax, (m, len(tight), m + kmax)
        assert sum(name[0] == 'coordinate' for name in tight) == m
        assert sum(name[0] == 'independent' for name in tight) == kmax
    # Every vertex of the generating convex hull satisfies the proposed H-description.
    gen = []
    for i in range(m):
        vtx = np.zeros(m)
        vtx[i] = 1
        gen.append(vtx)
        vtx2 = np.zeros(m)
        vtx2[i] = 1
        vtx2[(i + 1) % m] = 1
        gen.append(vtx2)
    for vtx in gen:
        assert (b - A[:, :m] @ vtx).min() > -1e-9
    return m, len(names), rho, len(tight)


if __name__ == '__main__':
    for m in range(3, 17):
        print('m, inequalities, radius, contacts:', check(m))
    print('WHEEL_ORDINARY_EDGE_INBALL_LP_CHECKS_PASSED')
