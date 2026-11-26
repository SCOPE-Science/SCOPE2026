"""Exact Q(sqrt(5)) chamber certificate for regular-dodecahedron central sections.
Run: python3 dodeca_exact.py. No external dependencies.
"""
from itertools import product, combinations
from collections import Counter

ZERO=(0,0)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sign(x):
 a,b=x
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if a*b>0:return (a>0)-(a<0)
 if 5*b*b>a*a:return (b>0)-(b<0)
 if 5*b*b<a*a:return (a>0)-(a<0)
 raise AssertionError('nonzero irrational cannot cancel')
def madd(*xx):
 v=ZERO
 for x in xx:v=add(v,x)
 return v
def scale(s,v):return tuple(mul(s,t) for t in v)
def vadd(*vv):return tuple(madd(*(v[i] for v in vv)) for i in range(3))
def vneg(v):return tuple(map(neg,v))
def dot(x,y):return madd(*(mul(x[i],y[i]) for i in range(3)))
def cross(x,y):return (madd(mul(x[1],y[2]),neg(mul(x[2],y[1]))),madd(mul(x[2],y[0]),neg(mul(x[0],y[2]))),madd(mul(x[0],y[1]),neg(mul(x[1],y[0]))))

def I(x):return (x,0)
phi2=(1,1);invphi2=(-1,1)
vertices=[tuple(I(v) for v in xyz) for xyz in product((-2,2),repeat=3)]
for s,t in product((-1,1),repeat=2):
 for a,b,c in [(ZERO,scale((s,0),(invphi2,ZERO,ZERO))[0],scale((t,0),(phi2,ZERO,ZERO))[0]),
                (scale((s,0),(invphi2,ZERO,ZERO))[0],scale((t,0),(phi2,ZERO,ZERO))[0],ZERO),
                (scale((t,0),(phi2,ZERO,ZERO))[0],ZERO,scale((s,0),(invphi2,ZERO,ZERO))[0])]:vertices.append((a,b,c))
assert len(vertices)==20 and len(set(vertices))==20
assert all(dot(v,v)==I(12) for v in vertices)
planes=[]
for v in vertices:
 if v not in planes and vneg(v) not in planes:planes.append(v)
assert len(planes)==10
# Genericity: no three great circles are concurrent.
for i,j,k in combinations(range(10),3):assert sign(dot(planes[k],cross(planes[i],planes[j])))!=0

# Derive every spherical chamber by exact pair-vertex perturbations.
patterns=set()
for i,j in combinations(range(10),2):
 w=cross(planes[i],planes[j])
 for pole in (-1,1):
  for x,y in product((-1,1),repeat=2):
   z=vadd(scale(I(pole*100000),w),scale(I(x),planes[i]),scale(I(y),planes[j]))
   pat=tuple(sign(dot(z,v)) for v in planes)
   assert all(s!=0 for s in pat)
   patterns.add(pat)
assert len(patterns)==92, len(patterns)

# Twelve supporting pentagonal facets, normal to icosahedron vertices.
facets=[]
for s,t in product((-1,1),repeat=2):
 for normal in [(ZERO,mul(I(s),phi2),I(2*t)),
                (mul(I(s),phi2),I(2*t),ZERO),
                (I(2*t),ZERO,mul(I(s),phi2))]:
  vals=[dot(normal,v) for v in vertices]
  mx=vals[0]
  for z in vals[1:]:
   if sign(add(z,neg(mx)))>0:mx=z
  fv=tuple(k for k,z in enumerate(vals) if z==mx)
  assert len(fv)==5, (normal,len(fv))
  facets.append(fv)
assert len(set(facets))==12

hist=Counter(); angles=Counter()
for pat in patterns:
 rays=[]
 for i,j in combinations(range(10),2):
  w=cross(planes[i],planes[j])
  for pole in (-1,1):
   r=scale(I(pole),w)
   if all(s*sign(dot(v,r))>=0 for s,v in zip(pat,planes)):
    rays.append((r,(i,j)))
 assert len(rays)>=3
 u=vadd(*(x[0] for x in rays))
 assert all(sign(dot(v,u))==s for s,v in zip(pat,planes))
 count=sum(min(sign(dot(vertices[k],u)) for k in f)<0<max(sign(dot(vertices[k],u)) for k in f) for f in facets)
 cosines=[]
 for w,(i,j) in rays:
  # cos(interior angle) = minus signed dot of inward unit face normals
  pair=mul(I(-pat[i]*pat[j]),dot(planes[i],planes[j]))
  assert pair[0]%4==0 and pair[1]%4==0
  cosines.append((pair[0]//4,pair[1]//4))
 hist[(count,len(rays))]+=1
 angles[(count,len(rays),tuple(sorted(Counter(cosines).items())))]+=1
print('chamber_types',sorted(hist.items()))
print('interior_angle_cosines',sorted(angles.items()))
assert hist=={(6,6):20,(8,3):60,(10,5):12},hist
assert angles=={
 (6,6,(((-1,0),3),((0,-1),3))):20,
 (8,3,(((0,1),1),((1,0),2))):60,
 (10,5,(((-1,0),5),)):12
},angles
print('EXACT CERTIFICATE PASS: 92 chambers, 20 spherical hexagons, 60 triangles, 12 pentagons')
