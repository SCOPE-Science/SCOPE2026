#!/usr/bin/env python3
"""Finite checks of a run-constrained modular distinct-subsequence language.
No external dependencies. General correctness rests on the proof, not these tests.
"""
from collections import deque
from itertools import product
from math import gcd


def transition(state, bit, modulus):
    if state is None:
        return None
    x, y, last_one = state
    if bit == 1 and last_one:
        return None
    return (x, (x+y) % modulus, 1) if bit else ((x+y) % modulus, y, 0)


def reachable(modulus):
    start = (1 % modulus, 1 % modulus, 0)
    order = [start]
    indices = {start: 0}
    queue = deque([start])
    edges = []
    while queue:
        state = queue.popleft()
        row = []
        for bit in (0, 1):
            target = transition(state, bit, modulus)
            if target not in indices:
                indices[target] = len(order)
                order.append(target)
                queue.append(target)
            row.append(indices[target])
        edges.append(tuple(row))
    return order, edges


def minimum_dfa_states(order, edges, modulus):
    accepting = {i for i, state in enumerate(order)
                 if state is not None and (state[0] + state[1] - 1) % modulus == 0}
    blocks = [s for s in (accepting, set(range(len(order))) - accepting) if s]
    while True:
        owner = {node: b for b, block in enumerate(blocks) for node in block}
        refined = []
        for block in blocks:
            partitions = {}
            for node in block:
                key = tuple(owner[edges[node][bit]] for bit in (0, 1))
                partitions.setdefault(key, set()).add(node)
            refined.extend(partitions.values())
        if len(refined) == len(blocks):
            return len(blocks)
        blocks = refined


def raw_distinct_count(bits):
    subs = {()}
    for bit in bits:
        subs |= {s + (bit,) for s in tuple(subs)}
    return len(subs)


def main():
    transition_cases = 0
    recognition_cases = 0
    for m in range(2, 21):
        states, edges = reachable(m)
        primitive = sum(gcd(x, y, m) == 1 for x in range(m) for y in range(m))
        target = 2 * primitive + 1
        assert len(states) == target, (m, len(states), target)
        assert minimum_dfa_states(states, edges, m) == target, m
        for state in states:
            if state is not None:
                assert gcd(state[0], state[1], m) == 1
        transition_cases += len(states)*2
        for n in range(0, 11):
            for bits in product((0, 1), repeat=n):
                state = (1 % m, 1 % m, 0)
                for bit in bits:
                    state = transition(state, bit, m)
                predicted = state is not None and (state[0] + state[1] - 1) % m == 0
                observed = not any(a == b == 1 for a, b in zip(bits, bits[1:])) and raw_distinct_count(bits) % m == 0
                assert predicted == observed, (m, bits)
                recognition_cases += 1
        print(f'm={m:2d} primitive={primitive:4d} reachable={len(states):4d} minimized={target:4d}')
    print(f'PASS: {transition_cases} directed transitions and {recognition_cases} direct word checks')


if __name__ == '__main__':
    main()
