#!/usr/bin/env python3
"""Independent path-tracing census for three-state graph excitation.

Builds the graph via adjacency incidence (not edge tuples), computes each update
from a ternary digit array, and discovers directed cycles by trajectory tracing.
"""
import json
from collections import Counter
from pathlib import Path

n=11
M=3**n
powers=[3**v for v in range(n)]
ngh=[[] for _ in range(n)]
for v in range(5):
    ngh[v].extend([(v-1)%5,(v+1)%5,5+(v-1)%5,5+(v+1)%5])
    ngh[v+5].extend([(v-1)%5,(v+1)%5,10])
ngh[10]=list(range(5,10))
assert all(i in ngh[j] for i in range(n) for j in ngh[i])
assert sum(len(row) for row in ngh)==40

def evolve(a):
    z=[0]*n
    rem=a
    for k in range(n):
        rem,z[k]=divmod(rem,3)
    v=0
    for k in range(n):
        if z[k]==1:step=2
        elif z[k]==2:step=0
        else:
            step=1 if any(z[h]==1 for h in ngh[k]) else 0
        v+=powers[k]*step
    return v

def verify():
    depth=[-1]*M
    p=[0]*M
    key=[-1]*M
    cycle_lengths={}
    for s in range(M):
        if depth[s]>=0:continue
        seq=[];indices={}
        cur=s
        while depth[cur]<0 and cur not in indices:
            indices[cur]=len(seq);seq.append(cur);cur=evolve(cur)
        if depth[cur]>=0:
            for t in reversed(seq):
                depth[t]=depth[cur]+1
                p[t]=p[cur]
                key[t]=key[cur]
                cur=t
        else:
            start=indices[cur]
            cyc=seq[start:]
            length=len(cyc)
            representative=min(cyc)
            cycle_lengths[representative]=length
            for t in cyc:
                depth[t]=0;p[t]=length;key[t]=representative
            for t in reversed(seq[:start]):
                v=evolve(t)
                depth[t]=depth[v]+1;p[t]=p[v];key[t]=representative
    assert all(z>=0 for z in depth)
    period_orbits=Counter(cycle_lengths.values())
    byperiod=Counter((depth[i],p[i]) for i in range(M))
    basin=Counter(key)
    histogram=Counter((cycle_lengths[k],basin[k]) for k in cycle_lengths)
    expected=json.loads(Path(__file__).with_name('COUNTS.json').read_text())
    assert {str(p):n for p,n in sorted(period_orbits.items())}==expected['period_orbit_counts']
    assert {str(z):sum(n for (d,pp),n in byperiod.items() if d==z) for z in sorted(set(depth))}==expected['first_entry_counts']
    for d,classes in expected['first_entry_by_period'].items():
        for p,z in classes.items():assert byperiod[(int(d),int(p))]==z,(d,p)
    for p,bins in expected['basin_size_histogram_by_period'].items():
        assert {str(b):n for (pp,b),n in sorted(histogram.items()) if pp==int(p)}==bins
    assert max(depth)==9 and depth.count(9)==120
    assert len(cycle_lengths)==1291 and basin[0]==13887
    print('PASS direct trajectory tracing: all',M,'states;',len(cycle_lengths),'cycles; nine-step count 120; extinction basin',basin[0])

if __name__=='__main__': verify()
