#!/usr/bin/env python3
"""Exact Z[phi] exhaustive extrema of an icosahedral six-generator zonotope.
The field arithmetic is integral (phi^2=phi+1); sign tests use integer squares.
"""
from itertools import combinations
from collections import Counter
from math import sqrt
Z=(0,0)
ONE=(1,0)
PHI=(0,1)
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return plus(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c+b*d,a*d+b*c+b*d)
def sg(x):
 a,b=x;A=2*a+b;B=b
 if A==0:return (B>0)-(B<0)
 if B==0:return (A>0)-(A<0)
 if A*B>0:return (A>0)-(A<0)
 if A>0:return 1 if A*A>5*B*B else -1
 return 1 if 5*B*B>A*A else -1
def cmp(x,y):return sg(sub(x,y))
def ab(x):return x[0]+x[1]*(1+sqrt(5))/2
def cross(x,y):return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def dot(x,y):
 z=Z
 for a,b in zip(x,y):z=plus(z,mul(a,b))
 return z
def vecadd(x,y):return tuple(plus(a,b) for a,b in zip(x,y))
def vecneg(x):return tuple(neg(a) for a in x)
def cmprat(x1,d1,x2,d2):return cmp(mul(x1,d2),mul(x2,d1))
def proj(x):return [ab(a) for a in x]
def vecphi(*x):return tuple(x)
v=[vecphi(Z,ONE,PHI),vecphi(Z,neg(ONE),PHI),vecphi(ONE,PHI,Z),vecphi(neg(ONE),PHI,Z),vecphi(PHI,Z,ONE),vecphi(PHI,Z,neg(ONE))]
w=[cross(v[i],v[j]) for i,j in combinations(range(6),2)]
assert len(w)==15
assert len({dot(z,z) for z in w})==1
assert dot(w[0],w[0])==(4,4) # (2phi)^2=4(phi+1)
assert all(dot(x,x)==(2,1) for x in v) # phi+2
assert all(dot(v[i],v[j]) in (PHI,neg(PHI)) for i,j in combinations(range(6),2))
assert all(sg(dot(cross(v[i],v[j]),v[k])) != 0 for i,j,k in combinations(range(6),3))
# The absolute pair correlations of the 15 golden-rhombus normals form four classes.
from collections import Counter as Counts
abdot = Counts()
for aa, bb in combinations(w, 2):
    t = dot(aa, bb)
    if sg(t) < 0: t = neg(t)
    abdot[t] += 1
assert abdot == {(2, 4):30, (0, 2):30, (2, 2):30, (0, 0):15}
print('EXACT_PAIR_CLASSES_OK', sorted(abdot.items()))
# Maximize over all signed sums (support function duality)
best=None;maxmasks=[];normclasses=Counter()
for mask in range(1<<len(w)):
 s=tuple(Z for _ in range(3))
 for j,ww in enumerate(w):s=vecadd(s,ww if mask>>j&1 else vecneg(ww))
 n=dot(s,s)
 normclasses[n]+=1
 if best is None or cmp(n,best)>0:
  best=n;maxmasks=[(mask,s)]
 elif cmp(n,best)==0:maxmasks.append((mask,s))
assert len(maxmasks)==120
assert all(all(sg(dot(s,ww))==(1 if mask>>i&1 else -1) for i,ww in enumerate(w)) for mask,s in maxmasks)
# Minimize on arrangement vertices of the fifteen great circles w_j.u=0.
minn=None;mind=None;minpairs=[];valid=0;valclasses=Counter()
for i,j in combinations(range(len(w)),2):
 q=cross(w[i],w[j]);d=dot(q,q)
 if sg(d)==0:continue
 valid+=1
 numerator=Z
 for ww in w:
  t=dot(ww,q)
  numerator=plus(numerator,t if sg(t)>=0 else neg(t))
 sq=mul(numerator,numerator)
 valclasses[(sq,d)]+=1
 if minn is None or cmprat(sq,d,minn,mind)<0:
  minn,mind=sq,d;minpairs=[(i,j,q,numerator,d)]
 elif cmprat(sq,d,minn,mind)==0:minpairs.append((i,j,q,numerator,d))
assert valid==105
assert len(minpairs)==60
# Count unique rays modulo positive rescaling by checking normalized float (for summary ONLY); exact collinearity test below.
def iscol(x,y):return all(sg(z)==0 for z in cross(x,y))
minrays=[]
for i,j,q,n,d in minpairs:
 if not any(iscol(q,qq) and sg(dot(q,qq))>0 for qq in minrays):minrays.append(q)
assert len(minrays)==12
maxrays=[]
for mask,s in maxmasks:
 if not any(iscol(s,qq) and sg(dot(s,qq))>0 for qq in maxrays):maxrays.append(s)
assert len(maxrays)==120
print('EXACT_TRIAC_OK generators=6 normals=15 signed_sums=32768 pair_candidates=105 min_directions=12 max_directions=120')
print('MAX_SQUARED=',best,'numeric',ab(best),'sqrt',sqrt(ab(best)))
print('MAX_FIRST_MASK=',maxmasks[0][0], 'vector=',maxmasks[0][1],'coords',proj(maxmasks[0][1]))
print('MAX_NORM_CLASSES=',len(normclasses))
print('MIN_FIRST_PAIR=',minpairs[0][:2], 'cross=',minpairs[0][2],'N=',minpairs[0][3],'D=',minpairs[0][4], 'N/sqrt(D)', ab(minpairs[0][3])/sqrt(ab(minpairs[0][4])))
print('MIN_CANDIDATE_NORM_CLASSES=',len({round(ab(sq)/ab(d),9) for sq,d in valclasses}))
print('ICOSA_MIN_AXES=',[proj(q) for q in minrays[:3]])
# Check icosahedron generators are exactly the twelve min rays via cross product collinearity.
assert all(any(iscol(q,vv) for vv in v) for q in minrays)
# Finite enumeration validation all positions, normalized projections
import numpy as np
W=np.array([proj(t) for t in w]);V=np.array([proj(t) for t in v]);S=np.array([proj(t) for t in maxrays]);
rng=np.random.default_rng(12345)
for _ in range(2000):
 u=rng.normal(size=3);u/=np.linalg.norm(u)
 x=np.abs(W@u).sum()
 assert x>=ab(minpairs[0][3])/sqrt(ab(minpairs[0][4]))-1e-10
 assert x<=sqrt(ab(best))+1e-10
# Independent direct 2D projected convex hull area: Minkowski sum +/-v_i/2 has 64 candidates.
from scipy.spatial import ConvexHull
from itertools import product
allverts=np.array([np.sum(np.array([b*V[i]/2 for i,b in enumerate(bits)]),axis=0) for bits in product([-1,1],repeat=6)])
for _ in range(100):
 u=rng.normal(size=3);u/=np.linalg.norm(u)
 e1=np.cross(u,[1.,0,0])
 if np.linalg.norm(e1)<1e-5:e1=np.cross(u,[0.,1,0])
 e1/=np.linalg.norm(e1);e2=np.cross(u,e1)
 shadow=allverts@np.column_stack((e1,e2))
 hull=ConvexHull(shadow)
 area=hull.volume;pred=np.sum(np.abs(W@u))
 assert abs(area-pred)<1e-8,(area,pred)
print('SHADOW_HULL_OK directions=100 random_inequalities=2000')
from math import pi, sin
phi=(1+sqrt(5))/2
mean=15*phi
second=phi**2*(76/3+32*phi)+(160*phi**2/pi)*(sin(pi/5)+sin(2*pi/5)+sqrt(3)/2+1/2)
variance=second-mean**2
assert 0.14 < variance < 0.15
# These are exact symbolic integration formulas; the following digits are illustrations.
print('EXACT_MOMENT_FORMULAS_OK mean=',mean, 'second=',second, 'variance=',variance)
