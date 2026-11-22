#!/usr/bin/env python3
"""Exact finite checks for equal-modulus four-term Fourier zero spectra.

Independent from the antipodal-pair proof: sums in Q(i,zeta_p) are
represented by Gaussian-integer coefficient arrays modulo Phi_p.
This tests finite instances, not the all-prime theorem.
"""
from itertools import product
from random import Random


def phase_pair(k):
    return ((1,0),(0,1),(-1,0),(0,-1))[k % 4]


def is_zero_exact(terms, p):
    # terms=(i_exponent, zeta_exponent) for four unit complex phases.
    coeff = [[0, 0] for _ in range(p)]
    for k, j in terms:
        a,b = phase_pair(k)
        coeff[j % p][0] += a
        coeff[j % p][1] += b
    # The minimal polynomial of zeta_p is 1+...+T^(p-1).
    return all(v == coeff[0] for v in coeff)


def predicted_count(alpha, p):
    matches=((0,1,2,3),(0,2,1,3),(0,3,1,2))
    m=0
    for a,b,c,d in matches:
        def opp(i,j):
            # alpha_i / alpha_j is a negative pth root iff i exponents differ by 2 mod 4.
            return (alpha[i][0] - alpha[j][0]) % 4 == 2
        if opp(a,b) and opp(c,d):
            m+=1
    assert m<=2
    return (0,p,2*p-1)[m]


def count_zero_direct(alpha,p):
    z=0
    for x,y,w in product(range(p),repeat=3):
        terms=[alpha[0]]
        for i,t in enumerate((x,y,w),1):
            k,j=alpha[i]
            terms.append((k,(j+t)%p))
        z += is_zero_exact(terms,p)
    return z


def main():
    checks=0
    rng=Random(316159)
    for p in (5,7,11):
        # Exhaust the four-sign alphabet with arbitrary pth-root offsets
        # after normalizing the first coefficient to 1, for p=5,7.
        if p<=7:
            for triple in product(product((0,2),range(p)),repeat=3):
                alpha=((0,0),)+triple
                actual=count_zero_direct(alpha,p)
                expected=predicted_count(alpha,p)
                assert actual==expected,(p,alpha,actual,expected)
                checks+=1
        # Exhaust independent quarter-turn phases at root-offset zero.
        for ks in product(range(4),repeat=4):
            alpha=tuple((k,0) for k in ks)
            actual=count_zero_direct(alpha,p)
            expected=predicted_count(alpha,p)
            assert actual==expected,(p,alpha,actual,expected)
            checks+=1
        for _ in range(250):
            alpha=tuple((rng.randrange(4),rng.randrange(p)) for _ in range(4))
            actual=count_zero_direct(alpha,p)
            expected=predicted_count(alpha,p)
            assert actual==expected,(p,alpha,actual,expected)
            checks+=1
        assert count_zero_direct(((0,0),(2,0),(1,0),(3,0)),p)==p
        assert count_zero_direct(((0,0),(0,0),(2,0),(2,0)),p)==2*p-1
        assert count_zero_direct(((0,0),(0,0),(0,0),(0,0)),p)==0
        checks+=3
    print('FINITE_CYCLOTOMIC_CHECKS_PASS',checks)


if __name__=='__main__':
    main()
