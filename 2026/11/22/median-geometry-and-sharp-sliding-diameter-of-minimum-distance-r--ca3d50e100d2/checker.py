"""Independent exhaustive checks for radius-r path domination sliding results.

Run: python checker.py
No external packages required. Finite checks supplement, not replace, the proof.
"""
from itertools import combinations
from collections import deque
from math import ceil, comb

def dominates(P, r, n):
    return all(any(abs(x-y)<=r for y in P) for x in range(1,n+1))

def gap_vector(P, r, n):
    k=len(P)
    gaps=[P[0]-1]+[P[i+1]-P[i]-1 for i in range(k-1)]+[n-P[-1]]
    capacities=[r]+[2*r]*(k-1)+[r]
    return tuple(c-g for c,g in zip(capacities,gaps))

def expected_number(k,r,d):
    return comb(d+k,k) - (2*comb(d-r-1+k,k) if d>=r+1 else 0)

def expected_diameter(k,r,d):
    if k==1:
        return min(d,2*r-d)
    return k*d-2*max(0,d-r)

def deficit_distance(a,b):
    s=total=0
    for x,y in zip(a[:-1],b[:-1]):
        s += x-y
        total += abs(s)
    return total

def check(r,n):
    k=(n+2*r)//(2*r+1)
    d=(2*r+1)*k-n
    states=[p for p in combinations(range(1,n+1),k) if dominates(p,r,n)]
    expected=expected_number(k,r,d)
    assert len(states)==expected, (r,n,'count',len(states),expected)
    index={p:i for i,p in enumerate(states)}
    g=[gap_vector(p,r,n) for p in states]
    assert len(set(g))==len(states)
    graph=[set() for _ in states]
    for i,p in enumerate(states):
        for j in range(k):
            for direction in [-1,1]:
                q=list(p);q[j]+=direction
                q=tuple(sorted(q))
                if len(set(q))==k and q in index:
                    graph[i].add(index[q])
    assert all(i in graph[j] for i,adj in enumerate(graph) for j in adj)
    diam=0
    for start in range(len(states)):
        distances={start:0};Q=deque([start])
        while Q:
            u=Q.popleft()
            for v in graph[u]:
                if v not in distances:
                    distances[v]=distances[u]+1;Q.append(v)
        assert len(distances)==len(states), (r,n,'disconnected')
        for v,ds in distances.items():
            assert ds==deficit_distance(g[start],g[v]), (r,n,'metric',states[start],states[v],ds,deficit_distance(g[start],g[v]))
            diam=max(diam,ds)
    assert diam==expected_diameter(k,r,d), (r,n,'diameter',diam,expected_diameter(k,r,d))
    return len(states),sum(len(x) for x in graph)//2,diam

if __name__=='__main__':
    cases=0;pair_checks=0
    for r,max_n in [(2,21),(3,22),(4,23),(5,24)]:
        for n in range(1,max_n+1):
            k=(n+2*r)//(2*r+1)
            state_count,edges,diam=check(r,n)
            cases+=1;pair_checks+=state_count*state_count
        print(f'r={r}: n=1..{max_n}, all exact-count, connectivity, all-pairs metric, diameter checks PASS')
    print(f'PASS {cases} parameter cases, {pair_checks} ordered-pair shortest-path checks')
