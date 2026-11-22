"""Exact enumeration and mod-2 boundary ranks for a two-clique, two-link graph.
Run with: python checker.py
Only standard Python 3 is required.
"""
from itertools import combinations


def perfect_matchings(n, edges):
    """Return tuples of edge indices of all perfect matchings."""
    by_v = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        by_v[u].append((j, v))
        by_v[v].append((j, u))
    out = []
    def rec(remaining, chosen):
        if not remaining:
            out.append(tuple(sorted(chosen)))
            return
        u = min(remaining)
        for j, v in by_v[u]:
            if v in remaining:
                rec(remaining - {u, v}, chosen + [j])
    rec(set(range(n)), [])
    return sorted(set(out))


def complex_faces(facets, n_edges):
    faces = [set() for _ in range(len(facets[0]) + 1)]
    faces[0].add(())
    for m in facets:
        for k in range(1, len(m) + 1):
            faces[k].update(combinations(m, k))
    return [sorted(fs) for fs in faces]


def rank_gf2(boundary_columns):
    pivots = {}
    for vector in boundary_columns:
        while vector:
            k = vector.bit_length() - 1
            if k in pivots:
                vector ^= pivots[k]
            else:
                pivots[k] = vector
                break
    return len(pivots)


def homology_mod2(faces):
    """Dimensions of ordinary homology from full exact boundary ranks."""
    ranks = [0]
    for k in range(1, len(faces)):
        idx = {face: i for i, face in enumerate(faces[k-1])}
        cols = []
        for face in faces[k]:
            col = 0
            for i in range(k):
                sub = face[:i] + face[i+1:]
                col ^= 1 << idx[sub]
            cols.append(col)
        ranks.append(rank_gf2(cols))
    ranks.append(0)
    betti = [len(faces[k]) - ranks[k] - ranks[k + 1] for k in range(1, len(faces))]
    return ranks, betti


def main():
    left = list(combinations(range(6), 2))
    right = list(combinations(range(6, 12), 2))
    bridges = [(0, 6), (1, 7)]
    edges = left + right + bridges
    matchings = perfect_matchings(12, edges)
    initial = [m for m in matchings if not (30 in m or 31 in m)]
    crossed = [m for m in matchings if 30 in m and 31 in m]
    assert len(matchings) == 234
    assert len(initial) == 225 and len(crossed) == 9
    assert all((30 in m) == (31 in m) for m in matchings)

    faces = complex_faces(matchings, 32)
    fvec = tuple(map(len, faces[1:]))
    assert fvec == (32, 340, 1476, 2589, 1404, 234), fvec
    ranks, betti = homology_mod2(faces)
    assert ranks == [0, 1, 31, 309, 1163, 1170, 234, 0], ranks
    assert betti == [0, 0, 4, 256, 0, 0], betti
    assert sum((-1)**k * a for k,a in enumerate(fvec)) == -251

    # Independently compare the punctured join with all intersection faces.
    A = set()
    for pm in perfect_matchings(4, list(combinations(range(4),2))):
        A.add(tuple((list(combinations(range(4),2)))[j] for j in pm))
    # K4 punctures have three possible perfect matchings each.
    assert len(A) == 3
    initial_faces = set()
    crossed_faces = set()
    for m in initial:
        for k in range(len(m)+1): initial_faces.update(combinations(m,k))
    for m in crossed:
        for k in range(len(m)+1): crossed_faces.update(combinations(m,k))
    common = initial_faces & crossed_faces
    assert len(common) == 1+12+42+36+9  # f-vector of join of three edges and three edges
    assert all((30 not in f and 31 not in f) for f in common)
    print('PASS: matchings=234, families=(225,9)')
    print('PASS: f_vector=', fvec)
    print('PASS: mod2_boundary_ranks=', ranks)
    print('PASS: reduced_betti=(0,0,4,256,0,0), chi=-251')
    print('PASS: intersection_faces=', len(common))

if __name__ == '__main__':
    main()
