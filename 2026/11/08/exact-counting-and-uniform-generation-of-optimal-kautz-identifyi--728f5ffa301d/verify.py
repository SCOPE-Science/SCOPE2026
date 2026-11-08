#!/usr/bin/env python3
"""Reproducible finite checks for identifying codes in ternary Kautz digraphs.

No external packages needed. Enumerates cycle covers independently of
closed-in-neighborhood signatures.
"""
from itertools import product

def words(n):
    return [''.join(t) for t in product('012', repeat=n)
            if all(t[i] != t[i + 1] for i in range(n - 1))]

def identify(n, code):
    verts = words(n)
    code = frozenset(code)
    signatures = [frozenset(code.intersection(
        [w] + [a + w[:-1] for a in '012' if a != w[0]])) for w in verts]
    return all(signatures) and len(set(signatures)) == len(verts)

def via_prefix(n):
    vert = words(n)
    p = words(n - 1)
    out = {v: [w for w in vert if w[:-1] == v] for v in p}
    count = 0
    for bits in product((0, 1), repeat=len(p)):
        code = [out[v][bits[j]] for j, v in enumerate(p)]
        if identify(n, code):
            count += 1
    return count

def via_switches(n):
    assert n >= 3
    base = words(n - 2)
    states = words(n - 1)
    in_states = {v: sorted(w for w in states if w[1:] == v) for v in base}
    out_states = {v: sorted(w for w in states if w[:-1] == v) for v in base}
    total,valid = 0,0
    for bits in product((0, 1), repeat=len(base)):
        code = []
        for j, v in enumerate(base):
            incoming, outgoing = in_states[v], out_states[v]
            for i in range(2):
                a, b = incoming[i], outgoing[i ^ bits[j]]
                assert a[1:] == b[:-1]
                code.append(a + b[-1])
        assert len(set(code)) == len(states)
        total += 1
        valid += identify(n, code)
    return total,valid

if __name__ == '__main__':
    assert via_prefix(2) == 2
    for n, expectation in [(3, 4), (4, 27), (5, 1728)]:
        totals = via_switches(n)
        assert totals == (2 ** (3 * 2 ** (n - 3)), expectation), (n, totals)
        if n <= 4:
            assert via_prefix(n) == expectation
        print('n',n,'cycle_covers',totals[0],'optimal_codes',totals[1])
    print('KAUTZ_CLASSIFICATION_FINITE_OK')
