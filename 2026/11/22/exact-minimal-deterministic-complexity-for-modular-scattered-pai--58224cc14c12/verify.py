#!/usr/bin/env python3
"""Independent finite checks of minimal complete DFA for 0^r1 avoidance
and scattered 01 counts modulo m. Standard-library only.
"""
from itertools import product


def recognize_direct(word, r, m):
    zeros = pairs = 0
    for symbol in word:
        if symbol == '0': zeros += 1
        else: pairs += zeros
    return ('0' * r + '1' not in word) and pairs % m == 0


def construct_dfa(r, m):
    initial = (0, 0, 0)
    states, ids, edges = [initial], {initial:0}, []
    for zero_residue, pair_residue, terminal_zeros in states:
        row = []
        for symbol in ('0', '1'):
            if symbol == '0':
                new_state = ((zero_residue + 1) % m, pair_residue,
                             min(r, terminal_zeros + 1))
            elif terminal_zeros == r:
                new_state = None
            else:
                new_state = (zero_residue, (pair_residue + zero_residue) % m, 0)
            if new_state is not None and new_state not in ids:
                ids[new_state] = len(states)
                states.append(new_state)
            row.append(None if new_state is None else ids[new_state])
        edges.append(row)
    sink = len(states)
    edges.append([sink, sink])
    edges = [[sink if dst is None else dst for dst in pair] for pair in edges]
    accepting = {index for index, state in enumerate(states) if state[1] == 0}
    return states, edges, accepting, sink


def moore_minimize(edges, accepting):
    classes = [int(index in accepting) for index in range(len(edges))]
    while True:
        signatures = [(classes[i], classes[e[0]], classes[e[1]])
                      for i,e in enumerate(edges)]
        label = {signature:i for i,signature in enumerate(sorted(set(signatures)))}
        new_classes = [label[s] for s in signatures]
        if new_classes == classes:
            return classes
        classes = new_classes


def run_checks():
    cases = checked = 0
    for r in range(1, 10):
        for m in range(2, 15):
            states, edges, accepting, sink = construct_dfa(r, m)
            classes = moore_minimize(edges, accepting)
            expected = 3 if r == 1 else r*m*m + 2
            assert len(set(classes)) == expected, (r, m, len(set(classes)), expected)
            if r >= 2:
                assert len(states) == (r+1)*m*m
                prefix_classes = [classes[i] for i,(_,_,j) in enumerate(states) if j<r]
                assert len(set(prefix_classes)) == r*m*m
                long_zero_accepting = {classes[i] for i,(_,c,j) in enumerate(states)
                                        if j==r and c==0}
                assert len(long_zero_accepting)==1
                assert all(classes[i] == classes[sink]
                           for i,(_,c,j) in enumerate(states) if j==r and c!=0)
            if r<=5 and m<=6:
                for length in range(0, 11):
                    for symbols in product('01', repeat=length):
                        word = ''.join(symbols)
                        state = 0
                        for symbol in symbols:state=edges[state][int(symbol)]
                        assert (state in accepting)==recognize_direct(word,r,m)
                        checked += 1
            cases += 1
    print(f'PASS {cases} independent reachable-DFA minimizations')
    print(f'PASS {checked} direct word-membership comparisons')
    print('All m=2..14, r=1..9 attain the claimed formula.')

if __name__=='__main__':run_checks()
