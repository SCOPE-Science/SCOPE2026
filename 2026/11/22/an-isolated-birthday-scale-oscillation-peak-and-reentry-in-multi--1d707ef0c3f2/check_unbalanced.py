#!/usr/bin/env python3
"""Independent unequal-shore enumeration for deterministic plurality with incumbent ties."""
from itertools import product
from collections import Counter


def winner(s, q):
    c=Counter(s)
    mx=max(c.values())
    w=[v for v,z in c.items() if z==mx]
    return w[0] if len(w)==1 else None


def nextstate(s,a,b,q):
    left=s[:a]; right=s[a:]
    lw=winner(left,q); rw=winner(right,q)
    return tuple(rw if rw is not None else x for x in left)+tuple(lw if lw is not None else x for x in right)


def entry(s,a,b,q):
    seen={}
    for t in range(5):
        if s in seen:return seen[s],t-seen[s]
        seen[s]=t;s=nextstate(s,a,b,q)
    assert False


def calc(a,b,q):
    def tally(n):
        return sum(winner(x,q) is not None for x in product(range(q),repeat=n))
    u,v=tally(a),tally(b);d,e=q**a-u,q**b-v
    return {(0,1):d*e+q,(0,2):q*(q-1),
            (1,1):u*v//q-q+q*(d+e),
            (1,2):u*v*(q-1)//q-q*(q-1),
            (2,1):(u-q)*e+(v-q)*d}


for q in (2,3,4):
    for a in (1,2,3):
        for b in (1,2,3):
            expected={k:v for k,v in calc(a,b,q).items() if v}
            got=Counter(entry(s,a,b,q) for s in product(range(q),repeat=a+b))
            assert dict(got)==expected,(q,a,b,got,expected)
print('ALL UNEQUAL-SHORE TESTS PASSED: 27 (alphabet, left size, right size) cases')
