#!/usr/bin/env python3
"""Exact independent checks for discounted hitting coverage of labelled cycles."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, ceil

def solve(A,b):
 n=len(A); A=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
 for j in range(n):
  k=next(i for i in range(j,n) if A[i][j]); A[j],A[k]=A[k],A[j]
  t=A[j][j]; A[j]=[v/t for v in A[j]]
  for i in range(n):
   if i!=j:
    t=A[i][j]
    if t:A[i]=[x-t*y for x,y in zip(A[i],A[j])]
 return [row[-1] for row in A]

def brute_worst(n,S,lam):
 if not S: return F(0)
 if len(S)==n:return F(1)
 V=[x for x in range(n) if x not in S]; pos={x:i for i,x in enumerate(V)}
 A=[[F(i==j) for j in range(len(V))] for i in range(len(V))]; b=[F(0) for i in V]
 for i,v in enumerate(V):
  for t in ((v-1)%n,(v+1)%n):
   if t in S:b[i]+=lam/2
   else:A[i][pos[t]]-=lam/2
 return min(solve(A,b))

def interval_worst(g,lam):
 if g==1:return F(1)
 A=[[F(i==j) for j in range(g-1)] for i in range(g-1)];b=[F(0)]*(g-1)
 for i in range(1,g):
  for t in (i-1,i+1):
   if t==0 or t==g:b[i-1]+=lam/2
   else:A[i-1][t-1]-=lam/2
 return min(solve(A,b))

def gap_profile(n,S):
 a=sorted(S)
 return [(a[(i+1)%len(a)]-a[i])%n or n for i in range(len(a))]

def formula_counts(n,L):
 ans=[0]*(n+1)
 for k in range(1,n+1):
  d=[0]*(n+1);d[0]=1
  for _ in range(k):
   nd=[0]*(n+1)
   for j in range(n+1):
    if d[j]:
     for g in range(1,min(L,n-j)+1):nd[j+g]+=d[j]
   d=nd
  assert (n*d[n])%k==0
  ans[k]=n*d[n]//k
 return ans

checked=0
for n in range(3,10):
 for lam in [F(1,2),F(2,3),F(4,5)]:
  phis=[F(1)]+[interval_worst(g,lam) for g in range(1,n+1)]
  assert all(phis[g]>=phis[g+1] for g in range(1,n))
  thresholds=set([F(1),F(1,5),F(1,3),F(1,2),F(2,3),F(4,5),F(9,10)]+phis[1:n+1])
  scores={}
  for mask in range(1,1<<n):
   S={i for i in range(n) if mask>>i&1}
   scores[mask]=brute_worst(n,S,lam)
  for tau in thresholds:
   if not (0<tau<=1):continue
   L=max([g for g in range(1,n+1) if phis[g]>=tau])
   expect=formula_counts(n,L)
   observed=[0]*(n+1)
   for mask in range(1,1<<n):
    S={i for i in range(n) if mask>>i&1}
    feasible=scores[mask]>=tau
    assert feasible==(max(gap_profile(n,S))<=L),(n,lam,tau,S,L)
    if feasible:observed[len(S)]+=1
   assert observed==expect,(n,lam,tau,observed,expect)
   assert next(i for i,v in enumerate(observed) if v)==(n+L-1)//L
   checked+=1
print('INDEPENDENT_EXACT_GAUSSIAN_AND_GAP_COUNTS_OK',checked,'parameter_cases n=3..9')
print('EXAMPLE_n10_lambda_half_tau_third',formula_counts(10,3)[4])
print('VERIFY_OK')
