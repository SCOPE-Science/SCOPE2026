#!/usr/bin/env python3
"""Finite checks for radius-two Rips complexes of flag-defective planes.
Run: python3 verify_star_flag.py. Uses only the Python standard library.
The uniform theorem is proved separately, not inferred from these checks.
"""
from collections import Counter
import heapq
from itertools import product

def pg_vectors(q):
    vectors = set()
    for v in product(range(q), repeat=3):
        if not any(v):
            continue
        k = next(i for i in range(3) if v[i])
        inv = pow(v[k], -1, q)
        vectors.add(tuple(x*inv % q for x in v))
    return sorted(vectors)

def plane_graph(q):
    v = pg_vectors(q); n = len(v)
    edges = set()
    for p, x in enumerate(v):
        for ell, y in enumerate(v):
            if sum(a*b for a,b in zip(x,y))%q == 0:
                edges.add((p,n+ell))
    assert n == q*q+q+1 and len(edges) == n*(q+1)
    assert all(sum(a==p for a,b in edges)==q+1 for p in range(n))
    assert all(sum(b==ell for a,b in edges)==q+1 for ell in range(n,2*n))
    assert all(sum((p,ell) in edges and (r,ell) in edges for ell in range(n,2*n))==1
               for p in range(n) for r in range(p+1,n))
    assert all(sum((p,ell) in edges and (p,m) in edges for p in range(n))==1
               for ell in range(n,2*n) for m in range(ell+1,2*n))
    return n,edges

def graph_data(n, edges):
    N = 2*n
    neighbors = [set() for _ in range(N)]
    for a,b in edges:
        neighbors[a].add(b); neighbors[b].add(a)
    D = [[10**6]*N for _ in range(N)]
    for a in range(N):
        queue=[a]; D[a][a]=0
        for u in queue:
            for v in neighbors[u]:
                if D[a][v]>D[a][u]+1:
                    D[a][v]=D[a][u]+1;queue.append(v)
        assert len(queue)==N, 'graph must stay connected'
    graph = [sum(1<<j for j in range(N) if j!=i and D[i][j]<=2) for i in range(N)]
    return D,graph

def maximal_cliques(adj):
    allv=(1<<len(adj))-1
    ans=[]
    def expand(R,P,X):
        if not P and not X:
            ans.append(R); return
        un=P|X
        pivot=max((i for i in range(len(adj)) if un>>i&1),
                  key=lambda i:(P&adj[i]).bit_count(),default=-1)
        candidates=P&~(adj[pivot] if pivot>=0 else 0)
        while candidates:
            v=(candidates&-candidates).bit_length()-1;bit=1<<v
            expand(R|bit,P&adj[v],X&adj[v]);P&=~bit;X|=bit;candidates&=~bit
    expand(0,allv,0)
    return ans

def all_subfaces(maximal):
    result=set()
    for m in maximal:
        s=m
        while s:
            result.add(s);s=(s-1)&m
    return result

def rips_faces(adj):return all_subfaces(maximal_cliques(adj))

def expected_faces(n,edge_set,p0,removed):
    N=2*n
    points=(1<<n)-1
    lines=((1<<n)-1)<<n
    deleted_points={a for a in range(n) for ell in removed if (a,ell) in edge_set}
    # The chosen point is connected to none of the other points whose unique line was deleted.
    point_base = points&~(1<<p0)
    point_other = points & ~sum(1<<a for a in deleted_points if a!=p0)
    # Line side: outside the chosen point's pencil forms a universal clique.
    pencil={ell for a,ell in edge_set if a==p0}
    intact=pencil-set(removed)
    outside=lines&~sum(1<<ell for ell in pencil)
    line_base=outside|sum(1<<ell for ell in intact)
    facets=[point_base,point_other,line_base]
    facets += [outside|(1<<ell) for ell in removed]
    for ell in range(n,N):
        incident=[a for a,b in edge_set if b==ell and ell not in removed]
        if ell not in removed:
            incident=[a for a,b in edge_set if b==ell]
        else:
            incident=[a for a,b in edge_set if b==ell and a!=p0]
        facets.append((1<<ell)|sum(1<<a for a in incident))
    for p in range(n):
        incident=[ell for a,ell in edge_set if a==p and (p!=p0 or ell not in removed)]
        facets.append((1<<p)|sum(1<<ell for ell in incident))
    return all_subfaces(facets)

def collapse(faces):
    fs=set(faces);co={f:set() for f in fs}
    for t in fs:
        s=t
        while s:
            b=s&-s;sub=t^b
            if sub:co[sub].add(t)
            s-=b
    heap=[]
    for s in fs:
        if len(co[s])==1:
            t=next(iter(co[s]))
            if not co[t]:heapq.heappush(heap,(-s.bit_count(),s))
    num=0
    while heap:
        _,s=heapq.heappop(heap)
        if s not in fs or len(co[s])!=1:continue
        t=next(iter(co[s]))
        if co[t] or t not in fs:continue
        fs.remove(s);fs.remove(t);num+=1
        affected=set()
        for u in (s,t):
            bits=u
            while bits:
                b=bits&-bits;v=u^b;bits-=b
                if v:
                    co[v].discard(u);affected.add(v)
        for v in affected:
            if v in fs and len(co[v])==1:
                w=next(iter(co[v]))
                if not co[w]:heapq.heappush(heap,(-v.bit_count(),v))
    return fs,num

def rank_mod2(vectors):
    pivots={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in pivots:v ^= pivots[p]
            else:pivots[p]=v;break
    return len(pivots)

def reduced_betti(faces):
    d=Counter(f.bit_count()-1 for f in faces)
    assert max(d)<=2, d
    edges=sorted(f for f in faces if f.bit_count()==2)
    triangles=(f for f in faces if f.bit_count()==3)
    pos={e:i for i,e in enumerate(edges)}
    cols=[]
    for t in triangles:
        bits=[1<<i for i in range(t.bit_length()) if t>>i&1]
        col=0
        for b in bits:col ^= 1<<pos[t^b]
        cols.append(col)
    r2=rank_mod2(cols)
    # The one-skeleton is connected in all cases under study.
    b1=d[1]-(d[0]-1)-r2
    b2=d[2]-r2
    return b1,b2

def run():
    for q in (2,3):
        n,full=plane_graph(q)
        p0=0
        flags=sorted(ell for a,ell in full if a==p0)
        for t in range(q+1):
            removed=set(flags[:t])
            edges=full-{(p0,ell) for ell in removed}
            D,adj=graph_data(n,edges)
            # Pairwise shortest paths must have exactly the predicted 2-neighborhoods.
            missing_points={a for a in range(n) if any((a,ell) in full for ell in removed) and a!=p0}
            for a in range(n):
                for b in range(a+1,n):
                    expect=not (p0 in (a,b) and (a if b==p0 else b) in missing_points)
                    assert (D[a][b]<=2)==expect
            pencil=set(flags)
            for a in range(n,2*n):
                for b in range(a+1,2*n):
                    expect=not ((a in pencil and b in pencil) and (a in removed or b in removed))
                    assert (D[a][b]<=2)==expect
            actual=rips_faces(adj)
            expected=expected_faces(n,full,p0,removed)
            assert actual==expected, (q,t,len(actual^expected))
            rest,pairs=collapse(actual)
            b1,b2=reduced_betti(rest)
            assert b1==0 and b2==q**3-t,(q,t,b1,b2)
            vec=tuple(Counter(f.bit_count()-1 for f in actual)[i]
                      for i in range(max(f.bit_count() for f in actual)))
            print(f'q={q} t={t} faces={len(actual)} collapses={pairs} '
                  f'residual={len(rest)} mod2_betti=(0,{b1},{b2}) fvector={vec}')
    print('PASS: all finite stage checks and structural-cover comparisons')

if __name__=='__main__':run()
