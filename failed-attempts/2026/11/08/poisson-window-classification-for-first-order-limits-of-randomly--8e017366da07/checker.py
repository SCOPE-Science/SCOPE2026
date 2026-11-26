#!/usr/bin/env python3
"""Finite consistency checks for colored equivalence-class Poisson-window theorem.

All checks are finite and supplementary to the mathematical proof.
"""
from math import comb, exp, factorial, log
from itertools import product
from collections import Counter


def profile(bits, b, q):
    counts = Counter()
    for start in range(0, len(bits), b):
        red = sum(bits[start:start+b])
        counts[(min(red, q), min(b-red, q))] += 1
    return tuple(sorted((key, min(q, val)) for key, val in counts.items()))


def game_equivalent(a, b, size, block, rank):
    """Independent full q-round EF recursion on two fixed partitions."""
    def related(x, y):
        return x//block == y//block
    def partial_ok(xs, ys):
        for i in range(len(xs)):
            if a[xs[i]] != b[ys[i]]:
                return False
            for j in range(len(xs)):
                if (xs[i] == xs[j]) != (ys[i] == ys[j]):
                    return False
                if related(xs[i],xs[j]) != related(ys[i],ys[j]):
                    return False
        return True
    def ef(xs, ys, left):
        if not partial_ok(xs,ys):
            return False
        if left == 0:
            return True
        return (
            all(any(ef(xs+(x,), ys+(y,), left-1) for y in range(size))
                for x in range(size))
            and all(any(ef(xs+(x,), ys+(y,), left-1) for x in range(size))
                for y in range(size))
        )
    return ef((), (), rank)


def test_profile_vs_game():
    # Exhaustively sample all 4-vertex blocks with two classes at rank 2;
    # compare a representative of each profile against selected others.
    b, m, q = 4, 2, 2
    groups={}
    for bits in product((0,1), repeat=b*m):
        groups.setdefault(profile(bits,b,q),[]).append(bits)
    comparisons=0
    for members in groups.values():
        representatives=[members[0], members[len(members)//2], members[-1]]
        for u in representatives[1:]:
            assert game_equivalent(representatives[0],u,b*m,b,q)
            comparisons+=1
    assert len(groups)>3
    return len(groups),comparisons


def test_exact_binomial_and_independence():
    # A two-color block has complementary tails; disjoint for b>2k.
    for b in range(5,15):
        for k in range(0,min(4,(b-1)//2)+1):
            p = comb(b,k)/2**b
            assert p*2 <= 1
            for m in (1,2,3,5,10):
                # Prob(exactly j all-red-like blocks and l all-blue-like blocks)
                for j,l in ((0,0),(1,0),(0,1),(1,1),(2,1)):
                    if j+l>m:continue
                    multinomial = factorial(m)//(factorial(j)*factorial(l)*factorial(m-j-l))
                    direct = multinomial * p**(j+l) * (1-2*p)**(m-j-l)
                    # Sum all possible arrangements of two disjoint category types.
                    total=0.0
                    for inds in product((0,1,2),repeat=m):
                        if inds.count(1)==j and inds.count(2)==l:
                            total+=p**(j+l)*(1-2*p)**(m-j-l)
                    assert abs(direct-total)<1e-11
    # Sequences m(b) round(0.7 / p_k(b)) cross a Poisson window.
    c=0.7
    for k in (0,1,2):
        for b in (30,40,50):
            p=comb(b,k)/2**b
            m=round(c/p)
            theta=1-(1-p)**m
            assert abs(theta-(1-exp(-c)))<2e-5
            jointzero=(1-2*p)**m
            assert abs(jointzero-exp(-2*c))<2e-5
    return True

if __name__ == '__main__':
    groups,compare=test_profile_vs_game()
    assert test_exact_binomial_and_independence()
    print('ALL_CHECKS_OK', 'q2_profiles=',groups,'EF_same_profile_cases=',compare)
