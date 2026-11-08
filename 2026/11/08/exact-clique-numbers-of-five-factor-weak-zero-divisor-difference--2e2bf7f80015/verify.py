#!/usr/bin/env python3
"""Verify exact clique formulas for five-factor finite-field difference graphs.

Standard library only. Independent Bron--Kerbosch enumeration searches the
30-vertex support quotient, avoiding reliance on the star/triangle proof.
"""
from itertools import combinations, product
from math import prod

N = 5
SUPPORTS = tuple(range(1, (1 << N) - 1))
PAIR_INDICES = tuple(combinations(range(N), 2))
TRIPLES = tuple(combinations(range(N), 3))


def expected(q):
    a = [x - 1 for x in q]
    weight = lambda ss: prod(a[k] for k in ss)
    triple_total = sum(weight(s) for s in TRIPLES)
    delta = {(i, j): a[i] * a[j] - weight(k for k in range(N) if k not in (i, j))
             for i, j in PAIR_INDICES}
    stars = [sum(max(0, delta[tuple(sorted((i, j)))]) for j in range(N) if i != j)
             for i in range(N)]
    triangles = [sum(max(0, delta[e]) for e in combinations(t, 2)) for t in TRIPLES]
    singleton = max(4 + a[i] * (
        1 + sum(a[j] for j in range(N) if j != i)
        + sum(a[j] * a[k] for j, k in combinations([j for j in range(N) if j != i], 2)))
        for i in range(N))
    return max(singleton, 5 + triple_total + max([0] + stars + triangles))


def seven_cases(q):
    a = sorted([x - 1 for x in q], reverse=True)
    w = lambda ss: prod(a[i] for i in ss)
    b = 5 + sum(w(s) for s in TRIPLES)
    d = lambda i, j: a[i] * a[j] - w(k for k in range(N) if k != i and k != j)
    u = 4 + a[0] * (
        1 + sum(a[1:]) + sum(a[j] * a[k] for j, k in combinations(range(1, 5), 2)))
    return max(u, b,
               b + d(0, 1),
               b + d(0, 1) + d(0, 2),
               b + d(0, 1) + d(0, 2) + d(0, 3),
               b + d(0, 1) + d(0, 2) + d(0, 3) + d(0, 4),
               b + d(0, 1) + d(0, 2) + d(1, 2))


def maximal_support_cliques():
    """Standard bitmask Bron--Kerbosch with pivot, without external packages."""
    adj = []
    for a in SUPPORTS:
        adj.append(sum((1 << j) for j, b in enumerate(SUPPORTS)
                       if a != b and (a & b)))
    out = []

    def bk(r, p, x):
        if not p and not x:
            out.append(tuple(SUPPORTS[j] for j in range(len(SUPPORTS)) if (r >> j) & 1))
            return
        cand = p | x
        u = max((i for i in range(len(SUPPORTS)) if cand & (1 << i)),
                key=lambda i: (p & adj[i]).bit_count(), default=None)
        todo = p if u is None else p & ~adj[u]
        while todo:
            vb = todo & -todo
            todo -= vb
            v = vb.bit_length() - 1
            bk(r | vb, p & adj[v], x & adj[v])
            p &= ~vb
            x |= vb
    bk(0, (1 << len(SUPPORTS)) - 1, 0)
    return out


FAMILIES = maximal_support_cliques()
assert len(FAMILIES) == 81, len(FAMILIES)


def quotient_optimum(q):
    a = [x - 1 for x in q]
    def weight(s):
        return 1 if s.bit_count() == 4 else prod(a[i] for i in range(5) if s & (1 << i))
    return max(sum(weight(s) for s in fam) for fam in FAMILIES)


qs = [(2, 2, 2, 2, 2), (11, 11, 11, 2, 2), (11, 11, 11, 11, 2),
      (3, 3, 3, 3, 3), (2, 3, 4, 5, 7), (2, 2, 2, 11, 11), (2, 2, 3, 5, 11)]
qs.extend(product([2, 3], [2, 4], [2, 5], [2, 3], [2, 7]))
for q in qs:
    got = quotient_optimum(q)
    assert got == expected(q) == seven_cases(q), (q, got, expected(q), seven_cases(q))
assert quotient_optimum((11, 11, 11, 2, 2)) == 1905
print('SUPPORT_OK configurations=%d maximal_families=%d example=%d' %
      (len(qs), len(FAMILIES), quotient_optimum((11, 11, 11, 2, 2))))

# Directly test weak adjacency minus zero-product adjacency using annihilator
# witnesses in the actual product of prime fields (not merely graph incidence).
for q in [(2, 2, 2, 2, 2), (3, 2, 2, 2, 2),
          (3, 3, 2, 2, 2), (2, 2, 2, 3, 3)]:
    elements = [x for x in product(*[range(p) for p in q])
                if 0 < sum(y != 0 for y in x) < 5]
    ann_basis = lambda x: [i for i in range(5) if x[i] == 0]
    support = lambda x: sum((1 << i) for i in range(5) if x[i] != 0)
    for x, y in combinations(elements, 2):
        # Any nonzero annihilator witnesses r,s may be replaced by their
        # nonzero singleton-coordinate witnesses, with r*s = 0 iff distinct.
        weak = any(i != j for i in ann_basis(x) for j in ann_basis(y))
        xy_nonzero = any((x[i] * y[i]) % q[i] for i in range(5))
        direct = weak and xy_nonzero
        sx, sy = support(x), support(y)
        predicted = bool(sx & sy) and (sx != sy or sx.bit_count() <= 3)
        assert direct == predicted, (q, x, y)
    print('RING_OK q=%s vertices=%d pairs=%d' %
          (q, len(elements), len(elements) * (len(elements) - 1) // 2))
print('VERIFY_OK')
