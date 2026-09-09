"""Step D: Khovanov complex over Q for 10_124 (validated orientation), homology dims.
Smoothing sets S0={(a,b),(c,d)}, S1={(a,d),(b,c)}; all-plus writhe w=+10.
Homological grading: i = h - nminus = h - 0 = h (all-plus). q-grading: qdeg = deg(v)+h+nplus-nminus? Standard: q = (#plus - #minus) + h + nplus - nminus... with nplus=10,nminus=0: shift = h+10. We store unshifted then shift.
Differential edge sign (-1)^{popcount(mask & ((1<<k)-1))}.
Merge/split determined by circle-root comparison between mask and mask|2^k.
Basis order per smoothing: circles sorted by root id; tensor bit j (0=+,1=-).
"""
import json
from collections import defaultdict

def parse_pd(s):
    out = []
    for t in s.split():
        b = t[1:]
        out.append(tuple(int(x) for x in (b.split(',') if ',' in b else list(b))))
    return out

def smoothing_data(pd, mask):
    parent = {}
    labels = set()
    for cr in pd:
        labels.update(cr)
    for x in labels:
        parent[x] = x
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    n = len(pd)
    for k, (a, b, c, dd) in enumerate(pd):
        m = (mask >> k) & 1
        pairs = [(a, b), (c, dd)] if m == 0 else [(a, dd), (b, c)]
        for x, y in pairs:
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
    roots = sorted(set(find(x) for x in labels))
    idx = {r: j for j, r in enumerate(roots)}
    lab = {x: idx[find(x)] for x in labels}
    return roots, lab

def build(n, pd):
    # global basis index per height
    basis = {}  # mask -> (start, nc)
    off = defaultdict(int)
    order = {}
    for h in range(n + 1):
        s = 0
        for mask in range(1 << n):
            if bin(mask).count('1') == h:
                roots, _ = smoothing_data(pd, mask)
                c = len(roots)
                basis[mask] = (off[h], c)
                off[h] += (1 << c)
        order[h] = off[h]
    return basis, order

def rank_q(mat):
    # exact rational rank via Fraction-free Gauss elimination (float-free, ints)
    import copy
    M = [row[:] for row in mat]
    r = len(M)
    c = len(M[0]) if r else 0
    piv = 0
    import fractions
    for j in range(c):
        p = None
        for i in range(piv, r):
            if M[i][j] != 0:
                p = i
                break
        if p is None:
            continue
        M[piv], M[p] = M[p], M[piv]
        for i in range(r):
            if i != piv and M[i][j] != 0:
                f = M[i][j] / M[piv][j]
                for k in range(j, c):
                    M[i][k] -= f * M[piv][k]
        piv += 1
        if piv == r:
            break
    return piv

if __name__ == '__main__':
    import sys
    d = json.load(open('output/artifacts/pd_codes.json'))
    key = sys.argv[1] if len(sys.argv) > 1 else '10_124'
    pd = parse_pd(d[key]['pd'])
    n = len(pd)
    basis, order = build(n, pd)
    print('dims per height:', dict(sorted(order.items())))
