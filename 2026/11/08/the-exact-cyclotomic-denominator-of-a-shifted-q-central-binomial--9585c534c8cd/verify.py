#!/usr/bin/env python3
"""Reproducibility checks for the cyclotomic denominator classification.

Use: python3 verify.py . No non-standard Python packages required.
"""
from math import gcd
from fractions import Fraction


def divisor_order(n, k, j, d):
    """Multiplicative exponent of the d-th cyclotomic factor, by direct counting."""
    return (int(d == 1) - int((k * n + j) % d == 0)
            + sum(int(k*m % d == 0) + int((k*m+j) % d == 0)
                  - 2*int(m % d == 0) for m in range(1, n+1)))


def non_k_part(n, k, j):
    m = gcd(n, j)
    for p in range(2, m+1):
        if m % p == 0 and isprime(p) and k % p == 0:
            while m % p == 0:
                m //= p
    return m


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))


def predicted_exponent(n, k, j, d):
    if d == 1: return 0
    if gcd(d, k) == 1 and n % d == 0 and j % d == 0:
        return -1
    return 0


def polynomial_evaluation(n, k, j, q):
    r = Fraction(1-q, 1-q**(k*n+j))
    for m in range(1, n+1):
        r *= Fraction((1-q**(k*m)) * (1-q**(k*m+j)), (1-q**m)**2)
    return r


def factor_degree_and_values(n, k, j, q):
    # Formula \prod_d Phi_d(q)^e via recursive evaluation of cyclotomic polynomials.
    D = k*n+j
    phi = {}
    z = Fraction(1, 1)
    for d in range(1, D+1):
        v = q**d-1
        for a in range(1, d):
            if d % a == 0:
                v //= phi[a]
        phi[d] = v
        e = divisor_order(n, k, j, d)
        if e >= 0: z *= phi[d]**e
        else: z /= phi[d]**(-e)
    return z


def main():
    cases = 0
    zeros = 0
    negatives = 0
    for n in range(1, 21):
        for k in range(1, 16):
            for j in range(1, 16):
                c = non_k_part(n,k,j)
                bad = []
                for d in range(1, k*n+j+1):
                    e = divisor_order(n,k,j,d)
                    if e < 0:
                        bad.append((d, e))
                    assert e >= predicted_exponent(n,k,j,d), (n,k,j,d,e)
                    assert (e == -1) == (d>1 and gcd(d,k)==1
                                            and n%d==0 and j%d==0), (n,k,j,d,e)
                expect = [(d,-1) for d in range(2,c+1) if c % d == 0]
                assert bad == expect, (n,k,j,bad,expect)
                if c > 1: negatives += 1
                else: zeros += 1
                cases += 1
    # Independent rational-function evaluations for several crucial nontrivial examples.
    for n,k,j in [(4,2,4),(9,3,9),(3,2,3),(4,3,4),(12,2,12),(7,5,14),
                  (2,1,2),(1,1,7),(4,2,3),(8,4,8)]:
        for q in (2,3):
            assert polynomial_evaluation(n,k,j,q) == factor_degree_and_values(n,k,j,q)
    assert non_k_part(4,2,4)==1
    assert non_k_part(9,3,9)==1
    assert non_k_part(4,3,4)==4
    assert non_k_part(6,2,6)==3
    print('VERIFY_OK cases=%d d_levels=1..kn+j polynomial=%d nonpolynomial=%d' %
          (cases,zeros,negatives))
    print('negative_cyclotomic_exponents=exact_all_cases independent_rational_evaluations=20 PASS')
    print('counterfamilies n=j=p^a k=p for a>=2: proven symbolically in RESULT.md')


if __name__ == '__main__': main()
