#!/usr/bin/env python3
"""Independent parametrized enumeration of minimum outgoing identifying codes."""
import collections
import itertools


def code(q, f):
    return {(a,b) for a in range(q) for b in range(q)
            if a != b and a != f[b]}


def valid(q, f):
    C = code(q, f)
    seen = set()
    for a in range(q):
        for b in range(q):
            if a == b:
                continue
            sig = frozenset(C.intersection({(a,b)} | {(b,c) for c in range(q) if c!=b}))
            if not sig or sig in seen:
                return False
            seen.add(sig)
    return True


def all_functions(q):
    for choices in itertools.product(range(q-1), repeat=q):
        yield tuple(t + (t>=i) for i,t in enumerate(choices))


def neighbors(q, f):
    for i in range(q):
        for a in range(q):
            if a not in (i,f[i]):
                yield f[:i] + (a,) + f[i+1:]


for q in range(3,7):
    fs = list(all_functions(q))
    accepted = {f for f in fs if valid(q,f)}
    predicted = {f for f in fs if max(collections.Counter(f).values()) < q-1}
    assert accepted == predicted
    assert len(accepted) == (q-1)**q - q*(q-1)
    degrees=collections.Counter(sum(g in accepted for g in neighbors(q,f)) for f in accepted)
    if q == 3:
        assert degrees == {0:2}
    if q == 4:
        assert degrees == {8:9, 7:48, 6:12}
    if q>=5:
        D=q*(q-2)
        assert degrees == {D:(q-1)**q-q*(q-1)-q*(q-1)**2*(q-2), D-1:q*(q-1)**2*(q-2)}
    print(f'q={q}: allowed={len(accepted)}; degrees={dict(sorted(degrees.items()))}; exchange_edges={sum(d*c for d,c in degrees.items())//2}')
