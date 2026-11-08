#!/usr/bin/env python3
"""Exact finite cross-checks for a nested binomial identity on divisor chains.

The mathematical proof uses formal generating functions; this script only
checks finite instances using two independently implemented definitions.
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def recursive_divisors(a):
    if not any(a):
        return 1
    proper = (b for b in product(*(range(v+1) for v in a)) if b != a)
    return 1 + sum(recursive_divisors(b) for b in proper)

def nested_finite_sum(a):
    if not a:
        return 1
    states = {0: 1}
    for v in a[:-1]:
        nxt = {}
        for total, weight in states.items():
            for i in range(v+1):
                t = total + i
                nxt[t] = nxt.get(t, 0) + weight * comb(v, i) * comb(v+total, v)
        states = nxt
    b = a[-1]
    return (1 << b) * sum(weight*comb(b+total, b) for total, weight in states.items())

def coefficient_recurrence(a):
    # Direct consequence of (2 prod(1-x_i)-1)F=1, distinct from nested formula.
    @lru_cache(None)
    def inner(b):
        if not any(b):return 1
        ans=0
        for mask in product((0,1), repeat=len(b)):
            if not any(mask) or any(mask[j]>b[j] for j in range(len(b))):
                continue
            bnext=tuple(b[j]-mask[j] for j in range(len(b)))
            ans+=2*((-1)**(sum(mask)+1))*inner(bnext)
        return ans
    return inner(a)

count=0
for width, max_e in [(1, 12),(2, 8),(3, 5),(4, 4),(5, 3),(6, 2)]:
    tested=0
    for a in product(range(1, max_e+1), repeat=width):
        lhs=recursive_divisors(a)
        rhs=nested_finite_sum(a)
        gf=coefficient_recurrence(a)
        assert lhs==rhs==gf,(a,lhs,rhs,gf)
        tested+=1
    count+=tested
    print(f'width={width}, exponent_max={max_e}, cases={tested}: agreement')
for a in [(), (0,), (0,2,0), (2,0,1), (1,0,0,3), (0,2,3,0)]:
    assert recursive_divisors(a)==nested_finite_sum(a)==coefficient_recurrence(a)
print(f'positive-exponent comparisons={count}; zero-exponent/empty controls=6; all checks passed')
