"""Exact arithmetic checks for the sharp species-accumulation crossover threshold.

Uses only Python's standard library. The universal proof is in RESULT.md;
finite checks here validate its numerical and algebraic witness data.
"""
from fractions import Fraction
from itertools import combinations_with_replacement

A = (1, 5, 5, 11)
B = (2, 2, 9, 9)
N = 22
OBS = {2: -2, 5: 57720, 12: -285614243977922}

def expected_formula(weights, n):
    d = sum(weights)
    return Fraction(len(weights) * d**n - sum((d - x)**n for x in weights), d**n)

def expected_independent_dp(weights, n):
    # Each integer-weighted ordered sequence contributes the product of its weights.
    d = sum(weights)
    states = {0: 1}
    for _ in range(n):
        new = {}
        for mask, count in states.items():
            for i, weight in enumerate(weights):
                nxt = mask | (1 << i)
                new[nxt] = new.get(nxt, 0) + count * weight
        states = new
    assert sum(states.values()) == d**n
    return Fraction(sum(mask.bit_count() * count for mask, count in states.items()), d**n)

def delta_n(n):
    return sum((N-x)**n for x in B) - sum((N-x)**n for x in A)

def main():
    assert sum(A) == sum(B) == N
    for n, want in OBS.items():
        actual = delta_n(n)
        assert actual == want, (n, actual, want)
        d1 = expected_formula(A, n) - expected_formula(B, n)
        d2 = expected_independent_dp(A, n) - expected_independent_dp(B, n)
        assert d1 == d2 == Fraction(want, N**n), (n,d1,d2)
        assert abs(d1) > Fraction(2*n, 10000)
    assert [OBS[n] > 0 for n in (2,5,12)] == [False,True,False]

    tested = 0
    # Supplementary finite sanity: all positive sorted ternary integer profiles
    # through denominator 14, all distinct pairs, 2..18 draws.
    for total in range(3, 15):
        profiles = [(a,b,total-a-b) for a in range(1,total)
                    for b in range(a,total) if b <= total-a-b]
        for p,q in combinations_with_replacement(profiles,2):
            if p == q:
                continue
            signs = []
            for n in range(2,19):
                d = sum((total-x)**n for x in q) - sum((total-x)**n for x in p)
                if d:
                    signs.append(1 if d > 0 else -1)
            assert sum(x != y for x,y in zip(signs, signs[1:])) <= 1
            tested += 1
    print('PASS: exact four-species values, independent seen-set DP, extension margins')
    print('PASS: supplementary ternary lattice checks, profile pairs:', tested)

if __name__ == '__main__':
    main()
