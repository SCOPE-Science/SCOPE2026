#!/usr/bin/env python3
"""Exact self-contained checks for uniform-block partition matroid Hausdorff geometry.
Run: python3 check_partition.py
No data files or third-party dependencies are needed.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb

def cost(q,c,k):
    if k<=c:
        return F((c-k)**2,q-k)
    return F((k-c)**2,k)

def radius(q,c,r):
    a,s=divmod(r*c,q)
    return a*cost(q,c,q)+(r-a-(s>0))*cost(q,c,0)+(cost(q,c,s) if s else 0)

def maxprofiles(q,c,r):
    a,s=divmod(r*c,q)
    if s==0:
        return {x for x in set(product([0,q],repeat=r)) if sum(x)==r*c}
    out=set()
    for pos in range(r):
        for full in combinations((i for i in range(r) if i!=pos),a):
            x=[0]*r
            for i in full:x[i]=q
            x[pos]=s
            out.add(tuple(x))
    return out

cases=0; profiles=0; weighted_vertices=0; resonance=0
for r in range(3,8):
    for q in range(2,7):
        for c in range(1,q):
            R=radius(q,c,r)
            pred=maxprofiles(q,c,r)
            best=None; arg=[]
            for ks in product(range(q+1),repeat=r):
                if sum(ks)!=r*c:continue
                profiles+=1
                val=sum((cost(q,c,k) for k in ks),F(0))
                if best is None or val>best:
                    best=val;arg=[ks]
                elif val==best:arg.append(ks)
                weighted_vertices+=__import__('math').prod(comb(q,k) for k in ks)
            assert R==best,(r,q,c,R,best)
            assert set(arg)==pred,(r,q,c,pred,set(arg))
            if (r*c)%q==c:resonance+=1
            cases+=1

# Independent Euclidean projection by a monotone threshold, no formula reused.
def project_capped_simplex(x,c):
    lo=min(x)-2;hi=max(x)+2
    for _ in range(100):
        mid=(lo+hi)/2
        y=[min(1.,max(0.,t-mid)) for t in x]
        if sum(y)>c:lo=mid
        else:hi=mid
    return [min(1.,max(0.,t-(lo+hi)/2)) for t in x]

for (r,q,c) in [(3,4,2),(4,5,2),(5,3,1),(5,4,3),(7,3,2)]:
    for ks in product(range(q+1),repeat=r):
        if sum(ks)!=r*c: continue
        x=[]; expected=F(0)
        for k in ks:
            v=[1.]*k+[0.]*(q-k)
            x.extend(v)
            expected+=cost(q,c,k)
            y=project_capped_simplex(v,c)
            actual=sum((u-v)**2 for u,v in zip(v,y))
            assert abs(actual-float(cost(q,c,k)))<1e-10
        assert expected<=radius(q,c,r)

# A positive-dimensional deep-hole face: r=3, q=4, c=2, saturated block,
# intermediate block and empty block. Arbitrary convex points in middle block.
r,q,c=3,4,2
v=[1.]*4+[.8,.6,.4,.2]+[0.]*4
assert abs(sum(v[4:8])-c)<1e-12
calc=sum((a-b)**2 for j in range(r) for a,b in zip(v[j*q:(j+1)*q],project_capped_simplex(v[j*q:(j+1)*q],c)))
assert abs(calc-float(radius(q,c,r)))<1e-10
print(f'BALANCED_PARTITION_HAUSDORFF_PASS parameter_cases={cases} occupancy_profiles={profiles} combinatorially_counted_vertices={weighted_vertices} arithmetic_face_resonances={resonance} independent_projection=PASS nonvertex_deep_hole=PASS')
