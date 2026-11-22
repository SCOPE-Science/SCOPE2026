#!/usr/bin/env python3
"""Finite, exact checks for the forest-complex cone/double-cover identity.

With vertices i+ and i-, let B(G) consist of the matching i+i- and
both cross-edges i+j-, j+i- for every edge ij of a simple graph G.
The involution swaps the signs. Its edge orbits correspond to the edges
of the graph cone G* (apex n). The mathematical proof is independent of
these finite tests.
"""
from itertools import combinations, permutations
from collections import Counter


def is_forest(n, edges):
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for a,b in edges:
        a,b=root(a),root(b)
        if a==b:return False
        parent[a]=b
    return True


def check(n, base, symmetries=True):
    base=tuple(sorted(tuple(sorted(e)) for e in base))
    all_possible=set(combinations(range(n),2))
    assert len(base)==len(set(base)) and set(base)<=all_possible
    # Orbit labels, first apex edges, then original edges.
    cover_orbits=[(tuple(sorted((i,i+n))),) for i in range(n)]
    for a,b in base:
        cover_orbits.append((tuple(sorted((a,b+n))),tuple(sorted((b,a+n)))))
    cone_edges=[(i,n) for i in range(n)]+list(base)
    assert len(cover_orbits)==len(cone_edges)
    assert len(set(e for o in cover_orbits for e in o))==sum(map(len,cover_orbits))
    # Check that these really are the complete orbits under the flip.
    def flip_edge(e):return tuple(sorted(((e[0]+n)%(2*n), (e[1]+n)%(2*n))))
    for o in cover_orbits:
        assert {flip_edge(e) for e in o}==set(o)
    # Every invariant edge subset is a union of precisely these orbits.
    f=Counter(); tested=0
    for mask in range(1<<len(cover_orbits)):
        edge_union=[e for i,o in enumerate(cover_orbits) if mask>>i & 1 for e in o]
        cone_subset=[e for i,e in enumerate(cone_edges) if mask>>i & 1]
        acyclic_cover=is_forest(2*n,edge_union)
        acyclic_cone=is_forest(n+1,cone_subset)
        assert acyclic_cover==acyclic_cone, (n,base,mask)
        if acyclic_cone:f[len(cone_subset)]+=1
        tested+=1
    if symmetries:
        for p in permutations(range(n)):
            if set(tuple(sorted((p[a],p[b]))) for a,b in base)!=set(base):continue
            label_map=[]
            for e in cone_edges:
                a,b=e
                translated=tuple(sorted((p[a] if a<n else n,p[b] if b<n else n)))
                j=next(j for j,x in enumerate(cone_edges) if tuple(sorted(x))==translated)
                label_map.append(j)
            assert len(set(label_map))==len(cone_edges)
            for i,o in enumerate(cover_orbits):
                def translate(v):return p[v] if v<n else p[v-n]+n
                image={tuple(sorted((translate(a),translate(b)))) for a,b in o}
                assert image==set(cover_orbits[label_map[i]])
    return tested,dict(f)


def all_graphs(n):
    edges=list(combinations(range(n),2))
    for mask in range(1<<len(edges)):
        yield [e for i,e in enumerate(edges) if mask>>i & 1]


def main():
    graph_count=0;total_masks=0
    for n in range(1,5):
        for graph in all_graphs(n):
            cases,_=check(n,graph)
            graph_count+=1
            total_masks+=cases
    assert graph_count==75
    n=5
    examples={
        'empty':[],
        'path':[(i,i+1) for i in range(n-1)],
        'cycle':[(i,(i+1)%n) for i in range(n)],
        'star':[(0,i) for i in range(1,n)],
        'two_components':[(0,1),(1,2),(0,2),(3,4)],
        'complete_bipartite':[(a,b) for a in (0,1) for b in (2,3,4)],
        'complete':list(combinations(range(n),2)),
    }
    for label,edges in examples.items():
        cases, f=check(n,edges)
        graph_count+=1;total_masks+=cases
        if label=='complete':
            assert [f.get(i,0) for i in range(n+1)]==[1,15,105,435,1080,1296]
    for n, expected in [(2,[1,3,3]),(3,[1,6,15,16]),(4,[1,10,45,110,125])]:
        cases,f=check(n,list(combinations(range(n),2)))
        assert [f.get(i,0) for i in range(n+1)]==expected
    print('CONE_DOUBLE_FOREST_EQUIVARIANT_FACE_TESTS_PASS')
    print(f'graphs_checked={graph_count}; invariant_edge_subsets_checked={total_masks}')
    print('all_simple_graphs_through_4_vertices_and_7_five_vertex_examples_checked')
    print('all_automorphisms_of_each_tested_graph_checked_on_orbit_labels')
    print('K_3,K_4,K_5,K_6_cone_f_vectors_checked')

if __name__=='__main__':
    main()
