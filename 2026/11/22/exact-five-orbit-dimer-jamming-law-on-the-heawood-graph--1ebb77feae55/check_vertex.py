#!/usr/bin/env python3
"""Exact rational vertex-mask recurrence for dimer deposition on a Fano incidence graph."""
from fractions import Fraction
from functools import lru_cache

LINES = [frozenset(((j + d) % 7 for d in (0, 1, 3))) for j in range(7)]
EDGES = sorted((i, 7 + j) for j, line in enumerate(LINES) for i in line)
assert len(EDGES) == 21 and len(set(LINES)) == 7

@lru_cache(maxsize=None)
def law(used):
    available = [(u, v) for u, v in EDGES if not (used >> u & 1 or used >> v & 1)]
    if not available:
        return (Fraction(1),)
    out = {}
    for u, v in available:
        for k, prob in enumerate(law(used | (1 << u) | (1 << v))):
            out[k + 1] = out.get(k + 1, Fraction(0)) + prob / len(available)
    return tuple(out.get(k, Fraction(0)) for k in range(max(out) + 1))

EXPECTED = {5: Fraction(19, 330), 6: Fraction(497, 792),
            7: Fraction(1247, 3960)}
got = {k: p for k, p in enumerate(law(0)) if p}
assert got == EXPECTED
assert sum(got.values()) == 1
assert sum(k * p for k, p in got.items()) == Fraction(24779, 3960)

# The first edge is arbitrary by flag transitivity. Fix it and split
# the next sixteen admissible choices by the number of remaining bonds.
u, v = EDGES[0]
used = (1 << u) | (1 << v)
classes = {}
for a, b in EDGES:
    if used >> a & 1 or used >> b & 1:
        continue
    next_used = used | (1 << a) | (1 << b)
    remaining = sum(1 for x, y in EDGES
                    if not (next_used >> x & 1 or next_used >> y & 1))
    classes.setdefault(remaining, []).append(law(next_used))
assert sorted((key, len(val)) for key, val in classes.items()) == [(11, 8), (12, 8)]
for key, vals in classes.items():
    assert all(row == vals[0] for row in vals)
assert classes[12][0][3:] == (Fraction(4, 105), Fraction(731, 1260), Fraction(481, 1260))
assert classes[11][0][3:] == (Fraction(89, 1155), Fraction(1559, 2310), Fraction(191, 770))
print('PASS vertex-mask recurrence:', got, 'states:', law.cache_info().currsize)
print('PASS two second-edge classes: 8+8, residual bonds 11 and 12')
