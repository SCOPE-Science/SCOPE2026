from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
W=[f'{i:04b}' for i in (0,1,2,3,4,5,8,10)]
@lru_cache(None)
def overlap(a,b):
 return next((j for j in (3,2,1) if a.endswith(b[:j])),0)
@lru_cache(None)
def dp(P):
 if len(P)==1: return {0:Fraction(1)}
 choices=[(overlap(W[p[-1]],W[q[0]]),i,j) for i,p in enumerate(P) for j,q in enumerate(P) if i!=j]
 high=max(z for z,_,_ in choices)
 allowed=[(z,i,j) for z,i,j in choices if z==high]
 D=defaultdict(Fraction)
 for z,i,j in allowed:
  np=tuple(sorted([p for t,p in enumerate(P) if t not in (i,j)]+[P[i]+P[j]]))
  for gain,prob in dp(np).items(): D[gain+z]+=prob/len(allowed)
 return dict(D)
P=tuple((i,) for i in range(8))
print({32-k:v for k,v in sorted(dp(P).items())});print('cache',dp.cache_info())
