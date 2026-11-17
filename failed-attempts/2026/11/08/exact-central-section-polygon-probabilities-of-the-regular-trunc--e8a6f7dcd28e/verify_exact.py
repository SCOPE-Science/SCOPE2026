"""Exact chamber count for normals of a regular truncated cube."""
from itertools import product, combinations
from collections import Counter, defaultdict
from math import acos,pi,sqrt
Z=(0,0);ONE=(1,0);T=(-1,1)
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sign(x):
 a,b=x
 if a==0:return (b>0)-(b<0)
 if b==0:return (a>0)-(a<0)
 if (a>0)==(b>0):return (a>0)*2-1
 d=a*a-2*b*b
 return ((a>0)*2-1)*(1 if d>0 else -1)
def scale(n,x):return (n*x[0],n*x[1])
def vadd(x,y):return tuple(add(a,b) for a,b in zip(x,y))
def vscale(n,x):return tuple(scale(n,a) for a in x)
def cross(x,y):return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def dot(x,y):return add(add(mul(x[0],y[0]),mul(x[1],y[1])),mul(x[2],y[2]))
def sq(x):return dot(x,x)
V=[]
for k in range(3):
 for ss in product((-1,1),repeat=3):V.append(tuple(scale(ss[i],T if i==k else ONE) for i in range(3)))
# all 24 different, 12 antipodal normal lines
assert len(set(V))==24
N=[]
for v in V:
 if v not in N and tuple(neg(x) for x in v) not in N:N.append(v)
assert len(N)==12
# minimal squared distance yields edges
Ds={(i,j):sq(tuple(sub(a,b) for a,b in zip(V[i],V[j]))) for i,j in combinations(range(24),2)}
mind=min(Ds.values(),key=lambda q:q[0]+q[1]*sqrt(2))
E=[(i,j) for (i,j),dd in Ds.items() if dd==mind]
assert len(E)==36,(mind,len(E))
# 12 circles, 132 transverse intersection points no triple in Q(sqrt2)
C=[]
for i,j in combinations(range(12),2):
 x=cross(N[i],N[j]);assert any(sign(xx) for xx in x)
 for v in (x,tuple(neg(y) for y in x)):
  if not any(all(sign(c)==0 for c in cross(v,w)) and sign(dot(v,w))>0 for w in C):C.append(v)
assert len(C)==132,len(C)
assert all(sum(sign(dot(c,n))==0 for n in N)==2 for c in C)
# enumerate four infinitesimal local sectors at every crossing via exact witness c*(100000)+eps*(sign_i n_i + sign_j n_j).
patterns={}
for c in C:
 i,j=(k for k in range(12) if sign(dot(c,N[k]))==0)
 for a,b in product((-1,1),repeat=2):
  w=vadd(vscale(100000,c),vadd(vscale(a,N[i]),vscale(b,N[j])))
  signs=tuple(sign(dot(w,n)) for n in N)
  assert all(t in (-1,1) for t in signs)
  assert signs[i]==a and signs[j]==b
  patterns[signs]=w
assert len(patterns)==134,len(patterns)
# Each convex spherical chamber is bounded by pair-crossing vertices satisfying inequalities.
# Each corner's interior angle has complementary arccos of signed normal dot.
# Normal squared radius common: norm^2 = (5,-2) and r= signed dot / norm^2
Q=sq(N[0]); assert Q==(5,-2)
counts=Counter(); classes=defaultdict(Counter); corners=defaultdict(Counter); vert_counts=Counter()
for signs,w in patterns.items():
 vertex_sign=tuple(sign(dot(v,w)) for v in V)
 section_edges=sum(vertex_sign[i]!=vertex_sign[j] for i,j in E)
 corners_in=[]
 for c in C:
  ds=[sign(dot(c,n))*sn for n,sn in zip(N,signs)]
  if min(ds)>=0:
   ii=[k for k,d in enumerate(ds) if d==0]
   assert len(ii)==2
   i,j=ii
   q=scale(signs[i]*signs[j],dot(N[i],N[j]))
   # rationalize divided Q=(5-2sqrt2) => numerator (5+2sqrt2)*q / 17
   rat=mul(q,(5,2))
   assert abs((rat[0]+rat[1]*sqrt(2))/17)<1
   corners_in.append(rat)
 assert len(corners_in)>=3
 area=2*pi-sum(acos((a+b*sqrt(2))/17) for a,b in corners_in)
 assert area>0 and area<2*pi
 counts[section_edges]+=1
 classes[section_edges][tuple(sorted(corners_in))]+=1
 corners[section_edges].update(corners_in)
 vert_counts[(section_edges,len(corners_in))]+=1
# Independent, explicitly specified finite certificate targets, not mere printed observations.
def pattern(seq): return tuple(sorted(seq))
expected_classes={
 4:Counter({pattern([(7,-4)]*4):6}),
 6:Counter({pattern([(-7,4)]*2+[(3,8)]+[(5,2)]*2):24,
            pattern([(3,8)]*3+[(7,-4)]*3):8}),
 8:Counter({pattern([(-7,4),(-5,-2),(-3,-8)]):48,
            pattern([(-5,-2)]*2+[(3,8),(7,-4)]):24}),
 10:Counter({pattern([(-3,-8)]+[(5,2)]*2+[(7,-4)]):24})
}
assert set(classes)==set(expected_classes)
assert all(classes[n]==expected_classes[n] for n in expected_classes)
assert counts==Counter({4:6,6:32,8:72,10:24})
probs={n:sum(k*(2*pi-sum(acos((a+b*sqrt(2))/17) for a,b in sig)) for sig,k in cls.items())/(4*pi) for n,cls in classes.items()}
assert abs(sum(probs.values())-1)<1e-12
angle_gamma=acos((3+8*sqrt(2))/17)
assert abs(sum(n*probs[n] for n in probs)-36*angle_gamma/pi)<1e-12
print('magnitude minimum distance',mind,'edges',len(E),'chambers',len(patterns),'section count',counts,'sides of chambers',vert_counts)
for n in sorted(counts):
 print('N',n,'chamber classes',classes[n])
 print('N',n,'corner signed cos (num A+B√2)/17',corners[n])
 print('N',n,'probability',sum(k*(2*pi-sum(acos((a+b*sqrt(2))/17) for a,b in alpha)) for alpha,k in classes[n].items())/(4*pi))
print('TOTAL',sum(sum(k*(2*pi-sum(acos((a+b*sqrt(2))/17) for a,b in alpha)) for alpha,k in cls.items()) for cls in classes.values())/(4*pi))
