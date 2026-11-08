"""Exact full-state verification for binary sequential majority on friendship graphs.

Run with Python 3.10+: python verify_absorption.py
The code uses no external packages.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb


def neighbors(k):
    adj = [list(range(1, 2*k+1))]
    for t in range(k):
        u, v = 2*t+1, 2*t+2
        adj.extend([[0, v], [0, u]])
    return adj


def predicted_terminal_law(state, k):
    initial_hub = state & 1
    supporting = opposing = 0
    mixed = []
    for t in range(k):
        u, v = (state >> (2*t+1)) & 1, (state >> (2*t+2)) & 1
        if u != v:
            mixed.append(t)
        elif u == initial_hub:
            supporting += 1
        else:
            opposing += 1
    j, d = len(mixed), opposing - supporting
    flip_positions = min(j + 1, max(0, d))
    def terminal(new_hub, settled_to_initial):
        result = new_hub
        for t in range(k):
            u, v = (state >> (2*t+1)) & 1, (state >> (2*t+2)) & 1
            if u == v:
                bit = u
            else:
                bit = initial_hub if t in settled_to_initial else 1-initial_hub
            result |= bit << (2*t+1)
            result |= bit << (2*t+2)
        return result
    out = defaultdict(Fraction)
    for r in range(1, flip_positions+1):
        for subset in combinations(mixed, r-1):
            out[terminal(1-initial_hub, set(subset))] += Fraction(1, (j+1)*comb(j, r-1))
    out[terminal(initial_hub, set(mixed))] += Fraction(j+1-flip_positions, j+1)
    return {m: v for m, v in out.items() if v}


def direct_terminal_law_factory(k):
    adj = neighbors(k)
    @lru_cache(None)
    def law(state):
        choices = []
        for u, adjacent in enumerate(adj):
            same = (state >> u) & 1
            ones = sum((state >> v) & 1 for v in adjacent)
            if (ones*2 > len(adjacent) and same == 0) or (ones*2 < len(adjacent) and same == 1):
                choices.append(state ^ (1 << u))
        if not choices:
            return {state: Fraction(1)}
        out = defaultdict(Fraction)
        for next_state in choices:
            for target, probability in law(next_state).items():
                out[target] += probability / len(choices)
        return dict(out)
    return law


def run():
    for k in range(1, 7):
        full = direct_terminal_law_factory(k)
        flip_sum = Fraction(0)
        consensus_sum = Fraction(0)
        for state in range(1 << (2*k+1)):
            actual = full(state)
            predicted = predicted_terminal_law(state, k)
            assert actual == predicted, (k, state, actual, predicted)
            assert sum(actual.values()) == 1
            if state & 1:
                flip_sum += sum(p for target, p in actual.items() if not target & 1)
            consensus_sum += sum(p for target, p in actual.items() if target == 0 or target == (1 << (2*k+1))-1)
        assert flip_sum * 2 == sum(
            sum(p for target,p in full(state).items() if ((target ^ state) & 1))
            for state in range(1 << (2*k+1))
        )
        expected_consensus = Fraction(3**k, 4**k) + Fraction(3**(k+1)-1-2**(k+1), 2*(k+1)*4**k)
        assert consensus_sum / (2*4**k) == expected_consensus, k
        print(f'k={k}: {2*4**k} complete labelled-state terminal distributions match; hub-flip probability={flip_sum/4**k}; consensus probability={expected_consensus}')
    print('PASS: exact terminal kernels, hub-flip masses and consensus identities')

if __name__ == '__main__':
    run()
