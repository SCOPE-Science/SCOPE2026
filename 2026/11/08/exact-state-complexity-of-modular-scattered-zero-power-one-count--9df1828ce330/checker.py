#!/usr/bin/env python3
"""Finite reproducibility tests for modular scattered-zero-power/one languages.

The mathematical proof, not these bounded checks, establishes the infinite theorem.
No third-party modules are required.
"""
from collections import deque
from itertools import product
from math import comb


def factor(n):
    p = 2
    fs = {}
    while p * p <= n:
        while n % p == 0:
            fs[p] = fs.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        fs[n] = fs.get(n, 0) + 1
    return fs


def period(d, m):
    result = 1
    for prime, a in factor(m).items():
        h = 0
        while prime ** (h + 1) <= d:
            h += 1
        result *= prime ** (a + h)
    return result


def choose(n, d):
    return comb(n, d) if n >= d else 0


def min_state_count(d, m, r=0):
    """Independent partition refinement, with no precomputed equivalence classes."""
    P = period(d, m)
    N = P * m
    f = [choose(z, d) % m for z in range(P)]
    transitions = []
    for z in range(P):
        for c in range(m):
            transitions.append((((z+1) % P)*m+c, z*m+(c+f[z]) % m))
    blocks = [frozenset(i for i in range(N) if i % m == r),
              frozenset(i for i in range(N) if i % m != r)]
    blocks = [b for b in blocks if b]
    work = list(blocks)
    while work:
        pivot = work.pop()
        for letter in (0, 1):
            x = {i for i in range(N) if transitions[i][letter] in pivot}
            updated = []
            for block in blocks:
                left = block.intersection(x)
                right = block.difference(x)
                if not left or not right:
                    updated.append(block)
                    continue
                left, right = frozenset(left), frozenset(right)
                updated.extend((left, right))
                if block in work:
                    work.remove(block)
                    work.extend((left, right))
                else:
                    work.append(left if len(left) <= len(right) else right)
            blocks = updated
    return len(blocks)


def direct_count(word, d):
    total = zeros = 0
    for symbol in word:
        if symbol == '0':
            zeros += 1
        else:
            total += choose(zeros, d)
    return total


def run_dfa(word, d, m):
    P = period(d, m)
    z = c = 0
    for symbol in word:
        if symbol == '0':
            z = (z + 1) % P
        else:
            c = (c + choose(z, d)) % m
    return c


def verify():
    periods = 0
    minimized = 0
    residues = 0
    words = 0
    for d in range(1, 10):
        for m in range(2, 15):
            P = period(d, m)
            assert all((choose(n+P, d)-choose(n, d)) % m == 0
                       for n in range(P + d + 1))
            # Check no positive smaller period in a sufficient direct window.
            for t in range(1, P):
                if t > 150:
                    break
                assert any((choose(n+t,d)-choose(n,d)) % m != 0
                           for n in range(d + P + 1))
            periods += 1
            if P*m <= 330:
                for r in range(min(m, 3)):
                    assert min_state_count(d, m, r) == P*m
                    minimized += 1
    for d in range(1, 6):
        for m in range(2, 9):
            P = period(d, m)
            for z in range(P):
                Z = z + P * max(0, (d-z+P-1)//P)
                for c in range(m):
                    word = '0'*d + '1'*c + '0'*(Z-d)
                    assert run_dfa(word,d,m) == c
                    residues += 1
    for n in range(13):
        for x in product('01', repeat=n):
            w = ''.join(x)
            for d in range(1, 6):
                for m in (2, 3, 4, 6):
                    assert run_dfa(w,d,m) == direct_count(w,d) % m
                    words += 1
    print('VERIFIED period_cases=%d minimized_cases=%d reachable_states=%d direct_word_checks=%d'
          % (periods, minimized, residues, words))


if __name__ == '__main__':
    verify()
