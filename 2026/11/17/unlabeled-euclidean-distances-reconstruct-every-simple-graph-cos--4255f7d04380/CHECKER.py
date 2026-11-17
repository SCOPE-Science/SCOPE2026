"""Standalone exact-integer regression test for Euclidean reconstruction of graph cosmological polytopes."""
from itertools import combinations
from collections import defaultdict
from random import Random


def canonical_points(n, edges):
    """Exact 3m vertices in R^(n+m), for a simple graph without isolates."""
    edges = sorted(tuple(sorted(e)) for e in edges)
    m = len(edges)
    if len(set(edges)) != m or any(u == v or not (0 <= u < n and 0 <= v < n) for u,v in edges):
        raise ValueError('Not a simple graph')
    P = []
    for j, (u,v) in enumerate(edges):
        for a,b,c in ((1,1,-1),(1,-1,1),(-1,1,1)):
            p=[0]*(n+m)
            p[u],p[v],p[n+j]=a,b,c
            P.append(tuple(p))
    return P


def squared_distances(points):
    return [[sum((x-y)**2 for x,y in zip(a,b)) for b in points] for a in points]


def graph_from_unlabeled_metric(D):
    """Recover graph edges using only integer squared distances, no vertex coordinates."""
    N=len(D)
    assert N % 3 == 0
    m=N//3
    pairs_by_sig=defaultdict(list)
    for i,j in combinations(range(N),2):
        sig=tuple(2*D[i][k]+2*D[j][k]-D[i][j] for k in range(N))
        pairs_by_sig[sig].append((i,j))
    groups=[p for p in pairs_by_sig.values() if len(p)>1]
    core=len(groups)
    graph_edges=set()
    membership=defaultdict(set)
    for g,pairs in enumerate(groups):
        for i,j in pairs:
            membership[i].add(g)
            membership[j].add(g)
    assert all(len(v)<=2 for v in membership.values()),'a point belongs to >2 midpoint classes'
    for labs in membership.values():
        if len(labs)==2:
            u,v=sorted(labs)
            graph_edges.add((u,v))
    next_vertex=core
    for g,pairs in enumerate(groups):
        for i,j in pairs:
            if len(membership[i])==len(membership[j])==1:
                graph_edges.add((g,next_vertex))
                next_vertex+=1
            else:
                assert max(len(membership[i]),len(membership[j]))==2
    if len(graph_edges)>m: raise AssertionError('too many reconstructed edges')
    for j in range(m-len(graph_edges)):
        graph_edges.add((next_vertex,next_vertex+1))
        next_vertex+=2
    assert len(graph_edges)==m
    return next_vertex,graph_edges,sorted(len(g) for g in groups)


def isomorphic(n,E,n2,F):
    if n!=n2 or len(E)!=len(F): return False
    A=[set() for _ in range(n)];B=[set() for _ in range(n)]
    for u,v in E:A[u].add(v);A[v].add(u)
    for u,v in F:B[u].add(v);B[v].add(u)
    if sorted(map(len,A))!=sorted(map(len,B)):return False
    order=sorted(range(n),key=lambda u:(-len(A[u]),-sum(len(A[w]) for w in A[u])))
    mapping={};used=set()
    def test(j):
        if j==n:return True
        u=order[j]
        for v in range(n):
            if v in used or len(A[u])!=len(B[v]):continue
            if all(((w in A[u])==(mapping[w] in B[v])) for w in mapping):
                used.add(v);mapping[u]=v
                if test(j+1):return True
                used.remove(v);del mapping[u]
        return False
    return test(0)


def run():
    tested=0
    for n in range(2,6):
        possible=list(combinations(range(n),2))
        for mask in range(1<<len(possible)):
            edges={e for j,e in enumerate(possible) if mask>>j&1}
            if not edges or set.union(*(set(e) for e in edges))!=set(range(n)):continue
            P=canonical_points(n,edges)
            output=graph_from_unlabeled_metric(squared_distances(P))
            assert isomorphic(n,edges,output[0],output[1]),(n,edges,output)
            assert output[2]==sorted(sum(u in e for e in edges) for u in range(n) if sum(u in e for e in edges)>1)
            tested+=1
    rng=Random(20261114)
    random_count=0
    for n in range(6,9):
        possible=list(combinations(range(n),2))
        for p in (0.25,0.5,0.8):
            for _ in range(25):
                edges={e for e in possible if rng.random()<p}
                if not edges or set.union(*(set(e) for e in edges))!=set(range(n)):continue
                P=canonical_points(n,edges)
                out=graph_from_unlabeled_metric(squared_distances(P))
                assert isomorphic(n,edges,out[0],out[1]),(n,edges,out)
                random_count+=1
    print(f'COSMO_METRIC_GRAPH_RECONSTRUCTION_PASS exhaustive={tested} random={random_count}')


if __name__=='__main__':run()
