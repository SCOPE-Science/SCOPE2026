#!/usr/bin/env python3
"""Self-contained exact-rational verification for edge-clock dimer adsorption on the icosahedral graph.
Run: python3 verifier.py  (Python 3.9+, standard library only).
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict, Counter

NEIGHBORS = (
 (1,5,7,8,11), (0,2,5,6,8), (1,3,6,8,9),
 (2,4,6,9,10), (3,5,6,10,11), (0,1,4,6,11),
 (1,2,3,4,5), (0,8,9,10,11), (0,1,2,7,9),
 (2,3,7,8,10), (3,4,7,9,11), (0,4,5,7,10))
N=12
FULL=(1<<N)-1
EDGES=tuple((a,b) for a in range(N) for b in NEIGHBORS[a] if a<b)
assert len(EDGES)==30 and all(len(x)==5 for x in NEIGHBORS)
assert all(a in NEIGHBORS[b] for a,b in EDGES)
EDGE_MASKS=tuple((1<<a)|(1<<b) for a,b in EDGES)

def distance(a,b):
 frontier={a}; visited={a}
 for d in range(4):
  if b in frontier:return d
  frontier={w for u in frontier for w in NEIGHBORS[u] if w not in visited}
  visited.update(frontier)
 raise AssertionError('bad diameter')

def state_type(occupied):
 unoccupied=FULL^occupied
 if unoccupied==0:return 'perfect'
 verts=tuple(i for i in range(N) if (unoccupied>>i)&1)
 assert len(verts)==2 and verts[1] not in NEIGHBORS[verts[0]]
 return 'distance_'+str(distance(*verts))

def choices(occupied):
 return tuple(edge for edge in EDGE_MASKS if not (edge&occupied))

@lru_cache(None)
def backward(state):
 edges=choices(state)
 if not edges:return {state_type(state):Q(1)}, Q(0)
 n=len(edges)
 distribution=defaultdict(Q)
 total_time=Q(1,n)
 for edge in edges:
  next_dist, next_time=backward(state|edge)
  for k,p in next_dist.items(): distribution[k]+=p/n
  total_time+=next_time/n
 return dict(distribution),total_time


def forward():
 # This independent probability-flow implementation neither invokes nor reads backward().
 masses={0:Q(1)}
 terminal=defaultdict(Q)
 holding_time=Q(0)
 visited_states=0
 for stage in range(7):
  next_mass=defaultdict(Q)
  for state,mass in masses.items():
   visited_states+=1
   live=[em for em in EDGE_MASKS if state&em==0]
   if not live:
    terminal[state_type(state)]+=mass
    continue
   holding_time+=mass/len(live)
   for em in live:next_mass[state|em]+=mass/len(live)
  masses=dict(next_mass)
 assert not masses
 return dict(terminal),holding_time,visited_states


def count_perfect_matchings():
 @lru_cache(None)
 def f(left):
  if left==0:return 1
  i=(left&-left).bit_length()-1
  return sum(f(left^(1<<i)^(1<<j)) for j in NEIGHBORS[i] if (left>>j)&1)
 return f(FULL)

def individual_terminal():
 @lru_cache(None)
 def dp(state):
  edges=choices(state)
  if not edges:return {FULL^state:Q(1)}
  mass=defaultdict(Q)
  for em in edges:
   for final, p in dp(state|em).items():mass[final]+=p/len(edges)
  return dict(mass)
 return dp(0)


def spectral_coefficients():
    # Solve the forward master equation, triangular in accepted dimer count.
    rates={0:{len(EDGE_MASKS):Q(1)}}
    for stage in range(1,7):
        layer=set()
        for old in rates:
            if old.bit_count()!=2*(stage-1):continue
            layer.update(old|em for em in choices(old))
        for state in sorted(layer):
            exit_rate=len(choices(state))
            incoming=defaultdict(Q)
            for edge in EDGE_MASKS:
                if state&edge != edge:continue
                predecessor=state^edge
                if predecessor not in rates:continue
                for exponent,weight in rates[predecessor].items():
                    incoming[exponent]+=weight
            coeff={j:a/Q(exit_rate-j) for j,a in incoming.items() if a}
            coeff[exit_rate]=-sum(coeff.values())
            rates[state]={j:a for j,a in coeff.items() if a}
    assert len(rates)==1720
    by_orbit={key:defaultdict(Q) for key in ('distance_2','distance_3','perfect')}
    for state,dictionary in rates.items():
        if not choices(state):
            for k,v in dictionary.items():by_orbit[state_type(state)][k]+=v
    total=defaultdict(Q)
    for key,coefs in by_orbit.items():
        for exponent,weight in coefs.items():total[exponent]+=weight
    return {k:v for k,v in total.items() if v},by_orbit

@lru_cache(None)
def laplace_transform(state, s):
    # Independent first-step transform of the *last successful event time*.
    live=choices(state)
    if not live:return Q(1)
    r=len(live)
    return sum((laplace_transform(state|em,s) for em in live),Q(0))/(r+s)


def check_time_spectrum():
    from pathlib import Path
    from csv import reader
    total,by_orbit=spectral_coefficients()
    here=Path(__file__).resolve().parent
    csv_path=here/'SPECTRUM.csv'
    with csv_path.open(newline='',encoding='utf-8') as f:
        rows=list(reader(f))
    assert rows.pop(0)==['exponential_rate','coefficient_numerator','coefficient_denominator']
    stored={int(r):Q(int(num),int(den)) for r,num,den in rows}
    assert stored==total and len(total)==17 and set(total)=={0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,21,30}
    assert total[0]==1 and sum(total.values())==0
    assert -sum((v/Q(k) for k,v in total.items() if k),Q(0))==Q(167225267,144471600)
    for s in (1,2,3,7,11):
        expected=sum((v*Q(s,s+k) for k,v in total.items()),Q(0))
        assert expected==laplace_transform(0,s),(s,expected,laplace_transform(0,s))
    # The terminal-type probabilities coincide with the constant part of each CDF.
    expected={'perfect':Q(3622453,8026200),'distance_2':Q(11150381,24078600),'distance_3':Q(103043,1203930)}
    for k,v in expected.items():assert by_orbit[k][0]==v and sum(by_orbit[k].values())==0
    print('PASS: 17-term CDF spectral table, forward master equations, five independent Laplace checks')



def all_perfect_matchings():
    @lru_cache(None)
    def rec(uncovered):
        if not uncovered:return ((),)
        a=(uncovered&-uncovered).bit_length()-1
        return tuple(tuple(sorted(((a,b),)+rest))
                     for b in NEIGHBORS[a] if uncovered>>b&1
                     for rest in rec(uncovered^(1<<a)^(1<<b)))
    return rec(FULL)


def check_matching_weights():
    from pathlib import Path
    from csv import reader
    weights=Counter()
    for matching in all_perfect_matchings():
        matching_masks=tuple((1<<a)|(1<<b) for a,b in matching)
        @lru_cache(None)
        def probability(selected):
            if selected==63:return Q(1)
            occupied=0
            for j,edge in enumerate(matching_masks):
                if selected>>j&1:occupied|=edge
            return sum((probability(selected|(1<<j)) for j in range(6)
                        if not selected>>j&1),Q(0))/len(choices(occupied))
        weights[probability(0)]+=1
    expected={Q(52,15435):5,Q(38999,10749375):10,
              Q(2188741,619164000):20,Q(118598,32248125):30,
              Q(92353,25515000):60}
    assert weights==expected and sum(v for v in weights.values())==125
    assert sum((p*n for p,n in weights.items()),Q(0))==Q(3622453,8026200)
    path=Path(__file__).resolve().parent/'MATCHING_WEIGHTS.csv'
    with path.open(newline='',encoding='utf-8') as f:rows=list(reader(f))
    assert rows.pop(0)==['probability_numerator','probability_denominator','matching_count']
    stored={Q(int(a),int(b)):int(c) for a,b,c in rows}
    assert stored==expected
    print('PASS: independently enumerated all 125 perfect matchings in five kinetic probability classes')

def main():
 assert max(sum(bool((m>>u)&1) for u in range(N)) for m in range(1<<N)
                if all(not((m>>a)&1 and (m>>b)&1) for a,b in EDGES))==3
 assert count_perfect_matchings()==125
 assert Counter(distance(i,j) for i in range(N) for j in range(i+1,N))=={1:30,2:30,3:6}
 a,mean_a=backward(0)
 b,mean_b,visited=forward()
 expected={
  'distance_2':Q(11150381,24078600),
  'distance_3':Q(103043,1203930),
  'perfect':Q(3622453,8026200),
 }
 assert a==b==expected,(a,b)
 assert sum(a.values())==1
 assert mean_a==mean_b==Q(167225267,144471600),(mean_a,mean_b)
 by_pair=individual_terminal()
 assert len(by_pair)==37 and by_pair[0]==expected['perfect']
 assert set(by_pair.values())=={Q(11150381,722358000), Q(103043,7223580), expected['perfect']}
 assert all(by_pair[(1<<i)|(1<<j)]==
            (Q(11150381,722358000) if distance(i,j)==2 else Q(103043,7223580))
            for i in range(N) for j in range(i+1,N) if distance(i,j)>1)
 print('PASS: icosahedron degree, distance orbits, independence number, perfect matchings')
 print('PASS: independent backward/forward exact distributions:', sorted(a.items()))
 print('PASS: exact exponential-arrival mean terminal time:',mean_a)
 print('PASS: per-pair vacancy probabilities, symmetry orbits and 37 terminal outcomes')
 check_time_spectrum()
 check_matching_weights()
 print('visited forward states:',visited,'backward memoized:',backward.cache_info().currsize)

if __name__=='__main__':main()
