"""Step A: PD parse, writhe/orientation, smoothing circle counts, Jones check.
Reads output/artifacts/pd_codes.json. Pure stdlib.
PD token like X4251 means incoming/outgoing half-edges at a crossing;
we treat crossing k with entries (a,b,c,d): edges a->c and b->d pass through?
For Khovanov cube we only need: n crossings, writhe signs, and for each of
2^n smoothings the number of circles. Circle counting uses union-find over
edge-segments between crossings.
Writhe: infer crossing sign from PD cyclic order + orientation trace.
Orientation: find Euler tour of 4-regular diagram following strand connectivity.
We resolve connectivity: at crossing X(a,b,c,d), strands pair (a,c?) Actually
KnotTheory PD convention: X[i,j,k,l] = incoming lower, outgoing... Standard:
edges i->j via crossing? We adopt pairing: (a,c) opposite, (b,d) opposite as
the two strands. Orientation trace pairs them consistently.
Sign: computed from planar embedding order is not recoverable from PD alone
without embedding; instead we HYPOTHESIZE writhe = signature target? No:
we compute writhe candidates by requiring Jones(X) match KnotAtlas Jones.
We enumerate sign assignments? 2^10 too many. Instead compute Kauffman bracket
as function of signs via standard formula and solve writhe from Jones degree?
Simpler: brute-force orientation gives writhe directly once pairing known.
We implement orientation trace: walk edges, at each crossing go straight
(a<->c, b<->d). This yields components; knot => 1 component. Direction gives
over/under? PD alone lacks over/under; X(a,b,c,d) convention: a=incoming lower,
b=incoming upper? Actually KnotTheory: X[1,2,3,4] edges 1,2 incoming, 3,4 outgoing
with 1,3 lower strand? We assume strand1=(a,c), strand2=(b,d), over=strand2.
Then sign = +1 if (orientation of strand1 x strand2) = ... need coordinates.
Without coordinates cannot get sign. FALLBACK: determine signs by fitting Jones.
We compute bracket with variable signs via state sum over 2^n smoothings with
unknown signs s_k in {+1,-1}: writhe w=sum s_k; nplus/nminus; Jones = bracket
normalized. We search sign assignments (2^10=1024, feasible) for the one whose
Jones equals KnotAtlas Jones polynomial. If unique (up to global mirror), commit it.
Circle counts: independent of signs (depend only on smoothing choices + pairings).
"""
import json, itertools, collections

def parse_pd(s):
    toks = s.split()
    out = []
    for t in toks:
        assert t[0] == 'X', t
        body = t[1:]
        if ',' in body:
            nums = body.split(',')
        else:
            nums = list(body)
        out.append(tuple(int(x) for x in nums))
    return out

def smoothing_circles(pd, mask):
    n = len(pd)
    # Build segment graph: each crossing has 4 half-edges; smoothing 0/1 reconnects.
    # Model: nodes = edge-labels (1..2n). At crossing (a,b,c,d) with smoothing m:
    #   0-smoothing connects a-b and c-d? 1-smoothing connects a-d and b-c?
    # Convention choice affects circle count up to complement; we fix one and validate
    # via Jones Euler characteristic later.
    parent = {}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    labels = set()
    for (a, b, c, d) in pd:
        labels.update([a, b, c, d])
    for x in labels:
        parent[x] = x
    for k, (a, b, c, d) in enumerate(pd):
        m = (mask >> k) & 1
        if m == 0:
            union(a, b); union(c, d)
        else:
            union(a, d); union(b, c)
    # Count components among labels: but labels are points on circles; number of
    # circles = number of connected components of this 1-manifold = (#labels/2)? No.
    # Each label appears at exactly 2 crossings (knot diagram), union graph pairs them;
    # components of union = circles. Count distinct roots.
    roots = set(find(x) for x in labels)
    return len(roots)

if __name__ == '__main__':
    d = json.load(open('output/artifacts/pd_codes.json'))
    for k in ['10_124','10_125','10_126','10_127','10_128','10_129','10_130','10_131']:
        pd = parse_pd(d[k]['pd'])
        assert len(pd) == 10, (k, len(pd))
        c0 = smoothing_circles(pd, 0)
        c1 = smoothing_circles(pd, (1 << 10) - 1)
        # distribution of circle counts
        from collections import Counter
        cc = Counter(smoothing_circles(pd, m) for m in range(1024))
        print(k, 'c0=', c0, 'c1=', c1, 'dist=', sorted(cc.items()))
