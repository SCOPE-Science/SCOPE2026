#!/usr/bin/env python3
"""Reproduce optimal two-window syndrome coverage and three-window covering for extended binary Hamming codes."""
from itertools import permutations

def mulx(a, poly, m):
    a <<= 1
    if a & (1 << m):
        a ^= poly
    return a

def primitive_polynomial(m):
    N = (1 << m) - 1
    for poly in range((1 << m)|1, 1 << (m + 1), 2):
        v, powers, seen = 1, [], set()
        for _ in range(N):
            if v == 0 or v in seen:
                break
            powers.append(v)
            seen.add(v)
            v = mulx(v, poly, m)
        if len(powers) == N and v == 1:
            return poly, powers
    raise AssertionError(f'No primitive polynomial degree {m}')

def syndromes_from_windows(vectors, b, cyclic=False):
    n = len(vectors)
    got = {0}
    for start in range(n if cyclic else n - b + 1):
        chunk = [vectors[(start+i) % n] for i in range(b)]
        for mask in range(1, 1 << b):
            val = 0
            for i in range(b):
                if mask >> i & 1: val ^= chunk[i]
            got.add(val)
    return got

def verify(m):
    n = 1 << m
    poly, powers = primitive_polynomial(m)
    x = [0] + powers
    assert len(set(x)) == n
    columns = [(1 << m) | value for value in x]
    for cyclic in (False, True):
        two = syndromes_from_windows(columns, 2, cyclic)
        three = syndromes_from_windows(columns, 3, cyclic)
        assert len(two) == (1 << (m+1)) - 1, (m, cyclic, len(two))
        assert len(three) == 1 << (m+1), (m, cyclic, len(three))
        miss = set(range(1 << (m+1))) - two
        assert len(miss) == 1
        u = (powers[-1] ^ 1)
        assert miss == {u}, (m, poly, miss, u)
    return m, poly, len(two), len(three)

if __name__ == '__main__':
    for m in range(2, 12):
        print('degree,polynomial,2-window,3-window:', verify(m))
    # Exhaustively confirm lower bound independently at the first nontrivial size.
    n=8
    best_noncyclic = 0
    best_cyclic = 0
    attaining = 0
    for p in permutations(range(n)):
        col=[8|i for i in p]
        covered = {0, *col, *(col[i]^col[i+1] for i in range(n-1))}
        count=len(covered)
        if count>best_noncyclic: best_noncyclic=count
        if count==15: attaining+=1
        cyc_count=len(covered | {col[-1]^col[0]})
        if cyc_count > best_cyclic: best_cyclic=cyc_count
    assert best_noncyclic==15 and best_cyclic==15
    print('EXHAUSTIVE_m3:', 40320, 'best_noncyclic',best_noncyclic, 'best_cyclic',best_cyclic, 'attaining_noncyclic',attaining)
    print('CHECK_OK')
