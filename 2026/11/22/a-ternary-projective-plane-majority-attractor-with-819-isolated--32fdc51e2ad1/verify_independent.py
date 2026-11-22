#!/usr/bin/env python3
"""Independent affine-incidence/set-based projective-plane classifier."""
from collections import Counter
from itertools import combinations
# Affine points (x,y); four points at infinity labelled 9..12.
point=set(range(13)); lines=[]
for slope in range(3):
 for intercept in range(3):
  lines.append(frozenset(3*x+(slope*x+intercept)%3 for x in range(3))|frozenset([9+slope]))
for x in range(3):lines.append(frozenset([3*x+y for y in range(3)]+[12]))
lines.append(frozenset([9,10,11,12]))
assert len(lines)==13 and all(len(L)==4 for L in lines)
assert all(sum(i in L for L in lines)==4 for i in point)
assert all(sum(i in L and j in L for L in lines)==1 for i,j in combinations(point,2))
N=1<<13
# Distinct transformations from point subsets to secant lines and back.
line_neigh=[{j for j,L in enumerate(lines) if i in L} for i in point]
line_bit=[frozenset(i for i in point if (s>>i)&1) for s in range(N)]

def point_to_line(s):
 S=line_bit[s]
 return sum(1<<j for j,L in enumerate(lines) if len(S&L)>=2)
def line_to_point(s):
 chosen={j for j in range(13) if (s>>j)&1}
 return sum(1<<i for i in point if len(chosen&line_neigh[i])>=2)

P=[point_to_line(s) for s in range(N)]
L=[line_to_point(s) for s in range(N)]
Hpoint=[L[P[s]] for s in range(N)]
Hline=[P[L[s]] for s in range(N)]
Rp={s for s in range(N) if Hpoint[s]==s}
Rl={s for s in range(N) if Hline[s]==s}
assert len(Rp)==len(Rl)==821
# full stabilization in at most 4 steps, cannot do it by 3
p4=[Hpoint[Hpoint[s]] for s in range(N)]
l4=[Hline[Hline[s]] for s in range(N)]
assert all(Hpoint[p4[s]]==p4[s] and Hline[l4[s]]==l4[s] for s in range(N))
assert set(p4)==Rp and set(l4)==Rl
pweights=Counter(p4); lweights=Counter(l4)
assert Counter(pweights.values())==Counter(lweights.values())=={1:819,157:1,7216:1}
# geometric classification of stable point zeros
expected={0,N-1}
for tri in combinations(point,3):
 if not any(set(tri)<=set(Li) for Li in lines):
  expected.add(sum(1<<i for i in tri))
for Li in lines:
 core=sum(1<<i for i in Li)
 for i in point-set(Li):
  expected.add(core+(1<<i))
  for tri in combinations(Li,3):expected.add((1<<i)+sum(1<<j for j in tri))
assert expected==Rp and len(expected)==821
# Fixed global states: (a,P(a)) with a in Rp.
assert all(L[P[a]]==a for a in Rp)
assert {P[a] for a in Rp}==Rl
fixed_basins=Counter(pweights[a]*lweights[P[a]] for a in Rp)
assert fixed_basins=={1:819,24649:1,52070656:1}
# Formula: every phase (a,b) either is fixed, or has opposite (L(b),P(a)).
two_basins=Counter()
visited=set()
for a in Rp:
 for b in Rl:
  if (a,b) in visited:continue
  counterpart=(L[b],P[a]);visited.add((a,b));visited.add(counterpart)
  if (a,b)!=counterpart:
   two_basins[pweights[a]*lweights[b]+pweights[counterpart[0]]*lweights[counterpart[1]]]+=1
assert two_basins=={2:334971,314:819,14432:819,2265824:1}
# Phase entry under F^t: side maps alternate with each iterate.
# Exact first-entrance depth for each shore, using alternating incidence maps
for side in [0,1]:
 d=[]
 for s in range(N):
  x=s
  for t in range(5):
   allowed=(Rp if (side+t)%2==0 else Rl)
   if x in allowed:break
   x=(P if (side+t)%2==0 else L)[x]
  else:raise AssertionError('not periodic within 4')
  d.append(t)
 assert Counter(d)=={0:821,1:572,2:4693,3:1170,4:936}
print('INDEPENDENT_POINTS',len(point),'LINES',len(lines))
print('PHASES',len(Rp),len(Rl))
print('FIBERS',sorted(Counter(pweights.values()).items()))
print('FIXED_BASINS',sorted(fixed_basins.items()))
print('TWO_CYCLE_BASINS',sorted(two_basins.items()))
print('SHORE_ENTRY_DEPTHS',sorted(Counter(d).items()))
