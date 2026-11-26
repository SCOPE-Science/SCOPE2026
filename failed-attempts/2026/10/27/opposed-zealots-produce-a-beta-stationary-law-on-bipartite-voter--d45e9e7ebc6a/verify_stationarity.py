#!/usr/bin/env python3
"""Exact rational stationary equation check for opposing zealots on K_{a+1,b+1}."""
from fractions import Fraction as F

def solve(A,b):
 n=len(b)
 for j in range(n):
  p=next(i for i in range(j,n) if A[i][j])
  A[j],A[p]=A[p],A[j];b[j],b[p]=b[p],b[j]
  q=A[j][j]; A[j]=[r/q for r in A[j]];b[j]/=q
  for i in range(n):
   if i!=j and A[i][j]:
    q=A[i][j]
    for k in range(j,n): A[i][k]-=q*A[j][k]
    b[i]-=q*b[j]
 return b

def exact(a,b):
 states=[(i,j) for i in range(a+1) for j in range(b+1)]
 N=len(states); idx={s:k for k,s in enumerate(states)}
 mat=[[F(0) for _ in range(N)] for _ in range(N)]
 for k,(i,j) in enumerate(states):
  rates=[]
  if i<a: rates.append(((i+1,j),F((a-i)*j,b+1)))
  if i>0: rates.append(((i-1,j),F(i*(b+1-j),b+1)))
  if j<b: rates.append(((i,j+1),F((b-j)*(i+1),a+1)))
  if j>0: rates.append(((i,j-1),F(j*(a-i),a+1)))
  for dst,q in rates:
   mat[idx[dst]][k]+=q
   mat[k][k]-=q
 mat[-1]=[F(1)]*N
 rhs=[F(0)]*(N-1)+[F(1)]
 pi=solve(mat,rhs)
 mean_A=sum(p*F(i,a) for p,(i,j) in zip(pi,states));mean_B=sum(p*F(j,b) for p,(i,j) in zip(pi,states))
 denom=F((a+b+1)**2*(3*a+3*b+2))
 expectA=F(b,a+b+1);expectB=F(b+1,a+b+1)
 assert mean_A==expectA,(a,b,mean_A,expectA)
 assert mean_B==expectB
 w=sum(p*F(i*j,a*b) for p,(i,j) in zip(pi,states))
 expected_w=F((a+3*b)*(b+1),(a+b+1)*(3*a+3*b+2))
 assert w==expected_w,(a,b,w,expected_w)
 if a>=2:
  aa=sum(p*F(i*(i-1),a*(a-1)) for p,(i,j) in zip(pi,states))
  expectaa=F(b*(a+3*b),(a+b+1)*(3*a+3*b+2))
  assert aa==expectaa,(a,b,aa,expectaa)
 if b>=2:
  bb=sum(p*F(j*(j-1),b*(b-1)) for p,(i,j) in zip(pi,states))
  expectbb=F((b+1)*(a+3*b+2),(a+b+1)*(3*a+3*b+2))
  assert bb==expectbb,(a,b,bb,expectbb)
 return a,b,N,mean_A,mean_B,w

for a in range(1,4):
 for b in range(1,4):print('PASS',exact(a,b))
