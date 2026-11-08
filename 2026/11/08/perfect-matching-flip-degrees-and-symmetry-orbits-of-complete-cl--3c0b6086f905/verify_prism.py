#!/usr/bin/env python3
"""Exhaustive perfect-matchings and four-cycle flip states of two-clique prisms."""
import collections
import json
from functools import lru_cache
from math import comb, factorial, prod


def doublefac_odd(h):
    return prod(range(1, 2*h, 2))


def partition_parts(m0,m1,unused):
    nb={v:set() for v in unused}
    for a,b in list(m0)+list(m1):
        nb[a].add(b);nb[b].add(a)
    todo=set(unused);sizes=[]
    while todo:
        seen={todo.pop()}; queue=list(seen)
        for v in queue:
            for w in nb[v]:
                if w not in seen:
                    seen.add(w);todo.discard(w);queue.append(w)
        assert len(seen)%2==0
        sizes.append(len(seen)//2)
    return tuple(sorted(sizes))


def expected_size(n,k,lam):
    h=(n-k)//2
    if h==0:return 1
    multiplicity=collections.Counter(lam)
    z=prod(t**m * factorial(m) for t,m in multiplicity.items())
    return comb(n,k)*doublefac_odd(h)*factorial(h)*2**(h-len(lam))//z


def run(n):
    N=2*n
    neighbors={v:set() for v in range(N)}
    for i in range(n):
        neighbors[i].add(n+i);neighbors[n+i].add(i)
    for a in range(n):
        for b in range(a+1,n):
            neighbors[a].add(b);neighbors[b].add(a)
            neighbors[n+a].add(n+b);neighbors[n+b].add(n+a)
    @lru_cache(None)
    def match(mask):
        if not mask: return ((),)
        v=(mask&-mask).bit_length()-1
        out=[]
        for w in sorted(neighbors[v]):
            if mask&(1<<w):
                edge=(min(v,w),max(v,w))
                for rest in match(mask^(1<<v)^(1<<w)):
                    out.append(tuple(sorted((edge,)+rest)))
        return tuple(out)
    states=tuple(sorted(match((1<<N)-1)))
    pos={m:i for i,m in enumerate(states)}
    adj=[set() for m in states]
    types=collections.Counter();deg_by_type={}
    for i,m in enumerate(states):
        rungs={a for a,b in m if b==a+n}
        unused=sorted(set(range(n))-rungs)
        m0={(a,b) for a,b in m if a<n and b<n}
        m1={(a-n,b-n) for a,b in m if a>=n and b>=n}
        lam=partition_parts(m0,m1,unused)
        k=len(rungs);h=(n-k)//2
        deg_expected=2*h*(h-1)+comb(k,2)+lam.count(1)
        types[(k,lam)]+=1
        deg_by_type[(k,lam)]=deg_expected
        for p in range(len(m)):
            a,b=m[p]
            for q in range(p+1,len(m)):
                c,d=m[q]
                for f,g in (((a,c),(b,d)),((a,d),(b,c))):
                    u,v=sorted(f);s,t=sorted(g)
                    if v in neighbors[u] and t in neighbors[s]:
                        dest=tuple(sorted(tuple(e for j,e in enumerate(m) if j not in (p,q))+((u,v),(s,t))))
                        assert dest in pos
                        adj[i].add(pos[dest])
        assert len(adj[i]) == deg_expected,(n,k,lam,len(adj[i]),deg_expected)
    for i,row in enumerate(adj):
        for j in row:assert i in adj[j]
    reached={0};queue=[0]
    for i in queue:
        for j in adj[i]:
            if j not in reached:
                reached.add(j);queue.append(j)
    assert len(reached)==len(states)
    for key,count in types.items():
        k,lam=key
        assert count==expected_size(n,k,lam),(key,count,expected_size(n,k,lam))
    count_formula=sum(comb(n,n-2*h)*doublefac_odd(h)**2 for h in range(n//2+1))
    edge_formula=sum((h*(h-1)+comb(n-2*h,2))*comb(n,n-2*h)*doublefac_odd(h)**2 for h in range(n//2+1))
    edges=sum(map(len,adj))//2
    assert len(states)==count_formula and edges==edge_formula
    return dict(n=n,matchings=len(states),flip_edges=edges,connected=True,orbit_count=len(types),orbit_counts=[dict(rungs=k,partition=list(lam),size=types[(k,lam)],degree=deg_by_type[(k,lam)]) for k,lam in sorted(types, key=lambda z:(-z[0],z[1]))], degree_distribution=dict(sorted(collections.Counter(map(len,adj)).items())))

if __name__=='__main__':
    for n in range(3,8):
        print(json.dumps(run(n),separators=(',',':'),sort_keys=True))
