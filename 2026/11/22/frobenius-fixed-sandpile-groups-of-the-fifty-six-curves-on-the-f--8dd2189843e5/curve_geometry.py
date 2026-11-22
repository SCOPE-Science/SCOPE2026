"""Exact 56 exceptional-curve incidence data for the Fermat double plane.
The coefficient ring is Z[t]/(t^4+1), where t is a primitive eighth root.
"""
from sympy import Matrix, eye

ZERO=(0,0,0,0);ONE=(1,0,0,0);T=(0,1,0,0)
def add(a,b): return tuple(a[i]+b[i] for i in range(4))
def neg(a): return tuple(-u for u in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 o=[0]*4
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if i+j>=4:o[i+j-4]-=x*y
   else:o[i+j]+=x*y
 return tuple(o)
def pwr(a,n):
 v=ONE
 for _ in range(n):v=mul(v,a)
 return v
zeta=[pwr(T,i) for i in range(8)]
delta=sub(zeta[1],zeta[3]);assert mul(delta,delta)==(2,0,0,0)
def cross(a,b):return (sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
curves=[]
for u,v,k in [(0,1,2),(0,2,1),(1,2,0)]:
 for j in [1,3,5,7]:
  L=[ZERO]*3;L[u]=ONE;L[v]=neg(zeta[j])
  for e in [1,-1]:curves.append(('h',u,v,j,e,tuple(L),('h',k,e)))
for a in range(4):
 for b in range(4):
  L=(neg(zeta[2*a]),neg(zeta[2*b]),ONE)
  for e in [1,-1]:curves.append(('n',a,b,e,tuple(L),('n',(b-a)%4,e)))
assert len(curves)==56

def unpack(c):return (c[5],c[6]) if c[0]=='h' else (c[4],c[5])
def qeval(c,P):
 L,meta=unpack(c)
 typ=meta[0]
 if typ=='h':return mul((ONE if meta[2]==1 else neg(ONE)),mul(P[meta[1]],P[meta[1]]))
 zz=zeta[2*meta[1]]
 q=add(add(mul(P[0],P[0]),mul(zz,mul(P[0],P[1]))),mul(mul(zz,zz),mul(P[1],P[1])))
 return mul((delta if meta[2]==1 else neg(delta)),q)
I=[[0]*56 for _ in range(56)]
for i in range(56):
 I[i][i]=-1
 for j in range(i+1,56):
  Li,_=unpack(curves[i]);Lj,_=unpack(curves[j]);P=cross(Li,Lj)
  if all(x==ZERO for x in P):
   assert Li==Lj or all(Li[k]==neg(Lj[k]) for k in range(3))
   v=2
  else:
   a=qeval(curves[i],P);b=qeval(curves[j],P)
   assert a!=ZERO and b!=ZERO, (i,j)
   assert a==b or a==neg(b),(i,j,a,b)
   v=int(a==b)
  I[i][j]=I[j][i]=v
assert all(row.count(-1)==1 and row.count(0)==27 and row.count(1)==27 and row.count(2)==1 for row in I)
B=[0,33,34,9,25,20,47,3]
G=Matrix([[I[i][j] for j in B] for i in B]);assert G.det() in [1,-1],G
assert all(I[B[i]][B[j]]==0 for i in range(7) for j in range(i+1,7))
assert sorted(I[B[7]][B[i]] for i in range(7))==[0]*5+[1]*2
labels={c[:5] if c[0]=='h' else c[:4]:i for i,c in enumerate(curves)}

def rank2(M):
 A=[[int(M[i,j])%2 for j in range(M.cols)] for i in range(M.rows)]
 r=0
 for j in range(M.cols):
  pi=next((i for i in range(r,M.rows) if A[i][j]),None)
  if pi is None:continue
  A[r],A[pi]=A[pi],A[r]
  for i in range(M.rows):
   if i!=r and A[i][j]:A[i]=[x^y for x,y in zip(A[i],A[r])]
  r+=1
 return r

