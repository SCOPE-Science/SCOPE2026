#!/usr/bin/env python3
"""S2b: checkerboard shading + Tait graph + spanning-tree determinant."""
from pretzel import build_pretzel, build_ends
from faces import rotation, faces


def shade(crossings, facelist, partner):
    # edge -> the two incident half-edges
    occ = {}
    for fi, f in enumerate(facelist):
        for h in f:
            pass
    edge_faces = {}
    he_face = {}
    for fi, f in enumerate(facelist):
        for h in f:
            he_face[h] = fi
    # map edge id -> faces: collect from half-edges
    from collections import defaultdict
    ef = defaultdict(set)
    # rebuild edge-of-halfedge: use rot order lists
    rot = rotation(crossings, build_ends(crossings))
    for xi, cyc in enumerate(rot):
        for s, e in enumerate(cyc):
            ef[e].add(he_face[(xi, s)])
    # BFS 2-color faces via dual adjacency
    adj = {i: set() for i in range(len(facelist))}
    for e, fs in ef.items():
        fs = list(fs)
        if len(fs) == 2:
            a, b = fs
            adj[a].add(b)
            adj[b].add(a)
    color = {0: 0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in color:
                color[v] = 1 - color[u]
                stack.append(v)
            assert color[v] == 1 - color[u], 'dual not bipartite'
    return color, ef


def spanning_trees(n, edges):
    # Kirchhoff cofactor via Bareiss (exact ints)
    M = [[0] * n for _ in range(n)]
    for a, b, s in edges:
        M[a][a] += 1
        M[b][b] += 1
        M[a][b] -= 1
        M[b][a] -= 1
    K = [row[:n - 1] for row in M[:n - 1]]
    return abs(bareiss_det(K))


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


def det_shaded(name, twists, mirror=False, shade_choice=0):
    crossings, nedges = build_pretzel(twists, mirror=mirror)
    ends = build_ends(crossings)
    rot = rotation(crossings, ends)
    facelist, partner = faces(crossings, ends, rot)
    color, ef = shade(crossings, facelist, partner)
    he_face = {}
    for fi, f in enumerate(facelist):
        for h in f:
            he_face[h] = fi
    shaded = [i for i, c in color.items() if c == shade_choice]
    idx = {f: k for k, f in enumerate(shaded)}
    tedges = []
    for xi, cyc in enumerate(rot):
        fs = [he_face[(xi, s)] for s in range(4)]
        sh = [f for f in fs if f in idx]
        assert len(sh) == 2, 'crossing must meet 2 shaded faces, got %s' % (fs,)
        tedges.append((idx[sh[0]], idx[sh[1]], xi))
    t = spanning_trees(len(shaded), tedges)
    print('%s shade=%d: shaded=%d tait-edges=%d det=%d'
          % (name, shade_choice, len(shaded), len(tedges), t))
    return t


if __name__ == '__main__':
    for nm, tw, mi in [('K10', [3, 3, 4], False), ('K11', [3, 3, 5], False),
                       ('K11m', [3, 3, 5], True)]:
        d0 = det_shaded(nm, tw, mi, 0)
        d1 = det_shaded(nm, tw, mi, 1)
        assert d0 == d1, 'shading mismatch'
    print('S2b-OK')
