"""Reproducible rational-vertex certificate and lattice count for 3-point directed metrics."""
from itertools import combinations, product
from fractions import Fraction

ROWS=[];RHS=[]
for j in range(6):
 a=[0]*6;a[j]=-1;ROWS.append(a);RHS.append(0)
 a=[0]*6;a[j]=1;ROWS.append(a);RHS.append(1)
for a in ((1,0,-1,0,0,-1),(0,1,0,-1,-1,0),(-1,0,1,0,-1,0),(0,-1,0,1,0,-1),(0,-1,-1,0,1,0),(-1,0,0,-1,0,1)):
 ROWS.append(a);RHS.append(0)

def solve(rows,rhs):
 n=len(rhs); A=[[Fraction(x) for x in row]+[Fraction(y)] for row,y in zip(rows,rhs)]
 for i in range(n):
  pivot=next((j for j in range(i,n) if A[j][i]),None)
  if pivot is None:return None
  A[i],A[pivot]=A[pivot],A[i]
  u=A[i][i]
  for k in range(i,n+1):A[i][k]/=u
  for j in range(i+1,n):
   u=A[j][i]
   if u:
    for k in range(i,n+1):A[j][k]-=u*A[i][k]
 v=[Fraction(0) for _ in range(n)]
 for i in range(n-1,-1,-1):v[i]=A[i][n]-sum(A[i][j]*v[j] for j in range(i+1,n))
 return tuple(v)

def vertices():
 V=set()
 for ix in combinations(range(18),6):
  x=solve([ROWS[i] for i in ix],[RHS[i] for i in ix])
  if x is not None and all(sum(a*b for a,b in zip(row,x))<=rhs for row,rhs in zip(ROWS,RHS)):
   V.add(x)
 assert len(V)==31,(len(V),V)
 assert all(x.denominator in (1,2) for v in V for x in v)
 assert sum(any(x.denominator==2 for x in v) for v in V)==2
 print('VERTICES_OK',len(V),'half-integral',2)

def count(m):
 out=0
 for x,y,u,v in product(range(m+1),repeat=4):
  s0=max(0,u-x,y-v);s1=min(m,y+u)
  t0=max(0,x-u,v-y);t1=min(m,v+x)
  out+=max(0,s1-s0+1)*max(0,t1-t0+1)
 return out

def formula(m):
 a=54*m**6+324*m**5+875*m**4+1340*m**3+1236*m**2+656*m+160-5*(m%2)
 assert a%160==0
 return a//160

def main():
 vertices()
 for m in range(20):
  a=count(m);b=formula(m)
  assert a==b,(m,a,b)
 print('COUNT_OK',[(i,count(i)) for i in range(9)])
 print('VERIFY_OK')
if __name__=='__main__':main()
