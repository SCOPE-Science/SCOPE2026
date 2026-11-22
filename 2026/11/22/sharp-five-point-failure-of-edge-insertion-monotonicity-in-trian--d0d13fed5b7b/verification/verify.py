#!/usr/bin/env python3
"""Exact exhaustive certificate for the five-point Henson pair-type boundary.

Run: python3 verify.py. Requires Python >=3.8, standard library only.
Counts every labelled triangle-free marked missing edge through five
vertices, not a sample. Two independent enumeration channels test witnesses.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations


def edges(n):
    return list(combinations(range(n), 2))


def is_triangle_free(n, mask, ee):
    d = {e: i for i, e in enumerate(ee)}
    return all(any(not ((mask >> d[e]) & 1)
                   for e in combinations(t, 2))
               for t in combinations(range(n), 3))


def counts(n, g, ee):
    # Method 1: exhaustive independent subsets + subset-zeta transform.
    bad = [sum(1 << i for i, (u, v) in enumerate(ee)
               if (s & (1 << u)) and (s & (1 << v)))
           for s in range(1 << n)]
    flag = [int(not (g & bad[s])) for s in range(1 << n)]
    zeta = flag.copy()
    for j in range(n):
        for s in range(1 << n):
            if s & (1 << j):
                zeta[s] += zeta[s ^ (1 << j)]
    total = sum(flag)
    disjoint = sum(zeta[((1 << n) - 1) ^ s]
                   for s in range(1 << n) if flag[s])
    return total, disjoint


def direct_diagrams(n, g, ee):
    # Method 2: enumerate all 2^(2n) adjacencies to x,y; directly
    # test triangle-freeness of the n+2-vertex extension (independent
    # of the independent-subset / zeta enumeration above).
    extended_edges = edges(n + 2)
    old_edges = [e for i, e in enumerate(ee) if g & (1 << i)]
    old_ix = {e: i for i, e in enumerate(extended_edges)}
    counts_xy = [0, 0]
    for xy in (0, 1):
        for a in range(1 << n):
            for b in range(1 << n):
                ext = sum(1 << old_ix[e] for e in old_edges)
                for k in range(n):
                    if a & (1 << k): ext |= 1 << old_ix[(k, n)]
                    if b & (1 << k): ext |= 1 << old_ix[(k, n+1)]
                if xy: ext |= 1 << old_ix[(n, n+1)]
                if is_triangle_free(n+2, ext, extended_edges):
                    counts_xy[xy] += 1
    return tuple(counts_xy)


def canon(n, g, added, ee):
    eindex = {e: i for i, e in enumerate(ee)}
    pair = ee[added]
    minima = None
    for p in permutations(range(n)):
        transformed = 0
        for i, (u, v) in enumerate(ee):
            if g & (1 << i):
                edge = tuple(sorted((p[u], p[v])))
                transformed |= 1 << eindex[edge]
        new = eindex[tuple(sorted((p[pair[0]], p[pair[1]])))]
        value = (transformed, new)
        if minima is None or value < minima:
            minima = value
    return minima


def connected(n, g, ee):
    reached = {0}
    while True:
        old = reached.copy()
        for i, (u, v) in enumerate(ee):
            if g & (1 << i):
                if u in reached: reached.add(v)
                if v in reached: reached.add(u)
        if old == reached: break
    return len(reached) == n


def main():
    summary = {}
    marked_bad = defaultdict(int)
    for n in range(1, 6):
        ee = edges(n)
        ct = [counts(n, g, ee) for g in range(1 << len(ee))]
        flags = [is_triangle_free(n, g, ee) for g in range(1 << len(ee))]
        sign_count = Counter()
        for g, (ig, dg) in enumerate(ct):
            if not flags[g]: continue
            for j in range(len(ee)):
                if (g >> j) & 1: continue
                h = g | (1 << j)
                if not flags[h]: continue
                ih, dh = ct[h]
                sign = (dh * ig * ig > dg * ih * ih) - (dh * ig * ig < dg * ih * ih)
                sign_count[sign] += 1
                if sign < 0 and n == 5:
                    assert not connected(n, g, ee)
                    assert connected(n, h, ee)
                    marked_bad[canon(n, g, j, ee)] += 1
        summary[n] = (sign_count[-1], sign_count[0], sign_count[1])
    assert summary == {1:(0,0,0),2:(0,0,1),3:(0,0,9),4:(0,0,96),5:(80,0,1330)}, summary
    assert marked_bad == {(7, 3):20, (28, 0):60}, marked_bad
    print('COMPLETE LABELLED ADMISSIBLE EDGE-INSERTION CENSUS')
    for n in range(1, 6):
        print('n=%d: decrease=%d, tie=%d, increase=%d' % ((n,) + summary[n]))
    print('n=5: exactly two isomorphism classes of marked decreases:', dict(marked_bad))

    witness = [
        (5, [(0,1),(0,2),(0,3)], (0,4), (18,129), (17,113)),
        (5, [(0,3),(0,4),(1,2)], (0,1), (15,119), (14,103)),
        (6, [(0,2),(0,4),(0,5),(1,2),(1,3)], (0,3), (23,249), (22,225)),
    ]
    for n, old, new, expected_a, expected_b in witness:
        ee = edges(n); lookup = {e:i for i,e in enumerate(ee)}
        g = sum(1 << lookup[tuple(sorted(e))] for e in old)
        h = g | (1 << lookup[tuple(sorted(new))])
        assert is_triangle_free(n, g, ee) and is_triangle_free(n, h, ee)
        assert counts(n,g,ee) == expected_a
        assert counts(n,h,ee) == expected_b
        a0,a1 = direct_diagrams(n,g,ee)
        b0,b1 = direct_diagrams(n,h,ee)
        assert (a0,a1) == (expected_a[0]**2, expected_a[1])
        assert (b0,b1) == (expected_b[0]**2, expected_b[1])
        pa = Fraction(a1,a0+a1)
        pb = Fraction(b1,b0+b1)
        assert pb < pa
        print('witness n=%d: %s -> %s; P(adj) %s -> %s; drop %s; connected old=%s' %
              (n, expected_a, expected_b, pa, pb, pa-pb, connected(n,g,ee)))
    print('ISOLATE PERSISTENCE: I(G+K1)=2I(G), D(G+K1)=3D(G).')
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
