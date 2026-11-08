"""Independent deletion--contraction evaluation of the Tutte coadjoint formula."""
from functools import lru_cache
from collections import Counter
from itertools import product

def canonical(n,edges):
 return (n,tuple(sorted((min(a,b),max(a,b)) for a,b in edges)))

def components(n,edges):
 p=list(range(n))
 def root(a):
  while p[a]!=a:p[a]=p[p[a]];a=p[a]
  return a
 for a,b in edges:p[root(a)]=root(b)
 return len({root(i) for i in range(n)})

@lru_cache(None)
def tutte(n,edges,x,y):
 if not edges:return 1
 a,b=edges[0];rest=list(edges[1:])
 if a==b:return y*tutte(n,tuple(rest),x,y)
 # bridge iff deleting edge increases component count
 if components(n,rest)>components(n,list(edges)):
  return x*tutte(*contract(n,rest,a,b),x,y)
 return tutte(n,tuple(rest),x,y)+tutte(*contract(n,rest,a,b),x,y)

def contract(n,edges,a,b):
 d=[i-(i>b) for i in range(n)]
 d[b]=d[a]
 return canonical(n-1,[(d[u],d[v]) for u,v in edges])

def from_subsets(n,edges,q):
 ans=0
 for bits in product((0,1),repeat=len(edges)):
  S=[e for e,b in zip(edges,bits) if b]
  r=n-components(n,S)
  ans+=q**(n-r)*(q-1)**(len(S)-r)
 return ans

cases=[('empty',4,[]),('tree',4,[(0,1),(1,2),(1,3)]),('triangle',3,[(0,1),(1,2),(0,2)]),('parallel',2,[(0,1),(0,1)]),('loops',2,[(0,0),(0,1),(1,1)]),('disconnected',5,[(0,1),(1,2),(0,2),(3,4)]),('K4',4,[(a,b) for a in range(4) for b in range(a+1,4)])]
for q in (2,3,4,5,7,8,9):
 for name,n,edges in cases:
  nn,ee=canonical(n,edges);expect=q**components(n,edges)*tutte(nn,ee,q+1,q)
  got=from_subsets(n,edges,q)
  assert got==expect,(q,name,got,expect)
  print('PASS',q,name,got)
print('ALL_TUTTE_RECURSION_CHECKS_PASS')
