#!/usr/bin/env python3
"""Independent finite checks of the forced-colouring enumerator for clique bouquets.

Uses explicit partial assignments and Farr's local forcing rule, then independently
calculates the closed-form coefficients. This is a finite stress test, not a proof
of the theorem for unbounded clique sizes or numbers of blades.
"""

from collections import Counter
from itertools import product
from math import comb, factorial


def falling(a, b):
    if b > a:
        return 0
    out = 1
    for j in range(b):
        out *= a-j
    return out


def closed_coefficients(sizes):
    s = max(sizes)
    top_count = sum(a == s for a in sizes)
    smaller = [a for a in sizes if a < s]
    small_total = sum(smaller)
    L = 1
    L_minus = 1
    for a in smaller:
        L *= falling(s, a)
        L_minus *= falling(s-1, a)
    shift = small_total + top_count*(s-1)
    factor = (s+1) * factorial(s)**top_count
    ans = Counter()
    for j in range(top_count+1):
        c = factor*L*comb(top_count, j)*s**(top_count-j)
        ans[shift+j] += c
        ans[shift+j+1] += c
    ans[shift] -= factor*s*L_minus
    return {k:v for k,v in ans.items() if v}


def graph_adjacency(sizes):
    n = 1 + sum(sizes)
    adj = [set() for _ in range(n)]
    offset = 1
    for a in sizes:
        vtx = list(range(offset, offset+a))
        for u in vtx:
            adj[0].add(u)
            adj[u].add(0)
        for i,u in enumerate(vtx):
            for v in vtx[i+1:]:
                adj[u].add(v)
                adj[v].add(u)
        offset += a
    return adj


def is_forcing(assignment, adj, palette):
    state = list(assignment)
    if any(state[u] >= 0 and state[u] == state[v]
           for u in range(len(adj)) for v in adj[u] if v > u):
        return False
    # Deterministic first-eligible dynamics is sufficient for consistent
    # partial colourings; each step takes the unique colour missing locally.
    while True:
        step = False
        for v in range(len(state)):
            if state[v] != -1:
                continue
            used = {state[u] for u in adj[v] if state[u] != -1}
            if len(used) != palette-1:
                continue
            remaining = set(range(palette)) - used
            if len(remaining) != 1:
                return False
            state[v] = remaining.pop()
            step = True
            break
        if not step:
            break
    return all(a >= 0 for a in state) and all(
        state[u] != state[v]
        for u in range(len(adj)) for v in adj[u] if v > u
    )


def direct_coefficients(sizes):
    adj = graph_adjacency(sizes)
    palette = max(sizes) + 1
    counts = Counter()
    for assignment in product(range(-1,palette), repeat=len(adj)):
        if is_forcing(assignment, adj, palette):
            counts[sum(v >= 0 for v in assignment)] += 1
    return dict(counts)


def checks():
    cases = [
        (1,1), (1,1,1), (1,1,1,1),
        (2,1), (2,1,1), (2,1,1,1), (2,2), (2,2,1), (2,2,2),
        (2,2,1,1), (2,2,2,1), (2,2,2,2),
        (3,1), (3,1,1), (3,2), (3,2,1), (3,3), (3,3,1),
        (3,1,1,1), (3,2,2), (3,2,1,1),
    ]
    for sizes in cases:
        exp = closed_coefficients(sizes)
        got = direct_coefficients(sizes)
        assert exp == got, (sizes, exp, got)
        n = 1+sum(sizes)
        s = max(sizes)
        t = sum(a==s for a in sizes)
        q = [a for a in sizes if a<s]
        L = 1
        L_minus = 1
        for a in q:
            L *= falling(s,a)
            L_minus *= falling(s-1,a)
        # Total proper full colourings, also specialization p=1/palette.
        assert got[n] == (s+1)*factorial(s)**t*L
        if s >= 2:
            h = sum(q) + t*(s-1)
            assert min(got) == h
            assert got[h] == (s+1)*factorial(s)**t*(L*s**t-s*L_minus)
        else:
            assert min(got) == 1
            assert got[1] == 2*n
        print("DIRECT_OK", sizes, "degree", n, "minimum", min(got),
              "count", sum(got.values()))
    # A further algebraic stress test over widely varying blade vectors.
    for s in range(2,15):
        for t in range(1,7):
            for a in range(1,s):
                sizes = (s,)*t + (a,)
                counts = closed_coefficients(sizes)
                h = a+t*(s-1)
                assert min(counts) == h and counts[h] > 0
                assert sum(counts.values()) == (
                    (s+1)*factorial(s)**t*
                    (2*(s+1)**t*falling(s,a)-s*falling(s-1,a))
                )
    print("FORMULA_BOUNDARIES_OK s=2..14,t=1..6,a=1..s-1")
    print("VERIFY_OK")

if __name__ == '__main__':
    checks()
