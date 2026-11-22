"""Independent coefficient recurrence for the joint (01,010) spectrum."""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import comb

def poly_by_gap(a,b):
 d={(0,0,0):1}
 for j in range(a+1):
  nd=defaultdict(int)
  for (k,t,h),val in d.items():
   for r in range(b-k+1):
    nd[k+r,t+r*j,h+r*j*(a-j)]+=val
  d=nd
 return {(t,h):v for (k,t,h),v in d.items() if k==b}

def by_partition(a,b):
 d=defaultdict(int)
 for x in combinations_with_replacement(range(a+1),b):
  d[(sum(x),sum(u*(a-u) for u in x))]+=1
 return dict(d)

checks=0; fiberchecks=0
for a in range(1,11):
 for b in range(1,11):
  d=poly_by_gap(a,b)
  e=by_partition(a,b)
  assert d==e,(a,b)
  assert sum(d.values())==comb(a+b,a)
  for t in range(a*b+1):
   spectrum={h:m for (tt,h),m in d.items() if tt==t}
   assert spectrum
   q,r=divmod(t,b); k,s=divmod(t,a)
   lo=s*(a-s);hi=a*t-((b-r)*q*q+r*(q+1)*(q+1))
   assert spectrum.get(lo)==1 and spectrum.get(hi)==1 and min(spectrum)==lo and max(spectrum)==hi,(a,b,t)
   assert all((h-(a-1)*t)%2==0 for h in spectrum)
   fiberchecks+=1
  checks+=1
print('PASS independent gap-product vs partition spectrum:',checks,'(a,b) pairs,',fiberchecks,'fibers, including exact coefficient multiplicities, normalization, sharp endpoint coefficients')
