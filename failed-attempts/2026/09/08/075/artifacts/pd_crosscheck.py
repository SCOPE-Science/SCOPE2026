"""Independent PD-based determinant cross-check (stdlib only).

Builds the Fox-colouring matrix from the frozen KnotAtlas PD codes
(independent input string + independent arc tracing from PD edge labels),
checks base determinants (=1, as tabulated) and all 11 single-crossing-change
neighbours per diagram. Crossing change at PD crossing i = cyclically permute
its four entries (swap over/under arches). Must reproduce results.json.
"""
import json
import re


def parse_pd(s):
    return [tuple(int(v) for v in m.group(1).split(',')) for m in re.finditer(r'X([\d,]+)', s)]


K34_PD = "X4,2,5,1 X8,4,9,3 X12,5,13,6 X2,8,3,7 X9,17,10,16 X11,18,12,19 X6,13,7,14 X15,20,16,21 X17,1,18,22 X19,14,20,15 X21,10,22,11"
K42_PD = "X4,2,5,1 X8,4,9,3 X12,5,13,6 X2,8,3,7 X9,18,10,19 X11,21,12,20 X6,13,7,14 X15,10,16,11 X17,22,18,1 X19,15,20,14 X21,16,22,17"


def bareiss_det(mat):
    n = len(mat)
    if n == 0:
        return 1
    a = [row[:] for row in mat]
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            s = -1
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    s = i
                    break
            if s == -1:
                return 0
            a[k], a[s] = a[s], a[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) // prev
            a[i][k] = 0
        prev = a[k][k]
        if prev == 0:
            return 0
    return a[n - 1][n - 1]


def pd_det(pd):
    n = len(pd)
    # arcs = edge labels; each crossing (a,b,c,d): a incoming under, b/c/d ccw;
    # over-arch is b->d? Standard KnotTheory convention: X[i,j,k,l]: i lower incoming,
    # j upper incoming... For Fox colouring only the partition matters: over-strand
    # passes through entries b,d? Actually X[a,b,c,d] with a=in-under, c=out-under,
    # b,d = over-strand ends. Relation: 2*over - under_in - under_out = 0.
    edges = sorted({e for x in pd for e in x})
    assert edges == list(range(1, max(edges) + 1)), edges
    m = max(edges)
    # map each edge to an arc index: consecutive edges linked through over-strand
    # belong to the same arc; arcs run under-to-under. Build union-find over edges:
    # at crossing (a,b,c,d): over-strand connects b,d -> same arc through crossing;
    # under-strand is broken: a and c are arc ends.
    parent = list(range(m + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for (a, b, c, d) in pd:
        union(b, d)
    # relation per crossing: over-arc = arc(b), under arcs: arc ending at a, arc starting at c.
    # arc of an edge label = its component; but under-arcs: edge a's component (incoming),
    # edge c's component (outgoing). Since under-strand breaks arcs, arc(a) != arc(c) in general.
    # However union only joined over-pairs, so arc(a), arc(c) are their components. Fine.
    comps = sorted(set(find(e) for e in range(1, m + 1)))
    idx = {c: i for i, c in enumerate(comps)}
    nrows = n
    ncols = len(comps)
    M = [[0] * ncols for _ in range(nrows)]
    for r, (a, b, c, d) in enumerate(pd):
        M[r][idx[find(b)]] += 2
        M[r][idx[find(a)]] -= 1
        M[r][idx[find(c)]] -= 1
    # drop last column (one redundancy); determinant = gcd-free: |det| of minor
    minor = [row[:ncols - 1] for row in M[:ncols - 1]]
    assert len(minor) == ncols - 1 and all(len(r) == ncols - 1 for r in minor)
    return abs(bareiss_det(minor))


def flip_pd(pd, i):
    # crossing change: swap which strand is over: (a,b,c,d) -> (b,c,d,a)? No:
    # rotate so under/over roles exchange: new = (b,c,d,a)?? That preserves cyclic order
    # but exchanges under-pair (a,c) with over-pair (b,d). Correct: (b,c,d,a) has
    # under-pair (b,d), over-pair (c,a). Yes.
    out = [list(x) for x in pd]
    a, b, c, d = out[i]
    out[i] = [b, c, d, a]
    return [tuple(x) for x in out]


def main():
    pd34, pd42 = parse_pd(K34_PD), parse_pd(K42_PD)
    assert len(pd34) == 11 and len(pd42) == 11
    base34, base42 = pd_det(pd34), pd_det(pd42)
    nb34 = [pd_det(flip_pd(pd34, i)) for i in range(11)]
    nb42 = [pd_det(flip_pd(pd42, i)) for i in range(11)]
    ref = json.load(open("results.json"))
    ok = (base34 == ref["K11n34"]["det"] == 1 and base42 == ref["K11n42"]["det"] == 1
          and sorted(nb34) == sorted(ref["K11n34"]["neighbor_dets"])
          and sorted(nb42) == sorted(ref["K11n42"]["neighbor_dets"]))
    print(json.dumps({"pd_base": [base34, base42], "pd_nb34": nb34, "pd_nb42": nb42,
                      "matches_gauss_results_json": ok}, indent=2))
    assert ok, "PD cross-check mismatch"
    print("PD_CROSSCHECK_OK")


if __name__ == "__main__":
    main()
