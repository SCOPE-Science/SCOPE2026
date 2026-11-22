from functools import lru_cache
from fractions import Fraction
from collections import defaultdict
W=[f'{i:04b}' for i in (0,1,2,3,4,5,8,10)]
@lru_cache(None)
def overlap(a,b):
 return next((j for j in range(min(len(a),len(b)),0,-1) if a.endswith(b[:j])),0)
@lru_cache(None)
def distrib(S):
 if len(S)==1:return {len(S[0]):Fraction(1)}
 choices=[(overlap(a,b),a,b) for a in S for b in S if a!=b]
 top=max(t for t,_,_ in choices)
 assert top<=3, "Unexpected component overlap"
 assert all(not any(x in a+b[t:] for x in S if x!=a and x!=b) for t,a,b in choices if t==top), "Unexpected absorption"
 pairs=[(t,a,b) for t,a,b in choices if t==top]
 D=defaultdict(Fraction)
 for t,a,b in pairs:
  merge=a+b[t:]
  ns=tuple(sorted(tuple(x for x in S if x!=a and x!=b and x not in merge)+(merge,)))
  for length,p in distrib(ns).items():D[length]+=p/len(pairs)
 return dict(D)
print('inputs',W)
a=distrib(tuple(W))
print('distribution', a)
print('failure probability',a.get(17),'total',sum(a.values()),'cache',distrib.cache_info())
