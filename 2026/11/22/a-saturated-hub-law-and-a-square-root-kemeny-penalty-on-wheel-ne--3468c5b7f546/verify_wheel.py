#!/usr/bin/env python3
"""Exact rational finite checks and independent spectral/asymptotic spot-checks.
All-size statements are proved analytically in RESULT.md, not by these tests.
"""
from fractions import Fraction as F
from math import sin, cos, pi, sqrt, exp, log

def inverse(A):
 n=len(A); Z=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for c in range(n):
  k=next(i for i in range(c,n) if Z[i][c]);Z[c],Z[k]=Z[k],Z[c]
  d=Z[c][c];Z[c]=[z/d for z in Z[c]]
  for i in range(n):
   if i!=c:
    d=Z[i][c]
    if d:Z[i]=[x-d*y for x,y in zip(Z[i],Z[c])]
 return [z[n:] for z in Z]

def chain(m,b,a):
 n=m+1;P=[[F(0) for _ in range(n)] for _ in range(n)]
 for i in range(m):
  u=i+1;v=(i+1)%m+1
  P[0][u]=P[u][0]=b
  P[u][v]=P[v][u]=a
 P[0][0]=1-m*b
 for i in range(1,n):P[i][i]=1-sum(P[i][j] for j in range(n) if j!=i)
 assert all(v>=0 for row in P for v in row)
 assert all(sum(row)==1 for row in P)
 return P

def kval(P):
 n=len(P)
 A=[[F(i==j)-P[i][j]+F(1,n) for j in range(n)] for i in range(n)]
 J=inverse(A)
 return sum(J[i][i] for i in range(n))-1

def spec(m,b,a):
 return 1/((m+1)*float(b))+sum(1/(float(b)+2*float(a)*(1-cos(2*pi*j/m))) for j in range(1,m))

checks=0
for m in range(3,13):
 b=F(1,m);a=(1-b)/2
 K=kval(chain(m,b,a));Ks=spec(m,b,a)
 assert abs(float(K)-Ks)<1e-9;checks+=1
 km=kval(chain(m,F(1,m),F(1,m)))
 assert K<=km and (K<km if m>3 else K==km);checks+=1
 for j in range(1,8):
  bj=b*F(j,8); aj=(1-bj)/2
  kj=kval(chain(m,bj,aj));assert K<kj;checks+=1
 for j in range(1,5):
  aj=a*F(j,5)
  kj=kval(chain(m,b,aj));assert K<kj;checks+=1
 print('m',m,'K_exact',str(K),'max_degree',str(km))
for m in [200,1000,5000,20000]:
 q=1-1/m
 rho=q/(1+sqrt(1-q*q))
 K=m/(m+1)+m/sqrt(1-q*q)*(1+rho**m)/(1-rho**m)-m
 lam=(3-sqrt(5))/2
 Kd=m/(m+1)+m*m/sqrt(5)*(1+lam**m)/(1-lam**m)-m
 print('asymptotic',m,'K/m^1.5=',K/m**1.5,'degree/m^2=',Kd/m**2,'ratio/sqrt(m)=',Kd/K/sqrt(m))
 assert abs(K/m**1.5 -1/sqrt(2)) <.13;checks+=1
 assert abs(Kd/m**2-1/sqrt(5)) <.01;checks+=1
print('PASS checks',checks)
