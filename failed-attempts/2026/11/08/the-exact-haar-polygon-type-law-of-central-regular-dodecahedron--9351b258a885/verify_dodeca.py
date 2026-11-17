#!/usr/bin/env python3
"""Exact certificate for the Haar central-section vertex-count law of a regular dodecahedron.
All geometry relevant to the chamber classification is computed in Z[phi] with exact signs.
Run: python dodeca_haar_checker.py
"""
from itertools import product, combinations
from collections import Counter
from math import acos, pi, sqrt

# Scalar a+b*phi, where phi^2=phi+1, phi=(1+sqrt(5))/2.
Z=(0,0); ONE=(1,0); PHI=(0,1); INV=(-1,1); ROOT5=(-1,2)
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    return (a*c+b*d,a*d+b*c+b*d)
def sign(x):
    """Exact sign: twice (a+b phi) = (2a+b)+b sqrt(5)."""
    a,b=x; A=2*a+b
    if A==0: return (b>0)-(b<0)
    if b==0 or (A>0)==(b>0): return (A>0)-(A<0)
    # Opposite signs; irrationality excludes equality of magnitudes.
    cmp=A*A-5*b*b
    assert cmp != 0
    t=A if cmp>0 else b
    return (t>0)-(t<0)
def scale(s,x): return x if s==1 else neg(x)
def vecscale(s,v): return tuple(scale(s,x) for x in v)
def dot(x,y):
    t=Z
    for a,b in zip(x,y):t=add(t,mul(a,b))
    return t
def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))
def nneg(x):return all(sign(a)>=0 for a in x)

V=[]
for ss in product((-1,1),repeat=3): V.append(tuple(scale(s,ONE) for s in ss))
for s,t in product((-1,1),repeat=2):
    V.extend([(Z,scale(s,INV),scale(t,PHI)),
              (scale(s,INV),scale(t,PHI),Z),
              (scale(s,PHI),Z,scale(t,INV))])
assert len(V)==20 and len(set(V))==20
assert set(dot(v,v) for v in V)=={(3,0)}
REP=[v for v in V if next(sign(x) for x in v if sign(x))>0]
assert len(REP)==10
indices={v:(i,1) for i,v in enumerate(REP)}
indices.update({vecscale(-1,v):(i,-1) for i,v in enumerate(REP)})
assert len(indices)==20
# Distance-squared of any dodecahedral edge in these coordinates: 8-4 phi.
EDGE_D2=(8,-4)
EDGES=[]
for i,j in combinations(range(20),2):
    d=tuple(sub(V[i][q],V[j][q]) for q in range(3))
    if dot(d,d)==EDGE_D2: EDGES.append((i,j))
assert len(EDGES)==30
# General position for ten great circles: no triple intersection is shared.
assert all(sign(dot(REP[k],cross(REP[i],REP[j])))!=0
           for i,j,k in combinations(range(10),3))
# The two ray directions on each intersection line (90 in total).
RAYS=[(i,j,eps,vecscale(eps,cross(REP[i],REP[j])))
      for i,j in combinations(range(10),2) for eps in (-1,1)]
assert len(RAYS)==90
TABLE=Counter()
DETAILS=Counter()
for b in product((-1,1),repeat=10):
    visible=[]
    for i,j,eps,w in RAYS:
        vals=[sign(scale(b[k],dot(REP[k],w))) for k in range(10)]
        if min(vals)>=0:
            visible.append((i,j,eps,w,vals))
    if len(visible)<3: continue
    # Exact interior feasibility: summing the ray vectors yields all strict halfspaces.
    if any(all(rec[4][k]==0 for rec in visible) for k in range(10)):continue
    assert all(sum(rec[4][k]>0 for rec in visible)>0 for k in range(10))
    assert len(set((i,j,eps) for i,j,eps,_,_ in visible))==len(visible)
    angle_dots=Counter()
    for i,j,eps,w,vals in visible:
        assert sum(x==0 for x in vals)==2
        assert vals[i]==vals[j]==0
        angle_dots[scale(b[i]*b[j],dot(REP[i],REP[j]))]+=1
    vertex_signs=[ori*b[idx] for v in V for idx,ori in [indices[v]]]
    n=sum(vertex_signs[i]!=vertex_signs[j] for i,j in EDGES)
    signature=tuple(sorted(angle_dots.items()))
    TABLE[n]+=1
    DETAILS[(n,len(visible),signature)]+=1
EXPECTED={
    (6,6,tuple(sorted({ONE:3,ROOT5:3}.items()))):20,
    (8,3,tuple(sorted({neg(ONE):2,neg(ROOT5):1}.items()))):60,
    (10,5,tuple(sorted({ONE:5}.items()))):12,
}
assert DETAILS==EXPECTED, (DETAILS,EXPECTED)
assert TABLE=={6:20,8:60,10:12},TABLE
assert sum(TABLE.values())==10*9+2==92
# The signed-normal pair angle at a spherical corner is arccos((s_i v_i) dot (s_j v_j)/3).
# Spherical polygon area = 2*pi - sum of these corner exterior angles.
a=acos(1/3); b=acos(sqrt(5)/3)
areas={6:2*pi-3*a-3*b,8:2*a+b-pi,10:2*pi-5*a}
p={k:TABLE[k]*areas[k]/(4*pi) for k in (6,8,10)}
assert abs(sum(p.values())-1)<1e-12
assert all(0<p[k]<1 for k in p)
print('EXACT_CERTIFICATE_OK regular_dodecahedron vertices=20 edges=30 great_circles=10 intersection_rays=90 feasible_chambers=92')
for k in (6,8,10):
    print(f'section_vertices={k} chambers={TABLE[k]} cell_area={areas[k]:.12f} probability={p[k]:.12f}')
