#!/usr/bin/env python3
"""Independent explicit-vertex test of secure domination in Mycielski bicliques.
Use outside-vertex guard swaps on the actual Mycielski adjacency relation;
no occupancy-profile algebra is used in this test.
"""
from itertools import combinations
from math import comb

def adjacency(m,n):
    # 0..m+n-1 original vertices; m+n..2*(m+n)-1 shadows; final apex
    q=m+n;N=2*q+1;adj=[set()for _ in range(N)]
    def edge(x,y):adj[x].add(y);adj[y].add(x)
    for i in range(m):
        for j in range(m,q):
            edge(i,j);edge(i,q+j);edge(q+i,j)
    for i in range(q):edge(2*q,q+i)
    return adj

def sdom(s,adj):
    N=len(adj);chosen=set(s)
    return all(i in chosen or any(j in chosen for j in adj[i]) for i in range(N))

def swap_secure(s,adj):
    S=set(s)
    if not sdom(S,adj):return False
    for v in range(len(adj)):
        if v not in S:
            if not any(sdom((S-{u})|{v},adj) for u in (S&adj[v])):
                return False
    return True

def direct(m,n):
    adj=adjacency(m,n);counts={}
    q=m+n
    classes=[set(range(m)),set(range(m,q)),set(range(q,q+m)),{2*q},set(range(q+m,2*q))]
    for k in (3,4,5):
        good=0;profiles={}
        for s in combinations(range(2*q+1),k):
            if swap_secure(s,adj):
                good+=1
                t=tuple(sum(x in cls for x in s) for cls in classes)
                profiles[t]=profiles.get(t,0)+1
        counts[k]=(good,profiles)
    return counts

def theoretical(m,n):
    return m*m*n*n + m*m*comb(n,2) + n*n*comb(m,2) + (m+n+1)*comb(m,2)*comb(n,2)

for m,n in [(5,5),(5,6),(6,6),(5,7),(6,7)]:
    res=direct(m,n)
    print((m,n),'sizes',*[f'{k}:{res[k][0]}'for k in (3,4,5)],'predicted',theoretical(m,n))
    assert res[3][0]==res[4][0]==0
    assert res[5][0]==theoretical(m,n)
    if m==5 and n==5: print('patterns',sorted(res[5][1]))
print('DIRECT_VERIFY_OK')
