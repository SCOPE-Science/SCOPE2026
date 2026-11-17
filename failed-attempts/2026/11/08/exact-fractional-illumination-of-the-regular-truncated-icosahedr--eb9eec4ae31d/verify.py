from fractions import Fraction as Q
from itertools import product,combinations
from collections import Counter
import math

class R:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):self.a=Q(a);self.b=Q(b)
 def __add__(self,t):
  t=c(t);return R(self.a+t.a,self.b+t.b)
 __radd__=__add__
 def __neg__(self):return R(-self.a,-self.b)
 def __sub__(self,t):return self+-c(t)
 def __rsub__(self,t):return c(t)+-self
 def __mul__(self,t):
  t=c(t);return R(self.a*t.a+self.b*t.b, self.a*t.b+self.b*t.a+self.b*t.b)
 __rmul__=__mul__
 def sign(self):
  # a + b phi = (2a+b+b sqrt(5))/2
  A=2*self.a+self.b; B=self.b
  if B==0:return (A>0)-(A<0)
  if A==0:return (B>0)-(B<0)
  if (A>0)==(B>0):return (A>0)-(A<0)
  h=A*A-5*B*B
  assert h!=0
  return (A>0)-(A<0) if h>0 else (B>0)-(B<0)
 def __eq__(self,t):
  t=c(t);return self.a==t.a and self.b==t.b
 def __repr__(self):return f'({self.a}+{self.b}phi)'
def c(t):return t if isinstance(t,R) else R(t)
Z=R(); O=R(1); PH=R(0,1)
def vec(*a):return tuple(map(c,a))
def dot(u,v):return sum((x*y for x,y in zip(u,v)),Z)
def cross(u,v):return vec(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def diff(u,v):return tuple(a-b for a,b in zip(u,v))
def opp(u):return tuple(-a for a in u)
def sqdist(a,b):return dot(diff(a,b),diff(a,b))
A=[vec(Z,R(i),PH*j) for i,j in product((-1,1),repeat=2)]+[vec(R(i),PH*j,Z) for i,j in product((-1,1),repeat=2)]+[vec(PH*i,Z,R(j)) for i,j in product((-1,1),repeat=2)]
assert len(A)==12 and len(set(map(str,A)))==12
E=[p for p in combinations(range(12),2) if sqdist(A[p[0]],A[p[1]])==4]
F=[t for t in combinations(range(12),3) if all(tuple(sorted(pair)) in E for pair in combinations(t,2))]
assert (len(E),len(F))==(30,20)
EF={e:[k for k,f in enumerate(F) if set(e)<=set(f)] for e in E}
assert all(len(s)==2 for s in EF.values())
N=A+[tuple(sum((A[j][k] for j in face),Z) for k in range(3)) for face in F]
assert len(N)==32
V=[(u,12+EF[e][0],12+EF[e][1]) for e in E for u in e]
assert len(V)==60
# Independently check the 32 claimed supporting facets of the truncated solid.
T=[tuple((2*A[u][j]+A[v][j])*Q(1,3) for j in range(3)) for e in E for u,v in (e,(e[1],e[0]))]
assert len(T)==60
for k,n in enumerate(N):
 vals=[dot(n,p) for p in T]
 top=next(v for v in vals if all((v-w).sign()>=0 for w in vals))
 eq=[j for j,val in enumerate(vals) if val==top]
 assert len(eq)==(5 if k<12 else 6),(k,len(eq))
 assert all((top-val).sign()>=0 for val in vals)
assert all(sum(dot(n,T[i])==next(val for val in [dot(n,p) for p in T] if all((val-dot(n,q)).sign()>=0 for q in T)) for n in N)==3 for i in range(60))
# pair 32 antipodal normals into 16 distinct planes
representatives=[]
for i in range(32):
 if not any(cross(N[i],N[j])==(Z,Z,Z) for j in representatives):representatives.append(i)
assert len(representatives)==16
L=[N[i] for i in representatives]
# vertices of affine 16-line arrangement in chart d=(x,y,1)
intersections=[]
for i,j in combinations(range(len(L)),2):
 r=cross(L[i],L[j])
 if r[2]==0:continue
 if r[2].sign()<0:r=opp(r)
 assert r[2].sign()>0
 if not any(cross(r,p)==(Z,Z,Z) for p in intersections):intersections.append(r)
mults=[sum(dot(n,p)==0 for n in L) for p in intersections]
expected=1+len(L)+sum(m-1 for m in mults)
print('lines',len(L),'intersection vertices',len(intersections),'multiplicities',dict(Counter(mults)),'Euler regions each hemisphere',expected)
# Every region in an affine line arrangement containing at least two nonparallel lines has a vertex.
# Generate one point in every local angular sector by perturbations using 256 lattice directions.
ang=[]
for k in range(-32,33):
 for dx,dy in [(32,k),(-32,k),(k,32),(k,-32)]:
  if dx and dy and math.gcd(dx,dy)>1:
   dx//=math.gcd(dx,dy);dy//=math.gcd(dx,dy)
  ang.append((dx,dy))
ang=list(dict.fromkeys(ang))

patterns={}
for r in intersections:
 base=tuple(dot(n,r).sign() for n in N)
 zeros=[i for i,s in enumerate(base) if not s]
 for dx,dy in ang:
  sig=list(base)
  for i in zeros:
   v=N[i][0]*dx+N[i][1]*dy
   sig[i]=v.sign()
  if not all(sig):continue
  bits=tuple(sig)
  if bits not in patterns:patterns[bits]=(r,(dx,dy))

plus=list(patterns)
print('sampled planar cells',len(plus),'expected',expected)
assert len(plus)==expected,(len(plus),expected)
allpatterns={p for p in plus}|{tuple(-x for x in p) for p in plus}
print('sphere sign regions',len(allpatterns))
counts=Counter()
sets={}
for sig in allpatterns:
 cov=frozenset(i for i,triple in enumerate(V) if all(sig[j]<0 for j in triple))
 counts[len(cov)]+=1
 sets[cov]=sig
print('illumination size spectrum',sorted(counts.items()),'distinct illuminating subsets',len(sets))
assert max(counts)==21
# face centered directions each cover 21, so max achieved.
for k in range(12,32):
 d=opp(N[k]); sig=tuple(dot(n,d).sign() for n in N)
 assert all(s!=0 for s in sig)
 assert sum(all(sig[j]<0 for j in tri) for tri in V)==21
print('20 face normals attain 21')
face_dirs=[opp(N[k]) for k in range(12,32)]
counts_per_vertex=[sum(all(dot(N[j],d).sign()<0 for j in triple) for d in face_dirs) for triple in V]
print('face direction weights per vertex',Counter(counts_per_vertex))
assert set(counts_per_vertex)=={7}

# 4 original vertices directions illuminate all; 3 impossible because max 21 and all coverage-size sets fail triple covering
C=[]
for u in A:
 sig=tuple(dot(n,u).sign() for n in N)
 assert all(s!=0 for s in sig)
 C.append(frozenset(i for i,tri in enumerate(V) if all(sig[j]<0 for j in tri)))
assert len(set.union(*(set(C[k]) for k in [0,1,5,7])))==60
print('four exact vertex-axis directions', [0,1,5,7], 'cover sizes',[len(C[k]) for k in [0,1,5,7]])
# all cells have covered count either 20 or21; test 3-set impossibility via bit masks
candidates=list(sets)
masks=[]
for s in candidates:
 b=sum(1<<i for i in s)
 masks.append(b)
whole=(1<<60)-1
# strongest easy obstruction: if triple cover, each size>=18; check every pair and third
triplets=0
for i,a in enumerate(masks):
 for j in range(i,len(masks)):
  b=a|masks[j]
  if b.bit_count()<39:continue
  missing=whole^b
  if any((m&missing)==missing for m in masks):
   triplets+=1
print('3-cover candidates',triplets)
assert triplets==0
print('EXACT_OK')
