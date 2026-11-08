from fractions import Fraction as F
from itertools import product,combinations_with_replacement
from functools import lru_cache

def accepted(z,t):
 s,tau=z
 return t>=tau if s==1 else 1-t>=tau

def candidates(pool):
 cs=sorted({F(0),F(1)}|{z[1] if z[0]==1 else 1-z[1] for z in pool})
 return tuple(sorted(set(cs+[(x+y)/2 for x,y in zip(cs,cs[1:])])))

def calc(n,k,pool):
 ts=candidates(pool)
 profiles=[]
 # only possible unqueried multisets (not their identities)
 for Uc in combinations_with_replacement(pool,n-k):
  profiles.append(tuple(sum(accepted(z,t) for z in Uc) for t in ts))
 # for full optimum with query observations
 max_min=-1; max_obs=None
 for obs in product(pool,repeat=k):
  known=tuple(sum(accepted(z,t) for z in obs) for t in ts)
  worstreg=[0]*len(ts)
  for unseen in profiles:
   possible=[a+b for a,b in zip(known,unseen)]
   optimum=max(possible)
   for i,s in enumerate(possible):
    worstreg[i]=max(worstreg[i],optimum-s)
  best=min(worstreg)
  if best>max_min:
   max_min=best;max_obs=obs
 return max_min,max_obs

groups=[('lower',(F(1,4),F(1,2))),('higher',(F(3,4),F(1))),('mixed-close',(F(1,2),F(3,4))),('mixed-wide',(F(1,4),F(3,4))),('mixed-max',(F(1,4),F(1))),('degenerate-equal-low',(F(1,2),F(1,2))),('degenerate-equal-high',(F(3,4),F(3,4)))]
cases=0
for label,(a,b) in groups:
    vals=[F(j,4) for j in range(1,5) if a<=F(j,4)<=b]
    pool=tuple((s,tau) for s in (1,-1) for tau in vals)
    for n in range(1,6):
        for k in range(n+1):
            got,_=calc(n,k,pool)
            expect=0 if b<=F(1,2) else (max(0,n-k-(k%2)) if a>F(1,2) else n-k)
            assert got==expect, (label,n,k,got,expect)
            cases+=1
    print('phase group',label,'verified 20 n,k cases')
print('All',cases,'exhaustive known-K adversarial continuations passed')

# Check the constructive mixed-threshold adversary at all endpoint and
# open-chamber representative lotteries on several independent rational grids.
def verify_mixed_witness(a, b):
    assert F(0) < a <= F(1, 2) < b <= F(1)
    endpoints = sorted({F(0), a, b, F(1)-a, F(1)-b, F(1)})
    tested = 0
    for t in endpoints + [(p+q)/2 for p, q in zip(endpoints, endpoints[1:])]:
        if t < b:
            other, witness = (1, b), F(1)
        elif t > F(1) - a:
            other, witness = (-1, a), a
        else:
            other, witness = (-1, b), a
        assert not accepted(other, t), (a,b,t,'rejection')
        assert accepted((1,a), witness) and accepted(other, witness), (a,b,t,'common point')
        tested += 1
    return tested

checks = 0
for den in (4, 6, 8, 10):
    levels = [F(j, den) for j in range(1, den+1)]
    for a in levels:
        for b in levels:
            if a <= F(1, 2) < b:
                checks += verify_mixed_witness(a, b)
print('Constructive mixed-threshold rejection/common-acceptance tests:', checks)
