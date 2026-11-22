#!/usr/bin/env python3
"""Exact arithmetic and independent cut enumeration for period-two chip firing.
Run: python3 verify_formula.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def no_reciprocal(k, ell, a, b):
    return sum((-1)**r * comb(k, r) * comb(ell, r) * factorial(r)
               * b**(k-r) * a**(ell-r) for r in range(min(k, ell)+1))


def rook_formula(n):
    m = n*(n-1)//2
    ans = Fraction(0)
    for a in range(n+1):
        b = n-a
        subtotal = Fraction(0)
        for k in range(a+1):
            for ell in range(b+1):
                h = no_reciprocal(k, ell, a, b)
                assert h >= 0
                subtotal += Fraction(comb(a,k)*comb(b,ell) *
                    (a-1)**(a-k)*(b-1)**(b-ell)*h, 2**(k+ell))
        ans += comb(n,a)*subtotal
    ans *= 2**(m-1)
    assert ans.denominator == 1
    return int(ans)


def direct_cut_count(n):
    original_edges = list(combinations(range(n), 2))
    size = n + len(original_edges)
    adj = [0]*size
    for j,(u,v) in enumerate(original_edges):
        z=n+j
        for w in (u,v):
            adj[w] |= 1<<z
            adj[z] |= 1<<w
    weighted_states=0
    for mask in range(1<<size):
        prod=1
        for i in range(size):
            opposites = (adj[i] & (mask if not(mask>>i)&1 else (~mask))).bit_count()
            prod *= opposites
            if not prod:
                break
        weighted_states += prod
    assert weighted_states % 2 == 0
    return weighted_states//2


def brute_reciprocal(k, ell, a, b):
    # Selected vertices indexed by 0..k-1 on the first shore and 0..ell-1 on the second.
    from itertools import product
    count=0
    for choices_a in product(range(b), repeat=k):
        for choices_b in product(range(a), repeat=ell):
            if all(choices_b[j] != i for i,j in enumerate(choices_a) if j<ell):
                count+=1
    return count


def run():
    for a in range(1,4):
        for b in range(1,4):
            for k in range(a+1):
                for ell in range(b+1):
                    assert no_reciprocal(k,ell,a,b)==brute_reciprocal(k,ell,a,b), (a,b,k,ell)
    expected={3:100,4:12312,5:3759616,6:2764042240,7:4765773791232,8:18876597230632960}
    for n in range(3,9):
        exact=rook_formula(n)
        assert exact==expected[n], (n, exact, expected[n])
        if n<=5:
            assert direct_cut_count(n)==exact, (n,exact)
        print(f'n={n} period_two_orbits={exact}')
    print('FORMULA_AND_CUT_CHECKS_PASSED')

if __name__=='__main__':
    run()
