#!/usr/bin/env python3
"""Reproducible finite checks for a combinatorial Rips collapse (stdlib only)."""
from itertools import combinations,product
from collections import deque, Counter

def girth_at_least_seven(n, edges):
    adj=[set() for _ in range(n)]
    for x,y in edges:adj[x].add(y);adj[y].add(x)
    for x,y in edges:
        seen={x};dq=deque([(x,0)])
        while dq:
            u,d=dq.popleft()
            if d>=5: continue
            for w in adj[u]:
                if {u,w}=={x,y}:continue
                if w==y:return False
                if w not in seen:seen.add(w);dq.append((w,d+1))
    return True

def analyze(n,edges,require_girth=True):
    edges={tuple(sorted(e)) for e in edges};adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    if require_girth:assert girth_at_least_seven(n,edges)
    N=2*n;ga=[set() for _ in range(N)]
    for v in range(n):ga[2*v].add(2*v+1);ga[2*v+1].add(2*v)
    for u,v in edges:
        for a in (0,1):ga[2*u+a].add(2*v+a);ga[2*v+a].add(2*u+a)
    dist=[[N+3]*N for _ in range(N)]
    for u in range(N):
        dist[u][u]=0;dq=deque([u])
        while dq:
            x=dq.popleft()
            for y in ga[x]:
                if dist[u][y]>dist[u][x]+1:dist[u][y]=dist[u][x]+1;dq.append(y)
    k2=[{v for v in range(N) if u!=v and dist[u][v]<=2} for u in range(N)]
    faces=set()
    def expand(T,cand):
        if T:faces.add(T)
        while cand:
            u=cand.pop()
            expand(T|frozenset([u]),{v for v in cand if v in k2[u]})
    expand(frozenset(),set(range(N)))
    F0=len(faces)
    proposed=set()
    def add_simplex(V):
        for j in range(1,len(V)+1):
            for t in combinations(V,j):proposed.add(frozenset(t))
    for v in range(n):
        for a in (0,1):
            add_simplex([2*v,2*v+1]+[2*u+a for u in sorted(adj[v])])
    for u,v in edges:add_simplex([2*u,2*u+1,2*v,2*v+1])
    assert faces==proposed,("maximal-clique-cover-failed",n,edges,len(faces),len(proposed),len(faces-proposed))
    count1=0
    for v in range(n):
        for a in (0,1):
            B=[2*u+a for u in sorted(adj[v])]
            pivot=2*v+a;other=2*v+1-a
            todo=[]
            for k in range(2,len(B)+1):
                for bs in combinations(B,k):
                    todo.append(frozenset(bs))
                    todo.append(frozenset((*bs,other)))
            for low in sorted(todo,key=lambda x:(-len(x),tuple(sorted(x)))):
                high=low|{pivot}
                assert low in faces and high in faces,('absent first',v,a,low,high)
                superfaces=[f for f in faces if low<f]
                assert superfaces==[high],('not free 1',v,a,low,superfaces)
                faces.remove(low);faces.remove(high);count1+=1
    desired=set()
    for u in range(n):
        for a in (0,1):desired.add(frozenset([2*u+a]))
        desired.add(frozenset((2*u,2*u+1)))
    for u,v in edges:
        x,y=2*u,2*v
        for T in [(x,y),(x+1,y+1),(x,y+1),(x,y,y+1),(x,x+1,y+1)]:desired.add(frozenset(T))
        tetra=frozenset((x,x+1,y,y+1));tri=frozenset((x+1,y,y+1))
        assert tetra in faces and tri in faces and [f for f in faces if tri<f]==[tetra],('not free 2a',u,v)
        faces.remove(tetra);faces.remove(tri)
        t2=frozenset((x,x+1,y));e2=frozenset((x+1,y))
        assert t2 in faces and e2 in faces and [f for f in faces if e2<f]==[t2],('not free 2b',u,v)
        faces.remove(t2);faces.remove(e2)
    assert faces==desired,('not product triangulation',n,len(faces),len(desired),len(faces-desired))
    return F0,count1,2*len(edges),len(faces)

def connected(n,edges):
    if not n:return True
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    seen={0};q=[0]
    for u in q:
        for v in adj[u]:
            if v not in seen:seen.add(v);q.append(v)
    return len(seen)==n

if __name__=='__main__':
    cases=0
    for n in range(1,6):
        complete=list(combinations(range(n),2))
        for bits in product((0,1),repeat=len(complete)):
            E=[complete[j] for j,v in enumerate(bits) if v]
            if connected(n,E) and girth_at_least_seven(n,E):
                stats=analyze(n,E)
                cases+=1
        print('connected forests at',n,'checked',cases,flush=True)
    for n in range(6,12):
        for name,edges in [
            ('cycle',[(u,(u+1)%n) for u in range(n)]),
            ('path',[(u,u+1) for u in range(n-1)]),
            ('star',[(0,u) for u in range(1,n)])
        ]:
            if girth_at_least_seven(n,edges):
                stats=analyze(n,edges);cases+=1
                print(name,n,stats,flush=True)
    n=14;E=[(i,(i+1)%7) for i in range(7)]+[(i,(i+1)%7+7) for i in range(7,14)]+[(0,7)]
    # correct two 7cycles, one bridge
    E=[(i,(i+1)%7) for i in range(7)]+[(i,i+1) for i in range(7,13)]+[(13,7)]+[(0,7)]
    stats=analyze(n,E);cases+=1;print('two septagons',stats,flush=True)
    n=11;E=[]
    for k in range(3):
        path=[0,2+3*k,3+3*k,4+3*k,1]
        E.extend(zip(path,path[1:]))
    stats=analyze(n,E);cases+=1;print('three length-four theta arms',stats,flush=True)
    print('HIGH_GIRTH_PRISM_RIPS2_COLLAPSE_OK',cases,flush=True)
