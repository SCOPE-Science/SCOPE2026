#!/usr/bin/env python3
"""Independent finite-field checks of the commutator-graph Fourier formulas."""
from itertools import product
from collections import Counter
from math import isclose, cos, sin, pi


def mm(A,B,n,p):
 return tuple(sum(A[n*i+k]*B[n*k+j] for k in range(n))%p for i in range(n) for j in range(n))

def add(A,B,p):
 return tuple((a+b)%p for a,b in zip(A,B))

def sub(A,B,p):
 return tuple((a-b)%p for a,b in zip(A,B))

def traceprod(A,B,n,p):
 return sum(A[n*i+j]*B[n*j+i] for i in range(n) for j in range(n))%p

def rank(mat,p):
 R=[list(row) for row in mat]; m=len(R); n=len(R[0]) if m else 0; r=0
 for j in range(n):
  k=next((k for k in range(r,m) if R[k][j]%p),None)
  if k is None:continue
  R[r],R[k]=R[k],R[r]
  inv=pow(R[r][j]%p,-1,p)
  R[r]=[(x*inv)%p for x in R[r]]
  for k in range(m):
   if k==r:continue
   z=R[k][j]%p
   if z:R[k]=[(a-z*b)%p for a,b in zip(R[k],R[r])]
  r+=1
  if r==m:break
 return r

def ad_matrix(C,n,p):
 E=[tuple(int(k==j) for k in range(n*n)) for j in range(n*n)]
 cols=[sub(mm(C,e,n,p),mm(e,C,n,p),p) for e in E]
 return list(zip(*cols))

def solve(M,y,p):
 M=[list(row)+[int(x)] for row,x in zip(M,y)]
 h=len(M); w=len(M[0])-1; pivot=[]; r=0
 for j in range(w):
  k=next((k for k in range(r,h) if M[k][j]%p),None)
  if k is None:continue
  M[r],M[k]=M[k],M[r];inv=pow(M[r][j]%p,-1,p)
  M[r]=[(a*inv)%p for a in M[r]]
  for k in range(h):
   if k!=r:
    z=M[k][j]
    if z: M[k]=[(a-z*b)%p for a,b in zip(M[k],M[r])]
  pivot.append(j);r+=1
 if any(all(v%p==0 for v in row[:w]) and row[w]%p for row in M):return None
 x=[0]*w
 for i,j in enumerate(pivot):x[j]=M[i][-1]%p
 return tuple(x)

def theory_value(A,B,C,n,p):
 M=ad_matrix(C,n,p); r=rank(M,p)
 sol=solve(M,tuple(-x%p for x in B),p)
 if sol is None:return 0j,r
 # A must be in the image of ad_C, equivalent to A annihilating kernel,
 # and -ad_C is adjoint to ad_C with respect to trace pairing.
 if solve(M,A,p) is None:return 0j,r
 phase=traceprod(A,sol,n,p)
 return p**(2*n*n-r)*complex(cos(2*pi*phase/p),sin(2*pi*phase/p)),r

def brute_value(A,B,C,n,p):
 elems=list(product(range(p),repeat=n*n))
 bins=[0]*p
 for X in elems:
  cx=mm(C,X,n,p); xc=mm(X,C,n,p)
  bracket=sub(cx,xc,p)
  phase0=(traceprod(A,X,n,p))
  for Y in elems:
   phase=(phase0+traceprod(B,Y,n,p)+traceprod(C,sub(mm(X,Y,n,p),mm(Y,X,n,p),p),n,p))%p
   bins[phase]+=1
 return sum(bins[j]*complex(cos(2*pi*j/p),sin(2*pi*j/p)) for j in range(p))

def verify_distribution(p):
 n=3; out=Counter()
 for k,C in enumerate(product(range(p),repeat=9)):
  r=rank(ad_matrix(C,n,p),p)
  out[r]+=1
 N5=p*(p*p+p+1)*(p**3-1)
 assert out=={0:p,4:N5,6:p**9-p-N5},(p,out,N5)
 R=p+N5*p**8+(p**9-p-N5)*p**12
 print('M3 complete adjoint ranks',p,dict(out),'convolution rank',R,'ambient',p**27,flush=True)
 return R

def verify_direct(n,p,number):
 zero=(0,)*(n*n)
 I=tuple(int(i==j) for i in range(n) for j in range(n))
 E=lambda ij: tuple(int(i==ij) for i in range(n*n))
 probes=[(E(0),E(1),E(1)),(zero,zero,I),(zero,zero,E(1)),(E(0),E(1),E(2)),(E(3),zero,E(0)),(E(5 if n*n>5 else 2),E(1),E(2))]
 for k,(A,B,C) in enumerate(probes[:number]):
  predicted,r=theory_value(A,B,C,n,p)
  actual=brute_value(A,B,C,n,p)
  assert isclose(actual.real,predicted.real,abs_tol=1.e-6,rel_tol=1.e-8)
  assert isclose(actual.imag,predicted.imag,abs_tol=1.e-6,rel_tol=1.e-8)
  print('raw Fourier check',n,p,k,'adjoint rank',r,'abs',round(abs(actual)),'passed',flush=True)

if __name__=='__main__':
 verify_distribution(2)
 verify_distribution(3)
 verify_direct(2,2,6)
 verify_direct(2,3,5)
 verify_direct(3,2,6)
 print('ALL_COMMUTATOR_GRAPH_CHECKS_OK',flush=True)

# Rational-canonical enumeration via exact formal power series.
from fractions import Fraction
from math import prod

def partitions(n,max_part=None):
 if n==0:yield ();return
 if max_part is None:max_part=n
 for first in range(min(n,max_part),0,-1):
  for rest in partitions(n-first,first): yield (first,)+rest

def irreducibles(q,d):
 def mobius(x):
  v=1;p=2
  while p*p<=x:
   if x%p==0:
    x//=p
    if x%p==0:return 0
    v=-v
    while x%p==0:x//=p
   p+=1
  if x>1:v=-v
  return v
 return sum(mobius(e)*q**(d//e) for e in range(1,d+1) if d%e==0)//d

def centralizer_series(q,N):
 # H(z,t): the coefficient of z^n t^c, multiplied by |GL_n|,
 # counts matrices in M_n(F_q) with centralizer dimension c.
 H={(0,0):Fraction(1)}
 for d in range(1,N+1):
  local={}
  for size in range(0,N//d+1):
   for lam in partitions(size):
    colsum=sum(sum(1 for x in lam if x>=j)**2 for j in range(1,(lam[0] if lam else 0)+1))
    c=d*colsum
    mult={j:lam.count(j) for j in set(lam)}
    aut=Fraction(q**c)
    for m in mult.values():
     for k in range(1,m+1):aut*=Fraction(q**(d*k)-1,q**(d*k))
    local[(size*d,c)]=local.get((size*d,c),Fraction(0))+1/aut
  for _ in range(irreducibles(q,d)):
   nxt={}
   for (s,c),a in H.items():
    for (ss,cc),b in local.items():
     if s+ss>N:continue
     key=(s+ss,c+cc)
     nxt[key]=nxt.get(key,Fraction(0))+a*b
   H=nxt
 return H

def check_centralizer_series(q,n):
 from collections import Counter
 G=prod(q**n-q**k for k in range(n))
 H=centralizer_series(q,n)
 dist=Counter()
 for (s,c),v in H.items():
  if s==n:
   w=v*G
   assert w.denominator==1,(q,n,c,w)
   dist[c]+=int(w)
 assert sum(dist.values())==q**(n*n)
 R=sum(v*q**(2*(n*n-c)) for c,v in dist.items())
 if n==3:
  N5=q*(q*q+q+1)*(q**3-1)
  assert dist=={9:q,5:N5,3:q**9-q-N5}
 print('RATIONAL_CANONICAL_SERIES_OK',q,n,'dist',dict(dist),'rank',R,flush=True)
 return R

if __name__=='__main__':
 for q in (2,3,4):
  for n in (1,2,3):check_centralizer_series(q,n)
 print('ALL_EULER_PRODUCT_CHECKS_OK')
