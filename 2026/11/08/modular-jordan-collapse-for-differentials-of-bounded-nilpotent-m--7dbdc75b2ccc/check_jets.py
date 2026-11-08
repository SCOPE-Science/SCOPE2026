#!/usr/bin/env python3
"""Independent finite prime-field tests of nilpotent-power first-order lift counts."""
import itertools
from collections import Counter
from math import prod

def mm(A,B,p,n):
 return tuple(sum(A[n*i+k]*B[n*k+j] for k in range(n))%p for i in range(n) for j in range(n))

def add(A,B,p):return tuple((x+y)%p for x,y in zip(A,B))
def z(n):return (0,)*(n*n)
def ident(n):return tuple(int(i==j) for i in range(n) for j in range(n))
def powmat(A,d,p,n):
 R=ident(n)
 for _ in range(d):R=mm(R,A,p,n)
 return R

def rank(M,p):
 if not M:return 0
 x=[list(row) for row in M]
 row=0
 for col in range(len(x[0])):
  k=next((k for k in range(row,len(x)) if x[k][col]%p),None)
  if k is None:continue
  x[row],x[k]=x[k],x[row]
  v=pow(x[row][col]%p,-1,p)
  x[row]=[(a*v)%p for a in x[row]]
  for k in range(len(x)):
   if k != row:
    c=x[k][col]%p
    if c:x[k]=[(a-c*b)%p for a,b in zip(x[k],x[row])]
  row+=1
  if row==len(x):break
 return row

def data(A,d,p,n):
 zz=z(n)
 powers=[ident(n)]
 for _ in range(d):powers.append(mm(powers[-1],A,p,n))
 if powers[-1]!=zz:return None
 ranks=[rank([powers[j][n*i:n*i+n] for i in range(n)],p) for j in range(d+1)]
 h=tuple(ranks[i-1]-ranks[i] for i in range(1,d+1))
 predict=sum(h[i]*h[d-1-i] for i in range(d))
 return powers,h,predict

def derivative_rank(powers,d,p,n):
 mat=[]
 for u in range(n*n):
  E=tuple(int(i==u) for i in range(n*n))
  out=z(n)
  for j in range(d):out=add(out,mm(mm(powers[j],E,p,n),powers[d-1-j],p,n),p)
  mat.append(out)
 return rank([tuple(mat[c][r] for c in range(n*n)) for r in range(n*n)],p)

def test(p,n,d,direct=True):
 zz=z(n); shape=Counter(); base=Counter(); lifts=0
 for A in itertools.product(range(p),repeat=n*n):
  got=data(A,d,p,n)
  if got is None:continue
  powers,h,r=got
  observed=derivative_rank(powers,d,p,n)
  assert observed==r,(p,n,d,A,h,observed,r)
  base[h]+=1
  if direct:
   count=0
   for B in itertools.product(range(p),repeat=n*n):
    # multiplication for A+eps B over dual numbers: (A+eps B)^d
    old=ident(n);higher=zz
    for _ in range(d):
     higher=add(mm(old,B,p,n),mm(higher,A,p,n),p)
     old=mm(old,A,p,n)
    if higher==zz:count+=1
   assert count==p**(n*n-r),(p,n,d,A,h,count,r)
  shape[h]+=p**(n*n-r)
  lifts+=p**(n*n-r)
 print('FIELD',p,'N',n,'POWER',d,'DIRECT',direct,'BASE_TYPES',sorted((str(k),v) for k,v in base.items()),'TOTAL_LIFTS',lifts)
 return lifts

if __name__=='__main__':
 assert test(2,2,3)==40
 assert test(3,2,3)==3**4+(3**2-1)*3**3
 assert test(2,3,3)==8576
 assert test(2,3,4)== (2**9 + 21*2**9 + 42*2**7) # d4: rank 2 for J3, rank0 for J2
 assert test(3,3,3,False)==3**9+104*3**8+624*3**6
 print('FIRST_ORDER_JORDAN_JETS_PASS')
