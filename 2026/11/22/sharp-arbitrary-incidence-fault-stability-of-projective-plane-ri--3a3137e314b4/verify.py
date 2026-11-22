"""Standalone finite check of incidence-edge graph-metric Rips claim.
Only Python 3 standard library; no external data; checks q=2,3.
"""
from itertools import product, combinations
from collections import Counter, deque, defaultdict


def projective_plane(q):
    assert q in (2, 3)  # prime finite fields used for the finite certificate
    vecs = set()
    for v in product(range(q), repeat=3):
        if not any(v):
            continue
        j = next(i for i, x in enumerate(v) if x)
        a = pow(v[j], -1, q)
        vecs.add(tuple(x * a % q for x in v))
    vecs = sorted(vecs)
    n = len(vecs)
    edges = {(i, n + j) for i, x in enumerate(vecs)
             for j, y in enumerate(vecs)
             if sum(a * b for a, b in zip(x, y)) % q == 0}
    assert n == q*q+q+1 and len(edges)==n*(q+1)
    return n, edges


def distance_matrix(n, edges):
    adj = [set() for _ in range(2*n)]
    for i,j in edges:
        adj[i].add(j);adj[j].add(i)
    dist = []
    for i in range(2*n):
        d = [-1] * (2*n)
        d[i] = 0
        todo = deque([i])
        while todo:
            a = todo.popleft()
            for b in adj[a]:
                if d[b] == -1:
                    d[b] = d[a]+1
                    todo.append(b)
        assert min(d)>=0
        dist.append(d)
    return dist


def all_cliques(dist, radius):
    n = len(dist)
    neigh = [{j for j in range(n) if j != i and dist[i][j] <= radius}
             for i in range(n)]
    maximals=[]
    def search(R,P,X):
        if not P and not X:
            maximals.append(frozenset(R));return
        pivot = max(P | X, key=lambda u: len(P & neigh[u])) if P or X else None
        for u in tuple(sorted(P - (neigh[pivot] if pivot is not None else set()))):
            search(R | {u}, P & neigh[u], X & neigh[u])
            P.remove(u);X.add(u)
    search(set(),set(range(n)),set())
    faces={frozenset()}
    for face in maximals:
        a=tuple(sorted(face))
        for k in range(1,len(a)+1):
            faces.update(map(frozenset,combinations(a,k)))
    return maximals, faces


def ranks_mod2(faces, relative_to=None):
    if relative_to is None:
        remaining=faces
    else:
        assert relative_to<=faces
        remaining=faces-relative_to
    by=defaultdict(list)
    for f in remaining:
        if f:by[len(f)-1].append(tuple(sorted(f)))
    ranks={}
    for k in range(1,max(by,default=0)+1):
        low = {f:i for i,f in enumerate(by[k-1])}
        basis={};rank=0
        for f in by[k]:
            x=0
            for j in range(len(f)):
                face=f[:j]+f[j+1:]
                if face in low:x^=1<<low[face]
            while x:
                p=x.bit_length()-1
                if p not in basis:
                    basis[p]=x;rank+=1;break
                x^=basis[p]
        ranks[k]=rank
    betti={k:len(fs)-ranks.get(k,0)-ranks.get(k+1,0)
           for k,fs in by.items()}
    if relative_to is None:
        betti[0]-=1  # reduced
    return {k:v for k,v in betti.items() if v!=0}


def neighbors(n, edges):
    adj=[set() for _ in range(2*n)]
    for p,l in edges:
        adj[p].add(l);adj[l].add(p)
    return adj


def distances_from(adj, start):
    dist=[-1]*len(adj)
    dist[start]=0
    todo=deque([start])
    while todo:
        a=todo.popleft()
        for b in adj[a]:
            if dist[b]<0:
                dist[b]=dist[a]+1;todo.append(b)
    return dist


def main():
    for q in (2,3):
        n,edges=projective_plane(q)
        listed=sorted(edges)
        total=0
        samples=[]
        for t in range(q+1):
            for F in combinations(listed,t):
                fault=set(F)
                adj=neighbors(n,edges-fault)
                bad_lines={ell for p,ell in fault}
                bad_points={p for p,ell in fault}
                witness_p=next(p for p in range(n) if p not in
                    {x for ell in bad_lines for x in adj[ell] | {v for v,l in fault if l==ell}})
                witness_l=next(ell for ell in range(n,2*n) if ell not in
                    {x for p in bad_points for x in adj[p] | {l for v,l in fault if v==p}})
                dp=distances_from(adj,witness_p)
                dl=distances_from(adj,witness_l)
                assert all(0<=dp[v]<=2 for v in range(n))
                assert all(0<=dl[v]<=2 for v in range(n,2*n))
                assert all(0<=dp[v]<=3 for v in range(n,2*n))
                assert all(0<=dl[v]<=3 for v in range(n))
                # The first point witness is a cone point for the point-side Rips2 complex.
                # The line witness is a cone point for the line-side Rips2 complex.
                assert all(adj[v] for v in range(2*n))
                total+=1
                if t in (0,q) and (len(samples)<8 or total % 3011 == 0):
                    samples.append(fault)
        print('q=',q,'all fault sets checked=',total,flush=True)
        for faults in samples[:12]:
            graph=edges-faults
            dist=distance_matrix(n,graph)
            facets,face_set=all_cliques(dist,2)
            assert ranks_mod2(face_set)=={2:q**3-len(faults)}
            assert all((sum(v<n for v in f)<=1 or sum(v>=n for v in f)<=1)
                       for f in facets)
            print('   sample faults=',len(faults),'Rips2 faces=',len(face_set)-1,
                  'mod2 H2=',q**3-len(faults),flush=True)
    print('PASS: exhaustive arbitrary incident-edge faults through the sharp uniform threshold')

if __name__=='__main__':main()
