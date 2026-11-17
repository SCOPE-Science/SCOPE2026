#!/usr/bin/env python3
"""Finite tests of the three-token covering construction and the exact scalar phase law."""
from collections import deque
from fractions import Fraction as Q
from itertools import product

def triple_states(d):
    return {a for a in product(range(d), repeat=3) if len(set(a)) >= 2}

def connected_guard_graph(d):
    states = triple_states(d)
    s0 = next(iter(states))
    seen = {s0}
    queue = deque([s0])
    edges = 0
    while queue:
        a = queue.popleft()
        for i in range(3):
            if a[(i+1)%3] == a[(i+2)%3]:
                continue
            for v in range(d):
                b = list(a);b[i] = v;b=tuple(b)
                if b != a:
                    edges += 1
                    assert b in states
                if b not in seen:
                    seen.add(b);queue.append(b)
    assert seen == states, (d,len(seen),len(states))
    return len(states),edges//2

def branches(d,w):
    anchor = 2*w*Q(d-1,d)
    no_anchor = 2*(1-min(Q(2,3),2*w/d))
    return anchor,no_anchor

def formula(d,w):
    if w <= Q(d,d+1):
        return 2*w*Q(d-1,d)
    if d == 2:
        return Q(2,3)
    return 2-Q(4,d)*w

n=0
for d in range(2,16):
    if d<=9:
        triple,edges=connected_guard_graph(d)
        assert triple == d**3-d
        assert edges>0
    for j in range(0,301):
        w=Q(j,300)
        a,b=branches(d,w)
        assert min(a,b) == formula(d,w), (d,w,a,b,formula(d,w))
        assert Q(0)<=formula(d,w)<=Q(2)
        n+=1
    critical=Q(d,d+1)
    a,b=branches(d,critical)
    assert a==b==formula(d,critical)
print('THREE_MAP_COVER_CHECK_OK',n,'phase identities; guarded triple graph connected for d=2..9')
