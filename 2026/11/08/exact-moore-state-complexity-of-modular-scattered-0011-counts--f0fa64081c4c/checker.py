#!/usr/bin/env python3
"""Reproduce exact finite-state and word-count checks for modular scattered 0011."""
from collections import deque
from itertools import product
from math import comb, gcd


def step(state, letter, m):
    a, b, c, d = state
    if letter == 0:
        return ((a + 1) % m, (b + a) % m, c, d)
    if letter == 1:
        return (a, b, (c + b) % m, (d + c) % m)
    raise ValueError(letter)


def run(word, m, start=(0, 0, 0, 0)):
    s = start
    for x in word:
        s = step(s, x, m)
    return s


def direct_count(word):
    # Direct combinatorial count using position quadruples, not the transition update.
    positions0 = [i for i, x in enumerate(word) if x == 0]
    positions1 = [i for i, x in enumerate(word) if x == 1]
    return sum(i < j < k < l for i in positions0 for j in positions0
               for k in positions1 for l in positions1)


def reachable(m):
    start = (0, 0, 0, 0)
    seen = {start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for letter in (0, 1):
            nxt = step(state, letter, m)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def moore_classes(states, m):
    # Refinement to the coarsest output-compatible stable partition.
    states = sorted(states)
    klass = {q: q[3] for q in states}
    rounds = 0
    while True:
        signatures = {q: (q[3], klass[step(q, 0, m)], klass[step(q, 1, m)])
                      for q in states}
        numbered = {s: i for i, s in enumerate(sorted(set(signatures.values())))}
        refined = {q: numbered[signatures[q]] for q in states}
        rounds += 1
        old_partition = len(set(klass.values()))
        new_partition = len(numbered)
        assert new_partition >= old_partition
        if new_partition == old_partition:
            return new_partition, rounds
        klass = refined


def verify():
    trials = 0
    for n in range(17):
        for bits in product((0, 1), repeat=n):
            trials += 1
            count = direct_count(bits)
            for m in (2, 3, 4, 5, 7, 11):
                assert run(bits, m)[3] == count % m, (bits, m)
    print('direct-subsequence-comparisons:', trials * 6)

    reach_tests = 0
    for m in range(2, 31):
        states = reachable(m)
        expected = m**3 * gcd(m, 2)
        assert len(states) == expected, (m, len(states), expected)
        phases = {(a, b) for a, b, c, d in states}
        assert phases == {(t % m, comb(t, 2) % m) for t in range(2 * m)}
        assert all(sum(1 for q in states if q[:2] == phase) == m**2
                   for phase in phases)
        assert len({(q[3], run((1,), m, q)[3], run((1, 1), m, q)[3],
                     run((0, 1, 1), m, q)[3]) for q in states}) == len(states)
        reach_tests += 1
    print('all-modulus-reachability-and-distinguishability-tests:', reach_tests)

    construction_tests = 0
    for m in range(2, 12):
        W = (1,) * (m - 1) + (0, 0, 1) + (0,) * (2 * m - 2)
        for c, d, t in product(range(m), range(m), range(2 * m)):
            # Check the finite, explicit reaching words used in the proof.
            word = W + (1,) * d + W * ((c - 1) % m) + (0,) * t
            assert run(word, m) == (t % m, comb(t, 2) % m, c, d), (m, c, d, t)
            construction_tests += 1
    print('explicit-witness-comparisons:', construction_tests)

    minimizations = 0
    for m in range(2, 12):
        states = reachable(m)
        count, rounds = moore_classes(states, m)
        assert count == len(states) == m**3 * gcd(m, 2)
        minimizations += 1
    print('independent-Moore-partition-minimizations:', minimizations)
    print('PASS')


if __name__ == '__main__':
    verify()
