#!/usr/bin/env python3
"""Scope G*: alternating Montesinos knot diagrams with length>=4,
total crossings in {17,18,19}, every twist region <=3 crossings.
Pure stdlib (no SnapPy/Sage available in this environment).

Part A: pretzel subfamily P(a1..an), ai in {2,3} (one twist region each),
  all same sign -> reduced alternating, crossings = sum(ai).
  Components counted exactly via union-find on the standard diagram.
Part B: length-4 Montesinos with 2-stage rational tangles [x,y], x,y in {1,2,3}.
  Internal tangle pairing from the classical parity rule for slope p/q;
  global components via union-find with cyclic closure.
Results are CANDIDATE counts (diagram/multiset level). Per-knot hyperbolicity
certification and exact isotopy classification are NOT done here -- that gap is
part of the documented block (see WORKLOG / target_exit_request).
"""
from itertools import product


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


def pretzel_components(a):
    n = len(a)
    N = 4 * n
    uf = UF(N)

    def T(i, k):
        return 2 * i + k

    def B(i, k):
        return 2 * n + 2 * i + k

    for i in range(n):
        uf.u(T(i, 0), T(i, 1))            # top arc within column
        uf.u(B(i, 1), B((i + 1) % n, 0))  # bottom arc to next column
        if a[i] % 2 == 0:                 # even: strands go straight
            uf.u(T(i, 0), B(i, 0))
            uf.u(T(i, 1), B(i, 1))
        else:                             # odd: strands swap
            uf.u(T(i, 0), B(i, 1))
            uf.u(T(i, 1), B(i, 0))
    return uf.ncomp()


def canonical(tp):
    # lexicographically minimal rotation/reflection representative
    n = len(tp)
    rots = [tuple(tp[(i + j) % n] for j in range(n)) for i in range(n)]
    rev = list(reversed(tp))
    rots += [tuple(rev[(i + j) % n] for j in range(n)) for i in range(n)]
    return min(rots)


def rat_pairing(p, q):
    """Internal endpoint pairing of Conway rational tangle of slope p/q.
    Endpoints 0=NW,1=NE,2=SW,3=SE. Classical parity rule:
      q even -> vertical (NW-SW, NE-SE);
      q odd  -> p even: horizontal (NW-NE, SW-SE); p odd: diagonal (NW-SE, SW-NE).
    """
    if q % 2 == 0:
        return ((0, 2), (1, 3))
    if p % 2 == 0:
        return ((0, 1), (2, 3))
    return ((0, 3), (1, 2))


def montesinos_components(slopes):
    """slopes: list of (p,q). Cyclic closure, e=0. Returns #components."""
    r = len(slopes)
    uf = UF(4 * r)
    for i, (p, q) in enumerate(slopes):
        for (x, y) in rat_pairing(p, q):
            uf.u(4 * i + x, 4 * i + y)
        j = (i + 1) % r
        uf.u(4 * i + 1, 4 * j + 0)  # top: NE_i - NW_j
        uf.u(4 * i + 3, 4 * j + 2)  # bottom: SE_i - SW_j
    return uf.ncomp()


def conway2(x, y):
    # slope of [x,y] = x + 1/y = (x*y+1)/y ; crossings = |x|+|y|
    from math import gcd
    p, q = x * y + 1, y
    g = gcd(p, q)
    return p // g, q // g


def main():
    print("== Part A: pretzel subfamily, ai in {2,3}, sum in {17,18,19} ==")
    grand_diagrams = 0
    types = {}
    for n in range(4, 12):
        for tup in product([2, 3], repeat=n):
            s = sum(tup)
            if s not in (17, 18, 19):
                continue
            c = pretzel_components(list(tup))
            grand_diagrams += 1
            if c == 1:
                key = canonical(tup)
                types[key] = types.get(key, 0) + 1
    print(f"pretzel diagrams (ordered, positive) with sum 17-19: {grand_diagrams}")
    print(f"of which KNOTS (components==1): {sum(types.values())} diagrams")
    print(f"distinct cyclic types that are knots: {len(types)}")
    knot_by_sum = {}
    for key, m in types.items():
        knot_by_sum.setdefault(sum(key), [0, 0])
        knot_by_sum[sum(key)][0] += m
        knot_by_sum[sum(key)][1] += 1
    for s in sorted(knot_by_sum):
        print(f"  sum={s}: knot diagrams={knot_by_sum[s][0]}, cyclic types={knot_by_sum[s][1]}")
    ex = [k for k in types if sum(k) == 17]
    print("example 17-crossing pretzel knot type:", ex[0] if ex else None)

    print()
    print("== Part B: length-4, all tangles 2-stage [x,y], x,y in {1,2,3} ==")
    tangles = []
    for x in (1, 2, 3):
        for y in (1, 2, 3):
            p, q = conway2(x, y)
            tangles.append(((x, y), (p, q), x + y))
    knot_cyc = {}
    ndiag = 0
    for combo in product(tangles, repeat=4):
        tot = sum(t[2] for t in combo)
        if tot not in (17, 18, 19):
            continue
        ndiag += 1
        if montesinos_components([t[1] for t in combo]) == 1:
            key = tuple(sorted(t[0] for t in combo))
            knot_cyc[key] = knot_cyc.get(key, 0) + 1
    print(f"length-4 2-stage diagrams with total 17-19: {ndiag}")
    print(f"of which KNOTS: {sum(knot_cyc.values())} diagrams, "
          f"{len(knot_cyc)} multiset types")
    shown = 0
    for key in sorted(knot_cyc):
        if shown < 5:
            print("  example type:", key, "cr =", sum(a + b for a, b in key))
            shown += 1


if __name__ == "__main__":
    main()
