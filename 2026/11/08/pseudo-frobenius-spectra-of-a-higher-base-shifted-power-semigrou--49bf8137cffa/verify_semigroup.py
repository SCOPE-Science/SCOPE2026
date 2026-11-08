#!/usr/bin/env python3
"""Independent integer Dijkstra verification of a closed-form numerical-semigroup claim."""
from math import gcd
from heapq import heappush,heappop

def formula(h,m,d):
 u=h*h-h+1;v=h**3-h+1;a=m*v;t=(h-1)**2
 L=lambda s:h*h*(s//u)+h*(s%u)
 assert v==h*u+t
 C=(m+1)*h**3-2*h*h-1
 pf=[a*C+d*(a-1-t),a*C+d*(a-1)]
 sumL=sum(L(s) for s in range(v))
 g=v*h**3*m*(m-1)//2+m*sumL+(d-1)*(a-1)//2
 return pf,g

def direct(h,m,d):
 u=h*h-h+1;v=h**3-h+1;a=m*v
 gens=[a,h*a+d,h*h*a+u*d,h**3*a+v*d]
 dist=[10**100]*a;dist[0]=0;heap=[(0,0)]
 while heap:
  n,r=heappop(heap)
  if n!=dist[r]:continue
  for b in gens[1:]:
   j=(r+b)%a;x=n+b
   if x<dist[j]:dist[j]=x;heappush(heap,(x,j))
 def member(n):return n>=0 and dist[n%a]<=n
 pf=sorted({x-a for x in dist if x>=a and all(member(x-a+b) for b in gens)})
 g=sum((x-r)//a for r,x in enumerate(dist))
 return pf,g

if __name__=='__main__':
 total=0
 for h in range(3,13):
  for m in range(1,5):
   for d in range(1,13):
    a=m*(h**3-h+1)
    if gcd(a,d)!=1:continue
    f=formula(h,m,d);actual=direct(h,m,d)
    assert f==actual, (h,m,d,f,actual)
    total+=1
  print('h',h,'tested',total,flush=True)
 print('PASS',total, 'parameter triples')
