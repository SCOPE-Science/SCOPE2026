"""Exact checks for hub-started probabilistic zero forcing on friendship graphs.
Run: python check_friendship.py. Uses Python's rational arithmetic only.
"""
from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
from math import comb

checks=0

def verified(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks+=1

@lru_cache(None)
def kernel(m,e,s):
    """State uses e entirely white pairs, s singly blue pairs, m-e-s full pairs."""
    b=2*m-2*e-s
    p=Q(1+b,2*m)
    a=(1-p)**2; c=2*p*(1-p); d=p*p
    dp={(0,0):Q(1)}
    for _ in range(e):
        out=defaultdict(Q)
        for (empty,single),w in dp.items():
            out[(empty+1,single)]+=w*a
            out[(empty,single+1)]+=w*c
            out[(empty,single)]+=w*d
        dp=dict(out)
    return dp

def state(mask,m):
    e=s=0
    for i in range(m):
        z=((mask>>(2*i))&3).bit_count()
        e+=(z==0);s+=(z==1)
    return e,s

def full_step(mask,m):
    b=mask.bit_count()
    p=Q(b+1,2*m)
    out={mask:Q(1)}
    for w in range(2*m):
        if mask>>w&1:
            continue
        forced=(mask>>(w^1))&1
        q=Q(1) if forced else p
        nxt=defaultdict(Q)
        for mask2,wt in out.items():
            nxt[mask2|(1<<w)]+=wt*q
            nxt[mask2]+=wt*(1-q)
        out={k:v for k,v in nxt.items() if v}
    return out

for m in range(1,6):
    for e in range(m+1):
        for s in range(m-e+1):
            P=kernel(m,e,s)
            verified(sum(P.values())==1,('normalization',m,e,s))
            for (ne,ns) in P:
                verified(ne+ns<=m and ne<=e,('reachable',m,e,s,ne,ns))
            b=2*m-2*e-s
            p=Q(b+1,2*m)
            expected_b=sum(w*(2*m-2*ne-ns) for (ne,ns),w in P.items())
            expected_s=sum(w*ns for (ne,ns),w in P.items())
            verified(expected_b==b+s+2*e*p,('blue drift',m,e,s))
            verified(expected_s==2*e*p*(1-p),('single drift',m,e,s))

for m in range(1,4):
    states_full={0:Q(1)}
    states_reduced={(m,0):Q(1)}
    for t in range(7):
        grouped=defaultdict(Q)
        for mask,wt in states_full.items():
            grouped[state(mask,m)]+=wt
        for pair in set(grouped)|set(states_reduced):
            verified(grouped[pair]==states_reduced.get(pair,Q(0)),('full vs quotient',m,t,pair))
        verified(sum(states_full.values())==1,('mass-full',m,t))
        verified(sum(states_reduced.values())==1,('mass-quotient',m,t))
        nxt=defaultdict(Q)
        for mask,wt in states_full.items():
            for new,prob in full_step(mask,m).items():
                nxt[new]+=wt*prob
        states_full=dict(nxt)
        reduced=defaultdict(Q)
        for (e,s),wt in states_reduced.items():
            for pair,prob in kernel(m,e,s).items():
                reduced[pair]+=wt*prob
        states_reduced=dict(reduced)

# Independent exact first-moment recurrence and absorbing-state solution.
@lru_cache(None)
def exact_mean(m,e,s):
    if e==s==0:return Q(0)
    P=kernel(m,e,s)
    selfprob=P.get((e,s),Q(0))
    numerator=Q(1)+sum(w*exact_mean(m,ne,ns) for (ne,ns),w in P.items() if (ne,ns)!=(e,s))
    return numerator/(1-selfprob)
for m in range(1,7):
    value=exact_mean(m,m,0)
    verified(value>0,('positive absorption time',m))
    print('m=',m,'exact mean=',float(value))
print('PASSED',checks,'exact rational assertions')
