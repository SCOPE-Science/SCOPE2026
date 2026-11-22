#!/usr/bin/env python3
"""Reproducibility checks for modular distinct-subsequence automata.

The checker independently constructs reachable residue pairs, directly
compares them with primitive vectors, and minimizes DFAs for two output residues.
It also cross-checks a direct enumerator of distinct subsequences of short words.
"""
from collections import deque
from itertools import product
from math import gcd, prod


def transition(state, letter, m):
    x, y = state
    if letter == 0:
        return ((x + y) % m, y)
    return (x, (x + y) % m)


def orbit(m):
    states = [(1 % m, 1 % m)]
    visited = {states[0]}
    for state in states:
        for letter in (0, 1):
            nxt = transition(state, letter, m)
            if nxt not in visited:
                visited.add(nxt)
                states.append(nxt)
    return states


def primitive_set(m):
    return {(x, y) for x, y in product(range(m), repeat=2) if gcd(gcd(x, y), m) == 1}


def minimized_count(states, m, residue):
    ix = {state: i for i, state in enumerate(states)}
    succ = [tuple(ix[transition(state, a, m)] for a in (0, 1)) for state in states]
    classes = [int((sum(state) - 1) % m == residue) for state in states]
    while True:
        signatures = [(classes[i], classes[succ[i][0]], classes[succ[i][1]]) for i in range(len(states))]
        lookup = {s: j for j, s in enumerate(sorted(set(signatures)))}
        updated = [lookup[s] for s in signatures]
        if updated == classes:
            return len(set(classes))
        # Compare equivalence relations, independent of block label numbering.
        if all((classes[i] == classes[j]) == (updated[i] == updated[j]) for i in range(len(states)) for j in range(i+1, len(states))):
            return len(set(updated))
        classes = updated


def jordan(m):
    return sum(1 for x, y in product(range(m), repeat=2) if gcd(gcd(x, y), m) == 1)


def projective(m):
    return len({frozenset(((u*x) % m, (u*y) % m) for u in range(m) if gcd(u, m) == 1)
        for x, y in primitive_set(m)})


def all_subseq_count(word):
    subsequences = {''}
    for c in word:
        subsequences |= {s + c for s in list(subsequences)}
    return len(subsequences)


def main():
    cases = 0
    for m in range(2, 32):
        states = orbit(m)
        want = primitive_set(m)
        assert set(states) == want, ('reachability', m)
        phi = sum(gcd(k, m) == 1 for k in range(m))
        assert jordan(m) == len(states)
        assert len(states) % phi == 0
        assert projective(m) == len(states)//phi
        assert minimized_count(states, m, m-1) == len(states)//phi, ('minus-one-language', m)
        assert minimized_count(states, m, 0) == len(states), ('zero-language', m)
        # The suffixes 0^(m-1), 1^(m-1) distinguish any different state outputs.
        for x,y in states:
            assert (sum((transition((x,y),0,m))) - 1) % m == (x + y + y - 1) % m
            for a in (0,1):
                z=(x,y)
                for _ in range(m-1):
                    z=transition(z,a,m)
                assert (sum(z)-1) % m == ((x if a == 0 else y)-1) % m
        print('m',m,'states',len(states),'minus-one-DFA',len(states)//phi,'zero-DFA',len(states),'phi',phi)
        cases += 1
    word_cases=0
    for n in range(0,13):
        for bits in product('01', repeat=n):
            w=''.join(bits)
            x=y=1
            for letter in bits:
                if letter=='0': x=x+y
                else: y=x+y
            assert x+y-1 == all_subseq_count(w), ('count',w)
            word_cases+=1
    print('PASS: moduli',cases,'direct words',word_cases)

if __name__ == '__main__':
    main()
