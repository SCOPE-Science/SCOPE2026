#!/usr/bin/env python3
"""Exact integer checks for the rational-slope gcd block theorem.

This checker verifies finite test ranges. The unrestricted statements follow
from the accompanying unimodular-change-of-coordinates proof.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm
from random import Random


def totient(n):
    if n < 1:
        raise ValueError("positive argument required")
    out = n
    d = 2
    while d * d <= n:
        if n % d == 0:
            while n % d == 0:
                n //= d
            out -= out // d
        d += 1
    if n > 1:
        out -= out // n
    return out


def theoretical_block(q, block):
    L = lcm(*range(1, q))
    out = Counter({d: 1 for d in range(block * L + 1, (block + 1) * L + 1)})
    for d in range(1, q):
        expected = sum(Fraction(L * totient(j), d * j)
                       for j in range(1, (q - 1) // d + 1))
        assert expected.denominator == 1, (q, d, expected)
        out[d] += expected.numerator
    return L, out


def direct_block(p, q, L, block):
    return Counter(gcd(n, (p*n)//q)
                   for n in range(block * q * L + 1, (block + 1) * q * L + 1))


def check_blocks():
    cases = 0
    for q in range(2, 12):
        for B in (0, 1, 2):
            L, predicted = theoretical_block(q, B)
            assert sum(predicted.values()) == q * L
            for p in range(1, 2*q + 2):
                if gcd(p, q) != 1:
                    continue
                actual = direct_block(p, q, L, B)
                assert actual == predicted, (p,q,B,L,actual,predicted)
                cases += 1
    return cases


def egcd(a,b):
    if b == 0:
        return a, 1, 0
    g,x,y = egcd(b,a%b)
    return g,y,x-(a//b)*y


def check_coordinates():
    rng = Random(20261105)
    cases = 0
    for q in range(2, 700):
        for _ in range(5):
            p = rng.randrange(1, 9*q+1)
            if gcd(p,q) != 1:
                continue
            g,U,V = egcd(q,p)
            assert g == 1 and U*q+V*p == 1
            r = rng.randrange(q)
            k = rng.randrange(0, 10000)
            t,s = divmod(p*r, q)
            assert gcd(q*k+r, p*k+t) == gcd(k+U*r+V*t, s)
            cases += 1
    return cases


def check_probability():
    for q in range(2, 100):
        values = [Fraction(1, d*q) * sum((Fraction(totient(j),j)
                  for j in range(1, (q - 1)//d+1)), Fraction(0))
                  for d in range(1,q)]
        assert sum(values, Fraction(0)) == Fraction(q-1, q)
    return 98


def main():
    a = check_blocks()
    b = check_coordinates()
    c = check_probability()
    print(f"EXACT_BLOCK_HISTOGRAMS_OK cases={a} q=2..11 blocks=0,1,2")
    print(f"UNIMODULAR_GCD_IDENTITY_OK cases={b} q=2..699")
    print(f"MASS_IDENTITY_OK cases={c} q=2..99")
    print("SAMPLE q=5 L=12 block=0 p=2 or 3: d=1 count=33 d=2 count=10 d=3 count=5 d=4 count=4")
    print("VERIFY_OK arithmetic=exact finite_checks_do_not_replace_general_proof=true")

if __name__ == '__main__':
    main()
