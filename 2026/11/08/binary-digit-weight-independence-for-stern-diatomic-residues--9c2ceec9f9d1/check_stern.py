#!/usr/bin/env python3
"""Finite-state and direct checks of modular Stern--digit-weight independence.

This program verifies finite test instances; the general theorem requires
an algebraic transitivity argument and Perron--Frobenius convergence.
"""
from collections import Counter, deque
from math import gcd


def primitive_states(modulus, digit_modulus):
    return {(a, b, t) for a in range(modulus)
            for b in range(modulus) for t in range(digit_modulus)
            if gcd(a, b, modulus) == 1}


def child_states(state, modulus, digit_modulus):
    a, b, t = state
    return ((a, (a + b) % modulus, t),
            ((a + b) % modulus, b, (t + 1) % digit_modulus))


def test_case(m, h, max_level=9):
    states = primitive_states(m, h)
    start = (1 % m, 1 % m, 1 % h)
    seen, todo = {start}, deque([start])
    while todo:
        v = todo.popleft()
        for w in child_states(v, m, h):
            if w not in seen:
                assert w in states
                seen.add(w)
                todo.append(w)
    assert seen == states, (m, h, len(seen), len(states))
    assert (0, 1 % m, 0) in states
    assert child_states((0, 1 % m, 0), m, h)[0] == (0, 1 % m, 0)

    # Dynamically generate an entire binary level via the two-child rule.
    measure = Counter({start: 1})
    s = [0] * ((1 << (max_level + 1)) + 2)
    s[1] = 1
    for n in range(2, len(s)):
        if n & 1:
            s[n] = s[n // 2] + s[n // 2 + 1]
        else:
            s[n] = s[n // 2]

    for level in range(max_level + 1):
        independent = Counter((s[n] % m, s[n + 1] % m,
                               n.bit_count() % h)
                              for n in range(1 << level, 1 << (level + 1)))
        assert measure == independent, (m, h, level)
        assert sum(measure.values()) == 2 ** level
        next_measure = Counter()
        for state, mult in measure.items():
            left, right = child_states(state, m, h)
            next_measure[left] += mult
            next_measure[right] += mult
        measure = next_measure
    return len(states)


def main():
    cases = 0
    for m in range(2, 13):
        for h in range(2, 7):
            size = test_case(m, h)
            cases += 1
            print(f"m={m} h={h} states={size} levels=0..9: PASS")
    print(f"Total: {cases} modulus pairs, reachability and independent Stern checks: PASS")


if __name__ == '__main__':
    main()
