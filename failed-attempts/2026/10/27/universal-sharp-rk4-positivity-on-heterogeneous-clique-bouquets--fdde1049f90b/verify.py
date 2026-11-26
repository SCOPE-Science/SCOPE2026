#!/usr/bin/env python3
"""Exact symbolic and rational checks for RK4 on clique bouquets.
Science only. Uses SymPy; no external data or network access.
"""
from fractions import Fraction
from itertools import product
from sympy import Matrix, eye, zeros, symbols, factor, simplify, nroots, Rational

h, z, x = symbols('h z x')
r = lambda w: 1 - w + w**2/2 - w**3/6 + w**4/24
cubic = z**3 - 4*z**2 + 12*z - 24
assert factor(24*(r(x)-r(z-x)) - 2*(z-2)*x*(z-x)*(z-2*x)) == factor((2*x-z)*cubic)
assert factor(24*r(x) - ((x*x-2*x+2)**2 + 4*((x-2)**2+1))) == 0
assert factor(r(x)-1) == x*(x**3-4*x**2+12*x-24)/24

# Sum of squares certificate for positivity of across-clique kernel B(h).
n = symbols('n', integer=True, positive=True)
Q = 1 - (n+1)*h/3 + (n*n+n+1)*h*h/12
assert factor(12*Q - ((n*n+n+1)*(h - 2*(n+1)/(n*n+n+1))**2) - (8*n*n+4*n+8)/(n*n+n+1)) == 0

cases = [
 [1,1],[1,1,1],[1,2],[1,3],[1,4],[2,2],[3,2],[2,3,1],
 [4,2,1],[3,3],[5,1,2],[2,2,2],[4,3,2],[5,4],[1,1,1,1,1]
]
comparisons=0
for parts in cases:
 N=1+sum(parts)
 A=zeros(N)
 blocks=[]; k=1
 for s in parts:
  V=list(range(k,k+s));blocks.append(V);k+=s
  for u in V:
   A[0,u]=A[u,0]=1
  for u in V:
   for v in V:
    if u != v: A[u,v]=1
 L=zeros(N)
 for u in range(N):
  L[u,u]=sum(A[u,v] for v in range(N))
  for v in range(N):
   if u!=v:L[u,v]=-A[u,v]
 LL=L*L;LLL=LL*L;LLLL=LLL*L
 T=eye(N)-h*L+h*h*LL/2-h**3*LLL/6+h**4*LLLL/24
 P=Rational(1,N)
 M=N-1
 rh=r(h);rn=r(N*h)
 B=(M-N*rh+rn)/(N*M)
 block_index={v:i for i,b in enumerate(blocks) for v in b}
 for u in range(N):
  for v in range(N):
   if u==0 and v==0: expected=P+Rational(M,N)*rn
   elif u==0 or v==0: expected=(1-rn)/N
   else:
    a=block_index[u];b=block_index[v]
    if a!=b:expected=B
    else:
     s=parts[a];rk=r((s+1)*h)
     expected=B+(rh-rk)/s+(rk if u==v else 0)
   assert factor(T[u,v]-expected)==0,(parts,u,v)
   comparisons+=1

from mpmath import mp
mp.dps=65
rho=mp.findroot(lambda t:t**3-4*t**2+12*t-24,(2,3))
assert 2<rho<3
checks=0
for parts in cases:
 N=1+sum(parts)
 A=zeros(N)
 blocks=[];k=1
 for s in parts:
  V=list(range(k,k+s));blocks.append(V);k+=s
  for u in V:A[0,u]=A[u,0]=1
  for u in V:
   for v in V:
    if u!=v:A[u,v]=1
 L=zeros(N)
 for i in range(N):
  L[i,i]=sum(A[i,j] for j in range(N))
  for j in range(N):
   if i!=j:L[i,j]=-A[i,j]
 P1=L;P2=P1*L;P3=P2*L;P4=P3*L
 for t in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('0.99999'),mp.mpf('1.00001'),mp.mpf('1.1')]:
  step=t*rho/N
  Rk=eye(N)-step*P1+(step**2/2)*P2-(step**3/6)*P3+(step**4/24)*P4
  mi=min(mp.mpf(str(Rk[i,j])) for i in range(N) for j in range(N))
  if t<=1: assert mi>mp.mpf('-1e-48'),(parts,t,mi)
  else: assert Rk[0,1]<0,(parts,t,Rk[0,1])
  checks+=N*N

print('VERIFY_OK: scalar reflection identity, positive RK4 polynomial, across-block SOS certificate,',len(cases),'exact symbolic clique-bouquet matrices,',comparisons,'exact matrix-entry identities,',checks,'high-precision timestep-entry tests')
