#!/usr/bin/env python3
"""Reproducible finite checks for ordered two-point configuration homology on stars.

Two independent cellular trace models are compared: the subdivided Abrams
cubical model and the crown-graph spine. All calculations use integer counts.
"""
from itertools import permutations


def verify(m):
    # Vertices: center 0; midpoint and tip on arm i are (2*i+1,2*i+2).
    vertices = tuple(range(2*m+1))
    edges = tuple((0, 2*i+1) for i in range(m)) + tuple(
        (2*i+1,2*i+2) for i in range(m))
    # All edges are oriented away from the center, so arm permutations preserve orientation.
    edges_set = set(edges)
    c0 = [(a,b) for a in vertices for b in vertices if a != b]
    c1 = [(e,v) for e in edges for v in vertices if v not in e]
    c2 = [(e,f) for e in edges for f in edges if set(e).isdisjoint(f)]
    # c1 includes both the edge-in-first and edge-in-second versions.
    # c2 is ordered because the particle labels distinguish tensor factors.
    N0,N1,N2 = len(c0),2*len(c1),len(c2)
    rank = N1-N0-N2+1
    assert rank == m*m-3*m+1
    # Integral non-splitting certificate: compute the parity image of an
    # integral fundamental-cycle basis of the crown graph, modulo two.
    # Every fundamental graph cycle is integral. Its parity image records
    # whether the two oriented edges in a leaf pair occur with opposite parity.
    edge_pairs=[(i,j) for i in range(m) for j in range(m) if i!=j]
    adjacency=[[] for _ in range(2*m)]
    for index,(i,j) in enumerate(edge_pairs):
        adjacency[i].append((m+j,index))
        adjacency[m+j].append((i,index))
    parent={0:(-1,-1)}
    todo=[0]
    for v in todo:
        for w,edge in adjacency[v]:
            if w not in parent:
                parent[w]=(v,edge)
                todo.append(w)
    assert len(parent)==2*m  # connected for m>=3
    treeedges={edge for (_,edge) in parent.values() if edge>=0}
    pair_index={(i,j):k for k,(i,j) in enumerate((
        (i,j) for i in range(m) for j in range(i+1,m)))}
    parity_vectors=[]
    for initial_edge,(i,j) in enumerate(edge_pairs):
        if initial_edge in treeedges:continue
        # Add the chord to the unique path between its endpoints in the tree.
        anc={};v=i
        while v>=0:
            pv,e=parent[v];anc[v]=e;v=pv
        v=m+j; route=[]
        while v not in anc:
            pv,e=parent[v];route.append(e);v=pv
        lca=v;v=i
        while v!=lca:
            pv,e=parent[v];route.append(e);v=pv
        route.append(initial_edge)
        bits=0
        for e in route:
            a,b=edge_pairs[e]
            bits ^= 1 << pair_index[(min(a,b),max(a,b))]
        parity_vectors.append(bits)
    assert len(parity_vectors)==rank
    pivots={}
    for vec in parity_vectors:
        while vec:
            bit=vec.bit_length()-1
            if bit in pivots:vec ^=pivots[bit]
            else:pivots[bit]=vec;break
    parity_rank=len(pivots)
    assert parity_rank==m*(m-3)//2
    checked=0
    for perm in permutations(range(m)):
        def f(v):
            return v if v == 0 else 2*perm[(v-1)//2]+1+(v-1)%2
        def ep(e):
            return (f(e[0]),f(e[1]))
        assert all(ep(e) in edges_set for e in edges)
        fixed=sum(perm[i]==i for i in range(m))
        two_cycles=sum(i<perm[i] and perm[perm[i]]==i for i in range(m))
        for swap in (False,True):
            if not swap:
                # fixed ordered distinct vertex pairs
                t0=sum(f(a)==a and f(b)==b for a,b in c0)
                # 1-cells: edge-vertex and vertex-edge
                t1=2*sum(ep(e)==e and f(v)==v for e,v in c1)
                # oriented squares have no sign from an arm permutation
                t2=sum(ep(e)==e and ep(g)==g for e,g in c2)
                predicted=fixed*fixed-3*fixed+1
            else:
                # Particle exchange interchanges both factors, giving a negative
                # orientation on 2-cubes but no negative sign on 1-cubes.
                t0=sum(f(b)==a and f(a)==b for a,b in c0)
                t1=0  # a tensor edge-vertex cell switches its factor
                t2=-sum(ep(g)==e and ep(e)==g for e,g in c2)
                predicted=1-2*two_cycles
            trace1=1-(t0-t1+t2)
            assert trace1==predicted, (m,perm,swap,trace1,predicted,t0,t1,t2)
            checked+=1
    return f'm={m} cells=({N0},{N1},{N2}) b1={rank} parity_cokernel_log2={parity_rank} checked={checked}'

if __name__=='__main__':
    for n in range(3,7): print(verify(n))
    print('ORDERED_STAR_CROWN_AND_JOINT_CHARACTER_PASS')
