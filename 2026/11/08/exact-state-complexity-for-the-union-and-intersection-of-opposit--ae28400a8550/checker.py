#!/usr/bin/env python3
"""Finite, independently implementable tests for two opposite-run subsequence ideals.

The mathematical proof for arbitrary positive parameters is in RESULT.md.
This checker tests bounded parameter ranges and words; it does not replace that proof.
"""
from collections import deque, defaultdict
from itertools import product


def subsequence(pattern, word):
    k = 0
    for c in word:
        if k < len(pattern) and pattern[k] == c:
            k += 1
    return k == len(pattern)


def product_dfa(a, b):
    P, Q = '0'*a+'1'*b, '1'*b+'0'*a
    n = a+b
    initial = (0, 0)
    queue = deque([initial])
    seen = {initial}
    edges = {}
    while queue:
        state = queue.popleft()
        nxt = []
        for letter in '01':
            t = tuple(s + int(s < n and pat[s] == letter)
                      for s, pat in zip(state, (P, Q)))
            nxt.append(t)
            if t not in seen:
                seen.add(t)
                queue.append(t)
        edges[state] = tuple(nxt)
    return seen, edges


def minimize(states, edges, accepting):
    blocks = [accepting, states-accepting]
    blocks = [b for b in blocks if b]
    while True:
        cid = {x:i for i,B in enumerate(blocks) for x in B}
        by_sig = defaultdict(set)
        for x in states:
            by_sig[(x in accepting, cid[edges[x][0]], cid[edges[x][1]])].add(x)
        new_blocks = list(by_sig.values())
        if len(new_blocks) == len(blocks):
            return new_blocks
        blocks = new_blocks


def predictions(a, b):
    n = a+b
    R = n*(n+3)//2+a*b
    return R, R-n


def transitions_accept(edges, state, suffix, a, b, operation):
    x = state
    for c in suffix:
        x = edges[x][int(c)]
    return (x[0] == a+b and x[1] == a+b) if operation=='intersection' else (x[0] == a+b or x[1] == a+b)


def run():
    cases = 0
    words = 0
    probes = 0
    for a in range(1, 19):
        for b in range(1, 19):
            states, edges = product_dfa(a, b)
            R, U = predictions(a,b)
            assert len(states) == R, ('reachability',a,b,len(states),R)
            for operation in ('union', 'intersection'):
                accepting = {x for x in states if ((x[0] == a+b and x[1] == a+b) if operation=='intersection' else (x[0] == a+b or x[1] == a+b))}
                blocks = minimize(states,edges,accepting)
                target = R if operation=='intersection' else U
                assert len(blocks) == target, ('minimization',a,b,operation,len(blocks),target)
            cases += 1
            # Check four universal distinguishing-probe families, with independent brute transition simulation.
            if a <= 9 and b <= 9:
                n = a+b
                for p,q in states:
                    if (p,q) != (n,n):
                        # Intersection probes.
                        for r in range(n+2):
                            x = '0'*r+'1'*b+'0'*a
                            expect = r >= max(a-p,0)
                            assert transitions_accept(edges,(p,q),x,a,b,'intersection') == expect
                            x = '0'*r+'1'*b
                            expect = (q >= b and r >= n-q)
                            assert transitions_accept(edges,(p,q),x,a,b,'intersection') == expect
                            # Union probes (outside absorbing accepting states).
                            if p<n and q<n:
                                x = '0'*r
                                expect = q >= b and r >= n-q
                                assert transitions_accept(edges,(p,q),x,a,b,'union') == expect
                                x = '0'*r+'1'*b
                                expect = (p >= a or r >= a-p)
                                assert transitions_accept(edges,(p,q),x,a,b,'union') == expect
                            probes += 1
                        for s in range(n+2):
                            x = '1'*s+'0'*a
                            expect = (p >= a and s >= n-p)
                            assert transitions_accept(edges,(p,q),x,a,b,'intersection') == expect
                            x = '1'*s+'0'*a+'1'*b
                            expect = s >= max(b-q,0)
                            assert transitions_accept(edges,(p,q),x,a,b,'intersection') == expect
                            if p<n and q<n:
                                x = '1'*s
                                expect = p >= a and s >= n-p
                                assert transitions_accept(edges,(p,q),x,a,b,'union') == expect
                                x = '1'*s+'0'*a
                                expect = (q >= b or s >= b-q)
                                assert transitions_accept(edges,(p,q),x,a,b,'union') == expect
                            probes += 1
    # Independent word enumeration: direct subsequence containment versus DFA.
    for a,b in product(range(1,5), repeat=2):
        _, edges = product_dfa(a,b)
        P,Q='0'*a+'1'*b, '1'*b+'0'*a
        for length in range(0,12):
            for seq in product('01',repeat=length):
                w=''.join(seq)
                p,q=(0,0)
                for c in w:
                    p,q=edges[(p,q)][int(c)]
                x,y=subsequence(P,w),subsequence(Q,w)
                assert (p == a+b) == x
                assert (q == a+b) == y
                assert (p == a+b and q == a+b) == (x and y)
                assert (p == a+b or q == a+b) == (x or y)
                words += 1
    print('PASS: %d parameter pairs, %d bounded direct-word checks, %d state/probe iterations' % (cases,words,probes))

if __name__ == '__main__':
    run()
