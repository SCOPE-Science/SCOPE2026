#!/usr/bin/env python3
"""Exact finite enumerations and rational asymptotic-sign certificate.

Run: python3 verify.py (rename this file verify.py for packaged result).
Standard library only. The proof is analytical; finite checks are corroboration.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt

def fib(n):
 a,b=0,1
 for _ in range(n): a,b=b,a+b
 return a

def graph_path(n): return [(i,i+1) for i in range(n-1)]
def graph_broom(n):return graph_path(n-2)+[(n-3,n-2),(n-3,n-1)]

def det_from_vertices(n,edges):
 inds=[mask for mask in range(1<<n) if not any((mask>>u&1) and (mask>>v&1) for u,v in edges)]
 z=len(inds)
 p=[F(sum(mask>>i&1 for mask in inds),z) for i in range(n)]
 deg=[sum(i==u or i==v for u,v in edges) for i in range(n)]
 D=F(1)
 for i in range(n):D*=p[i]*(1-p[i])**(1-deg[i])
 for u,v in edges:D*=1-p[u]-p[v]
 return D,z

def broom_formula(n):
 m=n-2
 suffix=lambda j: 5*fib(m-j)+4*fib(m-j-1)
 Z=5*fib(m)+4*fib(m-1)
 N=16*fib(m+1)**2
 for j in range(2,m+1):N*=fib(j)
 for j in range(2,m):N*=suffix(j)
 return F(N,Z**(m+3))

def path_formula(n):
 a=1
 for j in range(2,n+1):a*=fib(j)**2
 return F(a,fib(n+2)**(n+1))

def exact_limit_lower_certificate(K=25):
 scale=10**15
 L=F(1618033988749894,scale)
 U=F(1618033988749896,scale)
 assert (2*L-1)**2<5<(2*U-1)**2
 a_L=1/U**2;a_U=1/L**2
 c_U=5+4/L
 d_L=(4-5/L)/(5*U+4)
 d_U=(4-5/U)/(5*L+4)
 assert F(0)<d_L<d_U<1 and a_U<1
 lower=400*L**9/c_U**5
 for t in range(1,K+1):
  if (t-1)%2==0: num=1-d_U*a_U**(t-1)
  else:num=1+d_L*a_L**(t-1)
  if t%2==0:den=1-a_L**t
  else:den=1+a_U**t
  assert num>0 and den>0
  lower*=num/den
 tail=(d_U*a_U**K+a_U**(K+1))/(1-a_U)
 assert F(0)<tail<1
 lower*=1-tail
 assert lower>1,(float(lower),float(tail))
 return float(lower),float(tail)

def main():
 comparisons=0
 for n in range(4,13):
  db,_=det_from_vertices(n,graph_broom(n))
  dp,_=det_from_vertices(n,graph_path(n))
  assert db==broom_formula(n)
  assert dp==path_formula(n)
  if n==4:assert db<dp
  if n==5:assert db>dp and db==F(45,235298) and dp==F(900,4826809)
  comparisons+=1
 # For n<=4 there is only one tree through n=3 and two at n=4;
 # for n=5 the three unlabeled shapes are path, fork, and star.
 star5=[(0,i) for i in range(1,5)]
 ds,_=det_from_vertices(5,star5)
 assert ds==F(4096,24137569)<path_formula(5)<broom_formula(5)
 low,tail=exact_limit_lower_certificate()
 print('BROOM_COVARIANCE_CHECKS_PASSED comparisons=',comparisons,
       'rigorous_limit_lower=',format(low,'.10f'),
       'tail_bound=',format(tail,'.3g'))
if __name__=='__main__':main()
