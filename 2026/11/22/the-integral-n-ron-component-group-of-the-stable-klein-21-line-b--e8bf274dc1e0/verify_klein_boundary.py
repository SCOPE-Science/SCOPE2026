"""Exact integer certificate for the Klein arrangement's stable incidence boundary.

Run: python3 klein_boundary_verifier.py
Only the Python standard library is needed.
"""
from collections import Counter
from math import prod, isqrt

ZERO=(0,0);ONE=(1,0);NEG=(-1,0);ALPHA=(0,1)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]-2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def cross(x,y):
 return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
         sub(mul(x[2],y[0]),mul(x[0],y[2])),
         sub(mul(x[0],y[1]),mul(x[1],y[0])))
def same_point(x,y):return all(c==ZERO for c in cross(x,y))
Z=ZERO;P=ONE;N=NEG;A=ALPHA
# Coefficient rows (x,y,z), over Z[a]/(a^2+a+2).
LINES=[
 (P,Z,Z),(Z,P,P),(A,P,N),(A,N,P),(Z,N,P),(P,A,N),(A,N,N),
 (N,P,A),(A,P,P),(N,A,P),(N,N,A),(P,Z,P),(N,A,N),(P,A,P),
 (N,Z,P),(P,N,A),(P,P,A),(Z,Z,P),(N,P,Z),(P,P,Z),(Z,P,Z)
]
assert len(LINES)==21 and len(set(LINES))==21
points=[]; point_lines=[]
for i in range(21):
 for j in range(i+1,21):
  p=cross(LINES[i],LINES[j]); assert p!=(Z,Z,Z)
  k=next((k for k,q in enumerate(points) if same_point(p,q)),None)
  if k is None:k=len(points);points.append(p);point_lines.append(set())
  point_lines[k].update([i,j])
assert len(points)==49
assert Counter(map(len,point_lines))==Counter({3:28,4:21})
assert Counter(sum(i in s for s in point_lines) for i in range(21))=={8:21}
# Every unordered line pair occurs at exactly one singular point.
assert sum(len(s)*(len(s)-1)//2 for s in point_lines)==210
NVERT=70
L=[[0]*NVERT for _ in range(NVERT)]
for k,incidence in enumerate(point_lines):
 for i in incidence:
  j=k+21;L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
assert sum(row.count(-1) for row in L)==336
assert sum(L[i][j]!=0 for i in range(21) for j in range(21,70))==168
assert all(sum(row)==0 for row in L)
assert all(L[i][i]==8 for i in range(21))
assert Counter(L[21+i][21+i] for i in range(49))=={4:21,3:28}

def determinant_bareiss(a):
 a=[list(map(int,r)) for r in a];n=len(a);last=1;sign=1
 if n==1:return a[0][0]
 for k in range(n-1):
  if not a[k][k]:
   swap=next((i for i in range(k+1,n) if a[i][k]),None)
   assert swap is not None
   a[k],a[swap]=a[swap],a[k];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*pivot-a[i][k]*a[k][j]
    assert num%last==0
    a[i][j]=num//last
  for i in range(k+1,n):a[i][k]=0
  last=pivot
 return sign*a[-1][-1]

# Independent 20 by 20 weighted-quotient determinant, via Schur complement.
weights=[[0]*21 for _ in range(21)]
for incidence in point_lines:
 for i in incidence:
  for j in incidence:
   if i<j:
    assert weights[i][j]==0
    weights[i][j]=weights[j][i]=3 if len(incidence)==4 else 4
assert all(sum(row)==68 for row in weights)
W=[[68 if i==j else -weights[i][j] for j in range(21)] for i in range(21)]
assert all(sum(row)==0 for row in W)
WDET=determinant_bareiss([r[:-1] for r in W[:-1]])
expected={2:26,3:23,7:5,719:6}
TARGET=prod(p**v for p,v in expected.items())
assert WDET*(4*3**8)==TARGET
assert all(p>1 and all(p%d for d in range(2,isqrt(p)+1)) for p in expected)

# Independent small-matrix spectral relation for the 21-line weighted quotient.
Q=[[int(weights[i][j]==3) for j in range(21)] for i in range(21)]
def matmul(X,Y):
 n=len(X);return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
Q2=matmul(Q,Q); Q3=matmul(Q2,Q); Q4=matmul(Q3,Q)
assert all(Q4[i][j]-10*Q3[i][j]-31*Q2[i][j]+84*Q[i][j]==0 for i in range(21) for j in range(21))
# This is Q(Q-12I)(Q^2+2Q-7I)=0.

def rational_rank(matrix):
 from fractions import Fraction
 a=[[Fraction(x) for x in row] for row in matrix]
 n=len(a);m=len(a[0]);r=0
 for c in range(m):
  pivot=next((i for i in range(r,n) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  d=a[r][c]
  for j in range(c,m):a[r][j]/=d
  for i in range(r+1,n):
   v=a[i][c]
   if v:
    for j in range(c,m):a[i][j]-=v*a[r][j]
  r+=1
  if r==n:break
 return r

# For the symmetric matrix Q, the minimal polynomial divides
# x(x-12)(x^2+2x-7); its eigenspaces are orthogonal.
# The 12-eigenspace has dimension one (connected, regular graph),
# and eight zero eigenvalues leave six copies of each quadratic root.
assert rational_rank(Q)==13
assert rational_rank([[Q[i][j]-(12 if i==j else 0) for j in range(21)] for i in range(21)])==20
# Kirchhoff's theorem for the weighted 21-line graph:
# eigenvalues (nonzero): 72 [8 times], 71 +/- sqrt(8) [6 each].
assert WDET==72**8*(71**2-8)**6//21
assert 71**2-8==7*719

def pvaluation(x,p):
 if x==0:return 1000000
 z=0
 while x%p==0:x//=p;z+=1
 return z

def valuations_mod_pk(matrix,p,total_val):
 k=total_val+1;mod=p**k;n=len(matrix)
 a=[[x%mod for x in row] for row in matrix];vals=[]
 for j in range(n):
  v,i0,j0=min((pvaluation(a[i][l],p),i,l) for i in range(j,n) for l in range(j,n))
  assert v<1000000
  a[j],a[i0]=a[i0],a[j]
  for row in a:row[j],row[j0]=row[j0],row[j]
  divisor=p**v;unit=a[j][j]//divisor;smallmod=mod//divisor
  inv=pow(unit,-1,smallmod)
  for i in range(j+1,n):
   entry=a[i][j]
   if not entry:continue
   assert entry%divisor==0
   factor=(entry//divisor*inv)%smallmod
   a[i][j]=0
   for l in range(j+1,n):a[i][l]=(a[i][l]-factor*a[j][l])%mod
  vals.append(v)
 assert sum(vals)==total_val
 return sorted(vals)

results=[]
for root in (69,0):
 minor=[[L[i][j] for j in range(NVERT) if j!=root] for i in range(NVERT) if i!=root]
 primes={p:valuations_mod_pk(minor,p,e) for p,e in expected.items()}
 elementary=[prod(p**primes[p][i] for p in expected) for i in range(69)]
 assert all(elementary[i+1]%elementary[i]==0 for i in range(68))
 assert prod(elementary)==TARGET
 results.append(elementary)
assert results[0]==results[1]
factors=Counter(x for x in results[0] if x!=1)
assert factors=={4:1,72:1,216:1,155304:1,1087128:5}
assert 168-70+1==99
print('KLEIN_STABLE_BOUNDARY_COMPLETE_INTEGRAL_GROUP_OK')
print('vertices=70 edges=168 genus=99, triple_points=28 quadruple_points=21')
print('nonunit_smith_factors=',sorted(factors.items()))
print('order=',TARGET,'order_prime_factors=',expected)
print('independent_schur_20x20_det=',WDET,'two_root_reductions_match=True')
