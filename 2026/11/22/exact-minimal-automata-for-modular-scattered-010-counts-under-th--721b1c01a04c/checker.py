#!/usr/bin/env python3
"""Independent finite checks for the modular 010-count language with forbidden 11.
Standard library only. A finite check corroborates, but does not prove, the all-modulus theorem.
"""
import math
from collections import deque
from itertools import product


def direct_scattered_010(word):
    return sum(word[i] == 0 and word[j] == 1 and word[k] == 0
               for i in range(len(word)) for j in range(i+1, len(word))
               for k in range(j+1, len(word)))


def transitions(m):
    # States: (zeros, scattered_01, scattered_010, last_symbol).
    # Last_symbol = 0,1; initial state uses last_symbol=0, an equivalent
    # boundary condition, since 1 is legal as first letter.
    start = (0, 0, 0, 0)
    sink = (-1, -1, -1, -1)
    def step(q, bit):
        if q == sink:
            return sink
        a, b, c, last = q
        if bit == 0:
            return ((a+1)%m, b, (c+b)%m, 0)
        if last == 1:
            return sink
        return (a, (b+a)%m, c, 1)
    states = [start]
    index = {start:0}
    for state in states:
        for bit in (0,1):
            nxt = step(state, bit)
            if nxt not in index:
                index[nxt] = len(states)
                states.append(nxt)
    trans = [[index[step(q, bit)] for bit in (0,1)] for q in states]
    accept = [q != sink and q[2] == 0 for q in states]
    return states, trans, accept


def quotient_size(trans, accept):
    # Iterative right-congruence refinement; independent of reachability formula.
    colors = [int(b) for b in accept]
    iterations = 0
    while True:
        signatures = [(colors[i], colors[t[0]], colors[t[1]])
                      for i, t in enumerate(trans)]
        palette = {s:i for i,s in enumerate(sorted(set(signatures)))}
        refined = [palette[s] for s in signatures]
        iterations += 1
        if len(set(refined)) == len(set(colors)):
            return len(set(refined)), iterations
        colors = refined


def verify():
    total_words = total_states = total_bad = 0
    rows = []
    for m in range(2,15):
        states, trans, accept = transitions(m)
        predicted = 2*m**3//math.gcd(m,2)+1
        assert len(states) == predicted, (m,len(states),predicted)
        got, refinements = quotient_size(trans, accept)
        assert got == predicted, (m,got,predicted)
        valid = [q for q in states if q[0]>=0]
        allowed = {(a,b,c,t) for a in range(m) for b in range(m)
                   for c in range(m) for t in (0,1)
                   if (c-(a-1)*b)%math.gcd(m,2)==0}
        assert set(valid)==allowed, (m,len(valid),len(allowed))
        total_states += len(states)
        rows.append((m,predicted,refinements))
    # Direct independent arithmetic for all words of lengths <= 14.
    # One 010 count is computed from position triples, not from transitions.
    for length in range(15):
        for word in product((0,1), repeat=length):
            total_words += 1
            cnt = direct_scattered_010(word)
            forbidden = any(word[i:i+2] == (1,1) for i in range(len(word)-1))
            for m in range(2,10):
                state = 0
                states, trans, accept = machines[m]
                for bit in word:
                    state = trans[state][bit]
                assert accept[state] == (not forbidden and cnt%m == 0), (m,word)
                if forbidden:
                    assert states[state] == (-1,-1,-1,-1), (m,word)
                else:
                    assert states[state][2] == cnt%m, (m,word)
            if forbidden: total_bad += 1
    print('moduli: 2..14')
    print('m / minimal-DFA-states / refinement-rounds')
    for r in rows: print(*r)
    print('modular reachability+minimization states:',total_states)
    print('direct source words:',total_words)
    print('direct-recognition comparisons:',total_words*8)
    print('forbidden source words:',total_bad)
    print('all checks passed')


if __name__ == '__main__':
    machines = {m:transitions(m) for m in range(2,10)}
    verify()
