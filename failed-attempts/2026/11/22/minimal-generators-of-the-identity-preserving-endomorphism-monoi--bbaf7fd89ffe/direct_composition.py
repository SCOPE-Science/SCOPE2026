import sys,random

from generator_closure import test,mul,compose,parity,inverse
from orbit_census import gen_invol,maps_idemp_for_t
from itertools import product,permutations

def eval_map(a,s):
 if a[0]=='u':
  g=a[1];return compose(compose(inverse(g),s),g)
 n=len(s)
 if tuple(sorted(s))==tuple(range(n)):
  return a[1] if parity(s) else tuple(range(n))
 return a[2]

def check(n):
 rng=random.Random(17032026)
 perms=list(permutations(range(n)))
 S=[('s',t,e) for t in gen_invol(n) for e,r in maps_idemp_for_t(t)]
 U=[('u',g) for g in perms]
 universe=S+U
 sample_maps=[tuple(range(n))] + rng.sample(list(product(range(n),repeat=n)),100)
 c=('s',tuple(range(n)),tuple(range(n)))
 special=[c]+[q for q in S if parity(q[1])==0 and q[1]!=tuple(range(n))][:3]
 for a in special+rng.sample(universe,200):
  for b in special+rng.sample(universe,25):
   ab=mul(a,b)
   for s in sample_maps:
    v=eval_map(b,eval_map(a,s))
    w=eval_map(ab,s)
    assert v==w,(a,b,s,v,w)
 print('DIRECT_COMPOSITION_CHECKS_PASSED',n,len(universe))
check(5)
