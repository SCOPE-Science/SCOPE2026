#!/usr/bin/env python3
"""Exhaustive finite-field checks for fibers of commuting square-zero products."""
from itertools import product
from collections import Counter
from math import comb

def mul(A,B,q):
 n=len(A);p=len(B);z=len(B[0]) if B else 0;return [[sum(A[i][k]*B[k][j] for k in range(p))%q for j in range(z)] for i in range(n)]
def mat(n,q):
 for a in product(range(q),repeat=n*n):yield [list(a[i*n:(i+1)*n]) for i in range(n)]
def gauss(n,k,q):
 if k<0 or k>n:return 0
 numerator=denominator=1
 for i in range(k):numerator*=q**(n-i)-1;denominator*=q**(k-i)-1
 return numerator//denominator
def inject(n,t,q):
 z=1
 for i in range(t):z*=q**n-q**i
 return z
def mobius_both(u,d,q):
 z=0
 for j in range(u+1):
  for ell in range(d+1):
   z+=((-1)**(u-j+ell))*q**(comb(u-j,2)+comb(ell,2))*gauss(u,j,q)*gauss(d,ell,q)*q**(2*j*(d-ell))
 return z
def Z(b,q):
 return sum(gauss(b,k,q)*gauss(k,u,q)*mobius_both(u,b-k,q) for k in range(b+1) for u in range(k+1))
def fiber(n,t,q):
 if t==0:raise ValueError('nonzero target only')
 if 4*t>n:return 0
 a=n-2*t;b=n-4*t
 return q**(3*t*t+2*t*b)*inject(a,t,q)*inject(a-t,t,q)*Z(b,q)
def brute_Z(b,q):
 good=[];zero=[[0]*b for _ in range(b)]
 for X in mat(b,q):
  if mul(X,X,q)==zero:good.append(X)
 count=0
 for X in good:
  for Y in good:
   if mul(X,Y,q)==zero and mul(Y,X,q)==zero:count+=1
 return count
def brute_product(n,t,q):
 assert n==4 and t==1
 # Basis E,H,F (dimensions 1,2,1): all factors must kill E and map to E+H.
 N=[[0]*n for _ in range(n)];N[0][3]=1
 zero=[[0]*n for _ in range(n)]
 good=[]
 for data in product(range(q),repeat=9):
  B=[[0]*n for _ in range(n)]
  pos=[(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]
  for (i,j),x in zip(pos,data):B[i][j]=x
  if mul(B,B,q)==zero:good.append(B)
 count=0
 for B in good:
  for C in good:
   if mul(B,C,q)==N and mul(C,B,q)==N:count+=1
 return count
if __name__=='__main__':
 for b,q in [(0,2),(1,2),(2,2),(2,3),(3,2)]:
  val=Z(b,q); brute=brute_Z(b,q)
  assert val==brute,(b,q,val,brute)
  print('Z',b,q,val,'PASS')
 for q in (2,):
  val=fiber(4,1,q); brute=brute_product(4,1,q)
  assert val==brute,(q,val,brute)
  print('FIBER',4,1,q,val,'PASS')
 for n,t,q in [(4,1,3),(4,1,5),(5,1,2),(6,1,2),(8,2,2)]:
  print('FORMULA',n,t,q,fiber(n,t,q))
 print('COMMUTING_SQUARE_ZERO_PRODUCT_FIBERS_OK')
