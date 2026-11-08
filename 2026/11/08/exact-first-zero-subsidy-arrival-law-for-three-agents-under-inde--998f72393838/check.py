# Exact exhaustive finite-horizon test, not a proof for unbounded horizons.
# Requires only Python standard library.
from itertools import permutations, combinations
from fractions import Fraction
from collections import Counter

def brute(perms):
 m=len(perms[0]); rank=[]
 for p in perms:
  d=[0]*m
  for j,h in enumerate(p):d[h]=j
  rank.append(d)
 for hs in combinations(range(m),3):
  if len({min(hs,key=lambda h:r[h]) for r in rank})==3:return True
 return False

def removal(perms):
 m=len(perms[0]); rem=set(range(m)); k=0
 while len(rem)>=3:
  top=[next(h for h in p if h in rem) for p in perms]
  if len(set(top))==3:return True,k
  dup=next(x for x in top if top.count(x)>=2)
  rem.remove(dup);k+=1
 return False,k

for m in range(3,7):
 ps=list(permutations(range(m))); ref=ps[0]; totals=Counter()
 for p in ps:
  for q in ps:
   pair=(ref,p,q)
   a=brute(pair);b,k=removal(pair)
   assert a==b,(m,p,q,a,b,k)
   totals[(b,k)]+=1
 n=len(ps)**2; P=Fraction(1)
 print('m',m,'N',n,'frequency',sorted(totals.items()))
 for s in range(m,2,-1):
  p=Fraction((s-1)*(s-2),s*s)
  # success with k removed
  k=m-s
  assert Fraction(totals[True,k],n)==P*p
  P*=1-p
 assert Fraction(totals[False,m-2],n)==P
 print('FAILURE',P,'SUCCESS',1-P)
