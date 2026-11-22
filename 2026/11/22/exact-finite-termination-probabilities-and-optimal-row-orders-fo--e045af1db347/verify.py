#!/usr/bin/env python3
"""Finite checks for exact planar Kaczmarz row-ordering results.

The general statements are proved analytically in RESULT.md; this script
checks selected finite instances without claiming exhaustive infinite proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, cos, factorial, pi, sin


def matching_distribution(n):
    assert n >= 2 and n % 2 == 0
    m = n // 2
    binomial_moments = [Fraction(comb(m, j) * 2**j * factorial(n-j), factorial(n))
                        for j in range(m+1)]
    probabilities = []
    for k in range(m+1):
        probabilities.append(sum([(-1)**(j-k) * comb(j,k) * binomial_moments[j]
                                  for j in range(k,m+1)], Fraction(0)))
    assert sum(probabilities) == 1
    assert all(x >= 0 for x in probabilities)
    return probabilities


def orthogonal_pairs_in_order(perm):
    n = len(perm)
    if n % 2:
        return 0
    m = n // 2
    return sum(1 for a,b in zip(perm, perm[1:]) if (a-b)%n == m)


def squared_operator_norm(perm):
    n = len(perm)
    out = 1.0
    for a,b in zip(perm,perm[1:]):
        out *= cos(pi*(a-b)/n)**2
    return out


def main():
    assertions = 0
    for n in (2,4,6,8):
        exact = matching_distribution(n)
        observed = [0]*(n//2+1)
        for perm in permutations(range(n)):
            count = orthogonal_pairs_in_order(perm)
            observed[count] += 1
            assertions += 1
            value = squared_operator_norm(perm)
            assert (value < 1e-19) == (count > 0)
            assertions += 1
        assert [Fraction(x,factorial(n)) for x in observed] == exact
        assertions += 1
        if n>=4:
            probability = 1-exact[0]
            assert probability > 1-(Fraction(n-1,n))**(n-1)
            assertions += 1
        print(f'n={n} exact-termination probability {1-exact[0]} '
              f'({float(1-exact[0]):.10f}); iid {float(1-Fraction(n-1,n)**(n-1)):.10f}')

    for n in (3,5,7):
        observed_optimal=0
        target=sin(pi/(2*n))**(2*(n-1))
        for perm in permutations(range(n)):
            v=squared_operator_norm(perm)
            assertions+=1
            assert v >= target - 1e-12
            if abs(v-target)<1e-12:
                observed_optimal+=1
        assert observed_optimal==2*n
        assertions+=1
        print(f'n={n} optimal squared operator norm {target:.12g}; '
              f'number of optimal orders {observed_optimal}')

    # Confirm exact binomial moments by direct combinatorial enumeration.
    for n in (4,6,8):
        distribution=matching_distribution(n)
        for j in range(n//2+1):
            empirical=sum(comb(k,j)*distribution[k] for k in range(j,n//2+1))
            expected=Fraction(comb(n//2,j)*2**j*factorial(n-j),factorial(n))
            assert empirical==expected
            assertions+=1
    print('PASS',assertions,'finite checks')


if __name__=='__main__':
    main()
