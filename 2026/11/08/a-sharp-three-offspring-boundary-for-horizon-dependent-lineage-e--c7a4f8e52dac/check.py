"""Exact checks for the bounded-offspring extinction comparison theorem.

Run with Python 3.9+; no nonstandard dependencies. The general proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations


def pgf(p, z):
    return sum(prob * z ** i for i, prob in enumerate(p))


def mean(p):
    return sum(i * prob for i, prob in enumerate(p))


def extseq(p, generations):
    v = Q(0)
    out = []
    for _ in range(generations):
        v = pgf(p, v)
        out.append(v)
    return out


def sign(x):
    return (x > 0) - (x < 0)


p = tuple(Q(v, 15) for v in (4, 6, 0, 5))
q = tuple(Q(v, 15) for v in (5, 0, 9, 1))
assert sum(p) == sum(q) == 1
assert mean(p) == mean(q) == Q(7, 5)
a, b = p[0] - q[0], p[3] - q[3]
c = -a / b
assert c == Q(1, 4)
assert pgf(q, c) - c == Q(39, 320)
for z in (Q(i, 20) for i in range(21)):
    assert pgf(p, z) - pgf(q, z) == (1-z)**2 * (a+b*z)
pe, qe = extseq(p, 5), extseq(q, 5)
assert pe[0] - qe[0] == -Q(1, 15)
assert pe[1] - qe[1] == -Q(77, 3375)
assert pe[2] - qe[2] == Q(5919069959, 3113912109375)
assert all(x > y for x, y in zip(pe[2:], qe[2:]))

# Non-proof cross-check: exhaustive small rational coefficient grids, at equal means.
# Only strict ranking changes are counted, so exact ties cannot falsely register one.
checks = 0
for denom in range(4, 8):
    candidates = []
    for a0 in range(1, denom):
        for a1 in range(denom-a0+1):
            for a2 in range(denom-a0-a1+1):
                a3 = denom-a0-a1-a2
                pp = tuple(Q(x,denom) for x in (a0,a1,a2,a3))
                if mean(pp) > 1:
                    candidates.append((pp, extseq(pp, 5)))
    for (f, fs), (g, gs) in combinations(candidates, 2):
        if mean(f) != mean(g):
            continue
        delta = [sign(x-y) for x,y in zip(fs, gs)]
        distinct = [v for v in delta if v]
        changes = sum(x != y for x,y in zip(distinct,distinct[1:]))
        assert changes <= 1, (denom,f,g,delta)
        if f[3]==g[3]==0:
            assert changes == 0
        checks += 1

print('PASS: exact factorization, threshold and 3-generation reversal')
print('PASS: %d additional equal-mean rational pair comparisons' % checks)
print('LIMIT: finite grid is corroborative; general result uses the proof')
