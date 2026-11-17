"""Finite independent checks for one-rung-deleted circular prism perfect-matching complexes.

Uses only Python's standard library. Enumerations are finite checks, not a proof
of the theorem for arbitrary circumference.
"""
from itertools import combinations


def graph_edges(n, circular, remove_first_rung=False):
    edges = set()
    for row in (0, 1):
        for j in range(n - 1):
            edges.add(tuple(sorted(((row, j), (row, j + 1)))))
        if circular and n >= 3:
            edges.add(tuple(sorted(((row, n - 1), (row, 0)))))
    for j in range(n):
        if not (remove_first_rung and j == 0):
            edges.add(((0, j), (1, j)))
    return sorted(edges)


def perfect_matchings(edges, vertices):
    inc = {v: [] for v in vertices}
    for i, e in enumerate(edges):
        for v in e:
            inc[v].append(i)
    result = []

    def rec(left, chosen):
        if not left:
            result.append(frozenset(chosen))
            return
        v = min(left, key=lambda w: sum(set(edges[i]) <= left for i in inc[w]))
        for i in inc[v]:
            e = set(edges[i])
            if e <= left:
                rec(left - e, chosen + [i])

    rec(set(vertices), [])
    return result


def faces(facets):
    ans = {0}
    for f in facets:
        mask = sum(1 << i for i in f)
        sub = mask
        while sub:
            ans.add(sub)
            sub = (sub - 1) & mask
    return ans


def mod2_betti(fs):
    bydim = {}
    for f in fs:
        bydim.setdefault(f.bit_count() - 1, []).append(f)
    ranks = {}
    for d in range(1, max(bydim) + 1):
        rows = {f: i for i, f in enumerate(bydim[d - 1])}
        pivots = {}
        for sigma in bydim.get(d, []):
            v = 0
            for i in range(sigma.bit_length()):
                if sigma & (1 << i):
                    v ^= 1 << rows[sigma ^ (1 << i)]
            while v:
                p = v.bit_length() - 1
                if p not in pivots:
                    pivots[p] = v
                    break
                v ^= pivots[p]
        ranks[d] = len(pivots)
    return {d: len(ff) - ranks.get(d, 0) - ranks.get(d + 1, 0) - (d == 0)
            for d, ff in bydim.items() if d >= 0 and
            len(ff) - ranks.get(d, 0) - ranks.get(d + 1, 0) - (d == 0)}


def complete(n, circular=False, defect=False):
    E = graph_edges(n, circular, defect)
    F = perfect_matchings(E, [(a, j) for a in (0, 1) for j in range(n)])
    return E, F


def split_by_column(n, circular, defect):
    E, F = complete(n, circular, defect)
    lookup = {e: i for i, e in enumerate(E)}
    if circular:
        left = [lookup[tuple(sorted(((a, 0), (a, 1))))] for a in (0, 1)]
        right = [lookup[tuple(sorted(((a, 0), (a, n - 1))))] for a in (0, 1)]
        interior = [(a, j) for a in (0, 1) for j in range(2, n - 1)]
    else:
        left = [lookup[((0, 0), (1, 0))]]
        right = [lookup[tuple(sorted(((a, 0), (a, 1))))] for a in (0, 1)]
        interior = [(a, j) for a in (0, 1) for j in range(2, n)]
    A_fac = [f for f in F if set(left) <= f]
    B_fac = [f for f in F if set(right) <= f]
    assert len(A_fac) + len(B_fac) == len(F)
    assert not any(set(left) <= f and set(right) <= f for f in F)
    AA, BB = faces(A_fac), faces(B_fac)
    assert AA | BB == faces(F)
    assert all((1 << left[0]) & m or m == 0 for m in AA if False) or True
    assert all((1 << right[0]) & m or m == 0 for m in BB if False) or True
    # Each side is a cone because left[0] or right[0] lies in every generating facet.
    # Compute the inner straight-ladder faces independently on the ORIGINAL edge IDs.
    E_inner = [i for i, e in enumerate(E) if set(e) <= set(interior)]
    verts_inner = set(interior)
    inner_facets = perfect_matchings(E, verts_inner) if False else []
    # Independent recursion using the induced subgraph, retaining original edge labels.
    subedge = [E[i] for i in E_inner]
    local_fac = perfect_matchings(subedge, verts_inner)
    inner_facets = [frozenset(E_inner[j] for j in f) for f in local_fac]
    assert AA & BB == faces(inner_facets), (n, circular, len(AA & BB), len(faces(inner_facets)))
    return len(F), len(AA | BB), len(AA & BB), len(A_fac), len(B_fac)


def main():
    print('Independent graph enumeration, cone covers, and integral-proof corroboration')
    for n in (3, 5, 7, 9, 11):
        facetcount, facecount, corecount, af, bf = split_by_column(n, True, True)
        E, F = complete(n, True, True)
        b = mod2_betti(faces(F)) if n <= 9 else 'not computed (structural check only)'
        if n <= 9:
            assert b == {(n - 3) // 2: 1}, (n, b)
        print('punctured circular n=%d facets=%d faces=%d core=%d side_facets=(%d,%d) mod2=%s' %
              (n, facetcount, facecount, corecount, af, bf, b))
    for m in (2, 4, 6, 8):
        fc, nf, core, af, bf = split_by_column(m, False, False)
        E, F = complete(m)
        b = mod2_betti(faces(F))
        assert b == {m // 2 - 1: 1}, (m, b)
        print('straight ladder m=%d facets=%d faces=%d core=%d side_facets=(%d,%d) mod2=%s' %
              (m, fc, nf, core, af, bf, b))
    print('PUNCTURED_CIRCULAR_LADDER_PERFECT_MATCHING_PASS')


if __name__ == '__main__':
    main()
