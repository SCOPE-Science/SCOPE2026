#!/usr/bin/env python3
"""Standalone finite checks for directed-acyclic-subgraph fixed-space theorem.

Enumerates all small labeled digraphs on <=3 vertices, cyclic symmetry tests
on a reproducible family of four- and five-vertex digraphs, verifies the
exact orbit-face correspondence and checks the predicted reduced Euler
characteristic. No unbounded inference is made from these tests.
"""
from itertools import permutations, product
import random

def digraph_edges(n, mask):
    A = [(i,j) for i in range(n) for j in range(n) if i != j]
    return frozenset(A[i] for i in range(len(A)) if (mask >> i) & 1)

def acyclic(n, edges):
    indeg=[0]*n; adj=[[] for _ in range(n)]
    for u,v in edges:
        indeg[v]+=1; adj[u].append(v)
    st=[u for u in range(n) if indeg[u]==0]
    done=0
    while st:
        u=st.pop();done+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0: st.append(v)
    return done==n

def closure_perm(g):
    n=len(g); ident=tuple(range(n)); group={ident}; cur=ident
    while True:
        cur=tuple(g[cur[i]] for i in range(n))
        if cur in group: return tuple(sorted(group))
        group.add(cur)

def orbits(universe, group, action):
    rem=set(universe); blocks=[]
    while rem:
        a=min(rem); b=frozenset(action(g,a) for g in group)
        assert b<=rem, 'group action not closed'
        rem-=b; blocks.append(b)
    return tuple(sorted(blocks,key=lambda s:min(s)))

def strongly_connected_components(n,edges):
    reach=[[i==j for j in range(n)] for i in range(n)]
    for u,v in edges: reach[u][v]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    rem=set(range(n)); blocks=[]
    while rem:
        i=min(rem)
        b=frozenset(j for j in rem if reach[i][j] and reach[j][i])
        rem-=b;blocks.append(b)
    return tuple(blocks)

def verify(n, E, g):
    assert all((g[u],g[v]) in E for u,v in E)
    H=closure_perm(g)
    V_orbits=orbits(range(n),H,lambda a,u:a[u]); vi={v:i for i,B in enumerate(V_orbits) for v in B}
    E_orbits=orbits(E,H,lambda a,e:(a[e[0]],a[e[1]]))
    good=[]
    for O in E_orbits:
        if acyclic(n,O): good.append(O)
    arc=[(vi[next(iter(O))[0]],vi[next(iter(O))[1]]) for O in good]
    assert all(a!=b for a,b in arc)
    Q=frozenset(arc)
    r=len(good)
    if r>16: return None
    face_count=0;chi_red=-1
    for mask in range(1,1<<r):
        U=frozenset(e for j,O in enumerate(good) if mask>>j & 1 for e in O)
        V=frozenset(arc[j] for j in range(r) if mask>>j & 1)
        a=acyclic(n,U); b=acyclic(len(V_orbits),V)
        assert a==b,(n,E,g,mask,U,V,a,b)
        if a:
            face_count+=1
            chi_red+=1 if mask.bit_count()%2 else -1
    comps=strongly_connected_components(n,E)
    ci={v:i for i,C in enumerate(comps) for v in C}
    S_orbits=orbits(range(len(comps)),H,lambda a,i:ci[a[next(iter(comps[i]))]])
    cross=any(ci[u]!=ci[v] for u,v in E)
    dimension=len(V_orbits)-len(S_orbits)-1
    expected=0 if cross else (-1 if dimension%2 else 1)
    assert chi_red==expected,(n,E,g,V_orbits,comps,S_orbits,chi_red,expected)
    # Verify condensation and SCC orbit count in the quotient.
    qc=strongly_connected_components(len(V_orbits),Q)
    assert len(qc)==len(S_orbits)
    return face_count

def main():
    total=0; faces=0
    for n in (2,3):
        pairs=n*(n-1)
        for m in range(1<<pairs):
            E=digraph_edges(n,m)
            for g in permutations(range(n)):
                if all((g[u],g[v]) in E for u,v in E) and all((g.index(u),g.index(v)) in E for u,v in E):
                    val=verify(n,E,g)
                    if val is not None: faces+=val;total+=1
    rng=random.Random(20261115)
    for n in (4,5):
        pool=list(permutations(range(n)))
        target = [frozenset(), frozenset((i,j) for i in range(n) for j in range(n) if i!=j)]
        for j in range(160):
            E=digraph_edges(n,rng.getrandbits(n*(n-1)))
            target.append(E)
        # Also generate guaranteed symmetric digraphs under varied permutations.
        for g in pool[::max(1,len(pool)//15)]:
            H=closure_perm(g)
            possible=[(i,j) for i in range(n) for j in range(n) if i!=j]
            Os=orbits(possible,H,lambda a,e:(a[e[0]],a[e[1]]))
            for j in range(12):
                chosen=[O for O in Os if rng.getrandbits(1)]
                target.append(frozenset(e for O in chosen for e in O))
        for E in target:
            autos=[g for g in pool if all((g[u],g[v]) in E for u,v in E) and all((g.index(u),g.index(v)) in E for u,v in E)]
            for g in autos[:12]:
                val=verify(n,E,g)
                if val is not None: faces+=val;total+=1
    print('VERIFY_OK', 'graphs_with_automorphisms=',total,'checked_fixed_faces=',faces)

if __name__=='__main__':main()
