#!/usr/bin/env python3
"""Independent shortest-path exact-cover checks for perfect geodesic packings.

For each graph, all-pairs graph distances identify maximal geodesics;
an exact-cover recursion then enumerates vertex-disjoint path systems.  A
separate permutation-cycle calculation independently checks the theorem.
"""
from collections import Counter,deque
from itertools import permutations
from math import factorial

def cycle_lengths(p):
    n=len(p);seen=set();lengths=[]
    for i in range(n):
        if i not in seen:
            cur=i;ell=0
            while cur not in seen:
                seen.add(cur);cur=p[cur];ell+=1
            lengths.append(ell)
    return lengths

def expected_cycle_distribution(n):
    out=Counter()
    for p in permutations(range(n)):
        lengths=cycle_lengths(p)
        weight=1
        for ell in lengths:weight*=2**ell+2*(-1)**ell
        if weight:out[len(lengths)]+=weight
    return out

def direct(n):
    N=3*n
    adjacent=[[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i!=j and (i//n==j//n or i%n==j%n):adjacent[i].append(j)
    def distances(s):
        d=[N+1]*N;d[s]=0;q=deque([s])
        while q:
            x=q.popleft()
            for y in adjacent[x]:
                if d[y]>d[x]+1:d[y]=d[x]+1;q.append(y)
        return d
    d=[distances(i) for i in range(N)]
    # Independently construct all maximal geodesics (diameter is 2).
    paths=set()
    for u in range(N):
        for v in range(u+1,N):
            if d[u][v]!=2:continue
            for w in range(N):
                if d[u][w]==d[w][v]==1:
                    paths.add((1<<u)|(1<<v)|(1<<w))
    supports=[[] for _ in range(N)]
    pivot_target={}
    for path in paths:
        cells=[i for i in range(N) if (path>>i)&1]
        column_counts=Counter(i%n for i in cells)
        assert sorted(column_counts.values())==[1,2]
        pivot=next(c for c,k in column_counts.items() if k==2)
        target=next(c for c,k in column_counts.items() if k==1)
        pivot_target[path]=(pivot,target)
        for i in cells:supports[i].append(path)
    counts=Counter();full=(1<<N)-1
    def recurse(uncovered,selected):
        if uncovered==0:
            p=[-1]*n
            for path in selected:
                i,j=pivot_target[path];assert p[i]==-1;p[i]=j
            assert sorted(p)==list(range(n))
            counts[len(cycle_lengths(p))]+=1
            return
        chosen=min((i for i in range(N) if (uncovered>>i)&1),key=lambda a:sum((uncovered&v)==v for v in supports[a]))
        for path in supports[chosen]:
            if (uncovered&path)==path:recurse(uncovered^path,selected+[path])
    recurse(full,[])
    expected=expected_cycle_distribution(n)
    scalar=factorial(n)*(4*2**n+(3*n+5)*(-1)**n)//9
    assert counts==expected,(n,counts,expected)
    assert sum(counts.values())==scalar,(n,counts,scalar)
    return n,len(paths),sum(counts.values()),dict(sorted(counts.items()))

if __name__=='__main__':
    for n in range(2,8):print('GRAPH_OK',*direct(n),flush=True)
    print('VERIFY_OK direct_shortest_paths=PASS disjoint_exact_covers=PASS cycle_count_distribution=PASS closed_formula=PASS')
