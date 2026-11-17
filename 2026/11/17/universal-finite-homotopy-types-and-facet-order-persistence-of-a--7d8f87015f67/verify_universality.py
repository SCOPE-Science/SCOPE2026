#!/usr/bin/env python3
"""Reconstruct a directed in-tree from an ordered facet list, replay parallel firing,
and test the promised stagewise simplicial retractions. Uses exact integers."""
from collections import Counter, defaultdict
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def construct(facets):
    facets = [frozenset(f) for f in facets]
    assert facets and all(facets)
    assert all(not (i != j and f <= g) for i,f in enumerate(facets) for j,g in enumerate(facets))
    vertices = sorted(set().union(*facets))
    sink = ('sink',)
    nxt = {('v',v):sink for v in vertices}
    initial = {('v',v):int(v in facets[0]) for v in vertices}
    source_nodes = {}
    for j in range(1,len(facets)):
        for v in sorted(facets[j]):
            path=[('p',j,v,t) for t in range(j)]
            for h,p in enumerate(path):
                nxt[p]=path[h+1] if h+1<j else ('v',v)
                initial[p] = int(h==0)
                source_nodes[p]=(j,v,h)
    assert len(nxt)==len(initial)
    # Every non-sink has outdegree one, all arrows flow to sink.
    for v in nxt:
        walk={v}; x=nxt[v]
        while x!=sink:
            assert x not in walk
            walk.add(x); x=nxt[x]
    assert len(nxt)==len(vertices)+sum(j*len(facets[j]) for j in range(1,len(facets)))
    return facets, sink, nxt, initial, source_nodes


def replay(facets, sink, nxt, initial):
    chips=dict(initial)
    history=[]
    while True:
        firing=frozenset(x for x,z in chips.items() if z>=1)
        if not firing: break
        history.append(firing)
        assert len(history) <= len(nxt)+1
        new=chips.copy()
        for x in firing:
            new[x]-=1
            target=nxt[x]
            if target!=sink: new[target]+=1
        chips=new
    return history


def check_case(name, facets, verbose=True):
    facets, sink, nxt, initial, aux=construct(facets)
    history=replay(facets,sink,nxt,initial)
    assert len(history)==len(facets), (name,len(history),len(facets))
    for t, sigma in enumerate(history):
        expected={('v',v) for v in facets[t]}
        expected.update(('p',j,v,t) for j in range(t+1,len(facets)) for v in facets[j])
        assert sigma==frozenset(expected), (name,t)
    appearances=Counter(x for sigma in history for x in sigma)
    assert all(appearances[p]==1 for p in aux)
    for t in range(len(history)):
        anchor=min(facets[t])
        sigma=history[t]
        # The simplicial retraction fixes old target vertices and sends the
        # auxiliary vertices of this unique facet to its chosen target anchor.
        retracted={x if x[0]=='v' else ('v',anchor) for x in sigma}
        assert retracted == {('v',v) for v in facets[t]}
        # The target-only faces at time t are exactly those in the prefix K_t.
        actual_target_facets=[frozenset(x[1] for x in s if x[0]=='v') for s in history[:t+1]]
        assert actual_target_facets==facets[:t+1]
        # All auxiliary vertices have only one containing maximal firing simplex
        # and are dominated by the anchor, giving a strong simplicial collapse.
        for p in sigma:
            if p[0]=='p':assert sum(p in s for s in history[:t+1])==1
    if verbose:
        print(f'PASS {name}: {len(nxt)} firing vertices, {len(history)} stages, '
              f'{sum(1 for _ in aux)} auxiliary vertices, binary initial chips')


def check_projective_plane():
    faces=[tuple(map(int,s)) for s in
           ('012','013','024','035','045','125','134','145','234','235')]
    edges=Counter(tuple(sorted(e)) for face in faces for e in combinations(face,2))
    assert len(edges)==15 and set(edges.values())=={2}
    assert 6-15+10==1
    # Triangulated closed surface: vertex links are cycles.
    for v in range(6):
        links=[tuple(x for x in face if x!=v) for face in faces if v in face]
        assert len(links)==5
        degrees=Counter(x for edge in links for x in edge)
        assert len(degrees)==5 and set(degrees.values())=={2}
    # Compute H_1 over Z via a cycle basis (non-tree edges of K_6).
    cycle_edges={e:i for i,e in enumerate(combinations(range(1,6),2))}
    boundary=Matrix.zeros(10,10)
    for col,face in enumerate(faces):
        for k in range(3):
            e=tuple(face[h] for h in range(3) if h!=k)
            if 0 in e: continue
            boundary[cycle_edges[tuple(sorted(e))],col] += (-1)**k * (1 if e[0]<e[1] else -1)
    smith=smith_normal_form(boundary,domain=ZZ)
    invariant_factors=[abs(int(smith[i,i])) for i in range(10)]
    assert invariant_factors==[1]*9+[2], invariant_factors
    print('PASS RP2 integral homology: H_1 = Z/2, H_2=0; 10x10 Smith [1]^9+[2]')
    return faces

if __name__=='__main__':
    check_case('single 2-simplex',[(0,1,2)])
    check_case('two disconnected vertices',[(0,),(1,)])
    check_case('triangle boundary',[(0,1),(1,2),(0,2)])
    check_case('mixed-dimensional',[(0,1,2),(2,3),(4,)])
    faces=check_projective_plane()
    check_case('six-vertex RP2',faces)
    all_faces=[frozenset(e) for k in range(1,5) for e in combinations(range(4),k)]
    antichains=0
    for mask in range(1, 1 << len(all_faces)):
        fs=[f for i,f in enumerate(all_faces) if mask & (1<<i)]
        if any(i!=j and f<=g for i,f in enumerate(fs) for j,g in enumerate(fs)):
            continue
        check_case('four-vertex antichain',fs,verbose=False)
        antichains+=1
    print(f'PASS all {antichains} nonempty antichains on four labels')
    print('UNIVERSAL_AVALANCHE_TREE_STRONG_COLLAPSE_PASS')
