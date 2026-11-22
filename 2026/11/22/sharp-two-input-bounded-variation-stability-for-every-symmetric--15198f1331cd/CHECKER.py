#!/usr/bin/env python3
"""Finite, reproducible checks for sharp variation amplification by sliding trimmed means.

All assertions here are supplemental to the analytical proof in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
import random


def clamped_window(x, i, r):
    n = len(x)
    return [x[min(n - 1, max(0, i + h))] for h in range(-r, r + 1)]


def trimmed_filter(x, r, q):
    w = 2 * r + 1
    k = w - 2 * q
    assert r >= 1 and 0 <= q <= r and len(x) >= 2
    return [sum(sorted(clamped_window(x, i, r))[q:w-q], x[0]*0) / k
            for i in range(len(x))]


def variation(x):
    return sum(abs(x[i+1] - x[i]) for i in range(len(x)-1))


def sharp_example(r, q, extra=0):
    w = 2*r+1
    k = w-2*q
    # Even values first, then odd values; one jump at the half-path cut.
    base = [Fraction(2*j) for j in range(r+1)] + [Fraction(2*j+1) for j in range(r+1)]
    base += [base[-1]] * extra
    step = [Fraction(int(i >= r+1)) for i in range(len(base))]
    eps = Fraction(1, 19)
    other = [a + eps*b for a,b in zip(base, step)]
    fa = trimmed_filter(base, r, q)
    fb = trimmed_filter(other, r, q)
    delta = [b-a for a,b in zip(fa, fb)]
    assert variation(delta) == Fraction(w, k) * eps
    assert variation(step) == 1
    return [int(d/eps*k) for d in delta[:w+1]]


def formula_counts(r,q):
    k=2*r+1-2*q
    t=r-q+1
    left=[i if i<=t else t-((i-t)%2) for i in range(r+1)]
    return left + [k-c for c in reversed(left)]


def run():
    for r in range(1,31):
        for q in range(r+1):
            actual=sharp_example(r,q)
            expected=formula_counts(r,q)
            assert actual == expected, (r,q,actual,expected)
            assert all(abs(b-a)==1 for a,b in zip(actual,actual[1:]))
            if r<=10:
                assert sharp_example(r,q,extra=3)==expected
    print('EXACT_SHARP_ALL_RADII_1_TO_30_AND_TRIM_LEVELS_PASS')

    # Each neighboring pair of clamped windows shares w-1 labeled occurrences.
    # The two middle-k selectors must share the central k-1 common occurrences.
    for r in range(1,7):
        w=2*r+1
        common=list(range(0,2*w,2))[:w-1]
        for q in range(r+1):
            k=w-2*q
            forced=set(common[q:w-q-1])
            assert len(forced)==k-1
            for a in range(-2,2*w+2):
                selected=set(sorted(common+[a])[q:w-q])
                assert forced.issubset(selected)
    print('COMMON_CORE_ORDER_STATISTIC_LEMMA_PASS')

    for r in (1,2):
        w=2*r+1
        n=w+1
        for p in permutations(range(n)):
            x=[Fraction(z) for z in p]
            for q in range(r+1):
                k=w-2*q
                fx=trimmed_filter(x,r,q)
                for j in range(1,n):
                    v=[Fraction(int(i>=j)) for i in range(n)]
                    eps=Fraction(1,31)
                    fy=trimmed_filter([z+eps*vv for z,vv in zip(x,v)],r,q)
                    assert variation([b-a for a,b in zip(fx,fy)]) <= Fraction(w,k)*eps
    print('EXHAUSTIVE_SMALL_RANK_CHAMBERS_AND_SINGLE_JUMP_CHECKS_PASS')

    rng=random.Random(724313)
    for trial in range(1500):
        r=rng.randrange(1,8)
        q=rng.randrange(r+1)
        n=rng.randrange(2,5*r+8)
        x=[rng.uniform(-5,5) for _ in range(n)]
        y=[rng.uniform(-5,5) for _ in range(n)]
        outx=trimmed_filter(x,r,q)
        outy=trimmed_filter(y,r,q)
        d=[a-b for a,b in zip(x,y)]
        od=[a-b for a,b in zip(outx,outy)]
        assert variation(od) <= (2*r+1)/(2*r+1-2*q) * variation(d) + 1e-8
    print('RANDOM_TWO_INPUT_VARIATION_STRESS_PASS_1500')
    print('ALL_TRIMMED_MEAN_VARIATION_CHECKS_PASS')

if __name__ == '__main__':
    run()
