#!/usr/bin/env python3
"""Exact arithmetic checks for the projective degrees of the reduced incidence stratum.
No external packages are required. Finite checks corroborate the symbolic intersection-theory proof.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, comb


def complete_homogeneous(weights, bound):
    values = [0] * (bound + 1)
    values[0] = 1
    for weight in weights:
        for j in range(1, bound + 1):
            values[j] += weight * values[j-1]
    return values


def fixed_points(N, rank):
    for I in combinations(range(N), rank):
        complement = [j for j in range(N) if j not in I]
        euler = 1
        for i in I:
            for j in complement:
                euler *= j - i
        yield I, euler


def via_incidence_bundle(p, n):
    assert 1 <= p <= n-2
    r, N = p+2, n+1
    dimension_base = r*(N-r)
    dimension = dimension_base + 2*(r-1)
    factorials = [factorial(j) for j in range(dimension+1)]
    result = Fraction(0)
    for I, euler in fixed_points(N, r):
        h = complete_homogeneous(I, dimension_base)
        s = sum(I)
        total = 0
        for i in range(dimension_base+1):
            for j in range(dimension_base+1-i):
                z = dimension_base-i-j
                multinomial = factorials[dimension] // (
                    factorials[r-1+i]*factorials[r-1+j]*factorials[z]
                )
                total += multinomial*h[i]*h[j]*(-2*s)**z
        result += Fraction(total, 2*euler)
    assert result.denominator == 1 and result > 0
    return int(result)


def determinant_integer(matrix):
    size = len(matrix)
    total = 0
    for perm in permutations(range(size)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(size) for j in range(i+1, size))
        term = -1 if inversions % 2 else 1
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def via_degeneracy_locus(p, n):
    """Independent Thom-Porteous integral on Gr(p+1,n+1)^2."""
    assert 1 <= p <= n-2
    k, N = p+1, n+1
    c = N-k-1
    dimension = 2*k*(N-k) - p*c
    fixed = list(fixed_points(N, k))
    total = Fraction(0)
    for A, ea in fixed:
        for B, eb in fixed:
            h = complete_homogeneous(A+B, c+p)
            def chern(j):
                if j < 0 or j > c+p:
                    return 0
                return (-1)**j*h[j]
            porteous = determinant_integer([
                [chern(c+i-j) for j in range(p)] for i in range(p)
            ])
            # The Pluecker hyperplane class is minus the sum of roots of S.
            H = -sum(A)-sum(B)
            total += Fraction(H**dimension*porteous, 2*ea*eb)
    assert total.denominator == 1 and total > 0
    return int(total)


def line_pair_binomial(n):
    """Closed ballot-number formula when p=1."""
    assert n >= 3
    a = n-1
    c = a-1
    D = 3*a+1
    def tableaux(i):
        first = comb(2*a-i, a-i)
        second = comb(2*a-i, a+1) if a+1 <= 2*a-i else 0
        return first-second
    numerator = sum(comb(D, 2*a-i)*tableaux(i)*tableaux(c-i)
                    for i in range(c+1))
    assert numerator % 2 == 0
    return numerator//2


def main():
    expected = {
        (1, 3): 140,
        (1, 4): 6300, (2, 4): 6300,
        (1, 5): 288288, (2, 5): 4036032, (3, 5): 288288,
        (1, 6): 13453440, (2, 6): 2744501760,
        (1, 7): 638516736,
    }
    count = 0
    for n in range(3, 8):
        results = {}
        for p in range(1, n-1):
            a = via_incidence_bundle(p, n)
            b = via_degeneracy_locus(p, n)
            assert a == b, (p, n, a, b)
            if p == 1:
                assert a == line_pair_binomial(n)
            if (p, n) in expected:
                assert a == expected[p, n]
            results[p] = a
            count += 1
        for p, a in results.items():
            assert results[n-p-1] == a, (n, p)
    print('TWO_INDEPENDENT_INTERSECTION_DEGREE_FORMULAS_OK', count)
    print('DUALITY_AND_LINE_PAIR_BINOMIAL_FORMULAS_OK')
    print('CHECK_OK')

if __name__ == '__main__':
    main()
