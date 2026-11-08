#!/usr/bin/env python3
"""Exact Walsh enumeration for graph windows of binary quadratic forms.
No external libraries.  Prints multiplicities and asserts the complete theorem.
"""
from collections import Counter
from itertools import product

def fwht(a):
 a=a[:]; n=len(a)
 h=1
 while h<n:
  for j in range(0,n,2*h):
   for k in range(j,j+h):
    x,y=a[k],a[k+h]
    a[k],a[k+h]=x+y,x-y
  h*=2
 return a

def qform(x,r):
 return sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(r))&1

def check(m,r,linear=0):
 N=1<<(m+1); M=1<<m; k=m-2*r; M0=1<<(2*r)
 g=[0]*N
 for x in range(M):
  q=qform(x,r)^((x&linear).bit_count()&1)
  g[x+(q<<m)]=1
 dist=Counter()
 for a in range(N):
  h=[g[z]*g[z^a] for z in range(N)]
  dist.update(abs(v) for v in fwht(h) if v)
 pred=Counter()
 pred[M]+=1<<k
 if r:
  pred[M//2]+=(1<<k)*4*(M0-1)
  pred[(1<<k)*(1<<r)]+=(1<<k)*M0*M0
 else:
  pred[M]+=1<<k
 assert dist==pred, (m,r,dist,pred)
 print('m',m,'polar_rank',2*r,'linear',linear,'rank',sum(dist.values()),'nonzero_ambiguity_multiplicities',sorted(dist.items()),'N^2',N*N)

if __name__=='__main__':
 for m in range(1,7):
  for r in range(m//2+1):
   for ell in (0, (1<<(m-1)) if m else 0):
    check(m,r,ell)
 print('BINARY_QUADRATIC_GRAPH_AMBIGUITY_CHECKS_OK')

def check_direct_projector_gram(m, r):
 # Exact full projector Gram eigenvalues via Walsh diagonalization of its first row.
 N=1<<(m+1); M=1<<m
 g=[0]*N
 for x in range(M):
  g[x | (qform(x,r)<<m)]=1
 shifts=[]
 for a in range(N):
  for b in range(N):
   shifts.append([g[z^a]*((-1)**((b&z).bit_count()&1)) for z in range(N)])
 row=[]
 for h in shifts:
  row.append(sum(g[z]*h[z] for z in range(N))**2)
 actual=Counter(fwht(row))
 amp=Counter()
 for a in range(N):
  h=[g[z]*g[z^a] for z in range(N)]
  amp.update(abs(v) for v in fwht(h) if v)
 pred=Counter({0:N*N-sum(amp.values())})
 for c,n in amp.items():
  pred[N*c*c]+=n
 assert actual==pred,(m,r,actual,pred)
 print('GRAM_EXACT_OK','m',m,'r',r,'eigs',sorted(actual.items()))

if __name__=='__main__':
 for m,r in [(2,1),(3,1),(4,2)]:
  check_direct_projector_gram(m,r)
 print('EXACT_PROJECTOR_GRAM_CHECKS_OK')
