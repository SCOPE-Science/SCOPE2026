#!/usr/bin/env python3
"""Independent finite checks for reflection fixed loci of 3-cut complexes.

Runs with Python standard library only; does not load prior generated data.
"""
from itertools import combinations
from collections import defaultdict


def disconnected_three(n, vertices):
    # Edges of K_n minus C_n: cyclic distance at least two.
    seen = {vertices[0]}
    changed = True
    while changed:
        changed = False
        for u in tuple(seen):
            for v in vertices:
                if v not in seen and (u-v) % n not in (0, 1, n-1):
                    seen.add(v)
                    changed = True
    return len(seen) != 3


def orbits(n, a):
    unvisited = set(range(n))
    out = []
    while unvisited:
        i = min(unvisited)
        group = frozenset((i, (a-i) % n))
        out.append(group)
        unvisited.difference_update(group)
    return out


def ordered_orbits(n, a):
    groups = orbits(n, a)
    owner = {i:j for j, g in enumerate(groups) for i in g}
    adj = [set() for _ in groups]
    for i in range(n):
        j, k = owner[i], owner[(i+1)%n]
        if j != k:
            adj[j].add(k)
            adj[k].add(j)
    endpoints = [j for j,x in enumerate(adj) if len(x)==1]
    assert len(endpoints)==2 and all(len(x) <=2 for x in adj)
    order = [min(endpoints)]
    while len(order) < len(groups):
        nxt = adj[order[-1]] - (set(order[-2:-1]))
        assert len(nxt)==1
        order.append(nxt.pop())
    return groups, owner, {old:i for i,old in enumerate(order)}


def actual_min_hyperedges(n, a):
    groups, owner, relabel = ordered_orbits(n, a)
    projected = set()
    for vertices in combinations(range(n), 3):
        if disconnected_three(n, vertices):
            projected.add(frozenset(relabel[owner[v]] for v in vertices))
    minimal = {e for e in projected if not any(g < e for g in projected)}
    return len(groups), minimal


def ideal_hyperedges(m):
    assert m >= 3
    return {frozenset((0,1)), frozenset((m-2,m-1))} | {
        frozenset(range(j,j+3)) for j in range(1,m-3)
    }


def faces(m, edges):
    facets = [set(range(m))-set(e) for e in edges]
    return {s for s in range(1<<m) if any(not (set(i for i in range(m) if s >> i & 1)-f) for f in facets)}


def reduced_betti(m, edges):
    fs = faces(m, edges)
    by_dim = defaultdict(list)
    for s in fs:
        by_dim[s.bit_count()-1].append(s)
    ranks = {}
    for d in range(0, max(by_dim)+1):
        lows = {s:i for i,s in enumerate(by_dim[d-1])}
        pivots = {}
        for s in by_dim[d]:
            boundary = 0
            for i in range(m):
                if s>>i&1: boundary ^= 1 << lows[s ^ (1<<i)]
            while boundary:
                k = boundary.bit_length()-1
                if k in pivots: boundary ^= pivots[k]
                else:
                    pivots[k] = boundary
                    break
        ranks[d] = len(pivots)
    betti = {d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
             for d in range(0,max(by_dim)+1)}
    return {d:v for d,v in betti.items() if v}


def check_recursion(m):
    h = ideal_hyperedges(m)
    assert m>=5
    V=set(range(m)); L=V-{0,1}
    U = [V-e for e in h if e != frozenset((0,1))]
    assert all(0 in F for F in U)
    edge_from_intersection = {frozenset(L-F) for F in U}
    edge_from_intersection = {e for e in edge_from_intersection if not any(g < e for g in edge_from_intersection)}
    relabeled = {frozenset(i-2 for i in e) for e in edge_from_intersection}
    assert relabeled == ideal_hyperedges(m-2), (m, relabeled)


def main():
    cases = 0
    max_m = 0
    total_faces = 0
    for n in range(5, 29):
        for a in range(n):
            m, e = actual_min_hyperedges(n,a)
            assert e == ideal_hyperedges(m), (n,a,e,ideal_hyperedges(m))
            cases += 1
            max_m = max(max_m,m)
    for m in range(5,max_m+1):
        check_recursion(m)
    for m in (3,4):
        assert reduced_betti(m,ideal_hyperedges(m)) == {0:1}
    for m in range(3,max_m+1):
        b = reduced_betti(m,ideal_hyperedges(m))
        assert b == {(m-3)//2:1}, (m,b)
        total_faces += len(faces(m,ideal_hyperedges(m)))
    print('ORBIT_GRAPH_AND_GRAPH_CUT_CASES',cases)
    print('MAX_QUOTIENT_VERTICES',max_m)
    print('SUSPENSION_INTERSECTION_CHECKS',max_m-4)
    print('REDUCED_GF2_HOMOLOGY_CASES',max_m-2)
    print('TOTAL_MODEL_FACES_ENUMERATED',total_faces)
    print('ALL_REFLECTION_CHECKS_OK')

if __name__=='__main__':main()
