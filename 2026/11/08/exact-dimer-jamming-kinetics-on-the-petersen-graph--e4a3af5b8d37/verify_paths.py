#!/usr/bin/env python3
"""Independent 2-subset Kneser realization and complete matching-history census."""
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import combinations

verts=tuple(combinations(range(5),2))
edges=tuple((i,j) for i in range(10) for j in range(i+1,10)
            if not (set(verts[i]) & set(verts[j])))
assert len(verts)==10 and len(edges)==15
terminal=Counter(); matching_probs=defaultdict(Q); coeff=defaultdict(Q)
leaves=[0]

def walk(mask,selected,path_prob,event_rates):
    elig=[(i,a,b) for i,(a,b) in enumerate(edges)
          if mask & (1<<a|1<<b)==0]
    if not elig:
        leaves[0]+=1
        k=len(selected)
        terminal[k]+=path_prob
        matching_probs[tuple(sorted(selected))]+=path_prob
        coeff[0]+=path_prob*k
        # Hypoexponential CDF of each event-time sum, conditional on this history.
        for j in range(1,k+1):
            rr=event_rates[:j]
            assert len(set(rr))==len(rr)  # rates strictly decrease after each dimer
            for idx,r in enumerate(rr):
                z=Q(1)
                for m,s in enumerate(rr):
                    if m!=idx:z*=Q(s,s-r)
                coeff[r]-=path_prob*z
        return
    for ei,a,b in elig:
        walk(mask|(1<<a)|(1<<b), selected+(ei,),
             path_prob/Q(len(elig)),event_rates+(len(elig),))
walk(0,(),Q(1),())
assert leaves[0]==2190 and len(matching_probs)==71
assert terminal=={3:Q(1,25),4:Q(52,75),5:Q(4,15)}
assert Counter((len(m),v) for m,v in matching_probs.items())=={
  (3,Q(1,125)):5,(4,Q(13,1125)):60,(5,Q(2,45)):6}
expected={0:Q(317,75),1:-Q(4,7),2:-Q(25,26),3:-Q(10,7),
          5:-Q(7,25),6:-Q(7,9),10:-Q(67,350),15:-Q(326,20475)}
assert dict(coeff)==expected,(dict(coeff),expected)
assert sum(terminal.values())==1 and sum(coeff.values())==0
print('PATHS PASS: Kneser K(5,2); 2190 complete histories; 71 terminal labeled matchings.')
print('terminal matching law',dict(sorted(terminal.items())))
print('all-time rate coefficients',dict(sorted(coeff.items())))
