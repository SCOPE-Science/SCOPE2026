#!/usr/bin/env python3
"""Bounded recovery test for lane-1327 TARGET viability.
(1) Estimate full G* family size: rational tangles with <=3 crossings, all same
    sign, lengths r>=4, total crossings in {17,18,19}, dihedral quotient,
    knot filter via parity pairing rule.
(2) Timed end-to-end verification sample: exterior -> volume -> symmetry group
    -> canonical-cells-are-tetrahedra, on a spread of G* knots.
"""
import time
from math import gcd
from itertools import product

# ---- (1) slopes with crossing number <= 3 (all positive) ----
# crossing number of p/q = sum of partial quotients of regular CF.


def cf(p, q):
    a = []
    while q:
        a.append(p // q)
        p, q = q, p - q * (p // q)
    return a


slopes = []  # (p, q, crossings)
seen = set()
for p in range(1, 8):
    for q in range(1, 8):
        if gcd(p, q) != 1:
            continue
        c = sum(cf(p, q))
        if c <= 3 and (p, q) not in seen:
            seen.add((p, q))
            slopes.append((p, q, c))
print("slopes with c<=3:", sorted(slopes))
by_c = {}
for s in slopes:
    by_c.setdefault(s[2], []).append(s)
print("counts by crossing:", {c: len(v) for c, v in sorted(by_c.items())})


def rat_pairing(p, q):
    if q % 2 == 0:
        return ((0, 2), (1, 3))
    if p % 2 == 0:
        return ((0, 1), (2, 3))
    return ((0, 3), (1, 2))


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def f(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def u(self, a, b):
        ra, rb = self.f(a), self.f(b)
        if ra != rb:
            self.p[ra] = rb

    def ncomp(self):
        return len(set(self.f(a) for a in range(len(self.p))))


def mont_components(sl):
    r = len(sl)
    uf = UF(4 * r)
    for i, (p, q) in enumerate(sl):
        for (x, y) in rat_pairing(p, q):
            uf.u(4 * i + x, 4 * i + y)
        j = (i + 1) % r
        uf.u(4 * i + 1, 4 * j + 0)
        uf.u(4 * i + 3, 4 * j + 2)
    return uf.ncomp()


def canonical(sl):
    n = len(sl)
    rots = [tuple(sl[(i + j) % n] for j in range(n)) for i in range(n)]
    rv = list(reversed(sl))
    rots += [tuple(rv[(i + j) % n] for j in range(n)) for i in range(n)]
    return min(rots)


t0 = time.time()
dihedral_knot_types = {}
dihedral_all = 0
# cap length: total<=19 with each>=1 -> r<=19; but r>=10 with c<=3 forces many
# 1-crossing tangles; enumerate r=4..8 fully, estimate beyond.
for r in range(4, 9):
    nr = 0
    for combo in product(slopes, repeat=r):
        tot = sum(s[2] for s in combo)
        if tot not in (17, 18, 19):
            continue
        nr += 1
        key = canonical([(s[0], s[1]) for s in combo])
        dihedral_all += 1
        if mont_components([(s[0], s[1]) for s in combo]) == 1:
            dihedral_knot_types[key] = dihedral_knot_types.get(key, 0) + 1
    print(f"r={r}: ordered diagrams={nr}  elapsed={time.time()-t0:.1f}s")
print("dihedral knot types (r=4..8):", len(dihedral_knot_types))
