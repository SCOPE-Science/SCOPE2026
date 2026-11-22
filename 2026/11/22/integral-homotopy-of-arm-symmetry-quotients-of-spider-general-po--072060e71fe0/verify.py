#!/usr/bin/env python3
"""Independent finite checks for symmetric-arm quotients of general-position complexes.

The quotient is represented by orbits of flags of nonempty faces in the
barycentric subdivision: face ranks distinguish every flag vertex, hence
stabilizers act pointwise on flags. All chain calculations are exact mod p.
"""
from itertools import combinations, permutations, product
from math import comb, factorial
from collections import deque


def spider_graph(r, L):
    vertices = [(a, d) for a in range(r) for d in range(1, L+1)]
    vertices.append(('c', 0))
    adjacency = {v:set() for v in vertices}
    for a in range(r):
        for d in range(1,L+1):
            u=(a,d); v=('c',0) if d==1 else (a,d-1)
            adjacency[u].add(v); adjacency[v].add(u)
    return vertices, adjacency


def graph_general_position_faces(r,L):
    vertices, adj=spider_graph(r,L)
    n=len(vertices)
    # BFS distance to independently confirm all shortest-path exclusions.
    D={}
    for u in vertices:
        dist={u:0}; queue=deque([u])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if y not in dist: dist[y]=dist[x]+1; queue.append(y)
        assert len(dist)==n
        D[u]=dist
    faces=[()]
    for s in range(1,n+1):
        for face in combinations(vertices,s):
            allowed=all(D[u][w]+D[w][v]!=D[u][v]
                for u,v,w in combinations(face,3)
                for (u,v,w) in ((u,v,w),(u,w,v),(v,w,u)))
            if allowed:faces.append(face)
    return vertices,faces


def predicted_faces(r,L):
    B=[(a,d) for a in range(r) for d in range(1,L+1)]
    faces=[()]
    for s in range(1,r+1):
        for f in combinations(B,s):
            if len({a for a,d in f})==len(f): faces.append(f)
    c=('c',0)
    faces.append((c,))
    for u in B:faces.append((c,u))
    for a in range(r):
        for d,e in combinations(range(1,L+1),2):
            faces.append(((a,d),(a,e)))
    return {frozenset(f) for f in faces}


def equivariant_chain_orbits(r,L):
    vertices,full_faces=graph_general_position_faces(r,L)
    actual={frozenset(f) for f in full_faces}
    predicted=predicted_faces(r,L)
    assert actual==predicted, (r,L,len(actual),len(predicted),actual^predicted)
    # canonical label of vertex is a unique integer
    nums={v:i for i,v in enumerate(vertices)}
    F={tuple(sorted(nums[x] for x in f)) for f in actual if f}
    from itertools import chain
    perms=list(permutations(range(r)))
    actions=[]
    for p in perms:
        actions.append(tuple(nums[('c',0)] if v==('c',0) else nums[(p[v[0]],v[1])] for v in vertices))
    def mask(f):return sum(1<<j for j in f)
    F_masks=set(map(mask,F))
    # face submasks are genuine, since an abstract simplicial complex
    by_max={}
    for fm in F_masks:
        subs=[]
        s=(fm-1)&fm
        while s:
            subs.append(s); s=(s-1)&fm
        by_max[fm]=subs
    def act(m,p):
        x=0
        while m:
            l=m&-m; x|=(1<<p[l.bit_length()-1]);m^=l
        return x
    def canon(flag):
        return min(tuple(act(s,p) for s in flag) for p in actions)
    orbit_sets=[set() for _ in range(r)]
    for fm in F_masks:
        def explore(flag):
            orbit_sets[len(flag)-1].add(canon(flag))
            if len(flag)==r:return
            for s in by_max[flag[0]]:
                # insert proper subset first; maintains ascending nested order
                explore((s,)+flag)
        explore((fm,))
    cells=[sorted(s) for s in orbit_sets]
    lookup=[{f:j for j,f in enumerate(c)} for c in cells]
    boundaries=[]
    for d in range(1,r):
        cols=[]
        for flag in cells[d]:
            col={}
            for i in range(len(flag)):
                sub=canon(flag[:i]+flag[i+1:])
                idx=lookup[d-1][sub]
                col[idx]=col.get(idx,0)+(-1)**i
            cols.append({k:v for k,v in col.items() if v})
        boundaries.append(cols)
    # exact boundary^2=0 over integers
    for d in range(2,r):
        for col in boundaries[d-1]:
            res={}
            for idx,v in col.items():
                for j,w in boundaries[d-2][idx].items():
                    res[j]=res.get(j,0)+v*w
            assert all(v==0 for v in res.values())
    return cells,boundaries


def rank_mod(cols,p):
    basis={}
    for original in cols:
        col={i:v%p for i,v in original.items() if v%p}
        while col:
            pivot=min(col)
            if pivot not in basis:
                v=col[pivot];inv=pow(v,-1,p)
                basis[pivot]={k:(val*inv)%p for k,val in col.items() if (val*inv)%p}
                break
            b=basis[pivot];mult=col[pivot]
            for j,v in b.items():
                updated=(col.get(j,0)-mult*v)%p
                if updated:col[j]=updated
                else:col.pop(j,None)
    return len(basis)


def run_case(r,L):
    cells,boundaries=equivariant_chain_orbits(r,L)
    counts=[len(c) for c in cells]
    expected={0:1,1:comb(L,2)+L-1}
    if r>=3:expected[r-1]=expected.get(r-1,0)+comb(L-1,r)
    outputs={}
    for p in (2,3,5,7):
        ranks=[0]+[rank_mod(cols,p) for cols in boundaries]+[0]
        betti=[counts[d]-ranks[d]-ranks[d+1] for d in range(r)]
        expected_betti=[1+expected.get(0,0)-1]+[expected.get(d,0) for d in range(1,r)]
        assert betti==expected_betti,(r,L,p,betti,expected_betti)
        outputs[p]=betti
    return counts,outputs


def run():
    total=0
    for r in (3,4):
        for L in (1,2,3,4,5):
            cells,bettis=run_case(r,L)
            print(f'r={r} L={L}: quotient barycentric cell counts {cells}; predicted Betti vector matches primes 2,3,5,7: {bettis[2]}')
            total+=1
    print(f'PASS: {total} parameter profiles, {4*total} modular exact-rank checks, and all integral boundary-square cancellations')

if __name__=='__main__':run()
