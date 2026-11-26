"""Check the three six-dimer incidence types and representative weights."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations
from math import prod

V = range(1, 8)


def dot(x, y):
    return (x & y).bit_count() % 2


edges = {(x, y) for x in V for y in V if not dot(x, y)}
total = Counter()
representatives = {}
for p in V:
    for lam in V:
        if not dot(p, lam):
            continue
        X = [x for x in V if not dot(x, lam)]
        Y = {x: next(y for y in V if not dot(p, y) and not dot(x, y)) for x in X}
        points = [x for x in V if x != p]
        lines = [y for y in V if y != lam]
        census = defaultdict(set)
        for order in permutations(lines):
            m = dict(zip(points, order))
            if any((x, y) not in edges for x, y in m.items()):
                continue
            D = frozenset(x for x in X if m[x] == Y[x])
            assert len(D) == sum(not dot(x, lam) and not dot(p, y) for x, y in m.items())
            sig = frozenset((x, next(z for z in D if m[p ^ x] == (Y[z] ^ lam))) for x in D)
            assert {z for _, z in sig} == D and all(x != z for x, z in sig)
            assert all(m[x] == (Y[x] ^ lam) and m[p ^ x] == Y[x] for x in X if x not in D)
            assert sig not in census[len(D)]
            census[len(D)].add(sig)
            representatives.setdefault(len(D), tuple(m.items()))
        subtotals = {d: len(matches) for d, matches in census.items()}
        assert subtotals == {0: 1, 2: 3, 3: 2}
        for matches in census.values():
            rep = next(iter(matches))
            perm = [dict(zip(X, image)) for image in permutations(X)]
            assert {frozenset((g[x], g[z]) for x, z in rep) for g in perm} == matches
        total.update(subtotals)
assert total == {0: 28, 2: 84, 3: 56}


def order_weight(order):
    available = set(edges)
    reciprocals = []
    for x, y in order:
        assert (x, y) in available
        reciprocals.append(Fraction(1, len(available)))
        available = {(a, b) for a, b in available if x != a and y != b}
    assert not available
    return prod(reciprocals)


weights = {d: sum(map(order_weight, permutations(m))) for d, m in representatives.items()}
assert weights == {0: Fraction(261, 98560), 2: Fraction(91723, 23950080), 3: Fraction(8257, 1995840)}
print('Six-dimer orbit sizes:', dict(sorted(total.items())))
print('Probability per labelled matching:', dict(sorted(weights.items())))
