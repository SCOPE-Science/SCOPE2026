#!/usr/bin/env python3
"""Independent finite checks for closed-neighborhood collapses of C4-free graphs."""
from itertools import combinations
from collections import Counter
import random
from itertools import permutations

def check_graph(n, edge_mask, verify_collapse=True):
    E = list(combinations(range(n), 2))
    edges = {edge for i,edge in enumerate(E) if edge_mask>>i & 1}
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    squarefree = all(len(adj[u]&adj[v]) <= 1 for u in range(n) for v in range(u+1,n))
    tri = [s for s in combinations(range(n),3) if all(tuple(sorted(e)) in edges for e in combinations(s,2))]
    clique={m for m in range(1,1<<n) if all(tuple(sorted(e)) in edges for e in combinations([v for v in range(n) if m>>v &1],2))}
    faces=set()
    for v in range(n):
        N = sum(1<<u for u in adj[v]|{v})
        s=N
        while s:
            faces.add(s);s=(s-1)&N
    assert clique<=faces
    if squarefree and verify_collapse:
        active=set(faces); pairs=[]
        nonclique=faces-clique
        witnesses={}
        for m in nonclique:
            w=[v for v in range(n) if all((m>>u &1)==0 or u==v or u in adj[v] for u in range(n))]
            assert len(w)==1, ('witness uniqueness',n,edge_mask,m,w)
            witnesses[m]=w[0]
        lower=sorted((m for m in nonclique if not (m>>witnesses[m]&1)), key=lambda m:(-m.bit_count(),m))
        for m in lower:
            c=witnesses[m]; up=m|(1<<c)
            assert up in active and m in active
            cofaces=[p for p in active if p!=m and m&p==m]
            assert cofaces==[up], (n,edge_mask,m,up,cofaces)
            active.remove(m);active.remove(up);pairs.append((m,up))
        assert active==clique, (n,edge_mask,'not clique')
        assert 2*len(pairs)==len(faces)-len(clique)
        # canonical automorphism-invariant pair set: exact witness is unique.
        # Homology rank from connected graph with disjoint filled triangles.
        parent=list(range(n))
        def find(a):
            while parent[a]!=a:
                a=parent[a]
            return a
        for u,v in edges:parent[find(u)]=find(v)
        comp=len({find(v) for v in range(n)})
        beta=len(edges)-n+comp-len(tri)
        assert beta>=0
        chi=sum((-1)**(m.bit_count()-1) for m in faces)
        assert chi==comp-beta,(n,edge_mask,chi,beta)
        return len(faces),len(clique),len(pairs),beta,len(tri)
    return None


def check_symmetry(n, e_set, label):
    edges={tuple(sorted(x)) for x in e_set}
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    faces=set()
    for v in range(n):
        N=sum(1<<u for u in adj[v]|{v})
        s=N
        while s:faces.add(s);s=(s-1)&N
    clique={m for m in faces if all(tuple(sorted(e)) in edges for e in combinations([v for v in range(n) if m>>v&1],2))}
    pairs=set()
    for m in faces-clique:
        w=[v for v in range(n) if all((m>>u&1)==0 or u==v or u in adj[v] for u in range(n))]
        assert len(w)==1
        if not m>>w[0]&1:pairs.add((m,m|(1<<w[0])))
    automs=[]
    for perm in permutations(range(n)):
        if {tuple(sorted((perm[u],perm[v]))) for u,v in edges}==edges:automs.append(perm)
    def push(mask,perm):return sum(1<<perm[i] for i in range(n) if mask>>i&1)
    for perm in automs:
        assert {(push(a,perm),push(b,perm)) for a,b in pairs}==pairs
    print('EQUIVARIANT',label,n,len(automs),len(pairs))

def main():
    for n in range(1,7):
        c4=0;total=1<<(n*(n-1)//2)
        maxpairs=0;maxfaces=0;trigraphs=0
        for mask in range(total):
            x=check_graph(n,mask)
            if x is not None:
                c4+=1;maxfaces=max(maxfaces,x[0]);maxpairs=max(maxpairs,x[2]);trigraphs+=bool(x[4])
        print('EXHAUSTIVE',n,total,c4,maxfaces,maxpairs,trigraphs)
    check_symmetry(5, [(i,(i+1)%5) for i in range(5)],'C5')
    check_symmetry(5, [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],'two_triangles')
    check_symmetry(6, [(0,i) for i in range(1,6)],'star_5')
    # A sharp obstructing example: C4 gives a tetrahedron boundary, not the graph circle.
    cyc={(0,1),(1,2),(2,3),(0,3)}
    mask=sum(1<<i for i,p in enumerate(combinations(range(4),2)) if p in cyc)
    E=list(combinations(range(4),2));assert check_graph(4,mask) is None
    faces=set()
    for v in range(4):
        N={v,(v-1)%4,(v+1)%4}
        for k in range(1,4):
            for s in combinations(N,k):faces.add(frozenset(s))
    assert len(faces)==14 and sum(len(s)==3 for s in faces)==4
    print('C4_SHARPNESS',len(faces),'four triangular facets: S2; clique graph: S1')
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
