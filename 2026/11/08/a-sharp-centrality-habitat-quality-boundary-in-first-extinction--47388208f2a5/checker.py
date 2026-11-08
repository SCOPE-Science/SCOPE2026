#!/usr/bin/env python3
"""Exact-rational verification for the three-patch two-species competition theorem.

Python 3 standard library only. This is an independent full-state check;
the proof for all positive real parameters is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

EDGES = ((0, 1), (1, 2))
STATES = tuple(s for s in product((0, 1, 2), repeat=3) if 1 in s and 2 in s)
INDEX = {s: j for j, s in enumerate(STATES)}


def solve(a, b):
    """Solve an exact linear system Ax=b by pivoted rational elimination."""
    n = len(b)
    t = [a[i][:] + [b[i]] for i in range(n)]
    for k in range(n):
        pivot = next((j for j in range(k, n) if t[j][k]), None)
        if pivot is None:
            raise ArithmeticError('singular transient system')
        t[k], t[pivot] = t[pivot], t[k]
        d = t[k][k]
        t[k] = [v / d for v in t[k]]
        for i in range(n):
            if i != k and t[i][k]:
                f = t[i][k]
                t[i] = [t[i][j] - f * t[k][j] for j in range(n + 1)]
    return [t[i][-1] for i in range(n)]


def full_state_prob(c, mu):
    n = len(STATES)
    m = [[F(0) for _ in range(n)] for _ in range(n)]
    rhs = [F(0) for _ in range(n)]

    def event(i, state, nxt, rate):
        m[i][i] += rate
        if nxt in INDEX:
            m[i][INDEX[nxt]] -= rate
        elif 1 in nxt and 2 not in nxt:
            rhs[i] += rate

    for i, state in enumerate(STATES):
        for v, typ in enumerate(state):
            if typ:
                nxt = state[:v] + (0,) + state[v + 1:]
                event(i, state, nxt, mu if v == 1 else F(1))
            else:
                for x, y in EDGES:
                    nb = y if x == v else x if y == v else None
                    if nb is not None and state[nb]:
                        nxt = state[:v] + (state[nb],) + state[v + 1:]
                        event(i, state, nxt, c)
    ans = solve(m, rhs)
    return {state: ans[i] for i, state in enumerate(STATES)}


def formula(c, mu):
    return (c + 2) * (mu + 2) / (2 * (mu + 1) * (c + mu + 2))


def main():
    rates = [F(1, 9), F(1, 3), F(1, 2), F(1), F(2), F(4), F(6), F(10), F(17)]
    mortalities = [F(1, 10), F(1, 2), F(1), F(5, 4), F(3, 2), F(2), F(3), F(5), F(11)]
    count = 0
    for c in rates:
        for mu in mortalities:
            val = full_state_prob(c, mu)
            p = formula(c, mu)
            # A center and B left, A left and B center, A and B on endpoints
            assert val[(2, 1, 0)] == p
            assert val[(1, 2, 0)] == 1 - p
            assert val[(1, 0, 2)] == F(1, 2)
            assert (p > F(1, 2)) == (c > (mu - 1) * (mu + 2))
            assert (p == F(1, 2)) == (c == (mu - 1) * (mu + 2))
            count += 1
    for c, mu, expected in [(F(1), F(2), F(2, 5)),
                             (F(4), F(2), F(1, 2)),
                             (F(6), F(2), F(8, 15))]:
        assert formula(c, mu) == expected
    print(f'PASS: {count} complete 12-state rational parameter pairs and 3 boundaries')

if __name__ == '__main__':
    main()
