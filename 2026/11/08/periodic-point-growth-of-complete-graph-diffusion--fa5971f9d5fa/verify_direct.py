#!/usr/bin/env python3
"""Independent labelled-state verification of normalized periodic-point counts.
Only finite tests; the mathematical proof provides the all-size assertion.
"""
from itertools import product
from math import factorial

def step(state):
    return tuple(x + sum((y > x) - (y < x) for j, y in enumerate(state) if j != i)
                 for i, x in enumerate(state))

def weak_compositions(n):
    if n == 0:
        yield ()
        return
    for k in range(1, n + 1):
        for rest in weak_compositions(n - k):
            yield (k,) + rest

def formula(n):
    result = 0
    for groups in weak_compositions(n):
        term = factorial(n)
        for a in groups:
            term //= factorial(a)
        for a,b in zip(groups, groups[1:]):
            term *= a+b-1
        result += term
    return result

def adjacent_test(state):
    levels = sorted(set(state))
    counts = [state.count(k) for k in levels]
    return all(levels[i+1]-levels[i] <= counts[i]+counts[i+1]-1
               for i in range(len(levels)-1))

for n in range(1, 6):
    bound=2*n  # >= proven maximum span 2n-3 for n>=2
    periodic=0
    fixed=0
    tested=0
    for state in product(range(bound+1), repeat=n):
        if min(state) != 0: continue
        tested += 1
        s1=step(state)
        s2=step(s1)
        is_periodic = (s2 == state)
        assert is_periodic == adjacent_test(state), (n,state,s1,s2)
        if is_periodic:periodic += 1
        if s1 == state: fixed += 1
    assert periodic == formula(n), (n,periodic,formula(n))
    assert fixed == 1, (n,fixed)
    assert (periodic - 1) % 2 == 0
    print(f'n={n} tested_normalized={tested} fixed={fixed} primitive2={periodic-1} count={periodic} orbits={(periodic-1)//2}')
print('DIRECT_OK')
