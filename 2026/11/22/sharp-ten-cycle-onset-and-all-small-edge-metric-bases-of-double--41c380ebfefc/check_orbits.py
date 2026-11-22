#!/usr/bin/env python3
"""Six orbits of the 160 minimum three-landmark edge bases in DP(10,1)."""
from collections import deque
from itertools import combinations

n=10
N=4*n
E=set()
def add(a,b): E.add(tuple(sorted((a,b))))
for i in range(n):
    j=(i+1)%n
    add(i,j); add(3*n+i,3*n+j)
    add(i,n+i); add(2*n+i,3*n+i)
    add(n+i,2*n+j); add(2*n+i,n+j)
edges=sorted(E)
adj=[[] for _ in range(N)]
for a,b in edges:adj[a].append(b);adj[b].append(a)
D=[]
for s in range(N):
    ds=[N+1]*N;ds[s]=0
    q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if ds[y]>ds[x]+1:ds[y]=ds[x]+1;q.append(y)
    D.append(ds)
code=[[min(D[s][a],D[s][b]) for a,b in edges] for s in range(N)]
bases=set()
for T in combinations(range(N),3):
    if len(set(zip(*(code[v] for v in T))))==len(edges):bases.add(T)
assert len(bases)==160

def transform(v, shift, reflection, interchange):
    layer,i=divmod(v,n)
    if interchange:layer=3-layer
    if reflection:i=(-i)%n
    return layer*n+(i+shift)%n

orbits=[]
while bases:
    representative=min(bases)
    orb={tuple(sorted(transform(v,s,r,t) for v in representative))
         for s in range(n) for r in (0,1) for t in (0,1)}
    assert orb <= bases
    orbits.append((representative,len(orb)))
    bases.difference_update(orb)
assert len(orbits)==6
assert sorted(sz for _,sz in orbits)==[20,20,20,20,40,40]
print('representative (x:0..9,u:10..19,v:20..29,y:30..39)\torbit_size')
for rep,k in orbits: print(f'{rep}\t{k}')
print('total\t',sum(k for _,k in orbits))
