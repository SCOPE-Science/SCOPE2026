#!/usr/bin/env python3
"""Generate the 56 exceptional classes and 576 seven-curve contraction sets.

The basis is (H,E_1,...,E_7), with intersection form diag(1,-1,...,-1).
All seven simple root reflections act on the exceptional classes by integral isometries.
"""
from itertools import combinations
from collections import Counter

def dot(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
C=[]
for i in range(7):
    v=[0]*8;v[i+1]=1;C.append(tuple(v))
for i,j in combinations(range(7),2):
    v=[1]+[0]*7;v[i+1]=v[j+1]=-1;C.append(tuple(v))
for indices in combinations(range(7),5):
    v=[2]+[0]*7
    for i in indices:v[i+1]=-1
    C.append(tuple(v))
for i in range(7):
    v=[3]+[-1]*7;v[i+1]=-2;C.append(tuple(v))
assert len(C)==56 and len(set(C))==56
K=(-3,)+(1,)*7
assert all(dot(v,v)==-1 and dot(K,v)==-1 for v in C)
roots=[]
for i in range(6):
    v=[0]*8;v[i+1]=1;v[i+2]=-1;roots.append(tuple(v))
roots.append((1,-1,-1,-1,0,0,0,0))
assert all(dot(a,a)==-2 and dot(K,a)==0 for a in roots)
idx={v:i for i,v in enumerate(C)}
generators=[]
for a in roots:
    g=[]
    for v in C:
        j=dot(v,a)
        g.append(idx[tuple(v[k]+j*a[k] for k in range(8))])
    assert sorted(g)==list(range(56)) and all(g[g[i]]==i for i in range(56))
    generators.append(g)
adj=[{j for j,v in enumerate(C) if j!=i and dot(C[i],v)==0} for i in range(56)]
assert Counter(map(len,adj))=={27:56}
sept=[]
def grow(prefix,candidates):
    if len(prefix)==7:
        sept.append(tuple(prefix))
        return
    while candidates:
        i=candidates[0];candidates=candidates[1:]
        grow(prefix+[i],[j for j in candidates if j in adj[i]])
grow([],list(range(56)))
assert len(sept)==576 and len(set(sept))==576
S={t:i for i,t in enumerate(sept)}
for g in generators:
    assert len({S[tuple(sorted(g[j] for j in t))] for t in sept})==576
geiser=[idx[tuple(-K[k]-v[k] for k in range(8))] for v in C]
mate=[S[tuple(sorted(geiser[j] for j in t))] for t in sept]
assert all(mate[i]!=i and mate[mate[i]]==i for i in range(576))
with open('markings.txt','w',encoding='utf8') as out:
    for g in generators:out.write(' '.join(map(str,g))+'\n')
    for t in sept:out.write(' '.join(map(str,t))+'\n')
print('56 exceptional classes; 576 contraction sets; 288 Geiser pairs; seven involutive reflections')
