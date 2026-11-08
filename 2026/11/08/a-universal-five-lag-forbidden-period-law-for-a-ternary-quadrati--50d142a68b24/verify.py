#!/usr/bin/env python3
"""Exact checks for the five-lag nonzero-cycle exclusion over F_3.

Runs without external packages; Python 3.9+ recommended.
The local-transition enumeration is exhaustive; trajectory checks are finite examples.
"""
from itertools import combinations


def is_adjacent(pair):
    a, b = pair
    return ((b - a) % 5) in (1, 4)


def local_certification():
    pairs = list(combinations(range(5), 2))
    edges = {}
    for pair in pairs:
        zeros = set(pair)
        b = [int(t not in zeros) for t in range(5)]
        assert sum(b) == 3
        walk = [0]
        for t in range(4):
            walk.append((walk[-1] + b[t]) % 3)
        assert (walk[0] - walk[-1]) % 3 == b[4]
        candidates = set()
        for offset in range(3):
            out = tuple(t for t, value in enumerate(walk) if (value + offset) % 3 == 0)
            if len(out) == 2:
                candidates.add(out)
        edges[pair] = candidates
        assert len(candidates) == (0 if is_adjacent(pair) else 2)
        assert all(is_adjacent(out) for out in candidates)
    assert sum(len(tgts) for tgts in edges.values()) == 10
    assert all(not edges[output] for dests in edges.values() for output in dests)
    return len(pairs), sum(map(len, edges.values()))


def check_trajectories():
    tests = states = 0
    for k in range(2, 11):
        fixed = 0
        for i in range(3**k):
            z = i
            state = []
            for _ in range(k):
                state.append(z % 3)
                z //= 3
            initial = tuple(state)
            for _ in range(5*k):
                state = state[1:] + [(state[0] + state[-1]*state[-1]) % 3]
            fixed += tuple(state) == initial
            states += 1
        assert fixed == 1, (k, fixed)
        tests += 1
    return tests, states


def main():
    masks, transitions = local_certification()
    lags, state_count = check_trajectories()
    print(f"VERIFY_OK masks={masks} transitions={transitions} square_zero=yes lags={lags} states={state_count} fixed_each=1 exact_modular=yes")


if __name__ == '__main__':
    main()
