"""Exact Z[phi] chamber certificate for uniform pentagonal antiprism shadows.
Run: python3 pentagonal_antiprism_shadow_verify.py  (stdlib only).
"""
from itertools import product,combinations
from collections import Counter,defaultdict
from math import acos,pi,sqrt
Z=(0,0); ONE=(1,0); PHI=(0,1); SQRT5=(-1,2)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c+b*d,a*d+b*c+b*d)
def scale(k,x):return (k*x[0],k*x[1])
def sgn(x):
 a,b=x;A=2*a+b
 if b==0:return (a>0)-(a<0)
 if A==0:return (b>0)-(b<0)
 if (A>0)==(b>0):return (A>0)-(A<0)
 return ((A>0)-(A<0)) if A*A>5*b*b else ((b>0)-(b<0))
def vn(x):return tuple(neg(t) for t in x)
def dot(x,y):
 t=Z
 for a,b in zip(x,y):t=add(t,mul(a,b))
 return t
def cross(x,y):
 return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def zero(x):return all(t==Z for t in x)

# The physical normals are: top e_z and n_j=(cos(j*pi/5), sin(j*pi/5),(-1)^(j+1)d),
# with j=0,...,9 and d=1-cos(pi/5). Since n_(j+5)=-n_j, there are six axes.
# Scaling coordinates of all normals by the same positive invertible diagonal
# operator does not alter the feasible sign patterns/chamber vertex counts.
# In the transformed coordinates H_j lie in Z[phi].
D=(2,-1) # 2d=2-phi
H=[(Z,Z,ONE),((2,0),Z,neg(D)),(PHI,(2,0),D),
   ((-1,1),(0,2),neg(D)),((1,-1),(0,2),D),(neg(PHI),(2,0),neg(D))]
assert len(H)==6
# Each pair of axes meets in two directed rays, with no triple concurrence.
R=[]
for i,j in combinations(range(6),2):
 c=cross(H[i],H[j]);assert not zero(c)
 for v in (c,vn(c)):
  assert not any(zero(cross(v,w)) and sgn(dot(v,w))>0 for w in R), 'coincident rays or triple axes'
  R.append(v)
assert len(R)==30
SIGNS=[tuple(sgn(dot(n,v)) for n in H) for v in R]
assert all(sum(z==0 for z in sig)==2 for sig in SIGNS)

# Adjacent sides of the ten lateral faces form a decagon.
# Each odd-indexed face meets the top pentagon; each even face meets the bottom.
def face_signs(bits):
 side=[bits[k+1] for k in range(5)]+[-bits[k+1] for k in range(5)]
 return bits[0],-bits[0],side

# The exact side-side normalized dot products are in {+/-1/3,+/-sqrt(5)/3}.
# For lateral normals j,k, the denominator after multiplying by 4 is 4+D^2.
DEN=add((4,0),mul(D,D))
COS2=[(2,0),PHI,(-1,1),(1,-1),neg(PHI)] # 2cos(m*pi/5), 0<=m<=4

def angle_symbol(i,j,bi,bj):
 t=bi*bj
 if i==0 or j==0:
  k=j if i==0 else i
  # z of side normal = (-1)^j d with j=(k-1), i.e. odd k => +d.
  st=t*(1 if k%2==0 else -1)
  return 'P' if st>0 else 'C'  # P=pi-C, C=acos(rho)
 k=i-1;l=j-1
 co=scale(2,COS2[abs(k-l)]) # 4*cos(angle diff)
 num=add(co,scale((-1)**(k+l),mul(D,D)))
 num=scale(t,num)
 for letter,s in [('A',ONE),('B',SQRT5),('D',neg(ONE)),('E',neg(SQRT5))]:
  if scale(3,num)==mul(DEN,s):return letter
 raise ValueError(('unexpected dot product',i,j,bi,bj,num,DEN))

num_cells=Counter();types=defaultdict(Counter);examples={}
for bits in product((-1,1),repeat=6):
 vertices=[j for j,s in enumerate(SIGNS) if all(b*x>=0 for b,x in zip(bits,s))]
 if len(vertices)<3:continue
 top,bottom,side=face_signs(bits)
 count=sum(side[k]!=side[(k+1)%10] for k in range(10))
 count+=sum(side[k]!=top for k in range(1,10,2))
 count+=sum(side[k]!=bottom for k in range(0,10,2))
 labels=[]
 for v in vertices:
  i,j=(k for k,z in enumerate(SIGNS[v]) if z==0)
  labels.append(angle_symbol(i,j,bits[i],bits[j]))
 signature=''.join(sorted(labels))
 num_cells[count]+=1;types[count][signature]+=1
 examples.setdefault((count,signature),''.join('1' if b>0 else '0' for b in bits))
assert num_cells==Counter({6:10,8:20,10:2}),num_cells
assert types=={6:Counter({'ABBPP':10}),8:Counter({'CCE':10,'DDE':10}),10:Counter({'AAAAA':2})},types
A=acos(-1/3);B=acos(-sqrt(5)/3);C=acos((3-sqrt(5))/4/sqrt(1+((3-sqrt(5))/4)**2))
Dangle=acos(1/3);E=acos(sqrt(5)/3)
area6=A+2*B+2*(pi-C)-3*pi
area8a=2*C+E-pi
area8b=2*Dangle+E-pi
area10=5*A-3*pi
p6=10*area6/(4*pi)
p8=10*(area8a+area8b)/(4*pi)
p10=2*area10/(4*pi)
assert all(q>0 for q in (area6,area8a,area8b,area10))
assert abs(p6+p8+p10-1)<1e-12
print('EXACT_PENTAGONAL_ANTIPRISM_CHAMBERS_OK rays=30 cells=32')
print('signature_counts', {k:dict(v) for k,v in types.items()})
print('example_masks',examples)
print('probabilities',{'6':p6,'8':p8,'10':p10},'expected',6*p6+8*p8+10*p10)
print('PENTAGONAL_ANTIPRISM_SILHOUETTE_OK')

# Independent geometric check on projected point configurations, not part
# of the proof of the continuum claim.
if __name__=='__main__':
 from random import Random
 from math import cos,sin,hypot
 rng=Random(20261104)
 xyz=[]
 for j in range(5):
  t=2*pi*j/5
  xyz.append((cos(t),sin(t),.5))
  xyz.append((cos(t+pi/5),sin(t+pi/5),-.5))
 def convex_hull_size(xy):
  pts=sorted(xy)
  def cr(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
  lo=[]
  for q in pts:
   while len(lo)>=2 and cr(lo[-2],lo[-1],q)<=0:lo.pop()
   lo.append(q)
  up=[]
  for q in pts[::-1]:
   while len(up)>=2 and cr(up[-2],up[-1],q)<=0:up.pop()
   up.append(q)
  return len(lo)+len(up)-2
 def sd(j,u):
  d=1-cos(pi/5)
  if j==0:return u[2]
  t=(j-1)*pi/5
  return cos(t)*u[0]+sin(t)*u[1]+(-1 if j%2 else 1)*d*u[2]
 trial=10000
 for _ in range(trial):
  u=[rng.gauss(0,1) for i in range(3)]
  norm=sqrt(sum(x*x for x in u));u=[x/norm for x in u]
  ex=(-u[1],u[0],0)
  if hypot(ex[0],ex[1])<1e-7:continue
  t=hypot(ex[0],ex[1]);ex=tuple(x/t for x in ex)
  ey=(u[1]*ex[2]-u[2]*ex[1],u[2]*ex[0]-u[0]*ex[2],u[0]*ex[1]-u[1]*ex[0])
  xy=[(sum(v[i]*ex[i] for i in range(3)),sum(v[i]*ey[i] for i in range(3))) for v in xyz]
  hull=convex_hull_size(xy)
  bs=[1 if sd(j,u)>0 else -1 for j in range(6)]
  top,bottom,side=face_signs(bs)
  cut=sum(side[k]!=side[(k+1)%10] for k in range(10))
  cut+=sum(side[k]!=top for k in range(1,10,2))
  cut+=sum(side[k]!=bottom for k in range(0,10,2))
  assert hull==cut,(u,hull,cut)
 print('INDEPENDENT_PROJECTED_HULL_CROSSCHECK_OK',trial)
# Separate cross-check against the elementary exterior-dihedral expectation
# formula for all right regular antiprisms (not used to derive the law).
from math import cos
c=cos(pi/5); d=1-c; h=.5
m=10/pi*(acos(d/sqrt(4*h*h+d*d))+acos((4*c*h*h-d*d)/(4*h*h+d*d)))
assert abs(m-(6*p6+8*p8+10*p10))<1e-12
print('MEAN_FROM_TWO_EDGE_ORBITS_OK',format(m,'.15f'))
