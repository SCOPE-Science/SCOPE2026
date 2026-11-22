"""Independent ordered-surjection construction, direct chip dynamics replay."""
from itertools import product
from collections import Counter
from math import comb,factorial

def stirling(n,k):
  return sum((-1)**(k-j)*comb(k,j)*j**n for j in range(k+1))//factorial(k)

def step(x,m,n):
  fl=[int(z>=n) for z in x[:m]];fr=[int(z>=m) for z in x[m:]]
  return tuple(x[i]-n*fl[i]+sum(fr) for i in range(m))+tuple(x[m+i]-m*fr[i]+sum(fl) for i in range(n))

def labels(size,k):
  for a in product(range(k),repeat=size):
    if len(set(a))==k:yield a

def test(m,n):
  waves={};counts=Counter()
  for k in range(1,min(m,n)+1):
    for al in labels(m,k):
      for br in labels(n,k):
        for first in (0,1):
          rounds=[]
          for j in range(k):
            rounds.extend(([i for i in range(m) if al[i]==j],[m+i for i in range(n) if br[i]==j]) if first==0 else ([m+i for i in range(n) if br[i]==j],[i for i in range(m) if al[i]==j]))
          x=[0]*(m+n)
          for i in range(m+n):
            t=next(t for t,group in enumerate(rounds) if i in group)
            neigh=range(m,m+n) if i<m else range(m)
            x[i]=sum(next(j for j,g in enumerate(rounds) if w in g)>t for w in neigh)
          x=tuple(x);assert sum(x)==m*n
          assert x not in waves,(m,n,k,first,x)
          waves[x]=2*k;counts[2*k]+=1
          y=x
          for idx,group in enumerate(rounds):
            firing=tuple(i for i,val in enumerate(y) if val >= (n if i<m else m))
            assert firing==tuple(group),(m,n,k,x,idx,firing,group)
            y=step(y,m,n)
          assert y==x
  expected={2*k:2*factorial(k)**2*stirling(m,k)*stirling(n,k) for k in range(1,min(m,n)+1)}
  assert dict(counts)==expected,(counts,expected)
  print('Constructed K_{%d,%d}: waves=%d period profile=%s'%(m,n,len(waves),dict(sorted(counts.items()))))

for m,n in [(1,1),(2,3),(3,3),(3,4),(4,4)]:test(m,n)
print('PASS: every constructed orbit has the specified exact firing schedule and disjoint state')
