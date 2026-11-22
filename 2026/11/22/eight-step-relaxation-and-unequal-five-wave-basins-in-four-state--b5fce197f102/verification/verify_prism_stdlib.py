#!/usr/bin/env python3
"""Exact exhaustive four-color GHM on GP(5,1); Python standard library only.
Graph labels: upper u_0,...,u_4, lower v_0,...,v_4.
Every output is derived from exhaustive integer enumeration, no random sampling.
"""
from array import array
from collections import Counter

N=10; TOTAL=4**N
# Construct the prism as the Cartesian product of a five-cycle with an edge.
neighbors=[]
for v in range(10):
    i=v%5;rail=v//5
    neighbors.append((((i-1)%5)+5*rail,((i+1)%5)+5*rail,i+5*(1-rail)))
assert all(len(set(ns))==3 for ns in neighbors)
assert all(u in neighbors[v] for u,ns in enumerate(neighbors) for v in ns)

def step(s):
    x=tuple((s>>(2*i))&3 for i in range(N))
    y=0
    for v,c in enumerate(x):
        if c==0:d=int(any(x[j]==1 for j in neighbors[v]))
        elif c==3:d=0
        else:d=c+1
        y|=d<<(2*v)
    return y

trans=array('I',(step(s) for s in range(TOTAL)))
# Full functional graph by path marking; independent of iteration-composition code.
mark=bytearray(TOTAL)
depth=bytearray(TOTAL)
period=bytearray(TOTAL)
representative=array('I',[0])*TOTAL
cycles_by_period=Counter()
for s in range(TOTAL):
    if mark[s]==2:continue
    cur=s;walk=[]
    while mark[cur]==0:
        mark[cur]=1
        walk.append(cur)
        cur=trans[cur]
    if mark[cur]==1:
        start=walk.index(cur)
        cycle=walk[start:]
        p=len(cycle)
        rep=min(cycle)
        cycles_by_period[p]+=1
        for u in cycle:
            depth[u]=0;period[u]=p;representative[u]=rep;mark[u]=2
        walk=walk[:start]
    for u in reversed(walk):
        v=trans[u]
        depth[u]=depth[v]+1
        period[u]=period[v]
        representative[u]=representative[v]
        mark[u]=2
assert all(z==2 for z in mark)
H=Counter(zip(depth,period))
basins=Counter(representative)
repperiod={int(representative[i]):int(period[i]) for i in range(TOTAL) if depth[i]==0}
assert len(repperiod)==sum(cycles_by_period.values())
assert sum(H.values())==TOTAL
assert cycles_by_period=={1:1,4:530,5:6}
assert sum(b for rep,b in basins.items() if repperiod[rep]==5)==31980
assert max(depth)==8
assert sum(1 for z in depth if z==8)==20
# Explicit twenty symmetry permutations D_5 x C_2.
def action(s,j,sgn,swap):
    t=0
    for v in range(10):
        to=(sgn*(v%5)+j)%5+5*((v//5)^swap)
        t|=((s>>(2*v))&3)<<(2*to)
    return t

def cycle_rep(s):
    a=s;verts=[]
    while True:
        verts.append(a);a=trans[a]
        if a==s:break
        assert a not in verts
    return min(verts)

types=[]
unused=set(repperiod)
while unused:
    seed=min(unused)
    orbit={cycle_rep(action(seed,j,sgn,sw)) for j in range(5) for sgn in (-1,1) for sw in (0,1)}
    assert orbit<=unused
    assert len(set(orbit))==len(orbit)
    assert all(repperiod[c]==repperiod[seed] for c in orbit)
    unused-=orbit
    types.append((repperiod[seed],len(orbit),seed,sum(basins[c] for c in orbit),tuple(sorted(basins[c] for c in orbit))))
type_sizes=Counter((p,k) for p,k,_,_,_ in types)
assert type_sizes[(5,2)]==1 and type_sizes[(5,4)]==1
assert type_sizes[(4,10)]==11 and type_sizes[(4,20)]==21
# Tail forms one geometric class, all states entering 5-period cycles.
tail=[i for i in range(TOTAL) if depth[i]==8]
assert all(period[i]==5 for i in tail)
tailorbit={action(tail[0],j,sgn,sw) for j in range(5) for sgn in (-1,1) for sw in (0,1)}
assert tailorbit==set(tail)
print('graph=GP(5,1) states=',TOTAL,'automorphisms=20')
print('primitive cycles',dict(sorted(cycles_by_period.items())))
print('maxdepth',max(depth),'tail',len(tail),'tail_witness',tail[0])
print('basins', {p:sum(b for r,b in basins.items() if repperiod[r]==p) for p in (1,4,5)})
for (d,p),b in sorted(H.items()):print('census',d,p,b)
print('symmetry_class_sizes',dict(sorted(type_sizes.items())))
for p,k,s,b,weights in types:
    if p==5:print('five_cycle_class',k,s,b,weights)
print('tail_cycle_rep',representative[tail[0]],'tail_basin',basins[representative[tail[0]]]); print('PASS: full state census, symmetry classes, full delay orbit')
