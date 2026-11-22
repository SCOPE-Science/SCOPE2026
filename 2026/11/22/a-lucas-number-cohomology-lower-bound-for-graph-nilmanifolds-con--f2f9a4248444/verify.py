#!/usr/bin/env python3
"""Exact integer certificate for the cyclic weight-Euler lower bound.
Run with: python3 verify.py  (Python standard library only).
This checks the finite-state identity; it does not assert equality with total Betti numbers.
"""
from collections import defaultdict

M = (
    (1, 0, 0, 0),
    (1, -1, 1, 0),
    (0, -1, 1, -1),
    (0, 0, 0, -1),
)
IDENTITY = (1, 0, 0, 1)


def multiply(a, b):
    a00, a01, a10, a11 = a
    b00, b01, b10, b11 = b
    return (a00*b00+a01*b10, a00*b01+a01*b11,
            a10*b00+a11*b10, a10*b01+a11*b11)


def states_and_transitions():
    states = [IDENTITY]
    index = {IDENTITY: 0}
    k = 0
    while k < len(states):
        a = states[k]
        for b in M:
            p = multiply(a, b)
            if p not in index:
                index[p] = len(states)
                states.append(p)
        k += 1
    transitions = [[index[multiply(a, b)] for b in M] for a in states]
    return states, transitions


def apply(transitions, v):
    return [sum(v[j] for j in js) for js in transitions]


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def bound(n):
    assert n >= 1
    correction = 2**n - 4 * (-1)**n
    assert correction % 3 == 0
    return (2**n)*lucas(n) + correction//3


def brute_euler(n):
    # Independent of the matrix product: count exterior-algebra monomials.
    euler = defaultdict(int)
    for vertices in range(1 << n):
        for edges in range(1 << n):
            w = [(vertices >> i) & 1 for i in range(n)]
            for i in range(n):
                if (edges >> i) & 1:
                    w[i] += 1
                    w[(i+1) % n] += 1
            parity = (vertices.bit_count() + edges.bit_count()) % 2
            euler[tuple(w)] += -1 if parity else 1
    return sum(abs(v) for v in euler.values())


def main():
    states, transitions = states_and_transitions()
    assert len(states) == len(set(states)) == 25
    assert all(max(abs(x) for x in a) <= 1 for a in states)
    assert all(len(js) == 4 for js in transitions)
    v0 = [abs(a[0] + a[3]) for a in states]
    v1 = apply(transitions, v0)
    v2 = apply(transitions, v1)
    v3 = apply(transitions, v2)
    v4 = apply(transitions, v3)
    remainder = [v4[i] - 3*v3[i] - 4*v2[i] + 8*v1[i] + 8*v0[i]
                 for i in range(25)]
    # T*(T^4 - 3*T^3 - 4*T^2 + 8*T + 8*I)*q=0,
    # hence the scalar recurrence holds for all n>=1.
    assert apply(transitions, remainder) == [0]*25
    print('MONOID_STATES', len(states))
    print('ANNIHILATOR_CHECK', 'PASS')
    v = v0
    values = []
    for n in range(1, 19):
        v = apply(transitions, v)
        total = v[0]  # start product at identity
        assert total == bound(n), (n, total, bound(n))
        values.append(total)
    assert values[:4] == [4, 12, 36, 116]
    print('CLOSED_FORM_CHECK', 'PASS', 'n=1..18')
    for n in range(3, 7):
        b = brute_euler(n)
        assert b == bound(n), (n,b,bound(n))
    print('DIRECT_EXTERIOR_MONOMIAL_CHECK', 'PASS', 'n=3..6')
    print('LOWER_BOUND_VALUES', [(n, bound(n)) for n in range(3, 12)])
    print('VERIFIED_LOWER_BOUND_CERTIFICATE_OK')


if __name__ == '__main__':
    main()
