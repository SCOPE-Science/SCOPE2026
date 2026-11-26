#!/usr/bin/env python3
"""Exact finite verifier for the perfect-matching complex of the Pappus graph.

Requires only the Python standard library. A graph edge is a vertex of the complex.
All simplicial orientations use increasing lexicographic graph-edge indices.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json


def graph():
    shift = (5, 7, -7, 7, -7, -5) * 3
    edges = {tuple(sorted((i, (i + 1) % 18))) for i in range(18)}
    edges.update(tuple(sorted((i, (i + shift[i]) % 18))) for i in range(18))
    edges = sorted(edges)
    assert len(edges) == 27
    adj = [[] for _ in range(18)]
    for j, (u, v) in enumerate(edges):
        adj[u].append((v, j))
        adj[v].append((u, j))
    assert all(len(a) == 3 for a in adj)
    return edges, adj


def perfect_matchings(adj):
    def rec(remaining, chosen):
        if not remaining:
            yield chosen
            return
        v = min(remaining)
        for u, j in adj[v]:
            if u in remaining:
                yield from rec(remaining - {u, v}, chosen | (1 << j))
    return sorted(rec(frozenset(range(18)), 0))


def bipartite_perfect_matchings(edges, adj):
    parity = {0: 0}
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for u, _ in adj[v]:
            if u not in parity:
                parity[u] = 1 - parity[v]
                queue.append(u)
            else:
                assert parity[u] == 1-parity[v]
    assert len(parity) == 18
    left = sorted(v for v in parity if parity[v] == 0)
    right = sorted(v for v in parity if parity[v] == 1)
    assert len(left) == len(right) == 9
    eindex = {e: j for j, e in enumerate(edges)}
    variants = []
    for a in left:
        variants.append([(right.index(b), eindex[tuple(sorted((a,b)))])
                         for b, _ in adj[a]])
    out = []
    def rec(i, selected_right, selected_edges):
        if i == 9:
            out.append(selected_edges)
            return
        for j, e in variants[i]:
            if not ((selected_right >> j) & 1):
                rec(i+1, selected_right | (1<<j), selected_edges | (1<<e))
    rec(0, 0, 0)
    return sorted(out)


def extendible_faces(pms):
    faces = {0}
    for m in pms:
        sub = m
        while sub:
            faces.add(sub)
            sub = (sub - 1) & m
    return faces


def verify_independent_extension(edges, faces):
    # Independently enumerate ALL ordinary matchings by edge inclusion/exclusion,
    # then independently test whether each can be completed to a perfect matching.
    avoid = [(1 << a) | (1 << b) for a, b in edges]
    all_matchings = []
    def rec(i, covered, chosen):
        if i == len(edges):
            all_matchings.append((covered, chosen))
            return
        rec(i+1, covered, chosen)
        if covered & avoid[i] == 0:
            rec(i+1, covered | avoid[i], chosen | (1 << i))
    rec(0, 0, 0)
    assert len(all_matchings) == 35368

    @lru_cache(None)
    def can_cover(remaining):
        if not remaining:
            return True
        v = (remaining & -remaining).bit_length() - 1
        for j, (a,b) in enumerate(edges):
            if a != v and b != v:
                continue
            u = b if a == v else a
            if (remaining >> u) & 1 and can_cover(remaining ^ ((1<<v)|(1<<u))):
                return True
        return False
    all_vertices = (1 << 18) - 1
    computed = {m for covered, m in all_matchings
                if can_cover(all_vertices ^ covered)}
    assert computed == faces
    return len(all_matchings)


def facets(face):
    bits = [i for i in range(27) if (face >> i) & 1]
    return [(face ^ (1 << i), -1 if k & 1 else 1)
            for k, i in enumerate(bits)]


def morse(faces):
    live = set(faces) - {0}
    lower = {}
    upper = {}
    # Pair faces stagewise, toggling edge indices in descending order.
    for pivot in reversed(range(27)):
        bit = 1 << pivot
        for a in sorted(live):
            b = a | bit
            if a in live and not a & bit and b in live:
                lower[a] = b
                upper[b] = a
                live.remove(a)
                live.remove(b)
    crit = sorted(live, key=lambda f: (f.bit_count(), f))
    assert Counter(f.bit_count()-1 for f in crit) == {0: 1, 2: 5, 3: 10, 4: 1}
    assert len(lower) == len(upper) == 7901

    # Explicitly verify acyclicity by orienting every Hasse edge:
    # unmatched downward, matched upward.
    indeg = {f: 0 for f in faces if f}
    neighbors = defaultdict(list)
    incidences = 0
    for face in indeg:
        for facet, _ in facets(face):
            if facet == 0:
                continue
            if lower.get(facet) == face:
                x, y = facet, face
            else:
                x, y = face, facet
            neighbors[x].append(y)
            indeg[y] += 1
            incidences += 1
    queue = deque(x for x in indeg if indeg[x] == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in neighbors[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    assert visited == len(faces)-1
    assert incidences == 78921
    return lower, upper, live, crit, incidences


def differential(lower, upper, critical, crit):
    @lru_cache(None)
    def projection(f):
        if f in critical:
            return {f: 1}
        if f in upper:
            return {}
        partner = lower[f]
        sign = dict(facets(partner))[f]
        ans = defaultdict(int)
        for g, coef in facets(partner):
            if g == f:
                continue
            for cell, value in projection(g).items():
                ans[cell] -= sign * coef * value
        return {k:v for k,v in ans.items() if v}
    levels = {d: [f for f in crit if f.bit_count() == d+1] for d in range(5)}
    def matrix(d):
        lo = levels[d-1]
        hi = levels[d]
        row = {f:i for i,f in enumerate(lo)}
        data = [[0]*len(hi) for _ in lo]
        for j, h in enumerate(hi):
            for f, sign in facets(h):
                for a, coeff in projection(f).items():
                    data[row[a]][j] += sign * coeff
        return data
    return matrix(3), matrix(4), levels


def determinant(a):
    # Exact signed determinant by permutation expansion for square matrices of order 5.
    n = len(a)
    def rec(i, cols):
        if i == n:
            return 1
        total = 0
        for k,j in enumerate(cols):
            total += (-1 if k & 1 else 1) * a[i][j] * rec(i+1, cols[:k] + cols[k+1:])
        return total
    return rec(0, tuple(range(n)))


def gf2_homology(faces):
    # Ordinary simplicial boundary ranks, independently of the Morse reduction.
    by_dim = {d: sorted(x for x in faces if x.bit_count() == d+1)
              for d in range(9)}
    ranks = {0:1}
    for d in range(1,9):
        indices = {f:i for i,f in enumerate(by_dim[d-1])}
        pivots = {}
        for f in by_dim[d]:
            x = f
            col = 0
            while x:
                one = x & -x
                x -= one
                col ^= 1 << indices[f ^ one]
            while col:
                p = col.bit_length()-1
                if p not in pivots:
                    pivots[p] = col
                    break
                col ^= pivots[p]
        ranks[d] = len(pivots)
    dimensions = [len(by_dim[d]) for d in range(9)]
    bettis = [dimensions[d]-ranks.get(d,0)-ranks.get(d+1,0)
              for d in range(9)]
    assert dimensions == [27,297,1575,3780,4752,3456,1512,378,42]
    assert [ranks[d] for d in range(9)] == [1,26,271,1304,2471,2280,1176,336,42]
    assert bettis == [0,0,0,5,1,0,0,0,0]
    return dimensions, ranks, bettis


def main():
    edges, adj = graph()
    pms = perfect_matchings(adj)
    assert len(pms) == 42
    assert pms == bipartite_perfect_matchings(edges, adj)
    faces = extendible_faces(pms)
    assert len(faces) == 15820
    assert verify_independent_extension(edges, faces) == 35368
    low, high, critical, crit, incidences = morse(faces)
    d3, d4, levels = differential(low, high, critical, crit)
    expected3 = [
        [0,-1,-1,-1,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,1,0,1,0,1,1,1,1,0],
        [1,0,0,0,0,1,0,0,0,0],
        [-1,0,-1,0,1,0,1,1,0,-1]
    ]
    assert d3 == expected3
    assert d4 == [[0] for _ in range(10)]
    minor_columns = (0,1,2,4,8)
    minor = [[r[j] for j in minor_columns] for r in d3]
    assert determinant(minor) == -1
    assert all(sum(d3[i][j]*d4[j][0] for j in range(10)) == 0 for i in range(5))
    dimensions, ranks, bettis = gf2_homology(faces)
    certificate = {
        'graph_edges': [list(e) for e in edges],
        'perfect_matching_masks': pms,
        'faces_including_empty': len(faces),
        'nonempty_hasse_incidences': incidences,
        'matched_pairs': len(low),
        'critical_cells_by_dimension': {str(d): levels[d] for d in (0,2,3,4)},
        'morse_boundary_3': d3,
        'morse_boundary_4': d4,
        'primitive_minor_columns': list(minor_columns),
        'primitive_minor_determinant': -1,
    }
    saved = json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text('utf-8'))
    assert certificate == saved
    print('VERIFY_OK PAPPUS_PMC_INTEGRAL_MIXED_WEDGE')
    print('vertices=18 graph_edges=27 perfect_matchings=42 ordinary_matchings=35368')
    print('faces_including_empty=15820 nonempty_faces=15819 face_vector='+repr(dimensions))
    print('matched_pairs=7901 critical=1x0+5x2+10x3+1x4 directed_hasse='+str(incidences))
    print('morse_boundary_3='+repr(d3))
    print('morse_boundary_4='+repr(d4))
    print('primitive_minor_columns='+repr(minor_columns)+' determinant=-1')
    print('mod2_ranks='+repr([ranks[d] for d in range(9)]))
    print('mod2_reduced_betti='+repr(bettis))
    print('homotopy_wedge=5S3+1S4')

if __name__ == '__main__':
    main()
