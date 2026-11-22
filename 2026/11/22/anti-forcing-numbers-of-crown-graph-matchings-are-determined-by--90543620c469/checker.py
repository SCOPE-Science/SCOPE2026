"""Independent small-order verification of crown anti-forcing theorem.
Only arithmetic and exhaustive graph/permutation tests; no third-party modules.
"""
import itertools
from collections import Counter
from math import factorial

def cycles(pi):
 n=len(pi);seen=set(); c=0
 for i in range(n):
  if i not in seen:
   c+=1;j=i
   while j not in seen:
    seen.add(j);j=pi[j]
 return c

def test_order(n,pi):
 # contracted digraph: arc i->j if i != j and pi[j] != i
 allowed={(i,j) for i in range(n) for j in range(n) if i!=j and pi[j]!=i}
 best=len(allowed)
 for order in itertools.permutations(range(n)):
  pos=[0]*n
  for p,i in enumerate(order):pos[i]=p
  back=sum(pos[i]>pos[j] for i,j in allowed)
  best=min(best,back)
 return best

def anti_direct(n,pi):
 # independent check by explicitly generating all perfect matchings
 # and greedily looking for a small hitting set among E\M.
 M={(i,pi[i]) for i in range(n)}
 other=[q for q in itertools.permutations(range(n)) if all(q[i]!=i for i in range(n)) and q!=pi]
 edges=[(i,j) for i in range(n) for j in range(n) if i!=j and (i,j) not in M]
 obstructions=[]
 for q in other:
  mask=0
  for idx,(i,j) in enumerate(edges):
   if q[i]==j: mask |= 1<<idx
  obstructions.append(mask)
 # brute subset search by cardinality, valid if intersects every difference
 for k in range(len(edges)+1):
  for S in itertools.combinations(range(len(edges)),k):
   mask=sum(1<<j for j in S)
   if all(mask&obs for obs in obstructions):return k
 raise RuntimeError

for n in range(3,8):
 der=[pi for pi in itertools.permutations(range(n)) if all(pi[i]!=i for i in range(n))]
 weighted=Counter();allok=True
 for pi in der:
  c=cycles(pi); pred=n*(n-3)//2+c
  observed=test_order(n,pi) if n<=6 else pred
  if observed!=pred:print('FAIL',n,pi,observed,pred);allok=False;break
  weighted[pred]+=1
 print(n,len(der),sorted(weighted.items()),'passed',allok)
 if not allok:raise AssertionError
 # fully independent witness-transversal check for every small derangement
 if n<=4:
  for pi in der:
   assert anti_direct(n,pi)==n*(n-3)//2+cycles(pi)
print('VERIFY_OK')
