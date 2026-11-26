#!/usr/bin/env python3
"""Self-contained exact shattering verifier for maximal independent sets of paths.
No nonstandard Python packages required. It checks the finite-state quotient,
transfer counts, a separate reachability criterion and direct traces.
"""
from collections import deque, Counter
from math import comb

# Prefix states 0=start, 1=initial zero, 2=last one,
# 3=one following zero, 4=one following two zeros. -1=dead.
DELTA = ((1, 2), (-1, 2), (3, -1), (4, 2), (-1, 2))
FINAL = frozenset((2, 3))

def step_state(subset, symbol):
    return frozenset(DELTA[x][symbol] for x in subset if DELTA[x][symbol] != -1)

def step_family(family, supported):
    if supported:
        return frozenset(step_state(p, c) for p in family for c in (0, 1))
    return frozenset(step_state(p, 0) | step_state(p, 1) for p in family)

def construct_dfa():
    start = frozenset((frozenset((0,)),))
    nodes, indices = [start], {start: 0}
    edges = []
    for fam in nodes:
        targets = []
        for b in (0, 1):
            t = step_family(fam, b)
            if t not in indices:
                indices[t] = len(nodes)
                nodes.append(t)
            targets.append(indices[t])
        edges.append(tuple(targets))
    accepting = [all(bool(p & FINAL) for p in fam) for fam in nodes]
    return nodes, edges, accepting

def minimize(edges, accepting):
    blocks = [set(i for i, a in enumerate(accepting) if a),
              set(i for i, a in enumerate(accepting) if not a)]
    while True:
        by = {v: j for j, block in enumerate(blocks) for v in block}
        refined = []
        for block in blocks:
            classes = {}
            for i in sorted(block):
                sig = tuple(by[edges[i][b]] for b in (0, 1))
                classes.setdefault(sig, set()).add(i)
            refined.extend(classes.values())
        if len(refined) == len(blocks):
            break
        blocks = refined
    by = {v: j for j, block in enumerate(blocks) for v in block}
    # Reorder equivalence classes by BFS starting at initial state, free before marked.
    start = by[0]
    order, seen = [start], {start}
    for j in order:
        rep = min(blocks[j])
        for b in (0, 1):
            target = by[edges[rep][b]]
            if target not in seen:
                seen.add(target); order.append(target)
    assert len(order) == len(blocks)
    canon = {old: k for k, old in enumerate(order)}
    a = [accepting[min(blocks[j])] for j in order]
    e = [tuple(canon[by[edges[min(blocks[j])][b]]] for b in (0, 1)) for j in order]
    for oldblock in blocks:
        assert len({accepting[v] for v in oldblock}) == 1
        assert len({tuple(by[edges[v][b]] for b in (0, 1)) for v in oldblock}) == 1
    return a, e, blocks

def direct_mis(n):
    return [m for m in range(1 << n)
            if not (m & (m << 1)) and
            all((m >> i & 1) or (i and (m >> (i-1) & 1)) or
                (i+1 < n and (m >> (i+1) & 1)) for i in range(n))]

def direct_support(n, s, mis):
    return len({m & s for m in mis}) == (1 << s.bit_count())

def reach(n, start, stop, forbidden):
    # 0 is virtual left, n+1 is virtual right.
    stack = [start]; seen = {start}
    while stack:
        u = stack.pop()
        if u == stop: return True
        if u == 0:
            vlist = (1, 2)
        elif u in (n-1, n):
            vlist = (n+1, u+2, u+3)
        else:
            vlist = (u+2, u+3)
        for v in vlist:
            if 1 <= v <= n and v not in forbidden and v not in seen:
                seen.add(v); stack.append(v)
            if u != 0 and u in (n-1, n) and v == n+1 and v not in seen:
                seen.add(v); stack.append(v)
    return False

def pairwise_support(n, s):
    coords = tuple(i+1 for i in range(n) if s >> i & 1)
    if not reach(n, 0, n+1, set(coords)): return False
    for a in coords:
        if not reach(n, 0, a, {q for q in coords if q < a}): return False
        if not reach(n, a, n+1, {q for q in coords if q > a}): return False
    for i,a in enumerate(coords):
        for b in coords[i+1:]:
            if not reach(n, a, b, {q for q in coords if a < q < b}): return False
    return True

def transfer_poly(n, edges, accepting):
    dp = {(0, 0): 1}
    for _ in range(n):
        nex = Counter()
        for (u,k),v in dp.items():
            for b in (0, 1):
                nex[(edges[u][b],k+b)] += v
        dp=nex
    a=Counter()
    for (u,k),v in dp.items():
        if accepting[u]: a[k]+=v
    return dict(a)

def closed_coefficient(n, k):
    if k == 0: return 1
    h=n-3*k+1
    if h<0: return 0
    return sum(comb(k,r)*comb(h+r,r) for r in range(k+1))

def run():
    nodes, edges, accept = construct_dfa()
    assert len(nodes) == 28
    a,e,blocks=minimize(edges, accept)
    assert len(blocks) == 6
    assert a == [False, True, False, True, False, True]
    assert e == [(1,2),(1,3),(3,4),(5,4),(4,4),(1,2)]
    print('Finite-state quotient: 28 reachable families; six stable classes; exact transition table verified')
    checks = 0
    for n in range(1, 14):
        mis=direct_mis(n)
        counts=Counter()
        for s in range(1<<n):
            direct=direct_support(n,s,mis)
            pair=pairwise_support(n,s)
            assert direct==pair,(n,s,'pairwise')
            if direct: counts[s.bit_count()]+=1
            checks+=1
        trans=transfer_poly(n,e,a)
        expected={k:closed_coefficient(n,k) for k in range(n+1)}
        expected={k:v for k,v in expected.items() if v}
        assert dict(counts)==trans==expected,(n,counts,trans,expected)
        assert max(counts) == (n+1)//3
        print('n=',n,'hypotheses=',len(mis),'shattering polynomial=',dict(sorted(counts.items())))
    for n in range(1,101):
        assert transfer_poly(n,e,a)=={k:v for k in range(n+1) if (v:=closed_coefficient(n,k))}
    print('PASS:',checks,'direct support-vs-reachability comparisons through n=13; exact transfer-vs-closed-form through n=100')

if __name__=='__main__': run()
