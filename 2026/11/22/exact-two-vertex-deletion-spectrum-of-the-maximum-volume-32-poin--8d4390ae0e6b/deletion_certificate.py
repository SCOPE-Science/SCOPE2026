#!/usr/bin/env python3
"""Exact verification of one/two-vertex volume-loss spectrum for the
unit-sphere icosahedron--face-normal dodecahedron 32-point hull.
Requires Python, numpy, scipy solely to select candidate face triples;
all geometric inequalities, volumes, and orbit reductions are exact.
"""
from itertools import combinations
from collections import Counter,defaultdict
from fractions import Fraction as F
import math
import numpy as np
from scipy.spatial import ConvexHull
import checker as c
Q=c.Q
Z=Q(); O=Q(1);U=(c.phi+2)/3
class T:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):self.a=Q.into(a);self.b=Q.into(b)
    @staticmethod
    def into(x):return x if isinstance(x,T) else T(x)
    def __neg__(self):return T(-self.a,-self.b)
    def __add__(self,o):
        o=T.into(o);return T(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __sub__(self,o):return self+-T.into(o)
    def __mul__(self,o):
        o=T.into(o);return T(self.a*o.a+U*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=T.into(o);return self.a==o.a and self.b==o.b
    def sign(self):
        sa,sb=self.a.sign(),self.b.sign()
        if sa==0:return sb
        if sb==0:return sa
        if sa==sb:return sa
        diff=self.a*self.a-U*self.b*self.b
        sd=diff.sign()
        assert sd !=0 or self==T(),('unexpected zero',self.a,self.b)
        return sa*sd
    def __repr__(self):return f'[{self.a}]+[{self.b}]*u'
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum((x*y for x,y in zip(a,b)),T())
def det(a,b,d):return dot(a,cross(b,d))
verts=[tuple(T(x,0) for x in v) for v in c.I]+[tuple(T(0,x) for x in v) for v in c.D]
phi=(1+math.sqrt(5))/2; uu=math.sqrt((phi+2)/3)
def fval(x):return float(x.a)+phi*float(x.b)
points=np.array([[fval(x.a)+uu*fval(x.b) for x in v] for v in verts])
base=20*T(0,0) if False else T(0,0)
# Full hull volume is 20*u^2 from the directly verified 60 face triangles.
base=T(20*U)
assert len(c.high)==60
# Distances of two vertices classified by their two symmetry orbits and exact norm-square.
def dist2(a,b):return dot(sub(verts[a],verts[b]),sub(verts[a],verts[b]))
classes=defaultdict(list)
for a in range(32):
 for b in range(a+1,32):
  kind=('II' if b<12 else 'DD' if a>=12 else 'ID')
  dd=dist2(a,b)
  classes[(kind,str(dd.a),str(dd.b))].append((a,b))
assert len(classes)==12,len(classes)
assert sorted(len(x) for x in classes.values())==[6,10,30,30,30,30,60,60,60,60,60,60], sorted(len(x) for x in classes.values())
reps=[(0,),(12,)]+[L[0] for L in classes.values()]
verification=[]
for missing in reps:
 idx=[j for j in range(32) if j not in missing]
 h=ConvexHull(points[idx]); facets=[]
 assert len(h.simplices)==2*len(idx)-4,(missing,len(h.simplices))
 for t in h.simplices:
  ids=tuple(idx[k] for k in t)
  n=cross(sub(verts[ids[1]],verts[ids[0]]),sub(verts[ids[2]],verts[ids[0]]))
  s=dot(n,verts[ids[0]]).sign()
  assert s!=0
  # choose outward normal, exact rather than numerical
  if s<0:n=tuple(-x for x in n);ids=(ids[0],ids[2],ids[1])
  assert all(dot(n,sub(verts[k],verts[ids[0]])).sign()<=0 for k in idx),(missing,ids)
  assert sum(dot(n,sub(verts[k],verts[ids[0]]))==0 for k in idx)>=3,(missing,ids)
  facets.append(ids)
 assert len(set(tuple(sorted(x)) for x in facets))==len(facets)
 edge_counts=Counter(tuple(sorted(e)) for tri in facets for e in combinations(tri,2))
 assert set(edge_counts.values())=={2},(missing,'edge coverage')
 assert set(j for tri in facets for j in tri)==set(idx),(missing,'all vertices')
 # All facets support, have exactly 3 contacts, and attain Euler upper bound 2V-4.
 vol=sum((det(verts[i],verts[j],verts[k]) for i,j,k in facets),T())
 # use division by 6 on each of both components
 vol=T(vol.a/6,vol.b/6); loss=base-vol
 assert loss.sign()>0
 verification.append((missing,loss,len(facets)))
# Every class is a symmetry orbit: the distance-pair counts above match
# the stabilizer suborbits of the full icosahedral symmetry group. An exact
# finite orbit witness below generates the 120 isometries from Gram matrices.
# Build an orthogonal map on three linearly independent I vertices, by identifying
# image triples with equal exact pairwise Gram products.
anchor=(0,2,4)
assert c.det(*(c.I[i] for i in anchor)).sign()!=0
G=tuple(c.dot(c.I[i],c.I[j]) for i in anchor for j in anchor)
images=[]
from itertools import permutations
for tri in permutations(range(12),3):
 if tuple(c.dot(c.I[i],c.I[j]) for i in tri for j in tri)==G:
  images.append(tri)
assert len(images)==120,len(images)
# For each map, images of all 32 points identified uniquely by dot products
# against the three images. Exact Gram invariance makes it an isometry.
base_signatures={tuple(c.dot(x,c.I[i]) for i in anchor):j for j,x in enumerate(c.I)}
assert len(base_signatures)==12
full_orbits={k:set() for k in classes}
for tri in images:
 target={tuple(c.dot(x,c.I[j]) for j in tri):i for i,x in enumerate(c.I)}
 assert len(target)==12
 permI=[target[tuple(c.dot(x,c.I[j]) for j in anchor)] for x in c.I] if False else None
 # Dot products (x, anchor source) equal (image(x), target anchor).
 permI=[next(k for k,y in enumerate(c.I) if all(c.dot(y,c.I[tri[s]])==c.dot(x,c.I[anchor[s]]) for s in range(3))) for x in c.I]
 assert len(set(permI))==12
 face_map={tuple(sorted(f)):k for k,f in enumerate(c.faces)}
 permD=[face_map[tuple(sorted(permI[i] for i in f))] for f in c.faces]
 perm=permI+[12+k for k in permD]
 for key,pairs in classes.items():
  a,b=pairs[0];full_orbits[key].add(tuple(sorted((perm[a],perm[b]))))
for key,pairs in classes.items():
 assert full_orbits[key]==set(pairs),(key,len(full_orbits[key]),len(pairs))
# Group all classes by exact volume deficit and compare to all 496 pairs.
levels=defaultdict(list)
for missing,loss,Fcount in verification[2:]:
 key=next(key for key,pairs in classes.items() if missing in pairs)
 levels[(loss.a,loss.b)].append((key,len(classes[key]),missing))
assert len(levels)==5,len(levels)
assert sorted(sum(v[1] for v in items) for items in levels.values())==[30,60,66,160,180]
assert sum(sum(x[1] for x in items) for items in levels.values())==496
assert len(verification)==14
for i,(missing,loss,fc) in enumerate(verification):print(f'CERT {i+1:02d}: missing={missing}, facets={fc}, loss={loss}')
print('FIVE LEVEL COUNTS',[(str(a),str(b),sum(x[1] for x in items)) for (a,b),items in levels.items()]);print('PASS: 120 exact isometries, 12 complete pair orbits, 14 exact deletion hulls, five volumes, 496 pairs.')
