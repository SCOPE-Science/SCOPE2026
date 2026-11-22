#!/usr/bin/env python3
"""Exact independent indegree-elimination census for Paley prime graphs 13 and 17.
Uses masks for finite labelled configurations and a reverse topological sweep.
"""
from collections import Counter, deque
import json


def census(p):
    residues = {a*a % p for a in range(1,p)}
    assert len(residues)==(p-1)//2 and p in (13,17)
    masks = [sum(1<<j for j in range(p) if (j-i)%p in residues)
             for i in range(p)]
    assert all(m.bit_count()==(p-1)//2 for m in masks)
    assert all(((masks[i]>>j)&1)==((masks[j]>>i)&1)
               for i in range(p) for j in range(p))
    n=1<<p
    degree=(p-1)//2
    succ=[0]*n
    indeg=[0]*n
    for x in range(n):
        y=0
        for i,m in enumerate(masks):
            z=(x&m).bit_count()
            if z>degree//2 or (z==degree//2 and (x>>i)&1):
                y |= 1<<i
        succ[x]=y
        indeg[y]+=1
    # Kahn peel: all deleted nodes are transient; nondeleted nodes lie on cycles.
    q=deque(i for i,d in enumerate(indeg) if d==0)
    peel=[]
    while q:
        x=q.popleft();peel.append(x)
        y=succ[x];indeg[y]-=1
        if indeg[y]==0:q.append(y)
    entry=[-1]*n
    period=[0]*n
    orbit=[-1]*n
    period_hist=Counter()
    numorbits=0
    for x in range(n):
        if indeg[x]==0 or orbit[x]!=-1:continue
        cyc=[];y=x
        while orbit[y]==-1:
            orbit[y]=numorbits;cyc.append(y);y=succ[y]
        assert y==x
        length=len(cyc)
        assert length in (1,2)
        for y in cyc:
            entry[y]=0;period[y]=length
        period_hist[length]+=1
        numorbits+=1
    for x in reversed(peel):
        y=succ[x]
        entry[x]=entry[y]+1
        period[x]=period[y]
        orbit[x]=orbit[y]
    assert all(t>=0 for t in entry)
    assert all(d in (1,2) for d in period)
    basin=Counter(orbit)
    basin_by_type=Counter()
    for x in range(n):
        if entry[x]==0:
            basin_by_type[('periodic',period[x])]+=1
    orbit_length=[None]*numorbits
    for x in range(n):
        if entry[x]==0:
            orbit_length[orbit[x]]=period[x]
    basin_hist=Counter((orbit_length[a],b) for a,b in basin.items())
    fixed=[x for x in range(n) if succ[x]==x]
    assert len(fixed)==period_hist[1]
    con0=orbit[0];con1=orbit[n-1]
    assert succ[0]==0 and succ[n-1]==n-1 and con0!=con1
    maxdepth=max(entry)
    witness=next(i for i,t in enumerate(entry) if t==maxdepth)
    result={
        'p':p, 'states':n, 'degree':degree, 'edges':p*degree//2,
        'fixed':period_hist[1], 'two_cycles':period_hist[2],
        'max_entry':maxdepth,
        'entry_histogram':[[k,v] for k,v in sorted(Counter(entry).items())],
        'basin_histogram':[[k,b,v] for (k,b),v in sorted(basin_hist.items())],
        'unanimity_basin_each':basin[con0],
        'consensus_total':basin[con0]+basin[con1],
        'nonconsensus_fixed_basin':sum(basin[a] for a in basin
                    if orbit_length[a]==1 and a not in (con0,con1)),
        'two_cycle_basin':sum(basin[a] for a in basin if orbit_length[a]==2),
        'max_entry_population':sum(t==maxdepth for t in entry),
        'max_entry_witness_mask':witness,
        'nonuniform_fixed_by_weight':[[k,v] for k,v in sorted(
              Counter(x.bit_count() for x in fixed if x not in (0,n-1)).items())],
    }
    assert (result['consensus_total'] + result['nonconsensus_fixed_basin'] +
            result['two_cycle_basin'] == n)
    assert sum(t for k,b,t in result['basin_histogram'])==numorbits
    assert sum(b*t for k,b,t in result['basin_histogram'])==n
    assert sum(v for k,v in result['entry_histogram'])==n
    return result

if __name__=='__main__':
    for p in (13,17): print(json.dumps(census(p),sort_keys=True,separators=(',',':')))
