#!/usr/bin/env python3
"""Reproduce the Myhill--Nerode quotient of the remanent seven-cycle language.
Uses integer bitsets and only the Python standard library.
Run: python checker.py automaton_certificate.json
"""
import itertools
import json
import sys
from collections import deque
from pathlib import Path

def transitions_for_mask(n, mask):
    # Alphabet symbols: '+' means traverse along the oriented edge,
    # '-' means traverse against its orientation.
    plus = [0] * n
    minus = [0] * n
    for i in range(n):
        j = (i + 1) % n
        a, b = (i, j) if ((mask >> i) & 1) else (j, i)
        plus[a] |= 1 << b
        minus[b] |= 1 << a
    return minus, plus

def move(subset, outgoing):
    answer = 0
    while subset:
        bit = subset & -subset
        subset ^= bit
        answer |= outgoing[bit.bit_length() - 1]
    return answer

def enumerate_determinization(n):
    orients = [transitions_for_mask(n, mask) for mask in range(1 << n)]
    initial = tuple([(1 << n) - 1] * len(orients))
    # -1 represents a common absorbing failure, once some orientation has no run.
    dead = (-1,)
    states = [initial]
    words = ['']
    ids = {initial: 0}
    queue = deque([initial])
    table = []
    while queue:
        state = queue.popleft()
        i = ids[state]
        assert i == len(table)
        edges = []
        for letter in range(2):
            if state == dead:
                next_state = dead
            else:
                next_state = tuple(move(s, tr[letter])
                                   for s, tr in zip(state, orients))
                if not all(next_state):
                    next_state = dead
            if next_state not in ids:
                ids[next_state] = len(states)
                states.append(next_state)
                words.append(words[i] + ('-' if letter == 0 else '+'))
                queue.append(next_state)
            edges.append(ids[next_state])
        table.append(edges)
    accepting = [state != dead for state in states]
    return table, accepting, words

def moore_minimize(table, accepting):
    labels = [int(x) for x in accepting]
    sizes = [len(set(labels))]
    while True:
        signatures = [(labels[i], labels[t[0]], labels[t[1]])
                      for i, t in enumerate(table)]
        distinct = sorted(set(signatures))
        label_of = {sig: index for index, sig in enumerate(distinct)}
        updated = [label_of[s] for s in signatures]
        if len(set(updated)) == len(set(labels)):
            # Refinement cannot merge blocks, so equal count means stability.
            labels = updated
            break
        labels = updated
        sizes.append(len(set(labels)))
    return labels, sizes

def independent_pair_distinguishability(table, accepting):
    """Mark distinguishable state pairs until backward propagation is closed."""
    n = len(table)
    separated = {(i, j) for i in range(n) for j in range(i + 1, n)
                 if accepting[i] != accepting[j]}
    while True:
        new = set()
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in separated:
                    continue
                for c in (0, 1):
                    a, b = sorted((table[i][c], table[j][c]))
                    if (a, b) in separated:
                        new.add((i, j))
                        break
        if not new:
            break
        separated.update(new)
    return separated

def direct_accepts(word, n):
    # Independent, graph-edge traversal check without the product DFA.
    for mask in range(1 << n):
        states = set(range(n))
        for letter in word:
            new = set()
            for v in states:
                for i in range(n):
                    j = (i + 1) % n
                    a, b = (i, j) if (mask >> i) & 1 else (j, i)
                    if letter == '+' and v == a: new.add(b)
                    if letter == '-' and v == b: new.add(a)
            states = new
            if not states: break
        if not states: return False
    return True

def run(n=7, certificate=None):
    table, accepting, words = enumerate_determinization(n)
    labels, levels = moore_minimize(table, accepting)
    separated = independent_pair_distinguishability(table, accepting)
    for i in range(len(table)):
        for j in range(i + 1, len(table)):
            assert ((i, j) in separated) == (labels[i] != labels[j])
    result = {'cycle_vertices': n,
              'orientations': 1 << n,
              'reachable_determinized_states': len(table),
              'accepting_determinized_states': sum(accepting),
              'minimal_dfa_states': len(set(labels)),
              'moore_refinement_block_counts': levels,
              'transitions': table,
              'final_partition': labels,
              'shortest_access_words': words}
    # Verify full determination by distinct, direct graph-walk semantics.
    if n == 7:
        for l in range(11):
            for bits in itertools.product('+-', repeat=l):
                w = ''.join(bits)
                q = 0
                for a in w: q = table[q][0 if a == '-' else 1]
                assert accepting[q] == direct_accepts(w, 7), (w, q)
    if certificate is not None:
        assert result == certificate, 'Certificate disagrees with exhaustive regeneration'
    return result

if __name__ == '__main__':
    certpath = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('automaton_certificate.json')
    cert = json.loads(certpath.read_text(encoding='utf-8'))
    result = run(7, cert)
    assert result['reachable_determinized_states'] == 230
    assert result['accepting_determinized_states'] == 229
    assert result['minimal_dfa_states'] == 102
    # Independent baseline, as a contextual check, not another asserted novelty claim.
    for n, expected in ((3, 6), (5, 18)):
        check = run(n)
        assert check['minimal_dfa_states'] == expected
    print('VERIFIED: 128 orientations; 230 reachable subset states; 102 minimal states; baselines 6, 18')
