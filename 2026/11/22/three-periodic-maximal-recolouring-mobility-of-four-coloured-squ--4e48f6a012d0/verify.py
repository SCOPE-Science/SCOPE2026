#!/usr/bin/env python3
"""Exact reproducibility checks for the recolouring mobility theorem.

Python 3 standard library; no network, no external packages.  The unrestricted
claim is proved in RESULT.md; bounded enumeration checks the implementations.
"""
from itertools import product, permutations
from collections import Counter
from math import comb

IDENTITY = (0, 1, 2, 3)

def step(t, b):
    assert b in (0, 1)
    if b == 0:
        return (t[1], t[2], t[0], t[3])
    return (t[1], t[2], t[3], t[0])

def returns(bits):
    t = IDENTITY
    for b in bits:
        t = step(t, b)
    return t == IDENTITY

def degree_bits(bits):
    return sum(bits[i] == 0 and bits[(i + 1) % len(bits)] == 0
               for i in range(len(bits)))

def degree_coloring(w):
    n = len(w)
    return sum(3 == len({w[(i+j) % n] for j in (-2, -1, 1, 2)}) + 1
               for i in range(n))

def direct_distribution(n):
    # Exploit global colour symmetry: fix the first three symbols to 0,1,2.
    # All valid named colourings are obtained from these by 24 palette permutations.
    out = Counter()
    def visit(w):
        i = len(w)
        if i == n:
            if w[-1] in (w[0], w[1]) or w[-2] == w[0]:
                return
            out[degree_coloring(w)] += 24
            return
        for x in range(4):
            if x not in (w[-1], w[-2]):
                visit(w + (x,))
    visit((0, 1, 2))
    return out

def binary_distribution(n):
    out = Counter()
    for b in product((0, 1), repeat=n):
        if returns(b):
            out[degree_bits(b)] += 24
    return out

def transfer_distribution(n):
    # Direct weighted trace of the 48-state return/switch transfer.
    states = [(p, previous) for p in permutations(range(4))
              for previous in (0, 1)]
    total = Counter()
    for root in states:
        dp = {(root, 0): 1}
        for _ in range(n):
            next_dp = {}
            for ((perm, old), degree), multiplicity in dp.items():
                for bit in (0, 1):
                    to = (step(perm, bit), bit)
                    key = (to, degree + (old == bit == 0))
                    next_dp[key] = next_dp.get(key, 0) + multiplicity
            dp = next_dp
        for ((state, degree), count) in dp.items():
            if state == root:
                total[degree] += count
    return total

def max_formula(n):
    assert n >= 6
    if n % 3 == 0:
        return n, 24
    if n % 3 == 1:
        return n - 5, 24*n
    h = (n - 2) // 3
    # Count using integers after summing two rational contributions:
    exact4 = n * comb(h + 1, 3)
    exact6 = 2*n*(h - 1)
    assert (exact4 + exact6) % 4 == 0
    extremal_binary = (exact4 + exact6)//4 + (n == 8)
    return n - 8, 24*extremal_binary

def identity_gaps(gaps):
    t = IDENTITY
    for z in gaps:
        t = step(t, 1)
        for _ in range(z):
            t = step(t, 0)
    return t == IDENTITY

def small_word_table():
    # Replacing a positive gap a by 1+((a-1) mod 3) preserves both
    # positivity and the product since the return step has order three.
    for z in product(range(4), repeat=2):
        assert identity_gaps(z) == (z == (2, 2))
    for z in product(range(4), repeat=4):
        r = sum(x > 0 for x in z)
        residue = (4 + sum(z)) % 3
        if r <= 3:
            assert not (identity_gaps(z) and residue == 2)
        elif residue == 2 and identity_gaps(z):
            assert z == (1, 1, 1, 1)
    for a in range(1, 6):
        for u, v in product((1, 2, 3), repeat=2):
            t = IDENTITY
            for b in (1,)*a + (0,)*u + (1,)*(6-a) + (0,)*v:
                t = step(t, b)
            if t == IDENTITY and (6+u+v) % 3 == 2:
                assert (a, u, v) == (3, 1, 1)
    assert returns((1,)*8)


def main():
    small_word_table()
    for n in range(6, 16):
        a = direct_distribution(n)
        b = binary_distribution(n)
        assert a == b, (n, a, b)
        if n <= 12:
            assert transfer_distribution(n) == a, (n, transfer_distribution(n), a)
        m, count = max_formula(n)
        assert max(a) == m and a[m] == count, (n, m, count, a)
        print('length=%2d  colorings=%6d  max_degree=%2d  maximizers=%5d' %
              (n, sum(a.values()), m, count))
    for n in range(16, 19):
        b = binary_distribution(n)
        m, count = max_formula(n)
        assert max(b) == m and b[m] == count, (n, m, count, b)
    print('VERIFY_OK group_relations=checked finite_gap_table=checked '
          'transfer_orders=6..12 direct_coloring_orders=6..15 binary_products_orders=6..18 '
          'extremal_counts=6..18')

if __name__ == '__main__':
    main()
