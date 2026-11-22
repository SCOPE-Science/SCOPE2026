"""Exact finite combinatorial verifier for the eleven-vertex quadratic-residue tournament.

Requires Python 3.9+ standard library only. The graph, simplices, complete Morse
elimination orders, and relative elementary collapses are reconstructed here.
"""
from collections import Counter, defaultdict
from itertools import combinations

N = 11
Q = {pow(x, 2, N) for x in range(1, N)}
assert Q == {1, 3, 4, 5, 9}


def neighbors(stage):
    out = [{(v + q) % N for q in Q} for v in range(N)]
    if stage in ("deleted", "reversed"):
        assert 1 in out[0]
        out[0].remove(1)
    if stage == "reversed":
        out[1].add(0)
    return out


def complex_faces(stage):
    faces = set()
    for block in neighbors(stage):
        for r in range(1, len(block) + 1):
            for s in combinations(sorted(block), r):
                faces.add(frozenset(s))
    return faces


def counts(faces):
    return dict(sorted(Counter(len(s)-1 for s in faces).items()))


def eliminate(faces):
    """Recorded sequence of free simplicial pairs and deleted maximal critical cells.

    A critical cell is removed only when no elementary collapse is possible.
    Such an elimination order induces an acyclic face-poset Morse matching.
    For relative complexes, cells outside the subcomplex are processed only.
    """
    live = set(faces)
    pairs, critical = [], []
    while live:
        maximal = {f for f in live if not any(len(g) == len(f)+1 and f < g for g in live)}
        owners = defaultdict(list)
        for upper in maximal:
            for v in upper:
                lower = upper - {v}
                if lower in live:
                    owners[lower].append(upper)
        free = [(lower, uppers[0]) for lower, uppers in owners.items() if len(uppers) == 1]
        if free:
            lower, upper = min(free, key=lambda p:(-len(p[1]), tuple(sorted(p[0])), tuple(sorted(p[1]))))
            assert lower < upper and len(upper) == len(lower)+1
            assert upper in maximal and len(owners[lower]) == 1
            # Maximal-upper uniqueness is sufficient for freeness.
            assert not any(lower < other and other != upper for other in live)
            live.remove(lower)
            live.remove(upper)
            pairs.append((lower, upper))
        else:
            cell = max(maximal, key=lambda f:(len(f),-sum(f),tuple(-x for x in sorted(f))))
            assert not any(cell < g for g in live)
            live.remove(cell)
            critical.append(cell)
    assert 2 * len(pairs) + len(critical) == len(faces)
    return pairs, critical


def verify_acyclic(faces, pairs):
    """Verify the full directed Hasse graph has no directed cycle."""
    out = {face: [] for face in faces}
    matched = {(lower, upper) for lower, upper in pairs}
    assert len(matched) == len(pairs)
    for upper in faces:
        for v in upper:
            lower = upper - {v}
            if lower not in faces:
                continue
            if (lower, upper) in matched:
                out[upper].append(lower)
            else:
                out[lower].append(upper)
    colors = {}
    def dfs(u):
        if colors.get(u) == 1:
            raise AssertionError("Directed Morse cycle found")
        if colors.get(u) == 2:
            return
        colors[u] = 1
        for v in out[u]:
            dfs(v)
        colors[u] = 2
    for f in faces:
        dfs(f)
    assert len(colors) == len(faces)


def rank_mod2(rows, cols, faces):
    """Rank of the signed boundary matrix reduced modulo two, independently of Morse steps."""
    rindex = {s:i for i,s in enumerate(rows)}
    pivots = {}
    for upper in cols:
        mask = 0
        for v in upper:
            lower = upper - {v}
            if lower in rindex:
                mask ^= 1 << rindex[lower]
        while mask:
            pivot = mask.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = mask
                break
            mask ^= pivots[pivot]
    return len(pivots)


def mod2_betti(faces, expect_connected=True):
    bydim = {d:sorted((f for f in faces if len(f)==d+1), key=lambda f:tuple(sorted(f))) for d in range(6)}
    rank = {0:0, 6:0}
    for d in range(1,6):
        rank[d] = rank_mod2(bydim[d-1], bydim[d], faces)
    betti={d:len(bydim[d])-rank[d]-rank[d+1] for d in range(6)}
    # The degree-zero entry is unreduced; every complex here is connected.
    assert betti[0] == (1 if expect_connected else 0)
    return {d:b for d,b in betti.items() if b and d>0}


def main():
    expected = {
        "intact": ({0:11,1:55,2:110,3:55,4:11}, 110, {0:1,2:21}, {2:21}),
        "deleted": ({0:11,1:55,2:104,3:51,4:10},106,{0:1,2:18},{2:18}),
        "reversed":({0:11,1:55,2:109,3:61,4:15,5:1},117,{0:1,2:17},{2:17}),
    }
    C = {}
    for stage, (face_vector, num_pairs, critical_vector, betti_vector) in expected.items():
        C[stage] = complex_faces(stage)
        assert counts(C[stage]) == face_vector
        matches, critical = eliminate(C[stage])
        assert len(matches) == num_pairs
        verify_acyclic(C[stage], matches)
        assert counts(critical) == critical_vector
        assert mod2_betti(C[stage]) == betti_vector
        print(stage, "faces", len(C[stage]), "pairs", len(matches), "critical", critical_vector, "mod2", betti_vector)
    D,K,R = C["deleted"],C["intact"],C["reversed"]
    assert D < K and D < R
    for stage,whole, num_pairs, expected_crit in [
        ("intact/deleted",K,4,{2:3}),
        ("reversed/deleted",R,10,{3:1}),
    ]:
        diff = whole-D
        pairs,crit=eliminate(diff)
        assert len(pairs)==num_pairs and counts(crit)==expected_crit
        verify_acyclic(diff, pairs)
        assert mod2_betti(diff, expect_connected=False) == expected_crit
        print("relative", stage, "cells", len(diff), "pairs", len(pairs), "critical", expected_crit)
    # A direct finite combinatorial verification of the doubly-regular incidence.
    B = neighbors("intact")
    assert all(len(B[x] & B[y]) == 2 for x,y in combinations(range(N),2))
    assert all(sum({a,b} <= B[v] for v in range(N)) == 2 for a,b in combinations(range(N),2))
    # All 55 arcs form one orbit under affine maps with square multipliers.
    original = {(i,j) for i in range(N) for j in B[i]}
    orbit = {((a*0+b)%N,(a*1+b)%N) for a in Q for b in range(N)}
    assert original == orbit and len(orbit) == 55
    print("PASS: all 55 arcs, three absolute Morse models, and two relative collapse certificates")


if __name__ == "__main__":
    main()
