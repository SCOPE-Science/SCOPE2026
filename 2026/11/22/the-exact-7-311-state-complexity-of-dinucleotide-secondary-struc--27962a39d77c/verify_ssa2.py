#!/usr/bin/env python3
"""Exact DFA state-complexity certificate for length-two DNA secondary-structure avoidance.

Run: python3 verify_ssa2.py
Uses only Python standard library. All counts are exact integers.
"""
from collections import defaultdict, deque
from itertools import product

Q = 4
COMP = (1, 0, 3, 2)  # A<->T and C<->G
RC = tuple(4 * COMP[p % 4] + COMP[p // 4] for p in range(16))


def build():
    """Reachable streaming automaton; returning transitions and sink index."""
    initial = (4, 16, 0)
    states = [initial]
    index = {initial: 0}
    transitions = []
    for last, newest, mature in states:
        row = []
        for b in range(Q):
            if last == 4:
                target = (b, 16, 0)
            else:
                pair = Q * last + b
                if mature & (1 << RC[pair]):
                    row.append(-1)
                    continue
                target = (b, pair, mature | (0 if newest == 16 else (1 << newest)))
            if target not in index:
                index[target] = len(states)
                states.append(target)
            row.append(index[target])
        transitions.append(tuple(row))
    sink = len(states)
    transitions = [tuple(sink if v < 0 else v for v in row) for row in transitions]
    transitions.append((sink,) * Q)
    assert len(set(states)) == len(states)
    return states, transitions, sink


def moore(transitions, sink):
    """Successive exact suffix-equivalence partitions (up to length k)."""
    count = len(transitions)
    # Acceptance must be fixed throughout; partition ID 0 is not a reject flag.
    accepting = tuple(i != sink for i in range(count))
    labels = [int(x) for x in accepting]
    sizes = [len(set(labels))]
    while True:
        ids = {}
        nxt = []
        for i, row in enumerate(transitions):
            sig = (accepting[i],) + tuple(labels[j] for j in row)
            if sig not in ids:
                ids[sig] = len(ids)
            nxt.append(ids[sig])
        sizes.append(len(ids))
        # Refinement cannot merge prior blocks, so equal counts mean stable.
        if sizes[-1] == sizes[-2]:
            labels = nxt
            break
        labels = nxt
    quotient = {}
    for i, row in enumerate(transitions):
        key = labels[i]
        val = (accepting[i], tuple(labels[j] for j in row))
        if key in quotient:
            assert quotient[key] == val
        else:
            quotient[key] = val
    assert len(quotient) == sizes[-1]
    return sizes, labels


def hopcroft(transitions, sink):
    """Independent inverse-transition partition-splitting minimizer."""
    n = len(transitions)
    reverse = [[[] for _ in range(n)] for _ in range(Q)]
    for u, row in enumerate(transitions):
        for a, v in enumerate(row):
            reverse[a][v].append(u)
    blocks = {0: set(range(sink)), 1: {sink}}
    owners = [0] * sink + [1]
    todo = deque([1])
    waiting = {1}
    next_id = 2
    while todo:
        chosen = todo.popleft()
        waiting.remove(chosen)
        sample = tuple(blocks[chosen])  # freeze before any splits
        for a in range(Q):
            incoming = defaultdict(set)
            for v in sample:
                for u in reverse[a][v]:
                    incoming[owners[u]].add(u)
            for block_id, sub in incoming.items():
                old = blocks[block_id]
                if len(sub) == len(old):
                    continue
                old.difference_update(sub)
                blocks[next_id] = sub
                for u in sub:
                    owners[u] = next_id
                if block_id in waiting:
                    todo.append(next_id)
                    waiting.add(next_id)
                else:
                    small = block_id if len(old) <= len(sub) else next_id
                    todo.append(small)
                    waiting.add(small)
                next_id += 1
    assert sum(map(len, blocks.values())) == n
    assert all(owners[u] == b for b, group in blocks.items() for u in group)
    return len(blocks), owners


def direct_good(w):
    pairs = [Q * a + b for a, b in zip(w, w[1:])]
    for i, p in enumerate(pairs):
        for j in range(i + 2, len(pairs)):
            if p == RC[pairs[j]]:
                return False
    return True


def verify():
    states, transitions, sink = build()
    assert len(states) == 22985
    assert len(transitions) == 22986
    levels, labels = moore(transitions, sink)
    assert levels == [2, 17, 2715, 6807, 7295, 7311, 7311], levels
    minimum, other = hopcroft(transitions, sink)
    assert minimum == levels[-1] == 7311
    assert len({(labels[u], other[u]) for u in range(len(transitions))}) == minimum
    tested = 0
    for n in range(10):
        for w in product(range(Q), repeat=n):
            state = 0
            for letter in w:
                state = transitions[state][letter]
            assert (state != sink) == direct_good(w), w
            tested += 1
    assert tested == (4 ** 10 - 1) // 3
    print('reachable accepting states:', sink)
    print('reachable complete-DFA states:', len(transitions))
    print('suffix-equivalence partition sizes:', levels)
    print('independent inverse-transition minimization:', minimum)
    print('directly checked DNA words, lengths 0 through 9:', tested)
    print('minimal complete DFA states:', minimum)


if __name__ == '__main__':
    verify()
