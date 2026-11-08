#!/usr/bin/env python3
"""Exact prime-field checks of the characteristic-sensitive Jordan signature.

No third-party modules are required. Operators are built from original
matrix products; predicted ranks use nullities of powers of N.
"""
from itertools import product
from collections import Counter

def mm(A,B,p,n):
 return tuple(sum(A[n*i+k]*B[n*k+j] for k in range(n))%p for i in range(n) for j in range(n))
def ma(A,B,p):return tuple((x+y)%p for x,y in zip(A,B))
def zero(n):return (0,)*(n*n)
def eye(n):return tuple(int(i==j) for i in range(n) for j in range(n))
def rk(rows,p):
 if not rows:return 0
 x=[list(row) for row in rows]; z=0
 for col in range(len(x[0])):
  k=next((k for k in range(z,len(x)) if x[k][col]%p!=0),None)
  if k is None:continue
  x[z],x[k]=x[k],x[z]
  inv=pow(x[z][col]%p,-1,p)
  x[z]=[(v*inv)%p for v in x[z]]
  for y in range(len(x)):
   if y!=z:
    t=x[y][col]%p
    if t:x[y]=[(u-t*v)%p for u,v in zip(x[y],x[z])]
  z+=1
  if z==len(x):break
 return z

def matrank(A,p,n):return rk([A[i*n:(i+1)*n] for i in range(n)],p)
def dif(A,B,d,p,n, powers=None):
 if powers is None:
  powers=[eye(n)]
  for _ in range(d):powers.append(mm(powers[-1],A,p,n))
 out=zero(n)
 for i in range(d):out=ma(out,mm(mm(powers[i],B,p,n),powers[d-1-i],p,n),p)
 return out

def inspect(A,d,p,n):
 powers=[eye(n)]
 for _ in range(d):powers.append(mm(powers[-1],A,p,n))
 if powers[d]!=zero(n):return None
 h=[matrank(powers[i-1],p,n)-matrank(powers[i],p,n) for i in range(1,d+1)]
 r=sum(h[i]*h[d-1-i] for i in range(d))
 m_d=h[d-1]
 s=(m_d*m_d if d%p else 0)
 expected=(n*n-2*r+s,r-2*s,s)
 E=[tuple(int(j==k) for j in range(n*n)) for k in range(n*n)]
 columns=[dif(A,e,d,p,n,powers) for e in E]
 T=[tuple(columns[j][i] for j in range(n*n)) for i in range(n*n)]
 r1=rk(T,p)
 # Independent matrix-map composition for T squared (rather than using identity).
 columns2=[dif(A,c,d,p,n,powers) for c in columns]
 T2=[tuple(columns2[j][i] for j in range(n*n)) for i in range(n*n)]
 r2=rk(T2,p)
 columns3=[dif(A,c,d,p,n,powers) for c in columns2]
 assert all(c==zero(n) for c in columns3)
 actual=(n*n-2*r1+r2,r1-2*r2,r2)
 assert actual==expected,(p,n,d,A,h,actual,expected)
 # Independent universal operator identity T^2(X)=d N^(d-1) X N^(d-1).
 for E0,C2 in zip(E,columns2):
  C=mm(mm(powers[d-1],E0,p,n),powers[d-1],p,n)
  assert C2==tuple(d*u%p for u in C)
 return tuple(h),expected

def run(p,n,d,all_matrices=True):
 types=Counter()
 candidates=product(range(p),repeat=n*n)
 for idx,A in enumerate(candidates):
  if not all_matrices and idx % 101:continue
  x=inspect(A,d,p,n)
  if x is not None:types[x]+=1
 assert types
 print('p',p,'n',n,'d',d,'checked_bases',sum(types.values()),'profiles',repr(sorted(types.items())))

if __name__=='__main__':
 run(2,2,2)
 run(3,2,2)
 run(2,3,3)
 run(3,3,3)
 run(2,3,4)
 run(5,2,3)
 run(2,4,3,False)
 print('MODULAR_POWER_DERIVATIVE_JORDAN_PASS')
