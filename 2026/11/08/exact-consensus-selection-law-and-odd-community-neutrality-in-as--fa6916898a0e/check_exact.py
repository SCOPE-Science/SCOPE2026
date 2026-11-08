#!/usr/bin/env python3
"""Exact rational absorption calculation for asynchronous open-neighbor majority on complete bipartite graphs."""
from fractions import Fraction
from functools import lru_cache
from math import comb

def race(m,n,a,b):
    if 2*a==m and 2*b==n: return Fraction(0)
    if 2*a==m: return Fraction(int(2*b>n))
    if 2*b==n: return Fraction(int(2*a>m))
    sa=(2*a>m); sb=(2*b>n)
    if sa==sb:return Fraction(int(sa))
    if not sa: return 1-race(m,n,m-a,n-b)
    x=a; y=n-b
    r=a-m//2; s=(n+1)//2-b
    ans=Fraction(0)
    from math import perm
    for j in range(r):
        ans+=Fraction(comb(s+j-1,j)*perm(y,s)*perm(x,j),perm(x+y,s+j))
    return ans

@lru_cache(None)
def dp(m,n,a,b):
    if 2*a==m and 2*b==n:return Fraction(0)
    A=0;B=0
    if 2*b>n: A=m-a
    if 2*b<n: A=a
    if 2*a>m: B=n-b
    if 2*a<m: B=b
    if A+B==0:
      if a==0 and b==0: return Fraction(0)
      if a==m and b==n: return Fraction(1)
      raise AssertionError((m,n,a,b,'other terminal'))
    x=a+(1 if 2*b>n else -1 if 2*b<n else 0)
    y=b+(1 if 2*a>m else -1 if 2*a<m else 0)
    aa=dp(m,n,x,b) if A else Fraction(0)
    bb=dp(m,n,a,y) if B else Fraction(0)
    return Fraction(A,A+B)*aa+Fraction(B,A+B)*bb

if __name__=='__main__':
  total=0
  for m in range(1,9):
    for n in range(1,9):
      for a in range(m+1):
        for b in range(n+1):
          got=dp(m,n,a,b); exp=race(m,n,a,b)
          assert got==exp,(m,n,a,b,got,exp)
          total+=1
  print('PASS: exact DP agrees with finite-sum formula for',total,'count-states, all m,n<=8')
  for m,n in [(3,3),(4,4),(5,2),(7,4),(10,10),(15,4),(31,3),(100,4)]:
    print('all-opposed',(m,n),'Pr(final one)=',race(m,n,m,0))
