#!/usr/bin/env python3
"""Exact mod-two chain computation for two generalized Petersen graph complexes.
No external packages. The face condition is graph-geodesic general position.
"""
from collections import defaultdict, deque
from itertools import combinations

N = 20

def edges(k):
    edgeset=set()
    def add(a,b):edgeset.add(tuple(sorted((a,b))))
    for i in range(10):
        add(i,(i+1)%10)
        add(i,10+i)
        add(10+i,10+(i+k)%10)
    return sorted(edgeset)

def distance_bfs(ed):
    adj=[set() for _ in range(N)]
    for a,b in ed:adj[a].add(b);adj[b].add(a)
    ds=[]
    for s in range(N):
        dist=[99]*N;dist[s]=0;queue=deque([s])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if dist[w]==99:dist[w]=dist[v]+1;queue.append(w)
        assert max(dist)<99
        ds.append(dist)
    return ds

def distance_floyd(ed):
    d=[[99]*N for _ in range(N)]
    for i in range(N):d[i][i]=0
    for a,b in ed:d[a][b]=d[b][a]=1
    for h in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][h]+d[h][j]<d[i][j]:d[i][j]=d[i][h]+d[h][j]
    return d

def badtriples(d):
    bad=set()
    for a,b,c in combinations(range(N),3):
        if d[a][b]+d[b][c]==d[a][c] or d[a][c]+d[c][b]==d[a][b] or d[b][a]+d[a][c]==d[b][c]:
            bad.add((1<<a)|(1<<b)|(1<<c))
    return bad

def genfaces(bad):
    badpairs=[set() for _ in range(N)]
    for t in bad:
        top=t.bit_length()-1
        badpairs[top].add(t^(1<<top))
    by=defaultdict(list)
    # Full increasing-order DFS, never generating a nonface as an intermediate.
    def extend(mask,minimum):
        for v in range(minimum,N):
            if any((mask & q)==q for q in badpairs[v]):continue
            f=mask|(1<<v)
            by[f.bit_count()-1].append(f)
            extend(f,v+1)
    extend(0,0)
    return by

def colrank(by,d):
    lower={m:i for i,m in enumerate(by[d-1])}
    pivot={}
    for f in by[d]:
        vec=0;work=f
        while work:
            bit=work&-work;work-=bit
            vec^=1<<lower[f^bit]
        while vec:
            p=vec.bit_length()-1
            if p in pivot:vec^=pivot[p]
            else:pivot[p]=vec;break
    return len(pivot)

def rowrank(by,d):
    # Independent row-oriented GF(2) elimination.
    rows={f:0 for f in by[d-1]}
    for j,f in enumerate(by[d]):
        work=f
        while work:
            bit=work&-work;work-=bit
            rows[f^bit]^=1<<j
    pivots={}
    for vec in rows.values():
        while vec:
            p=(vec&-vec).bit_length()-1
            if p in pivots:vec^=pivots[p]
            else:pivots[p]=vec;break
    return len(pivots)

def boundary_squared_zero(by):
    for d in range(2,max(by)+1):
        for mask in by[d]:
            p={}
            work=mask
            while work:
                bit=work&-work;work-=bit
                child=mask^bit
                childwork=child
                while childwork:
                    bit2=childwork&-childwork;childwork-=bit2
                    sub=child^bit2
                    p[sub]=p.get(sub,0)^1
            assert not any(p.values())

def run(k,expected):
    ed=edges(k)
    assert len(ed)==30
    ds=distance_bfs(ed)
    assert ds==distance_floyd(ed)
    bad=badtriples(ds)
    by=genfaces(bad)
    assert sorted(by)==list(range(5))
    allfaces={f for faces in by.values() for f in faces}
    assert len(allfaces)==sum(map(len,by.values()))
    # Direct independent predicate: every listed face is geodesically admissible,
    # and every excluded triple is a minimal nonface.
    for f in allfaces:
        assert all((f&t)!=t for t in bad)
    for t in bad:assert t not in allfaces
    for f in allfaces:
        work=f
        while work:
            bit=work&-work;work-=bit
            if f^bit:assert f^bit in allfaces
    boundary_squared_zero(by)
    ranks={d:colrank(by,d) for d in range(1,5)}
    assert ranks=={d:rowrank(by,d) for d in range(1,5)}
    fv=[len(by[i]) for i in range(5)]
    betti={d:fv[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(5)}
    betti[0]-=1
    chi=sum((-1)**d*v for d,v in enumerate(fv))
    assert chi==1+sum((-1)**d*v for d,v in betti.items())
    assert (len(bad),fv,[ranks[d] for d in range(1,5)], [betti[d] for d in range(5)],chi)==expected
    # The shift by 5 of both layers is a free involutory graph automorphism;
    # its 10 vertex orbits induce GP(5,2), the Petersen quotient.
    shift=lambda u:(u+5)%10 if u<10 else 10+(u-10+5)%10
    assert all(tuple(sorted((shift(a),shift(b)))) in ed for a,b in ed)
    quot=set(tuple(sorted(((a%5)+(5 if a>=10 else 0),
                          (b%5)+(5 if b>=10 else 0)))) for a,b in ed)
    assert len(quot)==15
    print('GP(10,%d): bad=%d; f=%s; rank_boundary_1_to_4=%s; reduced_F2_betti=%s; chi=%d; checks=PASS' %
          (k,len(bad),fv,[ranks[d] for d in range(1,5)],[betti[d] for d in range(5)],chi))

if __name__=='__main__':
    run(2,(540,[20,190,600,550,60],[19,161,379,60],[0,10,60,111,0],-60))
    run(3,(720,[20,190,420,370,60],[19,131,289,60],[0,40,0,21,0],-60))
    print('ALL CHECKS PASS')
