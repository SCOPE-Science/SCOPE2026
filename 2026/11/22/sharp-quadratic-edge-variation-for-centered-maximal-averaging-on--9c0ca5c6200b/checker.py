#!/usr/bin/env python3
"""Standalone checks for the four-cycle centered maximal quadratic-variation theorem.

Run with Python 3: python checker.py
Checks symbolic branch identities with rational arithmetic; numerical tests are
supplementary and are not a substitute for the analytic cone inequalities.
"""
from fractions import Fraction as Q
from math import sqrt
import random

D = Q
ZERO = D(0)
ONE = D(1)

def branch(t, x, y, x_region, y_region):
    """Quadratic output / 4 from a specified linear branch, with exact data."""
    ap = t / 2 + x
    am = t / 2 - x if x_region == 'small' else ZERO
    if y_region == 'low':
        bp, bm = t / 6 + y / 3, t / 6 - y / 3
    elif y_region == 'mid':
        bp, bm = t / 6 + y / 3, ZERO
    else:
        bp, bm = y - t / 2, ZERO
    m = (ap + am - bp - bm) / 2
    u = (ap - am) / 2
    v = (bp - bm) / 2
    return m * m + u * u + v * v


def branch_matrix(x_region, y_region):
    axes = [(ONE, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ONE)]
    diag = [branch(*z, x_region, y_region) for z in axes]
    out = [[ZERO for _ in range(3)] for _ in range(3)]
    for i in range(3):
        out[i][i] = diag[i]
        for j in range(i + 1, 3):
            z = tuple(axes[i][k] + axes[j][k] for k in range(3))
            out[i][j] = out[j][i] = (branch(*z, x_region, y_region) - diag[i] - diag[j]) / 2
    return out


def m(rows):
    return [[D(z) for z in row] for row in rows]

EXPECTED = {
    ('small', 'low'): m([[D(1, 9), 0, 0], [0, 1, 0], [0, 0, D(1, 9)]]),
    ('small', 'mid'): m([[D(13, 72), 0, -D(1, 18)], [0, 1, 0], [-D(1, 18), 0, D(1, 18)]]),
    ('small', 'high'): m([[D(5, 8), 0, -D(1, 2)], [0, 1, 0], [-D(1, 2), 0, D(1, 2)]]),
    ('big', 'low'): m([[D(5, 72), D(1, 6), 0], [D(1, 6), D(1, 2), 0], [0, 0, D(1, 9)]]),
    ('big', 'mid'): m([[D(7, 72), D(5, 24), -D(1, 72)], [D(5, 24), D(1, 2), -D(1, 12)], [-D(1, 72), -D(1, 12), D(1, 18)]]),
    ('big', 'high'): m([[D(3, 8), D(3, 8), -D(3, 8)], [D(3, 8), D(1, 2), -D(1, 4)], [-D(3, 8), -D(1, 4), D(1, 2)]]),
}
for key, expected in EXPECTED.items():
    assert branch_matrix(*key) == expected, 'incorrect exact branch expansion: ' + str(key)

# The low-big block has characteristic polynomial 72*lambda^2 - 41*lambda + 1/2,
# or 144*lambda^2 - 82*lambda + 1 = 0.
root = sqrt(1537)
lam = (41 + root) / 144
beta = (31 + root) / 24
assert abs((144 * lam * lam - 82 * lam + 1)) < 3e-14
assert abs((lam - 0.5) * beta - 1 / 6) < 1e-14
assert 39 < root < 40 and .55 < lam < .56 and beta > .5
assert (127-root)/13824 > 0
assert (383+root)/10368 > 0
assert 5*lam/4 - 13/36 > 0
assert 5*lam/4 - 31/72 > 0
assert 9*lam/4 - 3/8 > 0

# Direct centered balls on C4, labeled (a+,a-,b+,b-), edges joining every a to every b.
def maximal(vals):
    totals = sum(vals)
    output = []
    for i in range(4):
        if i < 2:
            neighbor_sum = vals[2] + vals[3]
        else:
            neighbor_sum = vals[0] + vals[1]
        output.append(max(vals[i], (vals[i]+neighbor_sum)/3, totals/4))
    return output


def energy(vals):
    return sum((vals[i]-vals[j])**2 for i in (0,1) for j in (2,3))

rng = random.Random(20261121)
for _ in range(5000):
    a = [rng.uniform(0, 5) for k in range(4)]
    ea = energy(a)
    if ea > 1e-14:
        assert energy(maximal(a)) <= (lam + 5e-14) * ea

# Extremizer construction: min 0, two equal intermediate, one largest.
t = 1.0
extremal = [2*beta*t, 0.0, (beta-1)*t, (beta-1)*t]
assert abs(energy(maximal(extremal))/energy(extremal) - lam) < 1e-13
print('PASS: six exact rational branch matrices, algebraic identities,')
print('      cone signs, 5000 direct samples, and sharp equality witness')
print('lambda=%.15f C=%.15f beta=%.15f' % (lam, sqrt(lam), beta))
