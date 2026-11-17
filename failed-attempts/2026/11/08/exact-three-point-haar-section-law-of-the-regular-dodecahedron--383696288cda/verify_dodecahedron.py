#!/usr/bin/env python3
"""Exact Q(sqrt(5)) chamber certificate for the regular dodecahedron.
No external packages required.  All incidence and sign decisions are exact.
"""
from collections import defaultdict, Counter
from itertools import product, combinations

# A pair (a,b) denotes a+b*sqrt(5), with integral coefficients.
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def sub(x,y): return add(x,neg(y))
def mul(x,y): return x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0]
def sign(x):
    a,b=x
    if a==0: return (b>0)-(b<0)
    if b==0: return (a>0)-(a<0)
    if (a>0)==(b>0): return (a>0)-(a<0)
    t=a*a-5*b*b
    assert t!=0 # sqrt(5) is irrational for nonzero integral coefficients
    return ((a>0)-(a<0)) if t>0 else ((b>0)-(b<0))

def vecneg(x):return tuple(neg(y) for y in x)
def dot(x,y):
    z=(0,0)
    for a,b in zip(x,y):z=add(z,mul(a,b))
    return z

def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))
def same(x,y):return all(a==b for a,b in zip(x,y))
def signpattern(v,axes):return tuple(sign(dot(v,a)) for a in axes)

Z=(0,0); ONE=(2,0); PHI=(1,1); P2=(3,1) # all coordinates scaled by 2*golden_ratio
vertices=[]
for signs in product((-1,1),repeat=3):
    vertices.append(tuple(PHI if s==1 else neg(PHI) for s in signs))
for s,t in product((-1,1),repeat=2):
    x=ONE if s==1 else neg(ONE)
    y=P2 if t==1 else neg(P2)
    vertices.extend([(Z,x,y),(x,y,Z),(y,Z,x)])
assert len(vertices)==20 and len(set(vertices))==20
norm2=dot(vertices[0],vertices[0]);assert all(dot(v,v)==norm2 for v in vertices)
edges=[]
for i,j in combinations(range(20),2):
    d=tuple(sub(x,y) for x,y in zip(vertices[i],vertices[j]))
    if dot(d,d)==(16,0):edges.append((i,j))
assert len(edges)==30
axes=[]
for v in vertices:
    if v not in axes and vecneg(v) not in axes:axes.append(v)
assert len(axes)==10
axis_index={v:(i,1) for i,v in enumerate(axes)}
axis_index.update({vecneg(v):(i,-1) for i,v in enumerate(axes)})
assert len(axis_index)==20

# Every pair of distinct great circles has two antipodal intersection points.
# A pair of crossing lines bounds four chambers, all different signs at these
# two axes, with signs at the other eight axes prescribed by the crossing ray.
# Enumerate EVERY chamber without random sampling or numerical comparisons.
chambers=defaultdict(list) # sign tuple -> list of corner pair indices, signed rays
rays=set()
for i,j in combinations(range(10),2):
    c=cross(axes[i],axes[j]);assert any(sign(x)!=0 for x in c)
    for ray in (c,vecneg(c)):
        other={k:sign(dot(ray,axes[k])) for k in range(10) if k not in (i,j)}
        assert all(s in (-1,1) for s in other.values()) # no triple intersection
        # Ray is a distinct point of the arrangement; no duplicate crossings.
        ray_pattern=tuple(other.get(k,0) for k in range(10))
        assert ray_pattern not in rays
        rays.add(ray_pattern)
        for si,sj in product((-1,1),repeat=2):
            pattern=tuple(si if k==i else sj if k==j else other[k] for k in range(10))
            chambers[pattern].append((i,j,ray_pattern))
assert len(rays)==90 and len(chambers)==92
# All cells have at least three vertices, with no duplicated boundary corners.
assert all(len(c)>=3 and len(c)==len(set(v[2] for v in c)) for c in chambers.values())

# A central section meets an edge iff its endpoints have opposite signs.
# Crossings on rays from the vertex arrangement have measure zero.
results=Counter(); by_type=defaultdict(Counter); by_area=defaultdict(Counter)
cos_plus1=norm2;cos_plus5=mul((0,1),norm2)
for pattern,corners in chambers.items():
    point_signs=[pattern[axis_index[v][0]]*axis_index[v][1] for v in vertices]
    N=sum(point_signs[i]!=point_signs[j] for i,j in edges)
    angles=Counter()
    for i,j,_ in corners:
        w=mul(dot(axes[i],axes[j]),(3*pattern[i]*pattern[j],0))
        if w==cos_plus1: term='a' # arccos(1/3)
        elif w==neg(cos_plus1): term='A' # arccos(-1/3)
        elif w==cos_plus5: term='b' # arccos(sqrt(5)/3)
        elif w==neg(cos_plus5): term='B' # arccos(-sqrt(5)/3)
        else:raise AssertionError(('unexpected cosine',w))
        angles[term]+=1
    results[N]+=1
    by_type[N][len(corners)]+=1
    by_area[N][tuple(sorted(angles.items()))]+=1

assert results==Counter({6:20,8:60,10:12}),results
assert by_type=={6:Counter({6:20}),8:Counter({3:60}),10:Counter({5:12})},by_type
assert by_area=={6:Counter({(('a',3),('b',3)):20}),
                8:Counter({(('A',2),('B',1)):60}),
                10:Counter({(('a',5),):12})},by_area
print('DODECAHEDRON_EXACT_ARRANGEMENT_OK axes=10 crossings=90 chambers=92')
print('DODECAHEDRON_EXACT_SECTION_TYPES_OK',dict(sorted(results.items())))
print('DODECAHEDRON_EXACT_ANGLE_SIGNATURES_OK')

# Geometric check (not required for the exact combinatorial proof):
import math
alpha=math.acos(1/3);beta=math.acos(math.sqrt(5)/3)
areas={6:2*math.pi-3*alpha-3*beta,
       8:2*alpha+beta-math.pi,
       10:2*math.pi-5*alpha}
probs={k:results[k]*areas[k]/(4*math.pi) for k in results}
assert all(v>0 for v in areas.values())
assert abs(sum(probs.values())-1)<1e-13
print('DODECAHEDRON_SECTION_PROBABILITIES',[(k,round(probs[k],12)) for k in sorted(probs)])
print('DODECAHEDRON_MEAN',sum(k*probs[k] for k in probs))
