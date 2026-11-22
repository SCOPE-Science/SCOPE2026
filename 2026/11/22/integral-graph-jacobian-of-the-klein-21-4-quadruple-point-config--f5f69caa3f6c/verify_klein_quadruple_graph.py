from itertools import combinations
from collections import Counter, defaultdict
from sympy import zeros,Matrix, factorint
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy import symbols
# coefficients u+v a for a*a=-a-2
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def cross(x,y):return tuple(sub(mul(x[(k+1)%3],y[(k+2)%3]),mul(x[(k+2)%3],y[(k+1)%3])) for k in range(3))
def zero(x):return x==(0,0)
A=(0,1); z=(0,0); o=(1,0); n=(-1,0)
L=[(o,z,z),(z,o,o),(A,o,n),(A,n,o),(z,n,o),(o,A,n),(A,n,n),(n,o,A),(A,o,o),(n,A,o),(n,n,A),(o,z,o),(n,A,n),(o,A,o),(n,z,o),(o,n,A),(o,o,A),(z,z,o),(n,o,z),(o,o,z),(z,o,z)]
assert len(L)==21
pts=[]
for i,j in combinations(range(21),2):
 p=cross(L[i],L[j])
 assert any(not zero(x) for x in p)
 for item in pts:
  if all(zero(y) for y in cross(p,item['p'])):
   item['pairs'].append((i,j));break
 else: pts.append(dict(p=p,pairs=[(i,j)]))
print('points',len(pts),'pair counts',Counter(len(p['pairs']) for p in pts),flush=True)
Q=[x for x in pts if len(x['pairs'])==6]
T=[x for x in pts if len(x['pairs'])==3]
assert len(Q)==21 and len(T)==28
B=zeros(21,21)
for j,x in enumerate(Q):
 subset=sorted(set(sum(([a,b] for a,b in x['pairs']),[])))
 assert len(subset)==4
 for i in subset:B[i,j]=1
assert all(sum(B.row(i))==4 for i in range(21))
assert all(sum(B.col(j))==4 for j in range(21))
Lapl= zeros(42,42)
for i in range(42): Lapl[i,i]=4
for i in range(21):
 for j in range(21):
  if B[i,j]:Lapl[i,21+j]=-1;Lapl[21+j,i]=-1
R=Lapl[:-1,:-1]
print('rank',R.rank(),'det',R.det(method='domain-ge'),'factor',factorint(R.det(method='domain-ge')),flush=True)
D=smith_normal_form(R, domain=ZZ)
S=[int(D[i,i]) for i in range(D.rows) if abs(int(D[i,i]))>1]
print('smith',Counter(S),'nonunit',len(S), 'product',__import__('math').prod(S),flush=True)
print('charpoly',Lapl.charpoly().as_expr().factor(),flush=True)
from sympy import Poly
# independent materialization of printed 21 quadruple points
pa=add(A,o);m_pa=neg(pa)
quad_coords=[(o,z,z),(o,m_pa,n),(o,pa,o),(o,m_pa,o),(o,n,pa),(z,o,o),(pa,n,o),(z,z,o),(pa,n,n),(pa,o,o),(o,z,n),(o,o,pa),(o,n,z),(pa,o,n),(o,pa,n),(o,z,o),(z,o,n),(o,o,z),(o,n,m_pa),(o,o,m_pa),(z,o,z)]
B2=zeros(21,21)
for j,p in enumerate(quad_coords):
 for i,l in enumerate(L):
  if zero(add(add(mul(l[0],p[0]),mul(l[1],p[1])),mul(l[2],p[2]))):B2[i,j]=1
assert all(sum(B2.row(i))==4 for i in range(21)),[sum(B2.row(i)) for i in range(21)]
assert all(sum(B2.col(j))==4 for j in range(21))
assert sorted(tuple(int(x) for x in B2.col(j)) for j in range(21)) == sorted(tuple(int(x) for x in B.col(j)) for j in range(21))
assert int((B2*B2.T-B*B.T).norm())==0
print('two independently constructed incidence matrices agree up to column permutations',flush=True)

def vp(x,p,e):
 if x==0: return e
 v=0
 while x%p==0:
  x//=p;v+=1
 return v

def local_valuation(R,p,e):
 mod=p**e
 a=[[int(R[i,j])%mod for j in range(R.cols)] for i in range(R.rows)]
 n=len(a); vals=[]
 for k in range(n):
  i0,j0=min(((i,j) for i in range(k,n) for j in range(k,n)),key=lambda pair:vp(a[pair[0]][pair[1]],p,e))
  if vp(a[i0][j0],p,e)==e: vals.extend([e]*(n-k));break
  a[k],a[i0]=a[i0],a[k]
  for i in range(n):a[i][k],a[i][j0]=a[i][j0],a[i][k]
  v=vp(a[k][k],p,e);pv=p**v;unit=a[k][k]//pv
  inv=pow(unit,-1,p**(e-v))
  for i in range(k+1,n):
   assert a[i][k]%pv==0
   q=(a[i][k]//pv*inv)% (p**(e-v))
   for j in range(k,n): a[i][j]=(a[i][j]-q*a[k][j])%mod
   assert a[i][k]==0
  for j in range(k+1,n):
   assert a[k][j]%pv==0
   q=(a[k][j]//pv*inv)% (p**(e-v))
   for i in range(k,n): a[i][j]=(a[i][j]-q*a[i][k])%mod
   assert a[k][j]==0
  vals.append(v)
 return Counter(vals)

for sink in (0,21,41):
 R1=Lapl.copy();R1.row_del(sink);R1.col_del(sink)
 d=smith_normal_form(R1,domain=ZZ)
 ss=[abs(int(d[i,i])) for i in range(d.rows)]
 assert ss.count(0)==0
 assert Counter(x for x in ss if x>1)==Counter(S)
 for p in [2,3,7,23]:
  e=max(vp(x,p,200) for x in ss)+2
  loc=local_valuation(R1,p,e)
  assert loc==Counter(vp(x,p,e) for x in ss),(sink,p,loc)
  print('sink',sink,'prime',p,'valuation counts',sorted(loc.items()),flush=True)
print('KLEIN_21_4_QUADRUPLE_GRAPH_VERIFIED_OK',flush=True)
