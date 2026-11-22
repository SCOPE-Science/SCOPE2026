#!/usr/bin/env python3
"""Independent non-dynamical check of extinction using 1-form cycle sums.

Uses the irrotationality criterion for three-color Greenberg-Hastings dynamics
on finite connected graphs, in Gravner--Lyu--Sivakoff (2016), Theorem 3.
"""
from collections import deque
n=11
# 0..4 originals, 5..9 copies, 10 apex
adj=[set() for _ in range(n)]
for i in range(5):
    for j in ((i+1)%5,5+(i-1)%5,5+(i+1)%5):
        adj[i].add(j);adj[j].add(i)
    adj[10].add(5+i);adj[5+i].add(10)

parent=[-1]*n;parent[0]=0
q=deque([0]);tree=set()
while q:
    x=q.popleft()
    for y in sorted(adj[x]):
        if parent[y]<0:
            parent[y]=x;q.append(y)
            tree.add(tuple(sorted((x,y))))
assert len(tree)==n-1
all_edges={tuple(sorted((x,y))) for x in range(n) for y in adj[x]}
chords=sorted(all_edges-tree)
assert len(chords)==10

def walk_to_root(x):
    out=[x]
    while x!=0:
        x=parent[x];out.append(x)
    return out

def fundamental_cycle(a,b):
    A=walk_to_root(a); B=walk_to_root(b)
    shared=set(A)&set(B)
    lca=next(x for x in A if x in shared)
    A=A[:A.index(lca)+1]
    B=B[:B.index(lca)+1]
    return A+list(reversed(B[:-1]))+[a]
cycles=[fundamental_cycle(a,b) for a,b in chords]
assert all(all(v in adj[u] for u,v in zip(c,c[1:])) for c in cycles)

# GHM antisymmetric excitation 1-form: +1 on 0->1, -1 on 1->0.
def circulation(c,col):
    return sum((col[u]==0 and col[v]==1)-(col[u]==1 and col[v]==0) for u,v in zip(c,c[1:]))

count=0
for s in range(3**n):
    t=s;col=[]
    for _ in range(n):
        t,r=divmod(t,3);col.append(r)
    if all(circulation(c,col)==0 for c in cycles): count+=1
assert count==13887,count
print('PASS independent 1-form cycle-basis extinction check: 13887 of 177147 configurations, 10 fundamental cycles')
