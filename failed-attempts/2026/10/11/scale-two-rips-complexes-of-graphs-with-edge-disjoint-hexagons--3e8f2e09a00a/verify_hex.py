#!/usr/bin/env python3
"""Finite checks for a sparse-six-cycle graph-metric Rips homotopy theorem.
Uses only Python 3 standard library. Does not substitute for the general proof.
"""
from collections import deque
from itertools import combinations
import random

def graph(n, edges):
    E={tuple(sorted((int(a),int(b)))) for a,b in edges}
    assert all(0<=a<b<n for a,b in E)
    return n,E

def adj(G):
    n,E=G
    a=[set() for _ in range(n)]
    for u,v in E:a[u].add(v);a[v].add(u)
    return a

def dists(G):
    n,_=G;a=adj(G);out=[]
    for root in range(n):
        d=[n+1]*n;d[root]=0;q=deque([root])
        while q:
            v=q.popleft()
            for w in a[v]:
                if d[w]>n:d[w]=d[v]+1;q.append(w)
        out.append(d)
    return out

def simple_cycles_upto_six(G):
    a=adj(G);n=len(a);C=set()
    for s in range(n):
        def dfs(path):
            v=path[-1]
            if len(path)>=3 and s in a[v]:
                xs=path[:];cyc=tuple(xs if xs[1]<xs[-1] else [xs[0]]+xs[:0:-1]);C.add(cyc)
            if len(path)==6:return
            for w in a[v]:
                if w>s and w not in path:dfs(path+[w])
        dfs([s])
    return sorted(C,key=lambda x:(len(x),x))

def admissible(G):
    d=dists(G)
    if any(G[0]+1 in r for r in d):return None
    cycles=simple_cycles_upto_six(G)
    if any(len(c)<6 for c in cycles):return None
    H=[c for c in cycles if len(c)==6]
    e6=[{tuple(sorted((c[i],c[(i+1)%6]))) for i in range(6)} for c in H]
    if any(a&b for a,b in combinations(e6,2)):return None
    return H

def all_cliques(G):
    n,_=G;d=dists(G)
    A=[{j for j in range(n) if i!=j and d[i][j]<=2} for i in range(n)]
    result={frozenset()}
    def build(c,options):
        for j in options:
            nxt=c+(j,)
            result.add(frozenset(nxt))
            build(nxt,[k for k in options if k>j and k in A[j]])
    build((),list(range(n)))
    return result

def classification(G,H):
    n,_=G;a=adj(G)
    K0={frozenset()}
    for v in range(n):
        star=sorted(a[v]|{v})
        for k in range(1,len(star)+1):
            K0.update(map(frozenset,combinations(star,k)))
    extras={frozenset(c[i] for i in inds) for c in H for inds in ((0,2,4),(1,3,5))}
    K=all_cliques(G)
    assert K-K0==extras,(G,H,K-K0,extras)
    assert all(len(t)==3 for t in extras)
    return K,K0,extras

def rank_mod_p(boundary_columns,p):
    pivots={};r=0
    for col in boundary_columns:
        x={k:v%p for k,v in col.items() if v%p}
        while x:
            v=min(x)
            if v not in pivots:
                t=pow(x[v],-1,p)
                pivots[v]={i:(c*t)%p for i,c in x.items()}
                r+=1;break
            base=pivots[v];factor=x[v]
            for j,c in base.items():
                z=(x.get(j,0)-factor*c)%p
                if z:x[j]=z
                elif j in x:del x[j]
    return r

def betti(G,K,p):
    fs={}
    for f in K:
        if f:fs.setdefault(len(f)-1,[]).append(tuple(sorted(f)))
    for v in fs:fs[v].sort()
    ranks={0:0}
    for d in sorted(fs):
        if d==0:continue
        ix={f:i for i,f in enumerate(fs[d-1])}
        cols=[]
        for f in fs[d]:
            col={}
            for j in range(len(f)):
                k=ix[f[:j]+f[j+1:]]
                col[k]=(-1 if j%2 else 1)%p
            cols.append(col)
        ranks[d]=rank_mod_p(cols,p)
    return {d:len(cs)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d,cs in fs.items() if len(cs)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}

def cycle(n):return graph(n,((i,(i+1)%n) for i in range(n)))
def theta(*lengths):
    assert len(lengths)>=2 and min(lengths)>=3
    edges=[];last=2
    for L in lengths:
        path=[0]+list(range(last,last+L-1))+[1];last+=L-1
        edges+=list(zip(path,path[1:]))
    return graph(last,edges)

def double_hex(bridge):
    E=[(i,(i+1)%6) for i in range(6)]
    if bridge:
        E += [(i+6,6+(i+1)%6) for i in range(6)]+[(0,6)]
        return graph(12,E)
    E += [((i+5) if i>0 else 0,(i+5 if i<5 else 0)) for i in []]
    E += [((0 if i==0 else i+5),(0 if i==5 else i+6)) for i in range(6)]
    return graph(11,E)

def main():
    examples=[cycle(n) for n in range(6,11)]
    examples += [theta(*s) for s in ((3,3,4),(3,3,5),(3,4,4),(3,4,5),(4,4,4),(3,3,7),(3,4,6))]
    examples +=[double_hex(True),double_hex(False)]
    nbeta=0
    for i,G in enumerate(examples):
        H=admissible(G)
        assert H is not None,(i,G,'not eligible')
        K,_,_=classification(G,H)
        expected={d:r for d,r in ((1,len(G[1])-G[0]+1-len(H)),(2,len(H))) if r}
        for p in (2,3):
            got=betti(G,K,p)
            assert got==expected,(i,p,got,expected)
            nbeta+=1
    # Reproducible bounded stress test of the complete simplex decomposition
    rng=random.Random(19073);tested=0
    for n in range(6,12):
        for _ in range(95):
            E={(i,(i+1)%6) for i in range(6)}
            E={tuple(sorted(e)) for e in E}
            for u in range(6,n):
                if rng.random()<.8:E.add(tuple(sorted((u,rng.randrange(u)))))
            for u,v in combinations(range(n),2):
                if (u,v) not in E and rng.random()<.025:
                    E.add((u,v))
            G=graph(n,E)
            H=admissible(G)
            if H is None:continue
            classification(G,H)
            tested+=1
    assert tested>=100,tested
    print('VERIFY_OK',len(examples),'homology instances,',nbeta,'exact rank checks,',tested,'complete face-decomposition stress tests')

if __name__=='__main__':main()
