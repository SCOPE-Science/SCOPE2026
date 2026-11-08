"""Exhaustive arithmetic classification of smooth minimum nontrivial blocking quartics over F3.
No third-party code or historical data required. Python 3 with SymPy.
"""
from itertools import product, combinations
from collections import Counter, defaultdict
import sympy as sp

p=3
mons=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
points=sorted({tuple(v*pow(next(w for w in z if w),-1,3)%3 for v in z) for z in product(range(3),repeat=3) if any(z)})
assert len(points)==13
lines=[sum(1<<i for i,P in enumerate(points) if sum(a[j]*P[j] for j in range(3))%3==0) for a in points]
blocking=[]
for c in combinations(range(13),6):
 b=sum(1<<i for i in c)
 if all(b&L and (b&L)!=L for L in lines): blocking.append(b)
assert len(blocking)==234
B=min(blocking)
assert B.bit_count()==6

# RREF nullspace over F3 for quartic coefficients through prescribed six points.
mat=[[pow(P[0],i,3)*pow(P[1],j,3)*pow(P[2],k,3)%3 for i,j,k in mons] for t,P in enumerate(points) if B>>t&1]
rank=0;piv=[]
for c in range(15):
 r=next((r for r in range(rank,len(mat)) if mat[r][c]),None)
 if r is None:continue
 mat[rank],mat[r]=mat[r],mat[rank]
 v=pow(mat[rank][c],-1,3);mat[rank]=[(v*x)%3 for x in mat[rank]]
 for r in range(len(mat)):
  if r!=rank:
   f=mat[r][c];mat[r]=[(mat[r][z]-f*mat[rank][z])%3 for z in range(15)]
 piv.append(c);rank+=1
free=[k for k in range(15) if k not in piv]
assert len(piv)==6 and len(free)==9
basis=[]
for k in free:
 v=[0]*15;v[k]=1
 for t,j in enumerate(piv):v[j]=(-mat[t][k])%3
 basis.append(v)

def normalize(v):
 i=next((i for i,x in enumerate(v) if x),None)
 return tuple(x*pow(v[i],-1,3)%3 for x in v) if i is not None else None

def points_mask(v):
 out=0
 for idx,P in enumerate(points):
  if sum(v[t]*pow(P[0],i,3)*pow(P[1],j,3)*pow(P[2],k,3) for t,(i,j,k) in enumerate(mons))%3==0:out|=1<<idx
 return out
cands=set()
for scalars in product(range(3),repeat=9):
 v=normalize([sum(scalars[j]*basis[j][i] for j in range(9))%3 for i in range(15)])
 if v is not None and points_mask(v)==B:cands.add(v)
print('RATIONAL_CLASS_CANDIDATES',len(cands),flush=True)
assert len(cands)==567
x,y,z=sp.symbols('x y z'); vars=(x,y,z)
monexp=[x**i*y**j*z**k for i,j,k in mons]
def smooth(v):
 f=sum(int(v[t])*monexp[t] for t in range(15))
 grad=[sp.diff(f,q) for q in vars]
 for aff in vars:
  two=[q for q in vars if q!=aff]
  gb=sp.groebner([q.subs(aff,1) for q in grad],*two,modulus=3)
  if not gb.is_zero_dimensional and not (len(gb.polys)==1 and gb.polys[0].as_expr()==1):
   # nonzero dimensional may contain singularity; zero-dimensional ideal may too
   return False
  if not (len(gb.polys)==1 and gb.polys[0].as_expr()==1):return False
 return True
smooth_forms=[v for v in cands if smooth(v)]
print('SMOOTH',len(smooth_forms),flush=True)
assert len(smooth_forms)==222

# Stabilizer of the distinguished six-point locus under PGL3(F3).
def matmul(a,P):return tuple(sum(a[3*i+j]*P[j] for j in range(3))%3 for i in range(3))
def det(a):return (a[0]*(a[4]*a[8]-a[5]*a[7])-a[1]*(a[3]*a[8]-a[5]*a[6])+a[2]*(a[3]*a[7]-a[4]*a[6]))%3
def pnorm(P):
 for v in P:
  if v:return tuple(t*pow(v,-1,3)%3 for t in P)
 raise ValueError('zero point')
stab=[]
for a in product(range(3),repeat=9):
 if det(a)==0:continue
 if next(t for t in a if t)!=1:continue
 perm=[points.index(pnorm(matmul(a,P))) for P in points]
 if sum(1<<perm[i] for i in range(13) if B>>i&1)==B:stab.append(a)
assert len(stab)==24

# coordinate change action, 15 monomial coefficients
from functools import lru_cache
@lru_cache(None)
def transform_matrix(a):
 # polynomial dictionaries: multiply reduced mod 3
 row_polys=[]
 for m in range(3):
  q={tuple(int(j==i) for i in range(3)):a[3*m+j]%3 for j in range(3)}
  row_polys.append({k:v for k,v in q.items() if v})
 def pmult(u,v):
  out=defaultdict(int)
  for I,a0 in u.items():
   for J,b0 in v.items():out[tuple(I[t]+J[t] for t in range(3))]=(out[tuple(I[t]+J[t] for t in range(3))]+a0*b0)%3
  return dict(out)
 mat=[]
 for I in mons:
  poly={(0,0,0):1}
  for j,k in enumerate(I):
   for _ in range(k):poly=pmult(poly,row_polys[j])
  mat.append(tuple(poly.get(E,0) for E in mons))
 return mat

def action(v,a):
 mat=transform_matrix(a)
 return normalize(tuple(sum(v[t]*mat[t][j] for t in range(15))%3 for j in range(15)))
remaining=set(smooth_forms); reps=[];orbits=[]
while remaining:
 v=min(remaining)
 orb={action(v,a) for a in stab}
 assert orb<=set(smooth_forms)
 remaining-=orb;reps.append(v);orbits.append(len(orb))
print('STABILIZER_ORBITS',len(reps),sorted(orbits),flush=True)
assert len(reps)==10 and sorted(orbits)==[6]+[24]*9

# F_{3^n} represented by monic irreducible polynomial, direct finite arithmetic.
class Field:
 def __init__(self,n,poly):self.n=n;self.q=3**n;self.poly=poly;self.vec=[tuple((i//(3**j))%3 for j in range(n)) for i in range(self.q)]
 def add(self,x,y):return sum(((a+b)%3)*3**j for j,(a,b) in enumerate(zip(self.vec[x],self.vec[y])))
 def mul(self,x,y):
  if not x or not y:return 0
  n=self.n;u=[0]*(2*n-1)
  for i,a in enumerate(self.vec[x]):
   for j,b in enumerate(self.vec[y]):u[i+j]=(u[i+j]+a*b)%3
  for i in range(2*n-2,n-1,-1):
   c=u[i]
   for j in range(n):u[i-n+j]=(u[i-n+j]-c*self.poly[j])%3
  return sum(t*3**i for i,t in enumerate(u[:n]))
 def pow(self,x,n):
  z=1
  while n:
   if n&1:z=self.mul(z,x)
   x=self.mul(x,x);n//=2
  return z
 def projective_points(self):
  # Charts (1,a,b), (0,1,a), (0,0,1)
  for a in range(self.q):
   for b in range(self.q):yield (1,a,b)
  for a in range(self.q):yield (0,1,a)
  yield (0,0,1)

def count_points(v,F):
 P=F.pow;M=F.mul;A=F.add
 res=0
 for vals in F.projective_points():
  powers=[[P(t,i) for i in range(5)] for t in vals]
  acc=0
  for c,(i,j,k) in zip(v,mons):
   if c:acc=A(acc, M(c, M(powers[0][i],M(powers[1][j],powers[2][k]))))
  if acc==0:res+=1
 return res
fields=[Field(1,(0,1)),Field(2,(1,0)),Field(3,(1,2,0))]
for F in fields:
 assert all(F.pow(x,F.q)==x for x in range(F.q))

rows=[]
for v,orb in zip(reps,orbits):
 Ns=tuple(count_points(v,F) for F in fields)
 s1=3+1-Ns[0];s2=9+1-Ns[1];s3=27+1-Ns[2]
 c1=-s1;c2=(s1*s1-s2)//2;c3=(-s1**3+3*s1*s2-2*s3)//6
 coeff=(1,c1,c2,c3,3*c2,9*c1,27)
 rows.append((v,orb,Ns,coeff))
for row in rows:print('ROW',row,flush=True)
print('ISOGENY_ZETA_COUNTS',Counter(tuple(r[3]) for r in rows),flush=True)
print('BLOCKING_QUARTIC_ARITHMETIC_REPLAY_PASS',flush=True)
