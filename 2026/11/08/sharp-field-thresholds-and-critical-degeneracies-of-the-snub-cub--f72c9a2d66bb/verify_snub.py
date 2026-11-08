#!/usr/bin/env python3
"""Exact snub-cube Ising ground-manifold checker; standard library only."""
from itertools import permutations, product, combinations
from collections import Counter

# Cubic number field basis 1,t,t^2, t^3=t^2+t+1.
ONE=(1,0,0); INV=(-1,-1,1); T=(0,1,0); ZERO=(0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
    c=[0]*5
    for i in range(3):
        for j in range(3):c[i+j]+=a[i]*b[j]
    for k in (4,3):
        v=c[k];c[k]=0
        for j in (k-3,k-2,k-1):c[j]+=v
    return tuple(c[:3])
pts=[]
for p in permutations(range(3)):
    parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
    for signs in product((-1,1),repeat=3):
        if sum(s==1 for s in signs)%2==parity:
            base=(ONE,INV,T)
            pts.append(tuple(base[p[k]] if signs[k]==1 else neg(base[p[k]]) for k in range(3)))
assert len(pts)==24
sq_target=(2,4,-2)
def dsq(x,y):
    d=ZERO
    for k in range(3):
        z=add(x[k],neg(y[k])); d=add(d,mul(z,z))
    return d
edges=[(i,j) for i in range(24) for j in range(i+1,24) if dsq(pts[i],pts[j])==sq_target]
assert len(edges)==60
adj=[set() for _ in pts]
for i,j in edges:adj[i].add(j);adj[j].add(i)
assert all(len(a)==5 for a in adj)
triangles=[(i,j,k) for i,j,k in combinations(range(24),3) if j in adj[i] and k in adj[i] and k in adj[j]]
assert len(triangles)==32
tri_inc=Counter(tuple(sorted((a,b))) for tr in triangles for a,b in combinations(tr,2))
assert set(tri_inc)==set(edges) and Counter(tri_inc.values())=={1:24,2:36}
square_edges=[e for e in edges if tri_inc[e]==1]
blocks=[]; remaining=set(range(24))
while remaining:
    st=next(iter(remaining)); component={st}; frontier=[st]
    while frontier:
        u=frontier.pop()
        for a,b in square_edges:
            v= b if a==u else a if b==u else None
            if v is not None and v not in component:
                component.add(v); frontier.append(v)
    remaining-=component
    blocks.append(tuple(sorted(component)))
blocks.sort()
assert len(blocks)==6 and all(len(b)==4 for b in blocks)
for b in blocks:
    internal=[e for e in square_edges if e[0] in b and e[1] in b]
    assert len(internal)==4 and all(sum(u in e for e in internal)==2 for u in b)
options=[]
for b in blocks:
    opts=[]
    for mask in range(16):
        sel=sum((1<<b[i] for i in range(4) if mask>>i&1),0)
        if all(not(sel>>a&1 and sel>>c&1) for a,c in square_edges):opts.append(sel)
    assert Counter(x.bit_count() for x in opts)=={0:1,1:4,2:2}
    options.append(opts)
critical=Counter(); zero=Counter(); indep=Counter()
for choices in product(*options):
    mask=0
    for ch in choices:mask|=ch
    q=mask.bit_count()
    if all(not(mask>>a&1 and mask>>b&1) for a,b in edges):indep[q]+=1
    if all(0<sum((mask>>v)&1 for v in tri)<3 for tri in triangles):
        critical[q]+=1
        if q==12:zero[q]+=1
assert dict(sorted(critical.items()))=={8:3,9:24,10:84,11:72,12:18}
assert dict(sorted(indep.items()))=={0:1,1:24,2:216,3:912,4:1854,5:1680,6:564,7:48,8:3}
assert zero[12]==18 and sum(critical.values())==201 and sum(indep.values())==5302
print('VERIFY_EXACT_OK 24_vertices 60_edges 32_triangles 6_squares critical_201 zero_18 saturation_5302')
