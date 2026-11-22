#!/usr/bin/env python3
"""Finite checks for a marked-rare-obstruction theorem.

This script checks finite combinatorial identities and deterministic diameter
implications. It is not a substitute for the limiting Poisson-process proof.
Run: python3 check.py
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

checked = 0

def verify(statement):
    global checked
    assert statement
    checked += 1

# One-coordinate random-subset inclusion and shared-endpoint rates.
patterns = list(product((0, 1), repeat=2))
verify(sum(a <= b for a, b in patterns) == 3)
triples = list(product((0, 1), repeat=3))
verify(sum(a <= b and a <= c for a, b, c in triples) == 5)
verify(sum(a <= b and c <= b for a, b, c in triples) == 5)
verify(sum(a <= b and b <= c for a, b, c in triples) == 4)
verify(sum(a <= b and b <= a for a, b in patterns) == 2)

allowed = [(a, b) for a, b in patterns if a <= b]
ma = sum(F(a, 3) for a, b in allowed)
mb = sum(F(b, 3) for a, b in allowed)
va = sum(F(a * a, 3) for a, b in allowed) - ma * ma
vb = sum(F(b * b, 3) for a, b in allowed) - mb * mb
cov = sum(F(a * b, 3) for a, b in allowed) - ma * mb
verify((ma, mb, va, vb, cov) == (F(1, 3), F(2, 3), F(2, 9), F(2, 9), F(1, 9)))
verify(F(cov, va) == F(1, 2))
verify(5 < 3 * sqrt(3)) # Shared-endpoint correction decays exponentially.

# Direct enumerate independent uniform subsets of coordinate lengths 1..5.
for n in range(1, 6):
    universe = range(1 << n)
    total2 = len(universe) ** 2
    inc = eq = 0
    for a, b in product(universe, repeat=2):
        inc += (a & ~b) == 0
        eq += a == b
        verify(((a & ~b) == 0) == all((a >> t & 1) <= (b >> t & 1) for t in range(n)))
    verify(F(inc, total2) == F(3, 4) ** n)
    verify(F(eq, total2) == F(1, 2) ** n)
    same_source = same_target = chain = 0
    for a, b, c in product(universe, repeat=3):
        same_source += ((a & ~b) == 0 and (a & ~c) == 0)
        same_target += ((a & ~b) == 0 and (c & ~b) == 0)
        chain += ((a & ~b) == 0 and (b & ~c) == 0)
    verify(F(same_source, len(universe) ** 3) == F(5, 8) ** n)
    verify(F(same_target, len(universe) ** 3) == F(5, 8) ** n)
    verify(F(chain, len(universe) ** 3) == F(1, 2) ** n)


def distances(rows, m, n):
    # rows are bit masks: 1 encodes left -> right, 0 right -> left
    size = m + n
    edges = [[] for _ in range(size)]
    for i in range(m):
        for j in range(n):
            if rows[i] & (1 << j):
                edges[i].append(m + j)
            else:
                edges[m + j].append(i)
    all_dist = []
    for root in range(size):
        d = [float('inf')] * size
        d[root] = 0
        q = [root]
        for x in q:
            for y in edges[x]:
                if d[y] == float('inf'):
                    d[y] = d[x] + 1
                    q.append(y)
        all_dist.append(d)
    return all_dist

# Verify the subset/reachability equivalence and the global E => diameter law.
for m, n in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 3)):
    full = (1 << n) - 1
    for rows in product(range(1 << n), repeat=m):
        d = distances(rows, m, n)
        bad = 0
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                bad_ij = (rows[i] & ~rows[j]) == 0
                verify(bad_ij == (d[i][j] != 2))
                bad += bad_ij
        all_row_nontrivial = all(0 < a < full for a in rows)
        right_2 = all(d[m+i][m+j] == 2 for i in range(n) for j in range(n) if i != j)
        cross_3 = all(d[i][m+j] <= 3 and d[m+j][i] <= 3 for i in range(m) for j in range(n))
        if all_row_nontrivial and right_2 and cross_3:
            diameter = max(max(a) for a in d)
            verify(diameter == (4 if bad else 3))

print('PASS:', checked, 'assertions')
