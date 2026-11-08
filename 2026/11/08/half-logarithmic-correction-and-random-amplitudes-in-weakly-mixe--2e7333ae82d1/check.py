"""Finite exact tests for a slowly switched two-colour urn.
The analytic almost-sure and infinite-product arguments are in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

checks=0

def ck(cond, context):
    global checks
    assert cond, context
    checks+=1

def step(state, switch, a, b, c):
    u,v=state
    t=u+v
    if switch:
        return [((u+a,v+b), F(u,t)), ((u+b,v+a), F(v,t))]
    return [((u+c,v), F(u,t)), ((u,v+c), F(v,t))]

def imbalance(state):
    u,v=state
    return F(u,u+v)-F(1,2)

def drift(state, switch, a,b,c):
    t=sum(state)
    return F(1,1)-F(2*b*switch,t+a+b)

# Exact one-step conditional recurrences for both unbalanced directions.
for a,b,c in [(2,1,2),(2,1,5),(1,1,3),(4,2,3),(3,2,8)]:
  ck(a>=b and a+b!=c,'unbalanced parameters')
  for u,v in product(range(1,9), repeat=2):
    for xi in [0,1]:
      z=imbalance((u,v))
      dist=step((u,v),xi,a,b,c)
      m=sum((prob*imbalance(st) for st,prob in dist),F(0))
      ck(m==z*drift((u,v),xi,a,b,c),'exact drift')
      ck(sum((prob for st,prob in dist),F(0))==1,'probability normalization')
      ck(0<drift((u,v),xi,a,b,c)<=1,'positive drift factor')

# Exhaust all exogenous switch strings to finite depth; conditional scaled
# process is a martingale and conditional variance never decreases.
for a,b,c in [(2,1,2),(1,1,3),(4,2,3)]:
  for u0,v0 in [(1,1),(1,3),(3,2)]:
    for length in range(1,6):
      for switches in product([0,1],repeat=length):
        dist={(u0,v0):F(1)}
        J=F(1)
        old_E2=imbalance((u0,v0))**2
        for idx,xi in enumerate(switches):
          # total is deterministic when conditioned on switches.
          arbitrary=next(iter(dist))
          J*=drift(arbitrary,xi,a,b,c)
          nextdist=defaultdict(F)
          for state,pst in dist.items():
            for dest,edgep in step(state,xi,a,b,c):
              nextdist[dest]+=pst*edgep
          dist=nextdist
          mean=sum((prob*imbalance(st)/J for st,prob in dist.items()),F())
          E2=sum((prob*(imbalance(st)/J)**2 for st,prob in dist.items()),F())
          ck(mean==imbalance((u0,v0)), 'quenched martingale mean')
          ck(E2>=old_E2,'quenched martingale second moment')
          ck(sum(dist.values())==1,'exhaustive probabilities')
          old_E2=E2
        if 0 in switches:
          ck(old_E2>imbalance((u0,v0))**2,'nonzero noise after a Polya step')

print(f'{checks} exact rational assertions passed')
