#!/usr/bin/env python3
"""Independent full labelled-state replay for small complete tripartite graphs."""
from itertools import product
from collections import Counter
from math import comb

TABLE={
(1,1,2):4,(1,2,2):16,(1,2,3):8,(1,3,3):12,
(1,3,4):4,(1,4,4):4,(2,2,2):42,(2,2,3):32,
(2,2,4):6,(2,3,3):36,(2,3,4):12,(2,4,4):6,
(3,3,3):36,(3,3,4):12,(3,4,4):4,(4,4,4):1}

def surj(n,j):
    return sum((-1)**(j-k)*comb(j,k)*k**n for k in range(j+1))

def formula(a,b,c):
    from itertools import permutations
    return sum(coeff*sum(surj(a,i)*surj(b,j)*surj(c,k) for i,j,k in set(permutations(t))) for t,coeff in TABLE.items())

def step(x,parts):
    ends=[0,parts[0],parts[0]+parts[1],sum(parts)]
    excited=[any(v==1 for v in x[ends[i]:ends[i+1]]) for i in range(3)]
    out=[]
    for i in range(3):
        active=any(excited[j] for j in range(3) if j!=i)
        for v in x[ends[i]:ends[i+1]]:
            out.append(1 if v==0 and active else 0 if v==0 else (v+1)%4)
    return tuple(out)

def entry_period(x,parts):
    seen={};t=0
    while x not in seen:
        seen[x]=t
        x=step(x,parts)
        t+=1
        assert t<100
    return seen[x],t-seen[x]

checks=0;configurations=0
for a in range(1,4):
 for b in range(1,4):
  for c in range(1,4):
   if a+b+c>9: continue
   tally=Counter()
   for x in product(range(4),repeat=a+b+c):
    t,p=entry_period(x,(a,b,c))
    assert t<=6 and p in (1,4)
    tally[(t,p)]+=1
   assert tally[(0,1)]==1
   assert tally[(0,4)]==formula(a,b,c)
   assert sum(tally.values())==4**(a+b+c)
   assert max(t for t,p in tally)==(5 if (a,b,c)==(1,1,1) else 6)
   checks+=1; configurations+=4**(a+b+c)
   print('DIRECT',a,b,c,'initial_period4',tally[(0,4)],'first_entry_max',max(t for t,p in tally))
assert entry_period((0,3,1,2),(1,1,2))==(6,1)
print('DIRECT_CASES',checks,'CONFIGURATIONS',configurations)
print('INDEPENDENT_DIRECT_CHECK_PASS')
