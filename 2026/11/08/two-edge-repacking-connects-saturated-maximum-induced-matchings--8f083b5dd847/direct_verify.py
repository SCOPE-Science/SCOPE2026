"""Direct induced-matching enumeration and adjacency checks on square rook graphs.
Usage: python direct_verify.py
"""
from itertools import combinations
from collections import deque,Counter
from math import factorial

def full_graph(n):
    edges=[]
    for v in range(n*n):
        r,c=divmod(v,n)
        for w in range(v+1,n*n):
            s,d=divmod(w,n)
            if r==s or c==d: edges.append((v,w))
    return edges

def compatible(e,f,n):
    for v in e:
        for w in f:
            r,c=divmod(v,n); s,d=divmod(w,n)
            if r==s or c==d: return False
    return True

def enumerate_induced(n,target):
    es=full_graph(n); N=len(es)
    c=[0]*N
    for i,e in enumerate(es):
        b=0
        for j in range(i+1,N):
            if compatible(e,es[j],n): b|=1<<j
        c[i]=b
    out=[]
    def rec(state,opts,depth):
        if depth==target:
            out.append(tuple(state)); return
        while opts:
            i=(opts&-opts).bit_length()-1
            opts^=(1<<i)
            rec(state+[i],opts&c[i],depth+1)
    rec([], (1<<N)-1,0)
    return es,out

def signature(edges,ids,n):
    return tuple(sorted(tuple(sorted(e)) for e in [edges[i] for i in ids]))

def all_replacements(M, es, n):
    old=set(M); out=set()
    for rem in combinations(M,2):
        remain=old-set(rem)
        avail=[i for i,e in enumerate(es) if i not in old and all(compatible(e,es[j],n) for j in remain)]
        for i,j in combinations(avail,2):
            if compatible(es[i],es[j],n): out.add(frozenset(remain|{i,j}))
    return out

def run():
    for t in (1,2):
        n=3*t; es,sets=enumerate_induced(n,2*t)
        states={frozenset(x) for x in sets}
        pred=(factorial(n)//(2**t*factorial(t)))**2
        assert len(states)==pred,(n,len(states),pred)
        assert all(all(compatible(es[a],es[b],n) for a,b in combinations(S,2)) for S in states)
        if t==1:
            assert len(states)==9
        _, oversized=enumerate_induced(n,2*t+1)
        assert not oversized
        degpred=13*t*t-5*t
        for S in states:
            adj=all_replacements(S,es,n)
            assert len(adj)==degpred,(n,len(adj),S)
            assert adj<=states
        print(f'n={n} edges={len(es)} maximum_induced_matchings={len(states)} degree2={degpred} edges2={len(states)*degpred//2}')
        start=next(iter(states)); dist={start:0}; q=deque([start])
        while q:
            U=q.popleft()
            for V in all_replacements(U,es,n):
                if V not in dist:dist[V]=dist[U]+1;q.append(V)
        assert len(dist)==len(states)
        spheres=tuple(sum(d==j for d in dist.values()) for j in range(max(dist.values())+1))
        assert spheres==((1,8) if t==1 else (1,42,705,4904,2448))
        print(f'n={n} two_exchange_components=1 distances_from_seed={spheres}')
    print('PASS direct verifier')
if __name__=='__main__': run()
