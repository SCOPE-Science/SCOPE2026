#!/usr/bin/env python3
"""Exhaustive finite-state classification of three-state excitation on the Frucht graph.
Python 3 stdlib only. Prints canonical digest and full census; all states are visited.
"""
import collections
import hashlib
import json
from array import array

EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
V=12
N=3**V
P3=tuple(3**i for i in range(V))
nb=[0]*V
for i,j in EDGES: nb[i]|=1<<j; nb[j]|=1<<i
assert len(EDGES)==18 and all(x.bit_count()==3 for x in nb)

def step(s):
    z=s; excited=0; resting=0; out=0
    for i,weight in enumerate(P3):
        c=z%3; z//=3
        if c==1:excited|=1<<i;out+=2*weight
        elif c==0:resting|=1<<i
    while resting:
        bit=resting&-resting; resting-=bit;i=bit.bit_length()-1
        if nb[i]&excited:out+=P3[i]
    return out

succ=array('i',[0])*N
indeg=array('i',[0])*N
for s in range(N):
    y=step(s);succ[s]=y;indeg[y]+=1
queue=array('i',(i for i in range(N) if indeg[i]==0))
head=0
while head<len(queue):
    s=queue[head];head+=1
    y=succ[s];indeg[y]-=1
    if indeg[y]==0:queue.append(y)
period=array('h',[0])*N
transient=array('h',[0])*N
orbits=collections.Counter()
for s in range(N):
    if indeg[s]>0 and period[s]==0:
        x=s; cyc=[]
        while period[x]==0:
            cyc.append(x);period[x]=-1;x=succ[x]
        assert x==s
        p=len(cyc);orbits[p]+=1
        for x in cyc:period[x]=p
for s in reversed(queue):
    y=succ[s];period[s]=period[y];transient[s]=transient[y]+1
assert all(period) and len(queue)+sum(k*v for k,v in orbits.items())==N
census=collections.Counter((int(transient[s]),int(period[s])) for s in range(N))
assert sum(census.values())==N
max_time=max(transient)
max_states=[s for s in range(N) if transient[s]==max_time]
result={'vertex_count':V,'edges':[list(e) for e in EDGES],
        'total_states':N,'removed_by_peeling':len(queue),
        'primitive_orbits':{str(k):orbits[k] for k in sorted(orbits)},
        'first_entry_maximum':max_time,
        'maximum_entry_states':max_states,
        'entrance_census':[[t,p,c] for (t,p),c in sorted(census.items())]}
encoded=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
print(json.dumps(result,sort_keys=True,separators=(',',':')))
print('RESULT_SHA256',hashlib.sha256(encoded).hexdigest())
assert max_time==21 and len(max_states)==3
assert set(orbits)=={1,3,4,5,6,7,8}
assert [orbits[p] for p in sorted(orbits)]==[1,1912,22,10,2,28,4]
print('VERIFY_OK')
