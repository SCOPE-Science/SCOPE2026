#!/usr/bin/env python3
"""Exhaustive integer certificate for strict-majority on PG(2,3)."""
from collections import Counter
from itertools import product, combinations

Q=3
pts=sorted({tuple((a*pow(next(x for x in v if x),-1,Q))%Q for a in v)
            for v in product(range(Q),repeat=3) if any(v)})
assert len(pts)==13
masks=[sum(1<<j for j,w in enumerate(pts) if sum(a*b for a,b in zip(v,w))%3==0)
       for v in pts]
assert all(m.bit_count()==4 for m in masks)
assert all(bool(masks[i]&(1<<j))==bool(masks[j]&(1<<i)) for i in range(13) for j in range(13))
N=1<<13
f=[sum(1<<i for i,m in enumerate(masks) if (s&m).bit_count()>=3) for s in range(N)]
f2=[f[f[s]] for s in range(N)]
f3=[f[f2[s]] for s in range(N)]
f4=[f[f3[s]] for s in range(N)]
f5=[f[f4[s]] for s in range(N)]
f6=[f[f5[s]] for s in range(N)]
assert f6==f4 and any(f4[s]!=f2[s] for s in range(N))
R={s for s in range(N) if f2[s]==s}
assert len(R)==821 and set(f4)==R
assert all(f2[s]==s for s in R)
# In zeros notation, no-3-collinear triples; triple-on-line plus an outside point;
# whole line plus an outside point.
lines=masks
collinear=lambda trip: any(all(m&(1<<i) for i in trip) for m in lines)
patterns=set((0,N-1))
for tri in combinations(range(13),3):
 if not collinear(tri): patterns.add(sum(1<<i for i in tri))
for line in lines:
 on=[i for i in range(13) if line&(1<<i)]
 off=[i for i in range(13) if not line&(1<<i)]
 for i in off:
  patterns.add(line|(1<<i))
  for tri in combinations(on,3):patterns.add((1<<i)|sum(1<<j for j in tri))
assert len(patterns)==821
assert {N-1-r for r in R}==patterns
assert Counter(s.bit_count() for s in R)=={0:1,8:117,9:468,10:234,13:1}
weights=Counter(f4)
assert Counter(weights.values())=={1:819,157:1,7216:1}
assert weights[0]==7216 and weights[N-1]==157
assert all(weights[s]==weights[f[s]] for s in R)
# f is an involution on R, so F on R x R is an involution.
fixed_count=len(R)
two_cycle=(len(R)**2-len(R))//2
fixed_basin=Counter(weights[s]*weights[f[s]] for s in R)
assert fixed_basin=={1:819,24649:1,52070656:1}
two_basin=Counter()
seen=set()
for a in R:
 for b in R:
  if (a,b) in seen:continue
  opposite=(f[b],f[a])
  seen.add((a,b));seen.add(opposite)
  if opposite!=(a,b):
   two_basin[weights[a]*weights[b]+weights[opposite[0]]*weights[opposite[1]]]+=1
assert two_basin=={2:334971,314:819,14432:819,2265824:1}
assert fixed_count==821 and two_cycle==336610
assert sum(k*v for k,v in fixed_basin.items())+sum(k*v for k,v in two_basin.items())==N*N
# Earliest time for f^t(s) to enter R; F^t acts on both shores by f^t (possibly swapped).
depth=[]
for s in range(N):
 z=s;d=0
 while z not in R:
  z=f[z];d+=1
  assert d<=4
 depth.append(d)
assert Counter(depth)=={0:821,1:572,2:4693,3:1170,4:936}
cum=0; first={}
for d in range(5):
 cum+=depth.count(d)
 first[d]=cum*cum - (cum-depth.count(d))**2
assert first=={0:674041,1:1266408,2:35098947,3:15610140,4:14459328}
print('POINTS',len(pts),'LINES',len(lines),'STABLE',len(R),'PATTERNS',len(patterns))
print('R_WEIGHT',sorted(Counter(s.bit_count() for s in R).items()))
print('FIBERS',sorted(Counter(weights.values()).items()))
print('FIXED',fixed_count,'TWO_CYCLE',two_cycle)
print('FIXED_BASINS',sorted(fixed_basin.items()))
print('TWO_BASINS',sorted(two_basin.items()))
print('ENTRANCE',sorted(first.items()))
print('CHECKED_SHORE_STATES',N,'FULL_CONFIGURATION_COUNT',N*N)
