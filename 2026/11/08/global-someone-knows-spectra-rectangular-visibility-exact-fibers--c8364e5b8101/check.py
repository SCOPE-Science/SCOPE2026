#!/usr/bin/env python3
"""Reproducible exhaustive checks for finite S5 coordinate-observation semantics.
Only uses Python's standard library. Run: python3 check.py.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

def bits(items):
    t = list(items)
    for mask in range(1 << len(t)):
        yield frozenset(t[j] for j in range(len(t)) if mask >> j & 1)

def closure(h, team, k):
    if not h:
        return frozenset()
    projections = [set(x[i] for x in h) for i in range(k)]
    return frozenset(x for x in team if all(x[i] in projections[i] for i in range(k)))

def bundle(u,team,k):
    return frozenset(x for x in team if any(all(y in u for y in team if y[i] == x[i]) for i in range(k)))

def fiber_size(ns):
    out = 0
    for js in product(*[range(n+1) for n in ns]):
        term = (-1)**sum(js)
        for n,j in zip(ns,js):
            term *= comb(n,j)
        remaining = 1
        for n,j in zip(ns,js):
            remaining *= n-j
        out += term * (2**remaining)
    return out

def onto_count(m,n):
    return sum((-1)**j*comb(n,j)*(n-j)**m for j in range(n+1))

def check_team(team, k):
    c = Counter()
    for h in bits(team):
        u = team-h
        obs = bundle(u,team,k)
        target = team-closure(h,team,k)
        assert obs == target, ('modal identity',team,h,obs,target)
        assert bundle(obs,team,k)==obs
        c[closure(h,team,k)] += 1
    closed = set(c)
    assert all(closure(a,team,k)==a for a in closed)
    # Independent recursive inversion of zeta transform over closed sets.
    reconstructed = {}
    for a in sorted(closed,key=lambda v:(len(v),sorted(v))):
        reconstructed[a] = 2**len(a)-sum(reconstructed[b] for b in reconstructed if b < a)
        assert reconstructed[a] == c[a], ('fiber inversion',team,a)
    return sum(c.values())

def check_full(ns):
    team = frozenset(product(*[range(n) for n in ns]))
    k = len(ns)
    projections = [set(range(n)) for n in ns]
    counts=Counter()
    no_knowledge=[]
    for h in bits(team):
        c=closure(h,team,k)
        counts[c]+=1
        if c==team:
            no_knowledge.append(h)
    assert len(counts)==1+__import__('math').prod(2**n-1 for n in ns)
    for boxes in product(*[list(bits(range(n))) for n in ns]):
        if not all(boxes):
            continue
        b = frozenset(product(*boxes))
        assert counts[b]==fiber_size([len(z) for z in boxes]), (ns,boxes,counts[b])
    assert counts[frozenset()]==1
    maxn=max(ns)
    j=ns.index(maxn)
    optimal=[h for h in no_knowledge if len(h)==maxn]
    expectation=__import__('math').prod(onto_count(maxn,n) for i,n in enumerate(ns) if i!=j)
    assert min(map(len,no_knowledge))==maxn
    assert len(optimal)==expectation, (ns, len(optimal), expectation)
    return len(team), sum(counts.values()), len(counts), maxn, expectation

def main():
    teams=0
    truth_events=0
    for ns in ((2,2),(2,3),(3,3),(2,2,2)):
        points=list(product(*[range(n) for n in ns]))
        for t in bits(points):
            if not t:
                continue
            truth_events += check_team(t,len(ns))
            teams += 1
    full=[]
    for ns in ((1,2),(2,2),(2,3),(3,3),(2,2,2),(2,2,3)):
        full.append((ns,)+check_full(ns))
    print('arbitrary_nonempty_teams',teams)
    print('tested_truth_events',truth_events)
    print('full_products (sizes,worlds,truth_events,outputs,min_false,optima):')
    for row in full: print(row)
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':main()
