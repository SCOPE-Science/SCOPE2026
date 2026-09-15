"""Bounded recovery test for lane-20211 (n=1 case).

Enumerate one-vertex square presentations with 2 generators and s<=2 squares:
  pi1 = < a, b | r_1, ..., r_s >, each r_i a cyclic word of length 4.
For each: check Gromov link condition (link = graph on {a+,a-,b+,b-},
each square contributes 4 corner-edges; NPC needs simple graph, girth>=4)
and compute H1 = Z^2 / im(relators) abelianized (finite H1 is necessary
for property FA = FW_1, since Z-quotient gives unbounded line action).

A complete target route for n=1 needs an infinite torsion-free FA group
that is the fundamental group of a compact NPC square complex. Such a
group would have to appear (up to larger size) with H1 finite. We test
whether ANY small NPC candidate even clears the H1 bar.
"""
import itertools
from math import gcd

# generators: 0=a, 1=b, 2=A=a^-1, 3=B=b^-1 ; inverse: x^3
def inv(x):
    return x ^ 3  # 0<->3? No: 0=a,3=B. Fix: inv pairs (0,2),(1,3)
def inv2(x):
    return {0: 2, 2: 0, 1: 3, 3: 1}[x]

NAMES = ['a', 'b', 'A', 'B']
# half-edges at vertex: a_out, b_out, a_in, b_in  -> ids 0..3
# letter a means edge leaves via a_out, enters via a_in.
# corner contributed between consecutive letters x,y in cyclic word:
#   exit-half-edge of x^-1 side ... standard: corners join
#   out(x)?? Let's define: traversing letter x uses the oriented edge;
#   at the corner between letter x and letter y we join head(x) to tail(y).
#   head(a)=a_in(2), tail(a)=a_out(0); head(A)=a_out(0), tail(A)=a_in(2);
#   head(b)=b_in(3), tail(b)=b_out(1); head(B)=b_out(1), tail(B)=b_in(3).
HEAD = {0: 2, 2: 0, 1: 3, 3: 1}
TAIL = {0: 0, 2: 2, 1: 1, 3: 3}

def corners(word):
    n = len(word)
    return [(HEAD[word[i]], TAIL[word[(i + 1) % n]]) for i in range(n)]

def canon(word):
    rots = [tuple(word[i:] + word[:i]) for i in range(len(word))]
    iv = [inv2(x) for x in reversed(word)]
    rots += [tuple(iv[i:] + iv[:i]) for i in range(len(iv))]
    return min(rots)

def link_ok(words):
    seen = set()
    for w in words:
        for (u, v) in corners(w):
            if u == v:
                return False, 'loop'
            e = (min(u, v), max(u, v))
            if e in seen:
                return False, 'bigon'
            seen.add(e)
    # adjacency on 4 vertices; girth>=4 means no triangle
    adj = {i: set() for i in range(4)}
    for (u, v) in seen:
        adj[u].add(v)
        adj[v].add(u)
    for u in range(4):
        for v in adj[u]:
            if adj[u] & adj[v]:
                return False, 'triangle'
    return True, 'ok'

def abelian_invariants(words):
    # rows: exponent sums of (a,b)
    import numpy as np
    M = []
    for w in words:
        ea = sum(1 for x in w if x == 0) - sum(1 for x in w if x == 2)
        eb = sum(1 for x in w if x == 1) - sum(1 for x in w if x == 3)
        M.append((ea, eb))
    if not M:
        return ('Z^2', False)
    if len(M) == 1:
        (ea, eb) = M[0]
        if ea == 0 and eb == 0:
            return ('Z^2', False)
        return (f'Z x Z/{gcd(ea, eb)}', False)
    (a1, b1), (a2, b2) = M
    det = abs(a1 * b2 - a2 * b1)
    import math
    g = 0
    for v in (a1, b1, a2, b2):
        g = math.gcd(g, v)
    if det == 0:
        # rank-deficient: infinite H1 unless rows span rank2 over Q... det 0 -> rank<=1 -> infinite
        # unless both rows zero
        if g == 0:
            return ('Z^2', False)
        return ('Z x Z/k or Z^2', False)
    # finite of order det (times free rank 0) since 2 gens 2 rels full rank
    return (f'finite order {det}', True)

def all_words():
    out = set()
    for w in itertools.product(range(4), repeat=4):
        out.add(canon(list(w)))
    return sorted(out)

def main():
    words = all_words()
    print(f'distinct cyclic square words (2 gens): {len(words)}')
    npc1 = 0
    fin1 = []
    for w in words:
        ok, _ = link_ok([w])
        if ok:
            npc1 += 1
            inv_, finite = abelian_invariants([w])
            if finite:
                fin1.append((w, inv_))
    print(f's=1: NPC complexes: {npc1}, of which H1 finite: {len(fin1)}')
    for w, inv_ in fin1[:20]:
        print('   ', ''.join(NAMES[x] for x in w), inv_)
    # s=2 pairs
    npc2 = 0
    fin2 = []
    L = len(words)
    for i in range(L):
        for j in range(i, L):
            wi, wj = words[i], words[j]
            ok, _ = link_ok([wi, wj])
            if ok:
                npc2 += 1
                inv_, finite = abelian_invariants([wi, wj])
                if finite:
                    fin2.append(((wi, wj), inv_))
    print(f's=2: NPC complexes: {npc2}, of which H1 finite: {len(fin2)}')
    for (wi, wj), inv_ in fin2[:20]:
        print('   ', ''.join(NAMES[x] for x in wi), '+', ''.join(NAMES[x] for x in wj), inv_)

if __name__ == '__main__':
    main()
