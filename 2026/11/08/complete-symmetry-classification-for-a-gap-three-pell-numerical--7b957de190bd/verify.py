#!/usr/bin/env python3
"""Exact-arithmetic independent checks of Pell-triple numerical-semigroup symmetry."""
from math import gcd
from heapq import heappush, heappop
P=[0,1]
for _ in range(24): P.append(2*P[-1]+P[-2])
checked=0
for n in range(1,13):
 a,b,c=P[n],P[n+3],P[n+4]
 assert 5*c==a+12*b
 assert gcd(a,b)==P[gcd(n,3)]
 assert gcd(a,c)==P[gcd(n,4)]
 assert gcd(b,c)==1
 dist=[10**100]*a;dist[0]=0
 pq=[(0,0)]
 while pq:
  d,j=heappop(pq)
  if d!=dist[j]:continue
  for z in (b,c):
   jj=(j+z)%a;dd=d+z
   if dd<dist[jj]:dist[jj]=dd;heappush(pq,(dd,jj))
 g=sum(dist)//a-(a-1)//2;f=max(dist)-a
 expected=(n in (1,2,4) or n%3==0)
 assert (2*g==f+1)==expected,(n,a,b,c,f,g)
 checked+=1
print(f'VERIFY_OK indices={checked} through=12 exact_aperies=yes Pell_identity=yes rank_gcds=yes symmetry_iff_1_2_4_or_3_divides=yes')
