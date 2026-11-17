#!/usr/bin/env python3
"""Cross-check the census using the outer pentagon, spokes and inner star model."""
from collections import Counter

adj = [set() for _ in range(10)]
for i in range(5):
    edges = ((i,(i+1)%5),(i,i+5),(5+i,5+(i+2)%5))
    for a,b in edges:
        adj[a].add(b)
        adj[b].add(a)
assert sum(map(len,adj)) == 30 and all(len(s)==3 for s in adj)

def next_state(i):
    current=[];z=i
    for _ in range(10):
        current.append(z%3);z//=3
    future=[]
    for j in range(10):
        x=current[j]
        if x==0: future.append(int(1 in (current[k] for k in adj[j])))
        elif x==1: future.append(2)
        else:future.append(0)
    return sum(v*(3**j) for j,v in enumerate(future))

F=[next_state(i) for i in range(3**10)]
T=[-1]*len(F);P=[0]*len(F);orb=Counter()
for start in range(len(F)):
    if T[start]>=0:continue
    seen={};seq=[];s=start
    while T[s]<0 and s not in seen:
        seen[s]=len(seq);seq.append(s);s=F[s]
    if s in seen:
        k=seen[s];p=len(seq)-k;orb[p]+=1
        for v in seq[k:]:T[v]=0;P[v]=p
        seq=seq[:k]
    for v in reversed(seq):
        T[v]=1+T[F[v]];P[v]=P[F[v]]
C=Counter(zip(T,P))
assert orb==Counter({1:1,3:80,4:60,5:30,8:60})
assert max(T)==6 and C[(6,3)]==120 and sum(C.values())==3**10
assert [sum(v for (t,p),v in C.items() if t==i) for i in range(7)]==[1111,9533,21193,14492,11760,840,120]
print('OUTER_INNER_OK total=59049 cycles='+repr(sorted(orb.items()))+' entry_layer_sizes='+repr([sum(v for (t,p),v in C.items() if t==i) for i in range(7)]))
