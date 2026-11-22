#!/usr/bin/env python3
"""Standalone finite checks for two reverse arcs in K_{2,n} multipath complexes.

A directed-multipath face is an acyclic edge set of indegree and outdegree
at most one. This verifier enumerates all possible faces directly.
The infinite-family theorem is proved combinatorially in RESULT.md.
"""
from itertools import combinations


def arcs_for(n, shape):
    if n < 2 or shape not in ('disjoint', 'shared_source', 'shared_target'):
        raise ValueError('invalid parameters')
    forward = [(a, b) for a in (0, 1) for b in range(2, n + 2)]
    reverse = {
        'disjoint': [(2, 0), (3, 1)],
        'shared_source': [(2, 0), (2, 1)],
        'shared_target': [(2, 0), (3, 0)],
    }[shape]
    return forward + reverse


def is_multipath(selected, vertex_count):
    outdeg, indeg = [0] * vertex_count, [0] * vertex_count
    succ = {}
    for u, v in selected:
        outdeg[u] += 1
        indeg[v] += 1
        if outdeg[u] > 1 or indeg[v] > 1:
            return False
        succ[u] = v
    # A functional digraph has a directed cycle iff following some successor
    # repeats a vertex before reaching a sink.
    for start in succ:
        seen = set()
        current = start
        while current in succ:
            if current in seen:
                return False
            seen.add(current)
            current = succ[current]
    return True


def faces(n, shape):
    arcs = arcs_for(n, shape)
    # Only two outgoing forward arcs (one from each of the two a-vertices)
    # and at most two reverse arcs may occur in any multipath.
    found = {0}
    for k in range(1, 5):
        for index_set in combinations(range(len(arcs)), k):
            if is_multipath((arcs[i] for i in index_set), n + 2):
                found.add(sum(1 << i for i in index_set))
    return found


def rank_f2(vectors):
    pivots = {}
    for v in vectors:
        while v:
            lead = v.bit_length() - 1
            if lead in pivots:
                v ^= pivots[lead]
            else:
                pivots[lead] = v
                break
    return len(pivots)


def reduced_betti_f2(fset):
    by_dim = {}
    for face in fset:
        if face:
            by_dim.setdefault(face.bit_count()-1, []).append(face)
    rank = {}
    for k in sorted(by_dim):
        if k == 0:
            continue
        low = {face: j for j, face in enumerate(by_dim[k-1])}
        columns = []
        for face in by_dim[k]:
            boundary = 0
            for i in range(face.bit_length()):
                if (face >> i) & 1:
                    boundary ^= 1 << low[face ^ (1 << i)]
            columns.append(boundary)
        rank[k] = rank_f2(columns)
    betti = {}
    for k, group in by_dim.items():
        val = len(group)-rank.get(k, 0)-rank.get(k+1, 0)
        if k == 0:
            val -= 1
        if val:
            betti[k] = val
    return betti


def graph_stats(j_faces, vertex_limit):
    vertices = [i for i in range(vertex_limit) if (1 << i) in j_faces]
    edges = [face for face in j_faces if face.bit_count() == 2]
    assert all(face.bit_count() <= 2 for face in j_faces)
    adj = {v: set() for v in vertices}
    for mask in edges:
        pair = [i for i in vertices if mask & (1 << i)]
        assert len(pair) == 2
        a, b = pair
        adj[a].add(b)
        adj[b].add(a)
    unseen = set(vertices)
    components = 0
    while unseen:
        components += 1
        pending = [unseen.pop()]
        while pending:
            for v in adj[pending.pop()] & unseen:
                unseen.remove(v)
                pending.append(v)
    return len(vertices), len(edges), components


def main():
    count = 0
    for n in range(2, 11):
        for shape in ('disjoint', 'shared_source', 'shared_target'):
            fset = faces(n, shape)
            computed = reduced_betti_f2(fset)
            expected = ({1: 1, 2: 1} if shape == 'disjoint' else
                        {1: 1} if n <= 3 else {2: n*n-5*n+5})
            assert computed == expected, (n, shape, computed, expected)
            # Check simplex closure, including every codimension-one face.
            for mask in fset:
                for i in range(mask.bit_length()):
                    if mask & (1 << i):
                        assert mask ^ (1 << i) in fset
            if shape == 'disjoint':
                assert len(fset) == 4*n*n+4
                # Test each facewise domination pairing required by the proof.
                for j in range(2, n):
                    p, q = j, n+j
                    r1, r2 = 2*n, 2*n+1
                    assert all((mask | (1 << r1)) in fset for mask in fset
                               if mask & (1 << p))
                    assert all((mask | (1 << r2)) in fset for mask in fset
                               if mask & (1 << q))
            else:
                assert len(fset) == 3*n*n+n+3
                r1, r2 = 2*n, 2*n+1
                forward_mask = (1 << (2*n))-1
                base = {f for f in fset if not (f & ((1 << r1)|(1 << r2)))}
                l1 = {f & forward_mask for f in fset if f & (1 << r1)}
                l2 = {f & forward_mask for f in fset if f & (1 << r2)}
                assert not any((f & (1 << r1)) and (f & (1 << r2)) for f in fset)
                if shape == 'shared_source':
                    excluded = (0, n)  # p_1 and q_1
                else:
                    excluded = (0, 1)  # p_1 and p_2
                assert l1 == {f for f in base if not f & (1 << excluded[0])}
                assert l2 == {f for f in base if not f & (1 << excluded[1])}
                assert base == l1 | l2
                J = l1 & l2
                v, e, c = graph_stats(J, 2*n)
                assert v == 2*n-2
                assert e == (n-1)*(n-2)
                assert c == (2 if n<=3 else 1)
                if n >= 4:
                    assert e-v+1 == n*n-5*n+5
            count += 1
        print(f'n={n:2d}: three incidence patterns, exact faces and F2 Betti groups PASS')
    # Check exact four tetrahedral boundary faces in disjoint base n=2.
    fset = faces(2, 'disjoint')
    triangles = {tuple(i for i in range(6) if mask & (1 << i))
                 for mask in fset if mask.bit_count() == 3}
    tetra = {1, 2, 4, 5}  # p2, q1, r1, r2
    assert triangles == {tuple(sorted(tetra - {i})) for i in tetra}
    external = {tuple(i for i in range(6) if mask & (1 << i))
                for mask in fset if mask.bit_count() == 2 and
                not set(i for i in range(6) if mask & (1 << i)).issubset(tetra)}
    assert external == {(0,3), (0,5), (3,4)}
    print(f'base n=2: tetrahedral S2 and exterior attached path PASS')
    print(f'PASS: {count} exhaustive finite model checks; infinite statements rely on written proof')


if __name__ == '__main__':
    main()
