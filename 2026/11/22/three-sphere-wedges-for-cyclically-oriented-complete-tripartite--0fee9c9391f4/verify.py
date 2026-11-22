#!/usr/bin/env python3
"""Independent finite checks for the cyclic three-layer multipath complex.
No third-party packages are required. Run: python3 verify.py
"""
from collections import defaultdict
from itertools import combinations


def digraph_arcs(n):
    # Vertex 0 is a; vertices 1,2 are b_0,b_1; 3..n+2 are c_j.
    # Edge order: u_0,u_1; v_{0,j},v_{1,j} for j=0..n-1; w_j.
    arcs = [(0, 1), (0, 2)]
    for j in range(n):
        arcs.extend([(1, 3 + j), (2, 3 + j)])
    arcs.extend((3 + j, 0) for j in range(n))
    return arcs


def is_multipath(subset, arcs, n):
    out = [-1] * (n + 3)
    indeg = [0] * (n + 3)
    for edge_idx in subset:
        s, t = arcs[edge_idx]
        if out[s] >= 0 or indeg[t]:
            return False
        out[s] = t
        indeg[t] = 1
    for start in range(n + 3):
        visited = set()
        at = start
        while at >= 0:
            if at in visited:
                return False
            visited.add(at)
            at = out[at]
    return True


def direct_faces(n):
    arcs = digraph_arcs(n)
    # One arc from a, one into a and at most 2 B->C arcs: at most 4 total.
    return {t for k in range(5)
            for t in combinations(range(len(arcs)), k)
            if is_multipath(t, arcs, n)}


def structural_faces(n):
    # Independent decomposition: Gamma is the 2-by-n chessboard graph.
    # Every face uses at most one u, at most one w, and a matching in v.
    uv = [None, 0, 1]
    wv = [None] + list(range(n))
    matchings = [()] + [((i, j),) for i in range(2) for j in range(n)]
    matchings += [((0, j), (1, k)) for j in range(n)
                  for k in range(n) if j != k]
    faces = set()
    for u in uv:
        for w in wv:
            for matching in matchings:
                if u is not None and w is not None and (u, w) in matching:
                    continue  # Exactly the forbidden directed triangle.
                f = []
                if u is not None:
                    f.append(u)
                if w is not None:
                    f.append(2 + 2*n + w)
                f.extend(2 + 2*j + i for i, j in matching)
                faces.add(tuple(sorted(f)))
    return faces


def mod2_betti(faces):
    grouped = defaultdict(list)
    for f in faces:
        if f:
            grouped[len(f)-1].append(f)
    for d in grouped:
        grouped[d].sort()
    ranks = {}
    for d in range(1, max(grouped) + 1):
        index = {f: i for i, f in enumerate(grouped[d-1])}
        basis = {}
        for f in grouped[d]:
            c = 0
            for j in range(len(f)):
                c ^= 1 << index[f[:j]+f[j+1:]]
            while c:
                pivot = c.bit_length() - 1
                if pivot not in basis:
                    basis[pivot] = c
                    break
                c ^= basis[pivot]
        ranks[d] = len(basis)
    betti = {d: len(grouped[d])-ranks.get(d, 0)-ranks.get(d+1, 0)
             for d in grouped}
    return [len(grouped.get(d, [])) for d in range(4)], [betti.get(d, 0) for d in range(4)]


def main():
    for n in range(3, 11):
        direct = direct_faces(n)
        structural = structural_faces(n)
        assert direct == structural, (n, len(direct ^ structural))
        f, beta = mod2_betti(direct)
        expected_f = [3*n+2, 3*n*n+5*n,
                      n**3+5*n*n-4*n, 2*n*(n-1)**2]
        assert f == expected_f, (n, f, expected_f)
        if n >= 5:
            expected_betti = [1, 0, 0, n**3-6*n*n+8*n-1]
            assert beta == expected_betti, (n, beta, expected_betti)
        print('n=%d faces=%d f=%s betti_F2=%s' % (n, len(direct), f, beta))
    print('PASS: original directed-graph generation, structural model, face polynomial, independent mod-two homology (n=3..10).')

if __name__ == '__main__':
    main()
