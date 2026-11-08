#!/usr/bin/env python3
"""Independent finite checks of the two-run antisquare spectrum."""
from itertools import product


def predicted_count(a: int, b: int, k: int) -> int:
    s, t = sorted((a, b))
    if s == t:
        if k < s:
            return 2
        return 2*s if k >= s and (k-s) % (2*s) == 0 else 0
    if k < s:
        return 2
    if k == s:
        return s+1
    if k == t:
        return max(0, 2*s-t+1)
    return 0


def direct_count(a: int, b: int, k: int) -> tuple[int, int]:
    period = '0'*a + '1'*b
    p = len(period)
    # One full set of starting phases; enough characters for each full factor.
    source = period*((2*k+p-1)//p+2)
    words = set()
    valid_phases = 0
    for i in range(p):
        u = source[i:i+k]
        v = source[i+k:i+2*k]
        if all(c != d for c,d in zip(u,v)):
            valid_phases += 1
            words.add(u+v)
    return valid_phases, len(words)


def mismatch_count(a: int, b: int, k: int) -> int:
    period = '0'*a + '1'*b
    p = len(period)
    mismatch = [period[j] != period[(j+k)%p] for j in range(p)]
    return sum(all(mismatch[(i+j)%p] for j in range(k)) for i in range(p))


def test() -> None:
    checks = 0
    finite_totals = 0
    for a,b in product(range(1,23),repeat=2):
        p = a+b
        for k in range(1,4*p+1):
            phases, distinct = direct_count(a,b,k)
            via_mismatch = mismatch_count(a,b,k)
            expected = predicted_count(a,b,k)
            assert phases == distinct == via_mismatch == expected, (a,b,k,phases,distinct,via_mismatch,expected)
            checks += 1
        s,t=sorted((a,b))
        if s<t:
            total_formula = 3*s-1+max(0,2*s-t+1)
            total_direct = sum(direct_count(a,b,k)[1] for k in range(1,p+1))
            assert total_formula == total_direct
            finite_totals += 1
    print(f'PASS: {checks} (a,b,k) triples; direct distinct factors, phase comparisons, and independent mismatch conditions all agree with the theorem.')
    print(f'PASS: {finite_totals} unequal-run total-count checks (full possible order range).')
    print('PASS: both run lengths covered 1..22; antisquare orders covered 1..4(a+b) for every pair.')

if __name__=='__main__':
    test()
