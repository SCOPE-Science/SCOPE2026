"""Exact exhaustive synchronous majority dynamics on the Herschel graph.
Run: python check_functional.py
Vertices are numbered 1,...,11. Strict majority of neighbors; at ties retain opinion.
"""
from collections import Counter

ADJ = ((2,4,5), (1,3,6,7), (2,4,8), (1,3,9,10),
       (1,6,10), (2,5,11), (2,8,11), (3,7,9),
       (4,8,11), (4,5,11), (6,7,9,10))
N=11
assert all((i+1) in ADJ[j-1] for i,nb in enumerate(ADJ) for j in nb)
assert sum(map(len,ADJ))==36

def update(x):
    y=0
    for i,nb in enumerate(ADJ):
        one=sum((x>>(j-1))&1 for j in nb)
        old=(x>>i)&1
        if 2*one>len(nb): value=1
        elif 2*one<len(nb): value=0
        else:value=old
        y|=value<<i
    return y

trans=[update(x) for x in range(1<<N)]
recurrent={}; depth=[-1]*(1<<N); root=[-1]*(1<<N)
for x in range(1<<N):
    if depth[x]>=0:continue
    path=[];loc={};u=x
    while u not in loc and depth[u]<0:
        loc[u]=len(path);path.append(u);u=trans[u]
    if depth[u]>=0:
        k=root[u]
        for s in reversed(path):
            depth[s]=depth[trans[s]]+1
            root[s]=k
    else:
        cycle=path[loc[u]:]
        k=min(cycle)
        recurrent[k]=tuple(cycle)
        for s in cycle:depth[s]=0;root[s]=k
        for s in reversed(path[:loc[u]]):
            depth[s]=depth[trans[s]]+1
            root[s]=k
assert all(depth[x]>=0 for x in range(1<<N))
assert all(len(c) in (1,2) for c in recurrent.values())
counts=Counter(root)
period={k:len(c) for k,c in recurrent.items()}
assert sum(counts.values())==(1<<N)
assert sum(len(c) for c in recurrent.values())==sum(d==0 for d in depth)

f=Counter(counts[k] for k,c in recurrent.items() if len(c)==1)
t=Counter(counts[k] for k,c in recurrent.items() if len(c)==2)
d=Counter(depth)
j=Counter((depth[x],period[root[x]]) for x in range(1<<N))
assert Counter(period.values())=={1:20,2:61}
assert d=={0:142,1:840,2:466,3:252,4:252,5:48,6:48}
assert f=={1:6,7:12,501:2}
assert t=={4:24,8:12,14:6,25:6,27:12,206:1}
assert counts[0]==counts[(1<<N)-1]==501
assert all(period[root[x]]==1 for x in range(1<<N) if depth[x]>=4)
def iterate(x, t):
    for _ in range(t):
        x = trans[x]
    return x
assert all(iterate(x,8)==iterate(x,6) for x in range(1<<N))
assert any(iterate(x,7)!=iterate(x,5) for x in range(1<<N))
print('PASS: states',1<<N,'fixed',20,'primitive two cycles',61,'sharp entrance',6)
print('first entry time',sorted(d.items()))
print('first entry by eventual period',sorted((k,v) for k,v in j.items()))
print('fixed-point basin sizes',sorted(f.items()))
print('two-cycle basin sizes',sorted(t.items()))
print('unanimity basin sizes',counts[0],counts[(1<<N)-1])
print('maximal-depth count',d[6], 'sample',next(x for x in range(1<<N) if depth[x]==6))
