"""Exact combinatorial certificate for the random-view vertex count of the regular icosahedron.
No external dependencies. Operations lie in Z[phi], phi^2=phi+1.
"""
from itertools import combinations, product
from collections import defaultdict, Counter
from math import sqrt, pi, acos

# Exact a+b*phi arithmetic.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def sq(x):return mul(x,x)
def sign(x):
 a,b=x
 if b==0:return (a>0)-(a<0)
 # sign(a+b phi), phi irrational between 1 and 2:
 # root of z^2-z-1; x=a+b phi. Rational threshold -a/b.
 if a==0:return (b>0)-(b<0)
 if a*b>0:return (b>0)-(b<0)
 # compare phi against -a/b: phi>r iff r^2-r-1<0 for r>0 and r in (1,2), etc.
 A=abs(a);B=abs(b)
 if A<=B:return (b>0)-(b<0) # phi>1
 if A>=2*B:return (a>0)-(a<0) # phi<2
 # phi > A/B iff A^2 - AB - B^2 <0.
 comp=A*A-A*B-B*B
 return ((b>0)-(b<0)) * (-1 if comp>0 else 1)
zero=(0,0);one=(1,0);phi=(0,1)
def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vneg(a):return tuple(neg(x) for x in a)
def vsub(a,b):return vadd(a,vneg(b))
def dot(a,b):
 z=zero
 for x,y in zip(a,b):z=add(z,mul(x,y))
 return z
def cross(u,v):
 return (sub(mul(u[1],v[2]),mul(u[2],v[1])),sub(mul(u[2],v[0]),mul(u[0],v[2])),sub(mul(u[0],v[1]),mul(u[1],v[0])))
def N(x):return tuple(neg(t) for t in x)

verts=[]
for a,b in product((-1,1),repeat=2):
 for vec in [(zero,(a,0),(0,b)),((a,0),(0,b),zero),((0,b),zero,(a,0))]:
  verts.append(tuple(vec))
assert len(set(verts))==12
edges={e for e in combinations(range(12),2) if dot(vsub(verts[e[0]],verts[e[1]]),vsub(verts[e[0]],verts[e[1]]))==(4,0)}
assert len(edges)==30, len(edges)
faces=[tri for tri in combinations(range(12),3) if all(tuple(sorted(x)) in edges for x in combinations(tri,2))]
assert len(faces)==20,len(faces)
faceN=[vadd(vadd(verts[a],verts[b]),verts[c]) for a,b,c in faces]
assert all(dot(n,n)==dot(faceN[0],faceN[0]) for n in faceN)
axes=[];facetaxis=[]
for n in faceN:
 for i,m in enumerate(axes):
  if n==m or n==N(m):facetaxis.append((i,1 if n==m else -1));break
 else:axes.append(n);facetaxis.append((len(axes)-1,1))
assert len(axes)==10
edgeFaces=defaultdict(list)
for f,tri in enumerate(faces):
 for e in combinations(tri,2):edgeFaces[tuple(sorted(e))].append(f)
assert len(edgeFaces)==30 and all(len(ff)==2 for ff in edgeFaces.values())

def typ(i,j,sg):
 d=dot(axes[i],axes[j]);norm=dot(axes[i],axes[i]);dd=sq(d);rr=sq(norm)
 if mul((9,0),dd)==rr:k='b' # arccos 1/3
 elif mul((9,0),dd)==mul((5,0),rr):k='a' # arccos sqrt5/3
 else:raise AssertionError(('bad correlation',d,norm))
 s=sign(d)*sg[i]*sg[j]
 return k + ('+' if s>0 else '-')

region=defaultdict(list)
for i,j in combinations(range(10),2):
 c=cross(axes[i],axes[j]);assert c!=(zero,zero,zero)
 ds=[sign(dot(c,axes[k])) for k in range(10)]
 assert all(x!=0 for k,x in enumerate(ds) if k not in (i,j))
 for orientation in (1,-1):
  for si,sj in product((-1,1),repeat=2):
   sg=tuple(si if k==i else sj if k==j else orientation*ds[k] for k in range(10))
   region[sg].append((i,j,orientation))

assert len(region)==92,len(region)
assert sum(len(v) for v in region.values())==360
counts=Counter();profiles=Counter();allangles=Counter()
for sg, corners in region.items():
 assert len(set(corners))==len(corners)
 # silhouette if two neighboring face signs differ.
 faceSig=[sg[i]*j for i,j in facetaxis]
 Nedges=sum(faceSig[ff[0]]!=faceSig[ff[1]] for ff in edgeFaces.values())
 angles=Counter(typ(i,j,sg) for i,j,_ in corners)
 counts[Nedges]+=1
 profiles[(Nedges,len(corners),tuple(sorted(angles.items())))]+=1
 allangles.update(angles)
assert counts=={6:20,8:60,10:12},counts
assert profiles=={
 (6,6,(('a+',3),('b+',3))):20,
 (8,3,(('a-',1),('b-',2))):60,
 (10,5,(('b+',5),)):12
},profiles

alpha=acos(sqrt(5)/3);beta=acos(1/3)
p6=10-15*(alpha+beta)/pi
p8=15*(alpha+2*beta-pi)/pi
p10=6-15*beta/pi
assert min(p6,p8,p10)>0 and abs(p6+p8+p10-1)<1e-12
print('EXACT_ICOSAHEDRON_SHADOW_TYPE_CERTIFICATE_OK')
print('vertices',len(verts),'edges',len(edges),'faces',len(faces),'unoriented facet axes',len(axes))
print('cells',len(region),'vertex incidence',sum(map(len,region.values())))
print('profiles',sorted(profiles.items()))
print('probabilities',p6,p8,p10,'mean',6*p6+8*p8+10*p10)

# Separate geometric test: construct projected 2D convex hulls directly, without face signs.
import random
rr=random.Random(240417)
Vf=[tuple(float(a+b*(1+sqrt(5))/2) for a,b in v) for v in verts]
def count_projected_hull():
 u=[rr.gauss(0,1) for _ in range(3)];normu=sqrt(sum(t*t for t in u));u=[t/normu for t in u]
 f=[0.,0.,1.] if abs(u[2])<0.8 else [0.,1.,0.]
 e1=[u[1]*f[2]-u[2]*f[1],u[2]*f[0]-u[0]*f[2],u[0]*f[1]-u[1]*f[0]]
 norm=sqrt(sum(t*t for t in e1));e1=[t/norm for t in e1]
 e2=[u[1]*e1[2]-u[2]*e1[1],u[2]*e1[0]-u[0]*e1[2],u[0]*e1[1]-u[1]*e1[0]]
 points=sorted((sum(x*y for x,y in zip(v,e1)),sum(x*y for x,y in zip(v,e2))) for v in Vf)
 def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lower=[]
 for p in points:
  while len(lower)>1 and turn(lower[-2],lower[-1],p)<1e-10:lower.pop()
  lower.append(p)
 upper=[]
 for p in reversed(points):
  while len(upper)>1 and turn(upper[-2],upper[-1],p)<1e-10:upper.pop()
  upper.append(p)
 return len(lower)+len(upper)-2
ct=Counter(count_projected_hull() for _ in range(36000))
assert set(ct)=={6,8,10},ct
assert abs(ct[6]/36000-p6)<0.011 and abs(ct[8]/36000-p8)<0.011 and abs(ct[10]/36000-p10)<0.011,ct
print('INDEPENDENT_ORTHOGONAL_PROJECTION_HULL_TEST_OK',dict(sorted(ct.items())))
