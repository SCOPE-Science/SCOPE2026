#!/usr/bin/env python3
"""Finite corroboration of a marker-word factor classification."""
from math import floor

def gap_a(a,k): return int(floor(k**a+1e-11))
def gap_doubling(k): return 1<<(k-1)
def make_gaps(gap,n):
 g=[]; j=1
 while len(g)<3 or g[-1]<=n:
  g.append(gap(j)); j+=1
 return g
def formula(g,n):
 return n+1+int(n>=g[0]+1)+sum(max(0,min(g[j],n-g[j+1])) for j in range(len(g)-1))
def direct(g,n):
 p=[0]
 for d in g:p.append(p[-1]+d)
 N=p[-1]+n+1
 w=bytearray(N)
 for t in p:w[t]=1
 return len({bytes(w[i:i+n]) for i in range(N-n+1)})

for a in (1,1.01,1.25,1.5,2,2.25,3,4):
 for n in range(1,130):
  g=make_gaps(lambda j:gap_a(a,j),n)
  expected=formula(g,n)
  observed=direct(g,n)
  assert expected==observed,(a,n,expected,observed,g)
 print(a,'p(10)',formula(make_gaps(lambda j:gap_a(a,j),10),10),'p(75)',formula(make_gaps(lambda j:gap_a(a,j),75),75))
for n in range(1,130):
 g=make_gaps(gap_doubling,n)
 assert formula(g,n)==direct(g,n)
print('PASSED all finite full-language tests')
