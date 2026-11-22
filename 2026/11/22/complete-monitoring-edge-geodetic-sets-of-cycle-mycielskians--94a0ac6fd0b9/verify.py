#!/usr/bin/env python3
"""Standalone exhaustive checks of cycle-Mycielski monitoring formulas.

Uses no nonstandard packages. A pair monitors an edge precisely when its
shortest-path distance increases upon deleting that edge.
"""
from collections import Counter
from itertools import combinations
from math import comb, ceil


def graph(n):
    N = 2*n + 1
    edges = set()
    def edge(a,b):
        if a > b: a,b=b,a
        edges.add((a,b))
    for i in range(n):
        edge(i,(i+1)%n)
        edge(n+i,(i-1)%n)
        edge(n+i,(i+1)%n)
        edge(n+i,2*n)
    return N,sorted(edges)


def distances(N,edges):
    adj=[[] for _ in range(N)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    out=[]
    for root in range(N):
        d=[N+2]*N; d[root]=0; q=[root]
        for x in q:
            for y in adj[x]:
                if d[y]>N:
                    d[y]=d[x]+1;q.append(y)
        out.append(d)
    return out


def monitor_pair_masks(N,edges):
    base=distances(N,edges)
    checks=[]
    for j,e in enumerate(edges):
        dropped=distances(N,edges[:j]+edges[j+1:])
        p=[(1<<u)|(1<<v) for u in range(N) for v in range(u+1,N)
           if dropped[u][v]>base[u][v]]
        assert p,(N,e)
        checks.append(p)
    return checks


def is_monitor(mask,checks):
    return all(any((mask & p)==p for p in ps) for ps in checks)


def expected_all(n):
    out=Counter()
    for k in range(n//2+1):
        a=n*comb(n-k,k)//(n-k)
        assert a*(n-k)==n*comb(n-k,k)
        out[2*n-k]+=a
        out[2*n-k+1]+=a
    return out


def expected_minimal(n):
    out=Counter()
    for k in range((n+2)//3,n//2+1):
        a=n*comb(k,n-2*k)//k
        assert a*k==n*comb(k,n-2*k)
        out[2*n-k]+=a
    return out


def independently_expected(mask,n):
    all_shadows=((1<<n)-1)<<n
    if mask&all_shadows != all_shadows: return False
    return all((mask>>i)&1 or (mask>>((i+1)%n))&1 for i in range(n))


def exchange_shape(opts,n):
    adj={a:[] for a in opts};slides={a:[] for a in opts}
    E=set(graph(n)[1])
    for a,b in combinations(opts,2):
        diff=a^b
        if diff.bit_count()!=2:continue
        adj[a].append(b);adj[b].append(a)
        u,v=[i for i in range(2*n+1) if (diff>>i)&1]
        if (min(u,v),max(u,v)) in E:
            slides[a].append(b);slides[b].append(a)
    assert adj==slides,(n,'jump differs from slide')
    if n%2:
        assert len(opts)==n
        assert all(len(adj[a])==2 for a in opts)
        seen={opts[0]}; todo=[opts[0]]
        for a in todo:
            for b in adj[a]:
                if b not in seen:seen.add(b);todo.append(b)
        assert len(seen)==n
    else:
        assert len(opts)==2 and all(not adj[a] for a in opts)


def run():
    for n in range(5,10):
        N,E=graph(n)
        checks=monitor_pair_masks(N,E)
        counts=Counter(); all_valid=set(); opts=[]
        for mask in range(1<<N):
            got=is_monitor(mask,checks)
            expected=independently_expected(mask,n)
            assert got==expected,(n,mask,got,expected)
            if got:
                counts[mask.bit_count()]+=1
                all_valid.add(mask)
        assert counts==expected_all(n),(n,counts,expected_all(n))
        minimal=Counter()
        for mask in all_valid:
            if not any((mask^(1<<v)) in all_valid for v in range(N) if (mask>>v)&1):
                minimal[mask.bit_count()]+=1
        assert minimal==expected_minimal(n),(n,minimal,expected_minimal(n))
        k=min(counts)
        opts=[mask for mask in all_valid if mask.bit_count()==k]
        exchange_shape(opts,n)
        print('n=',n,'all=',dict(sorted(counts.items())),
              'minimal=',dict(sorted(minimal.items())),
              'optima=',len(opts),'jump-slide=',('cycle' if n%2 else 'two isolated'))
    # Larger graphs: compare all edge-monitor pairs with the local forcing certificates,
    # independently of the set-enumeration assertions above.
    for n in range(10,16):
        N,E=graph(n);ps=monitor_pair_masks(N,E)
        d={e: [p for p in pairs] for e,pairs in zip(E,ps)}
        for i in range(n):
            e=tuple(sorted((i,n+(i+1)%n)))
            want=sorted([(1<<i)|(1<<(n+(i+1)%n)),
                         (1<<((i-1)%n))|(1<<(n+(i+1)%n))])
            assert sorted(d[e])==want,(n,i,d[e],want)
        print('n=',n,'shadow-edge pair table verified')
    print('VERIFY_OK')

if __name__=='__main__':run()
