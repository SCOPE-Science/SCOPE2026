#!/usr/bin/env python3
"""Independent combinatorial construction of the row/column optimum families.
Checks each allowed coordinate slide using integer bit masks and shortest paths.
"""
from itertools import permutations,product
from collections import deque,Counter
from math import factorial


def build(n):
    rowstates=set()
    colstates=set()
    for missing in range(n):
        available=[i for i in range(n) if i!=missing]
        for cols in product(range(n),repeat=n-1):
            rowstates.add(sum(1<<(n*i+j) for i,j in zip(available,cols)))
        for rows in product(range(n),repeat=n-1):
            colstates.add(sum(1<<(n*i+j) for i,j in zip(rows,available)))
    union=sorted(rowstates|colstates)
    locator={s:i for i,s in enumerate(union)}
    adj=[[] for _ in union]
    for i,ss in enumerate(union):
        bits=[j for j in range(n*n) if ss & (1<<j)]
        nbr=set()
        for v in bits:
            removed=ss^(1<<v)
            for w in range(n*n):
                if (ss >> w)&1 or (v//n!=w//n and v%n!=w%n):continue
                other=removed|(1<<w)
                if other in locator:nbr.add(locator[other])
        adj[i]=sorted(nbr)
    return union,adj,rowstates,colstates,locator


def shortest(adj,source):
    d=[-1]*len(adj);d[source]=0;q=deque([source])
    while q:
        i=q.popleft()
        for j in adj[i]:
            if d[j]<0:d[j]=d[i]+1;q.append(j)
    return d


def starpair(n,r,c):
    a=sum(1<<(n*i+c) for i in range(n) if i!=r)
    b=sum(1<<(n*r+j) for j in range(n) if j!=c)
    return a,b


def main():
    for n in range(3,6):
        states,adj,rows,cols,loc=build(n)
        k=n-1
        assert len(rows)==len(cols)==n**n
        assert len(rows&cols)==n*n*factorial(k)
        assert len(states)==2*n**n-n*n*factorial(k)
        assert sum(map(len,adj))//2==n*k*(n**n-factorial(n))
        # For n<=4, entire all-pairs diameter spectrum; n=5, all star sources.
        chosen=range(len(states)) if n<=4 else sorted({loc[starpair(n,r,c)[0]] for r in range(n) for c in range(n)})
        extrema=Counter()
        for src in chosen:
            dist=shortest(adj,src)
            assert min(dist)==0 and max(dist)<=2*k
            for dest,dd in enumerate(dist):
                if dd==2*k: extrema[tuple(sorted((src,dest)))]+=1
        true={tuple(sorted((loc[a],loc[b]))) for r in range(n) for c in range(n) for a,b in [starpair(n,r,c)]}
        assert set(extrema)==true
        print('structural:',n, 'states',len(states),'slides',sum(map(len,adj))//2,
              'diameter',2*k,'antipodes',len(extrema),'source_count',len(chosen),flush=True)
    print('STRUCTURAL_VERIFY_OK')

if __name__=='__main__':main()
