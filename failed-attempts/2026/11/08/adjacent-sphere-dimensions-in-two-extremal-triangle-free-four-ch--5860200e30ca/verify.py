#!/usr/bin/env python3
"""Self-contained finite certificate for two P3-free graph complexes.

Only Python's standard library is required. Face posets use nonempty bitmasks;
vertex 0 is the least significant bit. All incidence directions are checked.
"""
from collections import Counter, deque
from itertools import combinations


def groetzsch_edges():
    # Mycielski construction of the five-cycle, with shadows 5,...,9 and hub 10.
    a = set()
    def edge(u, v):
        a.add(tuple(sorted((u, v))))
    for i in range(5):
        edge(i, (i + 1) % 5)
        edge(i, ((i + 1) % 5) + 5)
        edge(i, ((i - 1) % 5) + 5)
        edge(i + 5, 10)
    return sorted(a)


def chvatal_edges():
    # Explicit zero-based labels for the twelve-vertex Chvatal graph.
    return sorted([
        (0, 1), (0, 4), (0, 6), (0, 9),
        (1, 2), (1, 5), (1, 7),
        (2, 3), (2, 6), (2, 8),
        (3, 4), (3, 7), (3, 9),
        (4, 5), (4, 8),
        (5, 10), (5, 11),
        (6, 10), (6, 11),
        (7, 8), (7, 11),
        (8, 10),
        (9, 10), (9, 11),
    ])


def graph_data(n, edges):
    assert all(0 <= a < b < n for a, b in edges)
    assert len(set(edges)) == len(edges)
    neighborhoods = [0] * n
    for u, v in edges:
        neighborhoods[u] |= 1 << v
        neighborhoods[v] |= 1 << u
    return neighborhoods


def verify_four_chromatic(n, neigh):
    # Exhaustive exact backtracking for 3-color nonexistence; also produce 4-coloring.
    order = sorted(range(n), key=lambda i: -neigh[i].bit_count())
    def colorable(k):
        colors = [-1] * n
        def solve(j):
            if j == n:
                return colors[:]
            u = order[j]
            forbidden = {colors[v] for v in range(n) if neigh[u] >> v & 1 and colors[v] >= 0}
            for c in range(k):
                if c not in forbidden:
                    colors[u] = c
                    got = solve(j + 1)
                    if got is not None:
                        return got
            colors[u] = -1
            return None
        return solve(0)
    assert colorable(3) is None
    c4 = colorable(4)
    assert c4 is not None
    return c4


def compute_faces(n, neighbors, edges):
    # Definition A: every included vertex has at most one included neighbor.
    faces_a = {
        s for s in range(1, 1 << n)
        if all((s & neighbors[v]).bit_count() <= 1 for v in range(n) if s >> v & 1)
    }
    # Definition B: avoid every triple supporting two distinct graph edges.
    forbidden_triples = set()
    for a, b in edges:
        for c in range(n):
            if c not in (a, b):
                x = (1 << a) | (1 << b) | (1 << c)
                # With vertices a,b,c, at least two edges means induced degree >= 2.
                verts = (a,b,c)
                if sum(bool(neighbors[u] >> v & 1) for u,v in combinations(verts,2)) >= 2:
                    forbidden_triples.add(x)
    faces_b = set()
    for s in range(1, 1 << n):
        if not any(s & t == t for t in forbidden_triples):
            faces_b.add(s)
    assert faces_a == faces_b
    assert all((s & (s - 1)) in faces_a or s.bit_count() == 1 for s in faces_a)
    return faces_a, len(forbidden_triples)


def pairing(faces, pivot_order):
    unmatched = set(faces)
    pairs = []
    stage = []
    for vertex in pivot_order:
        count = 0
        bit = 1 << vertex
        for s in sorted(unmatched):
            if not s & bit and s | bit in unmatched:
                unmatched.remove(s)
                unmatched.remove(s | bit)
                pairs.append((s, s | bit))
                count += 1
        stage.append(count)
    assert len(set(x for pair in pairs for x in pair)) == 2 * len(pairs)
    assert len(faces) == 2*len(pairs) + len(unmatched)
    return pairs, unmatched, stage


def verify_hasse_acyclic(faces, pairs):
    # For a pair (low,high) orient low -> high; all other covers high -> low.
    pair_set = set(pairs)
    outgoing = {s: [] for s in faces}
    indegree = {s: 0 for s in faces}
    covers = 0
    for high in faces:
        bits = high
        while bits:
            bit = bits & -bits
            bits ^= bit
            low = high ^ bit
            if low == 0:
                continue
            assert low in faces
            x, y = ((low, high) if (low, high) in pair_set else (high, low))
            outgoing[x].append(y)
            indegree[y] += 1
            covers += 1
    queue = deque(s for s in sorted(faces) if indegree[s] == 0)
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert count == len(faces), (count, len(faces))
    return covers, count


def boundary_ranks_mod2(faces):
    # Separate check of the simplicial chain groups, over F_2.
    dims = {}
    for s in faces:
        dims.setdefault(s.bit_count()-1, []).append(s)
    ranks = {}
    for d in sorted(dims):
        if d == 0:
            ranks[d] = 0
            continue
        lows = {s:i for i,s in enumerate(dims[d-1])}
        pivots = {}
        rank = 0
        for s in dims[d]:
            bits = s
            column = 0
            while bits:
                bit = bits & -bits
                bits ^= bit
                column ^= 1 << lows[s ^ bit]
            while column:
                index = column.bit_length()-1
                if index not in pivots:
                    pivots[index] = column
                    rank += 1
                    break
                column ^= pivots[index]
        ranks[d] = rank
    reduced = {}
    maxdim = max(dims)
    for d in sorted(dims):
        b = len(dims[d]) - ranks[d] - ranks.get(d+1, 0)
        if d == 0:
            b -= 1
        if b:
            reduced[d] = b
    return reduced


def main():
    examples = [
        ('Groetzsch', 11, groetzsch_edges(), [0, 5, 4, 3, 1, 7, 10, 9, 8, 6, 2], 2, 20, 312),
        ('Chvatal', 12, chvatal_edges(), list(range(11, -1, -1)), 3, 24, 424),
    ]
    for name, n, edges, order, critical_dim, expected_edges, expected_faces in examples:
        nbrs = graph_data(n, edges)
        assert len(edges) == expected_edges
        assert len(set(order)) == n and set(order) == set(range(n))
        if name == 'Groetzsch':
            assert sorted(x.bit_count() for x in nbrs) == [3]*5+[4]*5+[5]
        else:
            assert sorted(x.bit_count() for x in nbrs) == [4]*12
        assert all(not ((nbrs[u] >> v & 1) and (nbrs[u] >> w & 1) and (nbrs[v] >> w & 1)) for u,v,w in combinations(range(n), 3))  # no triangles
        colors = verify_four_chromatic(n, nbrs)
        faces, obstruction_count = compute_faces(n, nbrs, edges)
        assert len(faces) == expected_faces
        counts = dict(sorted(Counter(s.bit_count()-1 for s in faces).items()))
        pairs, remaining, stage = pairing(faces, order)
        critical = dict(sorted(Counter(s.bit_count()-1 for s in remaining).items()))
        assert critical == {0:1, critical_dim:1}, (name, critical)
        cover_count, sorted_count = verify_hasse_acyclic(faces, pairs)
        betti = boundary_ranks_mod2(faces)
        assert betti == {critical_dim:1}, (name, betti)
        print('GRAPH',name,'vertices',n,'edges',len(edges),'chromatic',4,'triangle_free',True)
        print('FACES',len(faces),'f_vector',counts,'forbidden_triples',obstruction_count)
        print('PIVOTS',order)
        print('MATCHING_PAIRS',len(pairs),'stage_counts',stage)
        print('CRITICAL',sorted(remaining),'critical_dimensions',critical)
        print('HASSE',cover_count,'topologically_sorted',sorted_count,'acyclic',True)
        print('INDEPENDENT_MOD2_BETTI',betti)
        print('HOMOTOPY_SPHERE_DIMENSION',critical_dim)
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
