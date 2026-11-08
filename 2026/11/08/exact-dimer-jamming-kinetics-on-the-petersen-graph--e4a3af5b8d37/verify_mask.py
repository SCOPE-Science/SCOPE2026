#!/usr/bin/env python3
"""Exact finite-state master-equation verification for Petersen dimer adsorption."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache

E = tuple(sorted({tuple(sorted(e)) for e in
    ([(i, (i+1) % 5) for i in range(5)]
     + [(i, i+5) for i in range(5)]
     + [(i+5, 5+(i+2) % 5) for i in range(5)])}))
assert len(E) == 15 and len({v for e in E for v in e}) == 10

def allowed(m):
    return [m | (1 << a) | (1 << b) for a,b in E if not m & ((1 << a) | (1 << b))]

@lru_cache(None)
def final_law(m):
    succ=allowed(m)
    if not succ:
        return {m:Q(1)}
    result=defaultdict(Q)
    for v in succ:
        for end,p in final_law(v).items():
            result[end]+=p/len(succ)
    return dict(result)

ends=final_law(0)
terminal=Counter()
for m,p in ends.items():terminal[m.bit_count()//2]+=p
expected={3:Q(1,25),4:Q(52,75),5:Q(4,15)}
assert terminal==expected,terminal
assert len(ends)==36
assert Counter(m.bit_count()//2 for m in ends)=={3:5,4:30,5:1}
assert Counter((m.bit_count()//2,p) for m,p in ends.items())=={
    (3,Q(1,125)):5,(4,Q(26,1125)):30,(5,Q(4,15)):1}

# Propagate rational exponential coefficients in forward Kolmogorov equations.
seen={0}; todo=[0]
while todo:
    m=todo.pop()
    for v in allowed(m):
        if v not in seen:
            seen.add(v);todo.append(v)
order=sorted(seen,key=int.bit_count)
rate={m:len(allowed(m)) for m in order}
p={m:defaultdict(Q) for m in order}
p[0][15]=Q(1)
for m in order:
    for v in allowed(m):
        assert rate[v]<rate[m]
        for s,c in list(p[m].items()):
            inc=c/Q(rate[v]-s)
            p[v][s]+=inc
            p[v][rate[v]]-=inc
coefs=defaultdict(Q)
for m in order:
    for s,c in p[m].items():
        coefs[s]+=Q(m.bit_count(),2)*c
expected_coefs={
    0:Q(317,75),1:-Q(4,7),2:-Q(25,26),3:-Q(10,7),
    5:-Q(7,25),6:-Q(7,9),10:-Q(67,350),15:-Q(326,20475)
}
assert dict(coefs)==expected_coefs,(dict(coefs),expected_coefs)
assert sum(coefs.values())==0
assert -sum(s*c for s,c in coefs.items())==15
assert len(order)==272
print('MASK PASS: 272 reachable occupancy states; 36 terminal masks; exact law and all-time mean.')
print('terminal',dict(sorted(terminal.items())))
print('E[M(t)] coefficients',dict(sorted(coefs.items())))
