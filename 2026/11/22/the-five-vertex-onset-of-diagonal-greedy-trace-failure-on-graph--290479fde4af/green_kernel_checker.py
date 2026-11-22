"""Exact standalone enumeration for rank-two graph Green-kernel pivot selection.

Requires only the Python 3 standard library. Enumerates every labelled simple graph
on 2, 3, 4, or 5 vertices. All arithmetic uses fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import Counter


def connected(n, edges):
    neighbors = [[] for _ in range(n)]
    for u,v in edges:
        neighbors[u].append(v); neighbors[v].append(u)
    seen = {0}
    frontier = [0]
    while frontier:
        for v in neighbors[frontier.pop()]:
            if v not in seen:
                seen.add(v); frontier.append(v)
    return len(seen)==n


def invert(A):
    n=len(A)
    B=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if B[i][j]!=0)
        B[j],B[pivot]=B[pivot],B[j]
        d=B[j][j];B[j]=[x/d for x in B[j]]
        for i in range(n):
            if i!=j:
                d=B[i][j]
                if d: B[i]=[x-d*y for x,y in zip(B[i],B[j])]
    return [b[n:] for b in B]


def errors(K):
    n=len(K)
    error={}
    for u,v in combinations(range(n),2):
        a,b,c=K[u][u],K[u][v],K[v][v]
        det=a*c-b*b
        error[(u,v)]=sum(K[i][i]-(c*K[i][u]**2-2*b*K[i][u]*K[i][v]+a*K[i][v]**2)/det for i in range(n))
    return error


def choices(K,error):
    n=len(K)
    m=max(K[u][u] for u in range(n))
    first=[u for u in range(n) if K[u][u]==m]
    G=[]
    for u in first:
        post={v:K[v][v]-K[v][u]**2/K[u][u] for v in range(n) if v!=u}
        mx=max(post.values())
        G.extend([tuple(sorted((u,v))) for v in post if post[v]==mx])
    return sorted(set(G))


def is_witness(n,edges):
    if n!=5:return False
    E=set(tuple(sorted(e)) for e in edges)
    W={(0,1),(1,2),(1,3),(1,4),(2,3),(2,4)}
    for p in permutations(range(5)):
        if {tuple(sorted((p[a],p[b]))) for a,b in W}==E:return True
    return False


def run():
    totals=Counter()
    saved=None
    for n in range(2,6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            E=[e for k,e in enumerate(all_edges) if (mask>>k)&1]
            if not connected(n,E):continue
            totals[(n,'connected')]+=1
            A=[[F(i==j) for j in range(n)] for i in range(n)]
            for u,v in E:
                A[u][u]+=1; A[v][v]+=1
                A[u][v]-=1; A[v][u]-=1
            K=invert(A)
            e=errors(K)
            opt=min(e.values()); optpairs=[p for p in e if e[p]==opt]
            greedy=choices(K,e)
            if any(e[p]>opt for p in greedy):
                totals[(n,'some_fail')]+=1
            if all(e[p]>opt for p in greedy):
                totals[(n,'all_fail')]+=1
            if any(e[p]>opt for p in greedy):
                assert is_witness(n,E),('unexpected graph topology',n,E)
                assert len(greedy)==2 and len(optpairs)==1
                assert sorted(e[p] for p in greedy)==[F(22,23),F(22,23)]
                assert opt==F(37,39)
                assert optpairs[0] in [tuple(sorted(p)) for p in permutations(range(n),2)]
                if saved is None:saved=(n,E,optpairs,greedy,K)
    assert [totals[n,'connected'] for n in range(2,6)] == [1,4,38,728]
    assert [totals[n,'some_fail'] for n in range(2,6)] == [0,0,0,60]
    assert [totals[n,'all_fail'] for n in range(2,6)] == [0,0,0,60]
    assert saved is not None
    print('EXHAUSTIVE EXACT PASS: connected labelled graphs by n=2..5:',[totals[n,'connected'] for n in range(2,6)])
    print('all-greedy suboptimal counts:',[totals[n,'all_fail'] for n in range(2,6)])
    print('all 60 failing graphs are the same 5-vertex isomorphism class')
    print('unique isomorphism class: diamond with pendant leaf at a degree-3 vertex')
    print('witness optimum trace =',F(37,39),'greedy trace =',F(22,23),'gap =',F(22,23)-F(37,39))
    print('greedy-to-optimum trace ratio =',F(22,23)/F(37,39))

if __name__=='__main__':run()
