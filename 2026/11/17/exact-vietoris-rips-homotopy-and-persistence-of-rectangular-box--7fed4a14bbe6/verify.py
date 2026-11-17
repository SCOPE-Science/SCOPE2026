#!/usr/bin/env python3
"""Exact combinatorial checks for the Euclidean Rips filtration of box vertices.

All squared side lengths and squared-distance filtration values are rational
integers in these checks. The mathematical proof is independent of testing.
"""
from collections import Counter
from itertools import combinations


def face_grade(mask, weights):
    vertices = [i for i in range(8) if mask & (1 << i)]
    return max((sum(weights[k] for k in range(3)
                    if ((u ^ v) >> k) & 1)
                for u, v in combinations(vertices, 2)), default=0)


def filtration(weights):
    faces = [(face_grade(s, weights), s.bit_count() - 1, s)
             for s in range(1, 1 << 8)]
    faces.sort()
    return faces


def barcodes(weights):
    faces = filtration(weights)
    pos = {s: i for i, (_, _, s) in enumerate(faces)}
    pivots = {}
    pairs = {}
    births = set()
    for j, (grade, dim, mask) in enumerate(faces):
        col = 0
        if dim:
            for v in range(8):
                if mask >> v & 1:
                    col ^= 1 << pos[mask ^ (1 << v)]
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                pairs[p] = j
                break
        if not col:
            births.add(j)
    ans = Counter()
    for i, j in pairs.items():
        d = faces[i][1]
        start, end = faces[i][0], faces[j][0]
        if start != end:
            ans[(d, start, end)] += 1
    for i in births - pairs.keys():
        d, start = faces[i][1], faces[i][0]
        ans[(d, start, None)] += 1
    return ans


def expected_bars(w):
    a, b, c = w
    ans = Counter({(0, 0, None): 1})
    for dim, start, end, multiplicity in [
        (0, 0, a, 4), (0, 0, b, 2), (0, 0, c, 1),
        (1, b, a+b, 2), (1, c, a+c, 2),
        (1, c, b+c, 1), (3, b+c, a+b+c, 1)]:
        if start != end:
            ans[(dim, start, end)] += multiplicity
    return ans


def betti(faces):
    bydim = {}
    for _, d, m in faces:
        bydim.setdefault(d, []).append(m)
    rank = {}
    for d in sorted(bydim):
        if d == 0:
            rank[d] = 0
            continue
        row = {m: j for j, m in enumerate(bydim[d-1])}
        piv = {}
        for m in bydim[d]:
            col = 0
            for v in range(8):
                if m >> v & 1:
                    col ^= 1 << row[m ^ (1 << v)]
            while col:
                p = col.bit_length()-1
                if p in piv:
                    col ^= piv[p]
                else:
                    piv[p] = col
                    break
        rank[d] = len(piv)
    return {d:len(cols)-rank.get(d,0)-rank.get(d+1,0)-(d==0)
            for d,cols in bydim.items()}


def expected_betti(w,t):
    a,b,c = w
    if t<a: return {0:7}
    if t<b: return {0:3}
    if t<min(c,a+b): return {0:1,1:2}
    if c < a+b and c<=t<a+b:return {1:5}
    if a+b < c and a+b<=t<c:return {0:1}
    if t< a+c:return {1:3}
    if t< b+c:return {1:1}
    if t< a+b+c:return {3:1}
    return {}


def validate(weights):
    assert 0 < weights[0] <= weights[1] <= weights[2]
    got = barcodes(weights)
    expected = expected_bars(weights)
    if got != expected:
        raise AssertionError((weights, got, expected))
    scales = sorted({0, *weights, weights[0]+weights[1],
                     weights[0]+weights[2], weights[1]+weights[2],
                     sum(weights)})
    for s in scales:
        ff = [f for f in filtration(weights) if f[0] <= s]
        actual = {d:k for d,k in betti(ff).items() if k}
        pred = expected_betti(weights,s)
        if actual != pred:
            raise AssertionError(('homology',weights,s,actual,pred))
    return len(scales)


def main():
    count=0
    stages=0
    # All integer squared side lengths from one through twelve, including ties
    # and the Pythagorean wall, provide an extensive exact finite stress test.
    for a in range(1,13):
        for b in range(a,13):
            for c in range(b,13):
                stages += validate((a,b,c))
                count += 1
    assert count == 364, count
    print('INTEGER_WEIGHT_TRIPLES:',count)
    print('FILTRATION_STAGE_CHECKS:',stages)
    print('PERSISTENCE: exact boundary-matrix reduction over F_2: PASS')
    print('HOMOLOGY: independent per-stage mod-two boundary ranks: PASS')
    print('ALL_EQUAL_AND_PYTHAGOREAN_WALLS: included')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
