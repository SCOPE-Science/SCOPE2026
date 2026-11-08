#!/usr/bin/env python3
"""Exact functional-graph census of the 3-state Greenberg–Hastings rule on KG(5,2)."""
from itertools import combinations, permutations
from collections import Counter
from math import lcm
import hashlib, json

VERTICES = tuple(combinations(range(5), 2))
ADJ = tuple(tuple(j for j, v in enumerate(VERTICES) if i != j and not (set(u) & set(v))) for i, u in enumerate(VERTICES))
BASE = tuple(3**i for i in range(10))
TOTAL = 3**10

def digits(s):
    return tuple((s // BASE[i]) % 3 for i in range(10))

def transition(s):
    a = digits(s)
    return sum(BASE[i] * (2 if a[i] == 1 else 0 if a[i] == 2 else int(any(a[j] == 1 for j in ADJ[i]))) for i in range(10))

def permutation_images():
    locate = {v: i for i, v in enumerate(VERTICES)}
    for p in permutations(range(5)):
        yield tuple(locate[tuple(sorted((p[u], p[v])))] for u,v in VERTICES)

def orbit(s, images):
    a=digits(s)
    out=set()
    for im in images:
        b=[0]*10
        for j,k in enumerate(im):b[k]=a[j]
        out.add(sum(b[i]*BASE[i] for i in range(10)))
    return out

def run():
    assert len(VERTICES)==10 and all(len(x)==3 for x in ADJ)
    assert all(i in ADJ[j] for i in range(10) for j in ADJ[i])
    F=[transition(i) for i in range(TOTAL)]
    times=[-1]*TOTAL; periods=[0]*TOTAL; cycles=Counter()
    for start in range(TOTAL):
        if times[start] >= 0:continue
        position={};route=[]; cur=start
        while times[cur]<0 and cur not in position:
            position[cur]=len(route)
            route.append(cur)
            cur=F[cur]
        if cur in position:
            begin=position[cur]; p=len(route)-begin
            cycles[p]+=1
            for node in route[begin:]:
                times[node]=0;periods[node]=p
            tail=route[:begin]
        else:tail=route
        for node in reversed(tail):
            times[node]=times[F[node]]+1
            periods[node]=periods[F[node]]
    census=Counter(zip(times,periods))
    expected_cycles={1:1,3:80,4:60,5:30,8:60}
    assert dict(cycles)==expected_cycles,cycles
    assert sum(census.values())==TOTAL and max(times)==6
    assert sum(int(t==6) for t in times)==120
    assert all(times[F[s]]==max(times[s]-1,0) for s in range(TOTAL) if times[s]>0)
    # Global periodicity identity after six updates, with period dividing lcm(3,4,5,8)=120.
    assert lcm(*cycles.keys())==120
    for i in range(TOTAL):
        x=i
        for step in range(6):x=F[x]
        y=x
        for step in range(120):y=F[y]
        assert x==y
    images=tuple(permutation_images())
    assert len(images)==120 and len(set(images))==120
    extremals={s for s in range(TOTAL) if times[s]==6}
    reps=[];remaining=set(extremals)
    while remaining:
        r=min(remaining); o=orbit(r,images)
        assert o<=remaining
        assert len(o)==60
        reps.append(r);remaining-=o
    assert len(reps)==2
    assert sorted(tuple(Counter(digits(r))[i] for i in (0,1,2)) for r in reps)==[(3,3,4),(4,3,3)]
    result={'total':TOTAL,'cycles':dict(sorted(cycles.items())),'census':[{ 't':t,'p':p,'count':census[t,p]} for t in range(7) for p in (1,3,4,5,8)],'max_entry':6, 'max_entry_reps':[{'base3_integer':r,'colors':list(digits(r)), 'orbit_size':len(orbit(r,images))} for r in reps], 'group_size':len(images)}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
    return result

if __name__=='__main__':run()
