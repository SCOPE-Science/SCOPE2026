#!/usr/bin/env python3
"""Independent, exact checks of finite consequences of the palindrome theorem.

Only Python 3 standard library is used. This does not replace the proof.
"""
from collections import Counter


def coefficient(m, j):
    assert 0 <= j < m
    numerator = (1 << j) + (1 << (2*m-1-j))
    assert numerator % 3 == 0
    return numerator // 3


def coefficient_mod(m, j, k):
    # Return coefficient modulo 3^(k-1) without constructing huge powers of 2.
    modulus = 3**k
    numerator = (pow(2, j, modulus) + pow(2, 2*m-1-j, modulus)) % modulus
    assert numerator % 3 == 0
    return numerator // 3


def predicted_hist(m):
    count = 1 << (m-1)
    z = m // 3
    if m % 3 == 1:
        return ((count-2**z)//3, (count+2**(z+1))//3, (count-2**z)//3)
    return ((count+2**z)//3, (count-2**(z+1))//3, (count+2**z)//3)


def v3(n):
    s = 0
    while n % 3 == 0:
        n //= 3
        s += 1
    return s


def test_histograms():
    total = 0
    for m in range(1, 18):
        weights = [coefficient(m, j) for j in range(m)]
        observed = [0, 0, 0]
        # Gray-code enumeration is independent of the root-of-unity proof.
        for mask in range(1 << (m-1)):
            palindrome_quotient = weights[0] + sum(weights[j] for j in range(1,m) if mask & (1 << (j-1)))
            observed[palindrome_quotient % 3] += 1
        assert tuple(observed) == predicted_hist(m), (m, observed, predicted_hist(m))
        assert sum(observed) == 1 << (m-1)
        total += 1 << (m-1)
    print('PASS: exact modulo-nine counts, half-lengths 1..17,', total, 'binary palindromes')


def test_coefficients():
    tests = 0
    for m in range(1, 76):
        for j in range(m):
            w = coefficient(m, j)
            assert w % 3 == ((-1)**j * (2*m-1-2*j)) % 3
            assert v3(w) == v3(2*m-1-2*j)
            tests += 1
    print('PASS: exact coefficient congruence and ternary valuation,', tests, 'pairs')


def test_all_lifts():
    total_targets = 0
    for k in range(2, 8):
        m = (5 * 3**(k-2) + 3) // 2
        q = 3**(k-1)
        powers = [3**ell for ell in range(k)]
        pairs = []
        used = set()
        for ell in range(k-1):
            indices = [(2*m-1 - c*3**ell)//2 for c in (1,5)]
            assert all(j >= 1 and j < m for j in indices)
            assert all((2*m-1-2*j) in (3**ell,5*3**ell) for j in indices)
            assert not used.intersection(indices)
            used.update(indices)
            ww = [coefficient_mod(m,j,k) for j in indices]
            assert all(v3(w)==ell for w in ww)
            pairs.append(ww)
        baseline = coefficient_mod(m,0,k)
        for target in range(q):
            attained = baseline
            for ell,(a,b) in enumerate(pairs):
                mod = powers[ell+1]
                solutions = [(x,y) for x in (0,1) for y in (0,1) if (attained+x*a+y*b-target)%mod == 0]
                assert solutions, (k,m,target,ell)
                x,y = solutions[0]
                attained = (attained + x*a + y*b) % q
            assert attained == target,(k,m,target,attained)
            total_targets += 1
        print('PASS: every ternary target at exponent',k,'with',m,'half-digits,',q,'targets')
    print('PASS: explicit, digit-by-digit constructive witnesses for',total_targets,'target residues')


def main():
    test_histograms()
    test_coefficients()
    test_all_lifts()
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
