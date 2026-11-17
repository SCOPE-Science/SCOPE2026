"""Exact arithmetic diagnostics for weighted wheel Poincare constants.

Run with: python check_wheels.py
Finite checks supplement, not replace, the general analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def cut_score(r, a, b, mask):
    s = mask.bit_count()
    if not s:
        return F(0)
    changes = sum(bool(mask & (1 << j)) != bool(mask & (1 << ((j + 1) % r))) for j in range(r))
    energy = a * s + b * changes
    return F(2 * (a + b), r + 1) * F(s * (r + 1 - s), energy)


def formula(r, a, b):
    return F(2 * (a + b), r + 1) * max(
        [F(1, a)] + [F(s * (r + 1 - s), a * s + 2 * b) for s in range(1, r)]
    )


def metric_upper(r, a, b):
    ks = [min(j, r - j) for j in range(2, r - 1)]
    ts = {F(0), F(2)} | {F(2, k) for k in ks}
    return max(
        F(2 * (a + b), r + 1)
        * (1 + t + sum((min(F(2), t * k) for k in ks), F(0)) / 2)
        / (a + b * t) for t in ts
    )


def symmetric_cut_metric(r, s):
    arcs = [set((shift + k) % r for k in range(s)) for shift in range(r)]
    def distance(u, v):
        return F(sum((u in arc) != (v in arc) for arc in arcs), r)
    spoke = F(s, r)
    rim = F(2, r)
    # Hub is represented by -1, outside all arcs.
    assert distance(-1, 0) == spoke
    assert distance(0, 1) == rim
    for k in range(2, r - 1):
        assert distance(0, k) == min(2 * spoke, min(k, r - k) * rim)


checks = 0
for r in range(4, 14):
    for a, b in [(1, 1), (1, 2), (2, 1), (1, 16), (16, 1), (3, 7)]:
        a, b = F(a), F(b)
        expected = formula(r, a, b)
        assert metric_upper(r, a, b) == expected
        brute = max(cut_score(r, a, b, mask) for mask in range(1, 1 << r))
        assert brute == expected, (r, a, b, expected, brute)
        checks += (1 << r) - 1
for r in range(4, 160):
    for a, b in [(1, 1), (1, 2), (2, 1), (1, 500), (500, 1), (13, 37)]:
        assert metric_upper(r, F(a), F(b)) == formula(r, F(a), F(b)), (r, a, b)
        checks += 1
for r in range(4, 35):
    for s in range(2, r // 2 + 1):
        symmetric_cut_metric(r, s)
        checks += 1
print('WEIGHTED_WHEEL_EXACT_OK', checks, 'exact checks; r=4..159; all cuts r=4..13')
