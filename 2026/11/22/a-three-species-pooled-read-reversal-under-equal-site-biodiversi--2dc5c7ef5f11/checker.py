#!/usr/bin/env python3
"""Exact-arithmetic checks for the finite-read biodiversity sampling theorem.
This is supplementary verification; the stated analytical identities prove the theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, log


def complete_probability(probabilities, reads):
    # Exact enumeration of every ordered read sequence, without fitted parameters.
    ans = F(0)
    for seq in product(range(3), repeat=reads):
        if set(seq) == {0, 1, 2}:
            term = F(1)
            for i in seq:
                term *= probabilities[i]
            ans += term
    return ans


def split_probability(p, q, k, total=4):
    ans = F(0)
    for seq in product(range(3), repeat=total):
        if set(seq) == {0, 1, 2}:
            term = F(1)
            for i in seq[:k]:
                term *= p[i]
            for i in seq[k:]:
                term *= q[i]
            ans += term
    return ans


def test():
    checks = 0
    for den in range(3, 24):
        for ia in range(1, den-1):
            for ib in range(1, den-ia):
                ic = den-ia-ib
                a, b, c = F(ia, den), F(ib, den), F(ic, den)
                p, q = [a, b, c], [F(1), F(0), F(0)]
                mix = [(x+y)/2 for x, y in zip(p, q)]
                split = split_probability(p, q, 2)
                pool = complete_probability(mix, 4)
                assert split == 2*b*c
                assert pool == F(3, 2)*(1+a)*b*c
                assert pool - split == (3*a-1)*b*c/2
                assert (pool > split) == (a > F(1, 3))
                assert (pool == split) == (a == F(1, 3))
                assert split_probability(p,q,3) == 3*(1+a)*b*c
                assert split_probability(p,q,3) > pool
                assert complete_probability(mix,3) == F(3,4)*(1+a)*b*c
                assert complete_probability(mix,3) < split_probability(p,q,2,total=3)
                assert complete_probability(mix,2) == 0
                # Marginal detection: E (2+2) strictly dominates P (4 pooled).
                for s in range(3):
                    missE = (1-p[s])**2*(1-q[s])**2
                    missP = (1-mix[s])**4
                    assert missE < missP
                # Pooling equals a Binomial mixture over deterministic allocations.
                combination = sum(F(comb(4,k),16)*split_probability(p,q,k) for k in range(5))
                assert combination == pool
                checks += 1
    a, b, c = F(3,5), F(1,5), F(1,5)
    assert split_probability([a,b,c],[F(1),F(0),F(0)],2) == F(2,25)
    assert complete_probability([(1+a)/2,b/2,c/2],4) == F(12,125)
    assert split_probability([a,b,c],[F(1),F(0),F(0)],3) == F(24,125)
    # Rigorous sufficient bound for eventual reversal of the initial pooling advantage.
    s = min(b,c)
    ratio = ((1-s/2)**2)/(1-s)
    n=70
    assert ratio**n > 2
    miss_pool_lower = (1-s/2)**(2*n)
    miss_separate_upper = 2*(1-s)**n
    assert miss_pool_lower > miss_separate_upper
    print('PASS: %d exact rational community cases; all complete-inventory, marginal, threshold, mixture, and asymptotic-bound checks.' % checks)

if __name__ == '__main__':
    test()
