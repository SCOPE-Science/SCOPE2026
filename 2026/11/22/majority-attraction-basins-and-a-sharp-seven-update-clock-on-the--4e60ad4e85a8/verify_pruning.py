#!/usr/bin/env python3
"""Independent indegree-removal and reverse-edge basin calculation on an explicit graph."""
from collections import Counter,deque
# Edges written independently, rather than applying the Mycielski construction algorithm.
edges=[(0,1),(1,2),(2,3),(3,4),(4,0),
       (5,1),(5,4),(6,0),(6,2),(7,1),(7,3),(8,2),(8,4),(9,0),(9,3),
       (10,5),(10,6),(10,7),(10,8),(10,9)]
M=1<<11
nbr=[[] for _ in range(11)]
for u,v in edges:
    nbr[u].append(v);nbr[v].append(u)
assert len(edges)==20

def f(s):
    ans=0
    for u,js in enumerate(nbr):
        tally=sum(1 if (s>>j)&1 else -1 for j in js)
        v=int(tally>0 or (tally==0 and bool((s>>u)&1)))
        ans|=v<<u
    return ans
next_state=[f(s) for s in range(M)]
indeg=[0]*M
for q in next_state:indeg[q]+=1
Q=deque(i for i in range(M) if indeg[i]==0)
removed=[]
while Q:
    u=Q.popleft();removed.append(u)
    v=next_state[u];indeg[v]-=1
    if indeg[v]==0:Q.append(v)
cycle_id=[-1]*M; depth=[-1]*M; period=[-1]*M; cycles=[]
for u in range(M):
    if indeg[u]==0 or cycle_id[u]>=0:continue
    cyc=[];v=u
    while cycle_id[v]<0:
        cycle_id[v]=len(cycles);depth[v]=0;cyc.append(v);v=next_state[v]
    assert v==u
    for w in cyc:period[w]=len(cyc)
    cycles.append(cyc)
for u in reversed(removed):
    v=next_state[u]
    cycle_id[u]=cycle_id[v];depth[u]=1+depth[v];period[u]=period[v]
assert all(p>0 and d>=0 for p,d in zip(period,depth))
C=Counter((d,p) for d,p in zip(depth,period))
assert sorted(C.items())==sorted({(0,1):22,(0,2):70,(1,1):262,(1,2):130,(2,1):594,(2,2):10,(3,1):290,(4,1):280,(5,1):230,(6,1):130,(7,1):30}.items())
B=Counter(cycle_id)
assert Counter((len(cycles[i]), B[i]) for i in range(len(cycles))) == {(1,1):10,(1,6):10,(1,884):2,(2,2):5,(2,4):10,(2,6):10,(2,10):10}
assert len(cycles)==57 and len(removed)==M-92
assert all(next_state[next_state[next_state[next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]]]]]==next_state[next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]]] for x in range(M)) # F^9=F^7
assert any(next_state[next_state[next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]]]]!=next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]] for x in range(M)) # F^8 != F^6
print('VERIFY_PRUNING_OK',len(cycles),len(removed),sorted(C.items()), Counter((len(cycles[i]),B[i]) for i in range(len(cycles))))
