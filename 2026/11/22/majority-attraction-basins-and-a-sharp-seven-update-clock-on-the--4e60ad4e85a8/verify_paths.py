#!/usr/bin/env python3
"""Independent exhaustive successor-path classification for majority on mu(C5)."""
from collections import Counter
from itertools import product

N=11
adj=[set() for _ in range(N)]
def connect(i,j):
    adj[i].add(j); adj[j].add(i)
for i in range(5):
    connect(i,(i+1)%5)
    connect(5+i,(i-1)%5)
    connect(5+i,(i+1)%5)
    connect(10,5+i)
assert sum(map(len,adj))//2 == 20
mask=[sum(1<<j for j in nbr) for nbr in adj]

def successor(x):
    y=0
    for i in range(N):
        k=(x&mask[i]).bit_count()
        old=(x>>i)&1
        if 2*k>len(adj[i]) or (2*k==len(adj[i]) and old):
            y|=1<<i
    return y
F=[successor(x) for x in range(1<<N)]
depth=[None]*len(F); period=[None]*len(F); root=[None]*len(F)
for x in range(len(F)):
    if depth[x] is not None: continue
    walked=[]; seen={}; y=x
    while depth[y] is None and y not in seen:
        seen[y]=len(walked);walked.append(y);y=F[y]
    if depth[y] is None:
        start=seen[y]
        cyc=tuple(sorted(walked[start:]))
        for z in walked[start:]:
            depth[z]=0;period[z]=len(cyc);root[z]=cyc
    else:
        start=len(walked)
    for z in reversed(walked[:start]):
        depth[z]=depth[F[z]]+1
        period[z]=period[F[z]]
        root[z]=root[F[z]]
counts=Counter((depth[x],period[x]) for x in range(len(F)))
expected={(0,1):22,(0,2):70,(1,1):262,(1,2):130,(2,1):594,(2,2):10,(3,1):290,(4,1):280,(5,1):230,(6,1):130,(7,1):30}
assert counts==expected,(counts,expected)
basins=Counter(root)
assert Counter(basins[o] for o in basins if len(o)==1)=={1:10,6:10,884:2}
assert Counter(basins[o] for o in basins if len(o)==2)=={2:5,4:10,6:10,10:10}
assert sum(len(o)==1 for o in basins)==22
assert sum(len(o)==2 for o in basins)==35
assert max(depth)==7
assert sum(depth[x]==7 for x in range(len(F)))==30
assert all(root[x] in [(0,),((1<<N)-1,)] for x in range(len(F)) if depth[x]==7)
assert sum(basins[(v,)] for v in [0,(1<<N)-1])==1768
# Check stated symmetry and complement invariance of entire successor graph.
def permute(state,k=0,reflection=False,flip=False):
    r=0
    for i in range(5):
        j=(((-i) if reflection else i)+k)%5
        r|=((state>>i)&1)<<j
        r|=((state>>(5+i))&1)<<(5+j)
    r|=(state>>10&1)<<10
    if flip:r^=(1<<N)-1
    return r
for k,reflection,flip in product(range(5),[False,True],[False,True]):
    for x in range(len(F)):
        assert F[permute(x,k,reflection,flip)]==permute(F[x],k,reflection,flip)
classes=[]; unseen=set(basins)
while unseen:
    orb=min(unseen)
    family={tuple(sorted(permute(x,k,r,f) for x in orb)) for k,r,f in product(range(5),[False,True],[False,True])}
    assert family<=unseen
    assert len({basins[o] for o in family})==1
    classes.append((len(orb),len(family),basins[orb]))
    unseen-=family
assert Counter(classes)=={(1,2,884):1,(1,10,6):1,(1,10,1):1,(2,5,2):1,(2,10,4):1,(2,10,6):1,(2,10,10):1}
print('VERIFY_PATHS_OK', len(F), sorted(([d,p,c] for (d,p),c in counts.items())), sorted(Counter(classes).items()))
