#!/usr/bin/env python3
"""Independent exact finite-field matrix checks for finite projective planes."""
import numpy as np

def mul(a,b,q):
 if q!=4: return (a*b)%q
 if a==0 or b==0: return 0
 return (1,2,3)[((1,2,3).index(a)+(1,2,3).index(b))%3]
def add(a,b,q):return (a^b) if q==4 else (a+b)%q
def inv(a,q):
 for b in range(1,q):
  if mul(a,b,q)==1:return b
 raise ValueError(a)
def vecs(q):
 result=[]
 for a in range(q):
  for b in range(q):
   for c in range(q):
    if a==b==c==0:continue
    t=next(x for x in (a,b,c) if x)
    ti=inv(t,q)
    v=tuple(mul(x,ti,q) for x in (a,b,c))
    if v not in result:result.append(v)
 return result
def plane(q):
 vs=vecs(q)
 M=np.zeros((len(vs),len(vs)),dtype=np.int64)
 for i,x in enumerate(vs):
  for j,y in enumerate(vs):
   z=0
   for a,b in zip(x,y):z=add(z,mul(a,b,q),q)
   M[i,j]=int(z==0)
 return M

def rank(M,p=3):
 A=(M.copy()%p).astype(np.int64)
 n,m=A.shape;r=0
 for c in range(m):
  nz=np.flatnonzero(A[r:,c])
  if len(nz)==0:continue
  j=r+nz[0]
  if j!=r:A[[j,r]]=A[[r,j]]
  A[r]=(A[r]*pow(int(A[r,c]),-1,p))%p
  idx=np.flatnonzero(A[r+1:,c])+r+1
  if len(idx):A[idx]=(A[idx]-A[idx,c,None]*A[r])%p
  r+=1
  if r==n:break
 return r

def predicted(q,v,rho,t):
 from math import gcd
 z=q%3
 e=0;n=t
 while n%3==0:n//=3;e+=1
 if z==2:
  return 4 if t%4==0 and t%8!=0 else 4*v if t%8==0 else 0
 if z==1:
  H=min(3**e,4)+(v-2)*min(3**e,2)
  return H*(1+(t%2==0))
 K=min(3**e,2)*(1+(t%2==0))
 if t%4==0:K+=4*(v-1) if t%3==0 else 4*(v-rho)
 return K

def check(q):
 B=plane(q);v=len(B)
 assert v==q*q+q+1
 assert np.all(B.sum(0)==q+1) and np.all(B.sum(1)==q+1)
 assert np.array_equal(B@B.T,q*np.eye(v,dtype=np.int64)+np.ones((v,v),dtype=np.int64))
 rho=rank(B)
 Z=np.zeros_like(B);A=np.block([[Z,B],[B.T,Z]])%3
 n=A.shape[0];I=np.eye(n,dtype=np.int64)
 T=np.block([[A,-I],[I,Z if False else np.zeros_like(A)]])%3
 I2=np.eye(2*n,dtype=np.int64)
 orders={0:12,1:18,2:8};L=orders[q%3]
 X=I2.copy()
 for t in range(1,L+1):
  X=(T@X)%3
  if L%t==0:
   actual=2*n-rank(X-I2)
   expected=predicted(q,v,rho,t)
   assert actual==expected,(q,t,actual,expected)
   print('q=%d v=%d rho=%d t=%d fixed_space=%d'%(q,v,rho,t,actual))
  if t==L:assert np.array_equal(X,I2)
 print('verified exact order',L,'for q',q)
for q in [2,3,4,5,7]:check(q)
