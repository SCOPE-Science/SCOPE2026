#!/usr/bin/env python3
"""Independent complete trajectory-memoization check using Frucht's LCF graph.
No external libraries; vertex labels are different from those of the edge-list check.
"""
import collections
import hashlib
import json

NVERT=12
LCF=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
E={tuple(sorted((i,(i+1)%NVERT))) for i in range(NVERT)}
E.update(tuple(sorted((i,(i+LCF[i])%NVERT))) for i in range(NVERT))
assert len(E)==18
NB=[tuple(j for j in range(NVERT) if (min(i,j),max(i,j)) in E) for i in range(NVERT)]
assert all(len(n)==3 for n in NB)
# Explicit isomorphism from the separate, labeled edge-list model to this LCF model.
MAP=(5,3,2,1,0,7,6,4,10,11,8,9)
FIXED=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
       (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
assert {tuple(sorted((MAP[i],MAP[j]))) for i,j in FIXED}==E
N=3**NVERT
POW3=[3**i for i in range(NVERT)]

def next_state(s):
    colors=[];z=s
    for i in range(NVERT):colors.append(z%3);z//=3
    new=[]
    for i,c in enumerate(colors):
        if c==1:new.append(2)
        elif c==2:new.append(0)
        else:new.append(int(any(colors[j]==1 for j in NB[i])))
    return sum(c*POW3[i] for i,c in enumerate(new))

# DFS walks each state to either a previously solved path or a newly discovered cycle.
solved={}   # code -> (first periodic entry time, least period)
cycles=collections.Counter()
for start in range(N):
    if start in solved:continue
    path=[];local={};s=start
    while s not in solved and s not in local:
        local[s]=len(path);path.append(s);s=next_state(s)
    if s in local:
        cut=local[s];p=len(path)-cut;cycles[p]+=1
        for x in path[cut:]:solved[x]=(0,p)
        path=path[:cut]
    while path:
        x=path.pop();t,p=solved[next_state(x)];solved[x]=(t+1,p)
assert len(solved)==N
census=collections.Counter(solved.values())
maxT=max(t for t,p in census)
# A relabeling maps the LCF-configuration into edge-list labeling.
back=[0]*NVERT
for i,j in enumerate(MAP):back[j]=i

def to_fixed(s):
    vals=[(s//POW3[i])%3 for i in range(NVERT)]
    return sum(vals[MAP[i]]*POW3[i] for i in range(NVERT))
maxstates=sorted(to_fixed(s) for s, (t,p) in solved.items() if t==maxT)
C=[[t,p,c] for (t,p),c in sorted(census.items())]
print('CENSUS_SHA256',hashlib.sha256(json.dumps(C,separators=(',',':')).encode()).hexdigest())
print('MAX_TRANSIENT',maxT,'MAX_STATES_EDGE_LABELS',maxstates)
print('PRIMITIVE_ORBITS',json.dumps(dict(sorted(cycles.items()))))
print('CLASSES',len(C),'STATES',sum(c for t,p,c in C))
assert maxT==21 and len(maxstates)==3
assert dict(sorted(cycles.items()))=={1:1,3:1912,4:22,5:10,6:2,7:28,8:4}
print('VERIFY_OK')
