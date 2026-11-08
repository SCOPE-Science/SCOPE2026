#!/usr/bin/env python3
"""Finite checks for the line-graph Rips hexagon CW model; standard library only."""
from itertools import combinations
from collections import deque, Counter

def cycle(n): return (n, [(i,(i+1)%n) for i in range(n)])
def theta(m):
    e=[]; j=2
    for i in range(m):
        e += [(0,j),(j,j+1),(j+1,1)];j+=2
    return (j,e)
def subcomplete(n):
    e=[];v=n
    for i,j in combinations(range(n),2):
        e += [(i,v),(v,j)];v+=1
    return (v,e)
def fano_incidence():
    # Nonzero 3-bit vectors p and seven two-dimensional subspaces (lines).
    lines=[]
    for a in range(1,8):
        for b in range(a+1,8):
            c=a^b
            tri=tuple(sorted((a,b,c)))
            if tri not in lines:lines.append(tri)
    lines=sorted(lines)
    return (14,[(p-1,7+i) for i,L in enumerate(lines) for p in L])

def graph(n,edges):
    E=sorted({tuple(sorted(e)) for e in edges});adj=[set() for _ in range(n)]
    for u,v in E:
        assert u!=v;adj[u].add(v);adj[v].add(u)
    return E,adj

def all6(adj):
    n=len(adj); found=set()
    for s in range(n):
        def dfs(path):
            v=path[-1]
            if len(path)==6:
                if s in adj[v]:
                    t=tuple(path); opts=[t[i:]+t[:i] for i in range(6)]+[tuple(reversed(t))[i:]+tuple(reversed(t))[:i] for i in range(6)]
                    found.add(min(opts))
                return
            for w in adj[v]:
                if w not in path:dfs(path+[w])
        dfs([s])
    return sorted(found)

def girth_ge6(adj):
    for s in range(len(adj)):
        dist={s:0};parent={s:None};todo=deque([s])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if v not in dist:dist[v]=dist[u]+1;parent[v]=u;todo.append(v)
                elif parent[u]!=v and dist[v]+dist[u]+1<6:return False
    return True

def cliques_from_edges(n, E):
    adj=[set() for _ in range(n)]
    for i,j in E:adj[i].add(j);adj[j].add(i)
    faces=set()
    def expand(prefix,candidates):
        for k,v in enumerate(candidates):
            T=prefix+(v,); faces.add(T)
            expand(T,[u for u in candidates[k+1:] if u in adj[v]])
    expand((),list(range(n)))
    return faces

def faces_simplex(S):
    S=sorted(S);return {t for r in range(1,len(S)+1) for t in combinations(S,r)}

def rank2(vectors):
    pivots={}
    for x in vectors:
        while x:
            k=x.bit_length()-1
            if k in pivots:x^=pivots[k]
            else:pivots[k]=x;break
    return len(pivots)

def homology_mod2(faces):
    layers={d:sorted([s for s in faces if len(s)==d+1]) for d in range(max(map(len,faces)))}
    ranks={}
    for d in range(1,len(layers)):
        ids={s:i for i,s in enumerate(layers[d-1])}
        ranks[d]=rank2(sum((1<<ids[t[:j]+t[j+1:]] for j in range(len(t))),0) for t in layers[d])
    return [len(layers[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in layers]

def check(name, n, edges, mod2=True):
    E,adj=graph(n,edges);assert girth_ge6(adj),name
    labels={e:i for i,e in enumerate(E)}
    line_adj=[set() for _ in E]
    for i,e in enumerate(E):
        for j,f in enumerate(E):
            if i<j and set(e)&set(f):line_adj[i].add(j);line_adj[j].add(i)
    L2=[]
    for i in range(len(E)):
        d=line_adj[i].copy()
        for j in line_adj[i]:d.update(line_adj[j])
        d.discard(i)
        for j in d:
            if i<j:L2.append((i,j))
    K=cliques_from_edges(len(E),L2)
    C=set();Y=set()
    for u,v in E:
        S=[i for i,e in enumerate(E) if u in e or v in e]
        C.update(faces_simplex(S))
    for u in range(n):
        S=[i for i,e in enumerate(E) if u in e]
        Y.update(faces_simplex(S))
    six=all6(adj)
    exceptional=set()
    six_vectors=[]
    for cyc in six:
        sourceedges=[labels[tuple(sorted((cyc[i],cyc[(i+1)%6])))] for i in range(6)]
        exceptional.update({tuple(sorted(sourceedges[0::2])),tuple(sorted(sourceedges[1::2]))})
        six_vectors.append(sum(1<<sourceedges[i] for i in range(6)))
    extra=K-C
    assert extra==exceptional, (name,'noncentered mismatch', len(extra),len(exceptional),list(extra^exceptional)[:3])
    # Uniqueness of connector plus explicit elementary free-face collapses C -> Y.
    used=[];pairs=[]
    for sigma in C-Y:
        disjoint=[(i,j) for i,j in combinations(sigma,2) if not(set(E[i])&set(E[j]))]
        assert disjoint,(name,'outside clique-star but no disjoint pair')
        connectors=[]
        for e_idx,(u,v) in enumerate(E):
            if all(u in E[x] or v in E[x] for x in sigma):connectors.append(e_idx)
        assert len(connectors)==1,(name,'connector count',sigma,connectors)
        c=connectors[0]
        if c not in sigma: pairs.append((sigma,tuple(sorted(sigma+(c,)))))
    pairs.sort(key=lambda p:(-len(p[0]),p[0]))
    remaining=set(C)
    for low,up in pairs:
        assert low in remaining and up in remaining
        assert not any(low!=t and set(low).issubset(t) and t!=up for t in remaining),(name,'not free',low,up)
        remaining.remove(low);remaining.remove(up)
    assert remaining==Y,(name,'residual not Y')
    b=len(E)-n+1
    r2=rank2(six_vectors)
    if mod2:
        hbetti=homology_mod2(K)
        assert hbetti[0]==1,(name,hbetti)
        assert hbetti[1]==b-r2,(name,hbetti,b,r2)
        assert hbetti[2]==2*len(six)-r2,(name,hbetti,len(six),r2)
        assert all(v==0 for v in hbetti[3:]),(name,hbetti)
    else:hbetti=[]
    print(f'{name}: V={n} E={len(E)} hexagons={len(six)} K={len(K)} C={len(C)} extras={len(extra)} collapse_pairs={len(pairs)} b={b} rank2_hex={r2} beta_F2={hbetti} OK')

if __name__=='__main__':
    cases=[('C6',cycle(6)),('C7',cycle(7)),('C8',cycle(8)),('theta3',theta(3)),('theta4',theta(4)),('subK4',subcomplete(4)),('subK5',subcomplete(5)),('subK6',subcomplete(6)),('Heawood',fano_incidence())]
    for name,(n,edges) in cases:check(name,n,edges,mod2=True)
    print('LINE_GRAPH_RIPS2_HEXAGON_CW_CHECKS_OK')
