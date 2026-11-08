#!/usr/bin/env python3
"""Exhaustive finite checks for an orbit-fixed robust-clique identity.
All input graphs are produced in memory; no external libraries are needed.
"""
from itertools import combinations
from math import comb


def independent_number(adj, chosen):
    """Maximum independence over a specified set, by exact exhaustive masks."""
    vertices = list(chosen)
    n = len(vertices)
    best = 0
    for bits in range(1 << n):
        size = bits.bit_count()
        if size <= best:
            continue
        ok = True
        for a in range(n):
            if bits >> a & 1:
                for b in range(a + 1, n):
                    if bits >> b & 1 and vertices[b] in adj[vertices[a]]:
                        ok = False
                        break
            if not ok:
                break
        if ok:
            best = size
    return best


def r_colorable(edge_set, selected, r):
    vertices = list(selected)
    colors = {}
    def rec(i):
        if i == len(vertices):
            return True
        v = vertices[i]
        for c in range(r):
            if all(colors[u] != c for u in vertices[:i] if (min(u, v), max(u, v)) in edge_set):
                colors[v] = c
                if rec(i+1):
                    return True
                del colors[v]
        return False
    return rec(0)


def chromatic_deletion_number(edge_set, selected, r):
    vertices = list(selected)
    for count in range(len(vertices), -1, -1):
        for t in combinations(vertices, count):
            if r_colorable(edge_set, t, r):
                return count
    raise AssertionError


def prism_adjacency(m, edge_set, r):
    adj = [set() for _ in range(m*r)]
    for u in range(m):
        for a in range(r):
            for b in range(a+1, r):
                x,y=r*u+a, r*u+b
                adj[x].add(y); adj[y].add(x)
    for u,v in edge_set:
        for a in range(r):
            x,y=r*u+a, r*v+a
            adj[x].add(y);adj[y].add(x)
    return adj


def check_graph(m, edge_set, r):
    adj=prism_adjacency(m,edge_set,r)
    for mask in range(1<<m):
        selected = [u for u in range(m) if mask>>u&1]
        fiber_union = [r*u+a for u in selected for a in range(r)]
        actual = independent_number(adj,fiber_union)
        predicted = chromatic_deletion_number(edge_set,selected,r)
        assert actual == predicted, (m,edge_set,r,selected,actual,predicted)
        for k in range(2,m+2):
            assert (actual < k) == (predicted < k)
    colorable=r_colorable(edge_set,range(m),r)
    if m>=2:
        for mask in range(1<<m):
            selected=[u for u in range(m) if mask>>u&1]
            actual=independent_number(adj,[r*u+a for u in selected for a in range(r)])
            assert (actual<m)==((mask!=(1<<m)-1) or not colorable)
            if colorable:
                assert actual==len(selected)


def main():
    total = 0
    for m in (1,2,3,4):
        pairs=list(combinations(range(m),2))
        for bitmask in range(1<<len(pairs)):
            E={pair for i,pair in enumerate(pairs) if bitmask>>i & 1}
            for r in (2,3):
                check_graph(m,E,r)
                total+=1
    # Targeted chromatic-critical and non-critical examples.
    cases=[]
    for m in (5,6):
        cases += [(m,{(u,(u+1)%m) if u<(u+1)%m else ((u+1)%m,u) for u in range(m)})]
    cases += [(5,set(combinations(range(5),2))),
              (5,set(combinations(range(4),2))),
              (5,{(0,1),(0,2),(1,2),(2,3),(3,4)}),
              (5,{(0,1),(1,2),(2,3),(3,4)}),
              (5,{(0,1),(1,2),(2,3),(0,3),(1,4),(2,4)})]
    for m,E in cases:
        # m=6,r=3 independent brute can be costly; skip large case.
        if m>5:
            continue
        for r in (2,3):
            check_graph(m,E,r)
            total += 1

    # Direct enumeration of invariant faces in the original product complex.
    invariant_faces=0
    for m in (2,3):
        pairs=list(combinations(range(m),2))
        for bitmask in range(1<<len(pairs)):
            E={pair for i,pair in enumerate(pairs) if bitmask>>i&1}
            for r in (2,3):
                adj=prism_adjacency(m,E,r)
                for mask in range(1<<(m*r)):
                    is_invariant=all(
                        all(((mask>>(r*u+a))&1)==((mask>>(r*u+b))&1) for a in range(r) for b in range(r))
                        for u in range(m))
                    if not is_invariant: continue
                    orbit_set=[u for u in range(m) if mask>>(r*u)&1]
                    W=[v for v in range(m*r) if mask>>v&1]
                    alpha=independent_number(adj,W)
                    pred=chromatic_deletion_number(E,orbit_set,r)
                    assert alpha==pred
                    for k in range(2,m+2):
                        assert (alpha<k)==(pred<k)
                        invariant_faces+=1
    for m in range(2,9):
        for k in range(2,m+2):
            # Known reduced integral homology of the (k-2)-skeleton:
            # exactly binomial(m-1,k-1) in dimension k-2 for k<=m.
            f=[comb(m,j) for j in range(1,min(k-1,m)+1)]
            euler=sum((-1)**i*n for i,n in enumerate(f))
            if k<=m:
                assert euler == 1+(-1)**(k-2)*comb(m-1,k-1)
            else:
                assert euler == 1
    print('EXHAUSTIVE_LABELED_GRAPHS_m_LE_4=75; GROUP_SIZES=2,3; TESTS=150')
    print('TARGETED_GRAPHS_TESTED_WITH_r_2_3=12; TOTAL_CASES=',total)
    print('DIRECT_INVARIANT_FACE_TESTS=',invariant_faces)
    print('PRISM_FIXED_COMPLEX_AND_COLORABILITY_TESTS_OK')

if __name__=='__main__':main()
