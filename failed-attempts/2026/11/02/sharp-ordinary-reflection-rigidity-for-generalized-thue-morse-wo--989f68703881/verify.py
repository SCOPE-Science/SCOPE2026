#!/usr/bin/env python3
"""Finite, independent consistency checks for ordinary-reflection rigidity.

The infinite assertion is proved mathematically in RESULT.md; enumerating
prefixes is not a substitute for that proof.
"""
from math import gcd


def digit_sum(n, base):
    assert n >= 0 and base >= 2
    s = 0
    while n:
        s += n % base
        n //= base
    return s


def expected_r2(base, modulus):
    g = gcd(base-1, modulus)
    if g == 1:
        return modulus*(modulus+1)//2
    if g == 2:
        return modulus*modulus//4
    return modulus*modulus//g


def expected_pair_set(base, modulus):
    return {(a, (a+d) % modulus)
            for a in range(modulus)
            for d in range(modulus) if (d-1) % gcd(base-1,modulus) == 0}


def factor_sets(seq, length):
    return {tuple(seq[k:k+length]) for k in range(len(seq)-length+1)}


def reflection_classes(fs):
    return {min(w, w[::-1]) for w in fs}


def explicit_pair_witness(base, modulus, a, d):
    # The digits of L are exactly s ones; therefore s_b(L)=s.
    q = modulus // gcd(modulus,base-1)
    for h in range(q):
        if (1-(base-1)*h-d) % modulus == 0:
            s = (a-(base-1)*h) % modulus
            L = sum(base**j for j in range(s))
            n = base**h * (base*L+1) - 1
            return n
    raise AssertionError("No witness for claimed pair")


def run():
    c = 0
    for b in range(2,11):
        for m in range(3,11):
            expected = expected_pair_set(b,m)
            assert len(expected) == m*m//gcd(m,b-1)
            assert len(reflection_classes(expected)) == expected_r2(b,m)
            c += 2
            for a,d2 in expected:
                k=explicit_pair_witness(b,m,a,(d2-a)%m)
                assert (digit_sum(k,b)%m,digit_sum(k+1,b)%m)==(a,d2)
                c+=1

    # Independent direct digit expansion and uniform-morphism constructions.
    for b in range(2,8):
        for m in range(3,9):
            seq = [digit_sum(i,b)%m for i in range(18000)]
            W = [0]
            while len(W) < 18000:
                W = [(a+j)%m for a in W for j in range(b)]
            assert seq == W[:18000]
            c += 1
            for size in range(3,13):
                fs = factor_sets(seq,size)
                assert len(fs) == len(reflection_classes(fs))
                assert all(w == w[::-1] or w[::-1] not in fs for w in fs)
                c+=2
            fs2 = factor_sets(seq,2)
            assert fs2.issubset(expected_pair_set(b,m))
            # For length two, exact witness construction above establishes
            # every possible pair without relying on a finite prefix.
            c += 1

    # Sharpness: ordinary binary Thue-Morse has a reversed, nonpalindromic pair.
    s=[digit_sum(i,2)%2 for i in range(4096)]
    f3=factor_sets(s,3)
    assert any(w != w[::-1] and w[::-1] in f3 for w in f3)
    c+=1
    print('VERIFY_OK',c,'finite assertions')


if __name__ == '__main__':
    run()
