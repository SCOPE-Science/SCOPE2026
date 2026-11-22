#!/usr/bin/env python3
"""Finite checks of a two-parameter binary subsequence-recognition theorem.

Pure Python 3, standard library only. All enumeration bounds are finite tests,
not substitutes for the general proof.
"""
from collections import deque
from itertools import product


def is_subsequence(pattern, word):
    it = iter(word)
    return all(any(x == symbol for x in it) for symbol in pattern)


def direct_member(word, forbidden, k):
    return forbidden not in word and all(
        is_subsequence(''.join(v), word)
        for v in product('01', repeat=k)
    )


def build_automaton(forbidden, k):
    # States: (completed arches, partial-letter mask, KMP proper-prefix length).
    # Forbid-condition failure is an absorbing state.
    root = (0, 0, 0)
    bad = None
    states = [root]
    transitions = {}
    lookup = {root: 0}
    i = 0
    while i < len(states):
        state = states[i]
        if state is bad:
            transitions[i] = (lookup[bad], lookup[bad])
            i += 1
            continue
        count, partial, suffix = state
        adjacent = []
        for bit in '01':
            # KMP transition: longest suffix that is a prefix of forbidden.
            old_suffix = forbidden[:suffix]
            extension = old_suffix + bit
            if extension.endswith(forbidden):
                candidate = bad
            else:
                next_suffix = max(
                    (j for j in range(len(forbidden))
                     if extension.endswith(forbidden[:j])), default=0)
                next_count, next_partial = count, partial
                if count < k:
                    next_partial |= (1 << int(bit))
                    if next_partial == 3:
                        next_count, next_partial = count + 1, 0
                candidate = (next_count, next_partial, next_suffix)
            if candidate not in lookup:
                lookup[candidate] = len(states)
                states.append(candidate)
            adjacent.append(lookup[candidate])
        transitions[i] = tuple(adjacent)
        i += 1
    final = set(i for i,s in enumerate(states) if s is not None and s[0] == k)
    return states, transitions, final


def minimum_state_count(trans, final):
    n = len(trans)
    labels = [int(i in final) for i in range(n)]
    while True:
        signatures = [(labels[i], labels[trans[i][0]], labels[trans[i][1]])
                      for i in range(n)]
        dictionary = {key: j for j, key in enumerate(sorted(set(signatures)))}
        updated = [dictionary[s] for s in signatures]
        if all((updated[i] == updated[j]) == (labels[i] == labels[j])
               for i in range(n) for j in range(i+1,n)):
            return len(set(updated))
        labels = updated


def accepts(word, states, trans, final):
    s = 0
    for bit in word:
        s = trans[s][int(bit)]
    return s in final


def main():
    parameters = 0
    for d in range(2, 14):
        for k in range(1, 17):
            for forbidden, predicted in ((('0'*d)+'1', (d+2)*k+d+1),
                                         ('1'+('0'*d), (d+2)*k+2)):
                states, trans, final = build_automaton(forbidden,k)
                actual = minimum_state_count(trans,final)
                assert actual == predicted, (forbidden,k,actual,predicted)
                parameters += 1
    examples = 0
    for d in range(2, 6):
        for k in range(1, 4):
            for forbidden in ('0'*d+'1', '1'+'0'*d):
                states,trans,final = build_automaton(forbidden,k)
                for length in range(13):
                    for letters in product('01',repeat=length):
                        word=''.join(letters)
                        assert accepts(word,states,trans,final) == direct_member(word,forbidden,k), (forbidden,k,word)
                        examples += 1
    print(f'PASS: {parameters} complete DFAs independently minimized (d=2..13, k=1..16, both directions).')
    print(f'PASS: {examples} direct word/pattern acceptance comparisons (d=2..5, k=1..3, lengths 0..12).')
    print('PASS: exact formulas and reversal gap d-1 in all tested cases.')

if __name__ == '__main__':
    main()
