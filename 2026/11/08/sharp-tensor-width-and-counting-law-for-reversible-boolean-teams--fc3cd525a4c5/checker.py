#!/usr/bin/env python3
"""Finite semantic checks for the Boolean coordinate-injective team theorem."""
import itertools, math, collections

def matching(points):
    return all(all(x[i]!=y[i] for i in range(len(x))) for x,y in itertools.combinations(points,2))

def direct_width(points):
    n=len(points)
    if n==0:return 0
    for k in range(1,n+1):
        for assignment in itertools.product(range(k),repeat=n):
            if len(set(assignment))!=k: continue
            if all(matching([points[i] for i in range(n) if assignment[i]==j]) for j in range(k)):
                return k
    raise AssertionError

def formula_width(points):
    if not points:return 0
    d=len(points[0]); used=set()
    for x in points:
        c=min(x,tuple(1-b for b in x))
        used.add(c)
    return len(used)

def local_bound(points):
    if not points:return 0
    d=len(points[0]); return max(sum(x[i]==b for x in points) for i in range(d) for b in (0,1))

for d in (2,3):
    universe=list(itertools.product((0,1),repeat=d))
    dist=collections.Counter()
    extrema=[]
    for mask in range(1<<len(universe)):
        points=[x for j,x in enumerate(universe) if mask>>j & 1]
        t=formula_width(points); direct=direct_width(points); delta=local_bound(points)
        assert t==direct,(d,points,t,direct)
        dist[(len(points),t)]+=1
        assert not points or t<=2*delta
        if points and t==2*delta: extrema.append(points)
        if d==2: assert t==delta,(points,t,delta)
    M=2**(d-1)
    for s in range(2**d+1):
        for t in range(M+1):
            expected=math.comb(M,t)* (math.comb(t,s-t)*2**(2*t-s) if t<=s<=2*t else 0)
            assert dist[(s,t)]==expected,(d,s,t,dist[(s,t)],expected)
    print('CHECK_OK',d,'total',sum(dist.values()),'widths',dict(sorted(collections.Counter({t:sum(v for (s,j),v in dist.items() if j==t) for t in range(M+1)}).items())),'ratio2',len(extrema),'min_nonempty_ratio2',min(map(len,extrema)) if extrema else None)

for d in range(3,9):
    parity=[x for x in itertools.product((0,1),repeat=d) if sum(x[:3])%2==0]
    t=formula_width(parity); delta=local_bound(parity)
    assert t==2**(d-1) and delta==2**(d-2)
    print('PARITY_OK',d,len(parity),t,delta)
