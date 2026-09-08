#!/usr/bin/env python3
"""S4a: Fox Jacobian determinant (independent of cyclic order/rotation).
Validates pair connectivity + over/under pairing as intended pretzel knots.
Fox coloring relation per crossing: 2*over_in - under_in - under_out = 0 (Z).
det = |any (n-1)x(n-1) minor| of n x (#arcs) relation matrix."""
from pretzel import build_pretzel


def arcs_and_matrix(crossings):
    # arcs: maximal overpassing strands. Each crossing's over strand passes through.
    # Build: strand pieces = edge ids; join under_out -> under_in through crossing? Standard:
    # arcs are components of diagram with underpasses cut. Represent arc ids via union-find
    # over edge pieces: at crossing i, over edges (e1,e2) belong to same arc.
    parent = {}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    edges = set()
    for x in crossings:
        for e in x['under'] + x['over']:
            edges.add(e)
            if e not in parent:
                parent[e] = e
    for x in crossings:
        a, b = x['over']
        union(a, b)
    arcid = {}
    for e in edges:
        arcid[e] = find(e)
    labels = sorted(set(arcid.values()))
    idx = {l: k for k, l in enumerate(labels)}
    n = len(crossings)
    m = len(labels)
    M = [[0] * m for _ in range(n)]
    for i, x in enumerate(crossings):
        u1, u2 = x['under']
        o1, o2 = x['over']
        M[i][idx[arcid[u1]]] -= 1
        M[i][idx[arcid[u2]]] -= 1
        M[i][idx[arcid[o1]]] += 2
    return M, m


def bareiss_det(A):
    n = len(A)
    if n == 0:
        return 1
    M = [row[:] for row in A]
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    M[k], M[i] = M[i], M[k]
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return M[n - 1][n - 1]


def fox_det(twists, mirror=False):
    crossings, _ = build_pretzel(twists, mirror=mirror)
    M, m = arcs_and_matrix(crossings)
    # delete last row and last col -> (m-1)x(m-1)? Standard: n crossings, m arcs; for knot m=n+1? Use square minor:
    # Take first (m-1) rows? Need m-1 <= n. Use rows 0..m-2, cols 0..m-2.
    assert m - 1 <= len(M), 'not enough rows: arcs=%d xings=%d' % (m, len(M))
    K = [row[:m - 1] for row in M[:m - 1]]
    return abs(bareiss_det(K)), m


if __name__ == '__main__':
    for nm, tw, mi in [('K10', [3, 3, 4], False), ('K11', [3, 3, 5], False),
                       ('K11m', [3, 3, 5], True), ('trefoil', [1, 1, 1], False),
                       ('trefoil-m', [1, 1, 1], True)]:
        d, m = fox_det(tw, mi)
        print('%s mirror=%s: arcs=%d fox-det=%d' % (nm, mi, m, d))
    print('S4a-OK')
