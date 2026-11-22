#!/usr/bin/env python3
"""Exact complete-graph matching-slide geometry (stdlib only)."""
from collections import deque, defaultdict, Counter
from functools import lru_cache
from math import factorial
from itertools import combinations

@lru_cache(None)
def all_perfect_matchings(V):
    if not V: return ((),)
    a = V[0]; out=[]
    for b in V[1:]:
        R=tuple(v for v in V[1:] if v!=b)
        for t in all_perfect_matchings(R):
            out.append((tuple(sorted((a,b))),)+t)
    return tuple(out)

def all_two_hole_matchings(n):
    for holes in combinations(range(n),2):
        for m in all_perfect_matchings(tuple(v for v in range(n) if v not in holes)):
            yield tuple(sorted(m))

def adjacent(M,n):
    holes = list(set(range(n)) - {v for e in M for v in e})
    for i,(a,b) in enumerate(M):
        for h in holes:
            for s in (a,b):
                yield tuple(sorted(M[:i]+M[i+1:]+(tuple(sorted((s,h))),)))

def predicted(M,N,n):
    D=set(M)^set(N)
    graph=defaultdict(list)
    for a,b in D:
        graph[a].append(b); graph[b].append(a)
    comp={}; cycles=0
    for v in graph:
        if v in comp: continue
        stack=[v]; seen=[]
        while stack:
            z=stack.pop()
            if z in comp:continue
            comp[z]=v; seen.append(z)
            stack.extend(graph[z])
        if all(len(graph[z])==2 for z in seen):cycles+=1
    holes = list(set(range(n)) - {x for e in M for x in e})
    surcharge=int(holes[0] in comp and holes[1] in comp and comp[holes[0]]==comp[holes[1]])
    return len(set(N)-set(M))+cycles+surcharge,cycles,surcharge

def main():
    for k in range(1,6):
        n=2*k+2
        states=list(all_two_hole_matchings(n)); ids={M:i for i,M in enumerate(states)}
        V=factorial(n)//(2**(k+1)*factorial(k))
        assert len(states)==len(ids)==V
        d=[-1]*V; d[0]=0;queue=deque([0]);edges=0
        while queue:
            i=queue.popleft()
            neigh=list(adjacent(states[i],n))
            assert len(neigh)==len(set(neigh))==4*k
            edges+=len(neigh)
            for N in neigh:
                j=ids[N]
                if d[j]<0:d[j]=d[i]+1;queue.append(j)
        assert min(d)>=0 and edges==4*k*V
        same_hole=0; delta_count=0
        holes_src=set(range(n))-{v for e in states[0] for v in e}
        for j,N in enumerate(states):
            expected,c,delta=predicted(states[0],N,n)
            assert d[j]==expected,(k,j,d[j],expected,c,delta)
            delta_count+=delta
            if set(range(n))-{v for e in N for v in e} == holes_src:
                same_hole+=1
                assert delta==0
        assert same_hole==factorial(2*k)//(2**k*factorial(k))
        assert max(d)==(3*k+1)//2, (k,max(d))
        print(f'n={n} k={k} states={V} edges={edges//2} degree={4*k} '
              f'same_hole={same_hole} delta_one={delta_count} diameter={max(d)} ALL_PAIR_OK')
    print('VERIFY_SLIDE_OK')
if __name__=='__main__':main()
