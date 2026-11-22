"""Exact finite checks for stationary descent fluctuations under transpositions."""
from fractions import Fraction as F
from itertools import permutations, combinations
from math import comb

def cyc(p):return sum(p[i]>p[(i+1)%len(p)] for i in range(len(p)))
def linear(p):return sum(p[i]>p[i+1] for i in range(len(p)-1))
def swap(p,a,b):
 q=list(p);q[a],q[b]=q[b],q[a];return tuple(q)

def verify():
 tests=0
 for n in range(3,8):
  ps=list(permutations(range(n)))
  pairs=list(combinations(range(n),2)); m=len(pairs)
  lam=F(n-5,n-1); lamslow=F(n-3,n-1)
  vals={p:cyc(p) for p in ps}; ds={p:linear(p) for p in ps}
  vcyc=F(sum((2*vals[p]-n)**2 for p in ps),4*len(ps))
  vdes=F(sum((2*ds[p]-(n-1))**2 for p in ps),4*len(ps))
  assert vcyc==F(n,12); tests+=1
  assert vdes==F(n+1,12); tests+=1
  # pointwise eigen-relation of circular descents
  for p in ps:
   s=sum(vals[swap(p,a,b)] for a,b in pairs)
   assert F(s,m)-F(n,2)==lam*(F(vals[p])-F(n,2)),(n,p,s)
   tests+=1
  # stationary one-step covariance of ordinary and cyclic counts
  co=F(sum((2*ds[p]-(n-1))*(2*ds[swap(p,a,b)]-(n-1)) for p in ps for a,b in pairs),4*len(ps)*m)
  co0=F(sum((2*vals[p]-n)*(2*vals[swap(p,a,b)]-n) for p in ps for a,b in pairs),4*len(ps)*m)
  assert co==F(n+1,6*n)*lamslow+F((n-2)*(n+1),12*n)*lam,(n,co)
  assert co0==F(n,12)*lam
  tests+=2
  # exact expected quadratic variation
  qv=F(sum((vals[swap(p,a,b)]-vals[p])**2 for p in ps for a,b in pairs),len(ps)*m)
  assert qv==F(2*n,3*(n-1)); tests+=1
 # Two permutations with equal circular descent count can have different
 # conditional squared increments: the finite count is not strongly lumpable.
 p=(0,1,2,3,5,4); q=(0,1,2,4,5,3)
 assert cyc(p)==cyc(q)==2
 pp=list(combinations(range(6),2))
 gp=F(sum((cyc(swap(p,a,b))-cyc(p))**2 for a,b in pp),len(pp))
 gq=F(sum((cyc(swap(q,a,b))-cyc(q))**2 for a,b in pp),len(pp))
 assert (gp,gq)==(F(4,3),F(16,15));tests+=1
 print(f'PASS: {tests} exact tests; all permutations n=3,...,7')

if __name__=='__main__':verify()
