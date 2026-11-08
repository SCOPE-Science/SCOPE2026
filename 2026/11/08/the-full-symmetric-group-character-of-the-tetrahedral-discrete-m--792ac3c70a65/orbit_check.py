#!/usr/bin/env python3
"""Independent orbit-block Euler characteristic for tetrahedral Morse matching complex."""
from itertools import permutations
from collections import Counter
F=range(1,16)
E=tuple((a,b) for a in F for b in F if a&b==a and b.bit_count()==a.bit_count()+1)
EI={e:i for i,e in enumerate(E)}
facepos={f:i for i,f in enumerate(F)}
ends=[(1<<facepos[a])|(1<<facepos[b]) for a,b in E]

def pmask(mask,p):
    return sum(1<<p[i] for i in range(4) if mask>>i&1)

def perm_edge(j,p):
    a,b=E[j];return EI[(pmask(a,p),pmask(b,p))]

def valid(seq):
    marked=set(seq)
    used=0
    for j in seq:
        if used&ends[j]:return False
        used|=ends[j]
    adj=[[] for _ in F]
    for j,(a,b) in enumerate(E):
        if j in marked:a,b=b,a
        adj[facepos[a]].append(facepos[b])
    indeg=[0]*len(F)
    for row in adj:
        for w in row:indeg[w]+=1
    queue=[i for i in range(len(F)) if indeg[i]==0];n=0
    while queue:
        v=queue.pop();n+=1
        for w in adj[v]:
            indeg[w]-=1
            if indeg[w]==0:queue.append(w)
    return n==len(F)

def orbit_stat(p):
    nxt=[perm_edge(j,p) for j in range(len(E))]
    seen=set();orbs=[]
    for j in range(len(E)):
        if j in seen:continue
        orb=[];cur=j
        while cur not in seen:
            seen.add(cur);orb.append(cur);cur=nxt[cur]
        assert cur==j
        orbs.append(tuple(orb))
    ok_orbs=[]
    for orb in orbs:
        if valid(orb):ok_orbs.append(orb)
    counts=Counter()
    # Count compatible orbit blocks; prune invalid matchings and cycles.
    orbitsets=[]
    def search2(i,selected,blockcount,used):
        if i==len(ok_orbs):
            if blockcount:counts[blockcount]+=1
            return
        search2(i+1,selected,blockcount,used)
        blk=ok_orbs[i]
        bb=0
        for j in blk:bb|=ends[j]
        if bb&used:return
        joined=selected+blk
        if valid(joined):search2(i+1,joined,blockcount+1,used|bb)
    search2(0,(),0,0)
    L=sum((-1)**(k-1)*v for k,v in counts.items())
    return (len(orbs),len(ok_orbs),sorted(counts.items()),L,L-1)

for p in [(0,1,2,3),(1,0,2,3),(1,0,3,2),(1,2,0,3),(1,2,3,0)]:
    print('PERM',p,'ORBIT_EULER',orbit_stat(p))
print('INDEPENDENT_ORBIT_EULER_CHECKS_OK')
