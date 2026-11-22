#!/usr/bin/env python3
"""Exact independent 4096-state indegree-peeling census on GP(6,2).
All integers come from complete finite loops, not sampled trajectories.
"""
from collections import Counter, deque

N = 12
SIZE = 1 << N
neighbors = [set() for _ in range(N)]
for i in range(6):
    edges = ((i, (i+1)%6), (i, 6+i), (6+i, 6+(i+2)%6))
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
assert all(len(s)==3 for s in neighbors)
assert sum(len(s) for s in neighbors)//2==18

# One synchronous open-neighbor, degree-three majority update.
def step(state):
    result=0
    for i, ns in enumerate(neighbors):
        if sum((state >> j) & 1 for j in ns) >= 2:
            result |= 1 << i
    return result

successor = [step(x) for x in range(SIZE)]
indegree = [0]*SIZE
for v in successor: indegree[v] += 1
queue = deque(i for i,d in enumerate(indegree) if d==0)
peel = []
while queue:
    x=queue.popleft();peel.append(x)
    y=successor[x];indegree[y]-=1
    if indegree[y]==0:queue.append(y)
root=[-1]*SIZE
entry=[-1]*SIZE
period=[0]*SIZE
cycles=[]
for s in range(SIZE):
    if indegree[s] == 0 or root[s] != -1:continue
    cyc=[]; x=s
    while root[x] == -1:
        root[x]=-2;cyc.append(x);x=successor[x]
    assert x==s and len(cyc) in (1,2)
    rep=min(cyc)
    for c in cyc:
        root[c]=rep;entry[c]=0;period[c]=len(cyc)
    cycles.append(tuple(cyc))
for x in reversed(peel):
    y=successor[x]
    root[x],entry[x],period[x]=root[y],entry[y]+1,period[y]
assert all(0<=root[x]<SIZE and entry[x]>=0 and period[x] in (1,2) for x in range(SIZE))
basins=Counter(root)
first=Counter(entry)
byperiod={p:Counter(entry[i] for i in range(SIZE) if period[i]==p) for p in (1,2)}
basis={p:Counter(basins[min(c)] for c in cycles if len(c)==p) for p in (1,2)}
assert Counter(map(len,cycles)) == {1:14,2:184}
assert dict(sorted(first.items())) == {0:382,1:1278,2:1140,3:768,4:432,5:96}
assert dict(sorted(byperiod[1].items())) == {0:14,1:192,2:360,3:528,4:384,5:96}
assert dict(sorted(byperiod[2].items())) == {0:368,1:1086,2:780,3:240,4:48}
assert dict(sorted(basis[1].items())) == {1:2,8:6,13:4,736:2}
assert dict(sorted(basis[2].items())) == {2:42,4:24,6:27,10:24,12:12,14:12,16:3,21:24,26:2,70:12,92:2}
assert basins[0]==basins[SIZE-1]==736
assert sum(n*mult for n,mult in Counter(basins.values()).items())==SIZE
# D6, the full automorphism group: rotations and reflections of the outer ring
# induce the same index maps on the two inner triangles and spokes.
perms=[]
for sign in (-1,1):
    for shift in range(6):
        p=tuple((6*(j//6)+(shift+sign*(j%6))%6) for j in range(N))
        assert all(set(p[t] for t in neighbors[j]) == neighbors[p[j]] for j in range(N))
        perms.append(p)
assert len(set(perms))==12

def permute(x,p):
    return sum(((x>>i)&1)<<p[i] for i in range(N))
fixrep=Counter()
tworep=Counter()
for c in cycles:
    if len(c)==1:
        fixrep[min(permute(c[0],p) for p in perms)] += 1
    else:
        tworep[min(tuple(sorted((permute(c[0],p),permute(c[1],p)))) for p in perms)] += 1
assert len(fixrep)==7
assert len(tworep)==31
assert Counter(tworep.values())=={1:2,2:1,3:4,6:20,12:4}
assert Counter(fixrep.values())=={1:4,2:2,6:1}
# Burnside independently checks both geometric orbit counts.
burnside_fixed=sum(sum(permute(c[0],p)==c[0] for c in cycles if len(c)==1) for p in perms)
burnside_two=sum(sum(set((permute(c[0],p),permute(c[1],p)))==set(c)
                     for c in cycles if len(c)==2) for p in perms)
assert burnside_fixed==12*len(fixrep)==84
assert burnside_two==12*len(tworep)==372
assert basins[63]==basins[4032]==1
assert {x for x in range(SIZE) if entry[x]==5} and len([x for x in range(SIZE) if entry[x]==5])==96
assert successor[79] != 79 and entry[79]==5
print('GRAPH=GP(6,2) V=12 E=18 AUT=12 STATES=4096')
print('CYCLES fixed=14 two=184; symmetry_classes fixed=7 two=31')
print('ENTRY', sorted(first.items()))
print('ENTRY_BY_PERIOD', {p:sorted(v.items()) for p,v in byperiod.items()})
print('BASINS_BY_PERIOD', {p:sorted(v.items()) for p,v in basis.items()})
print('BASIN_TOTAL', sorted(Counter(basins.values()).items()))
print('CONSENSUS_BASINS', basins[0],basins[SIZE-1])
print('ISOLATED_FIXED', sorted(c[0] for c in cycles if len(c)==1 and basins[c[0]]==1))
print('MAX_ENTRY_EXAMPLE', 79, 'steps',entry[79])
print('ALL CHECKS PASSED')
