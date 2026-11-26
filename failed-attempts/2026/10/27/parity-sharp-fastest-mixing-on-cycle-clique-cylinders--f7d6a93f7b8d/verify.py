#!/usr/bin/env python3
"""Exact/finite checks for cycle-by-clique fastest-mixing formula."""
import math
import numpy as np
from scipy.optimize import linprog

def formulas(n,m):
    s=2*(1-math.cos(2*math.pi/n))
    L=2*(1-math.cos(2*math.pi*(n//2)/n))
    g_bal=2*s/(L+2*s)
    g_row=m*s/(2*m+(m-1)*s)
    g=min(g_bal,g_row)
    a=g/s; b=g/m
    return s,L,g_bal,g_row,g,a,b,1-2*a-(m-1)*b

def build(n,m,a,b):
    N=n*m; P=np.eye(N)
    for i in range(n):
      for j in range(m):
        u=i*m+j
        for ni in ((i+1)%n,):
          v=ni*m+j
          P[u,u]-=a;P[v,v]-=a;P[u,v]+=a;P[v,u]+=a
        for nj in range(j+1,m):
          v=i*m+nj
          P[u,u]-=b;P[v,v]-=b;P[u,v]+=b;P[v,u]+=b
    return P

num=0; lp=0; rat=0
for n in range(3,23):
 for m in range(2,13):
  s,L,gb,gr,g,a,b,r=formulas(n,m)
  assert a>=0 and b>=0 and r>=-1e-13,(n,m,a,b,r)
  assert (gb<=gr+1e-12)==((n%2==0) or (m<= (6 if n==3 else 7))), (n,m,gb,gr)
  lambdas=[1-a*2*(1-math.cos(2*math.pi*k/n))- (0 if j==0 else m*b) for k in range(n) for j in range(m)]
  sorted_l=sorted(lambdas,reverse=True)
  observed=max(sorted_l[1],-sorted_l[-1]);assert abs(observed-(1-g))<1e-10,(n,m,observed,g)
  # LP constraints: 1-a*s<=t, 1-m*b<=t, a*L+m*b-1<=t and row capacity.
  c=[0,0,1]
  A=[[-s,0,-1],[0,-m,-1],[L,m,-1],[2,m-1,0]]
  rhs=[-1,-1,1,1]
  sol=linprog(c,A_ub=A,b_ub=rhs,bounds=[(0,None),(0,None),(0,None)],method='highs')
  assert sol.success and abs(sol.fun-(1-g))<5e-9,(n,m,sol.message,sol.fun,g)
  lp+=1
  if n<=12 and m<=7:
   P=build(n,m,a,b);ev=np.linalg.eigvalsh(P)
   assert abs(ev[-1]-1)<1e-12 and abs(max(abs(ev[:-1]))-(1-g))<1e-10
   assert np.min(P)>-1e-12 and np.max(abs(P.sum(axis=1)-1))<1e-12
   num+=1
for m in range(3,13):
 for n in (101,201,401,1001):
  s,L,gb,gr,g,a,b,r=formulas(n,m)
  ah=bh=1/(m+1)
  vals=[1-ah*2*(1-math.cos(2*math.pi*k/n))-(0 if j==0 else m*bh) for k in range(n) for j in (0,1)]
  vals.sort(reverse=True)
  hg=1-max(vals[1],-vals[-1]);assert hg>0
  if n==1001: assert abs((g/hg)-(m+1)/2)<0.0015,(m,g/hg)
  rat+=1
for n in (101,201,401,1001):
 m=2;s,L,gb,gr,g,a,b,r=formulas(n,m)
 c=math.cos(math.pi/n)
 gap=(2/3)*(1-c)
 if n==1001:assert abs(g/gap-6)<0.0002
print('VERIFY_OK', 'LP_cases',lp,'dense_eigensystems',num,'asymptotic_checks',rat,'odd_m2_ratio_to_6',g/gap)
print('example_n3_m7',formulas(3,7))
print('example_n5_m7',formulas(5,7))
print('example_n5_m8',formulas(5,8))
print('example_n6_m8',formulas(6,8))
