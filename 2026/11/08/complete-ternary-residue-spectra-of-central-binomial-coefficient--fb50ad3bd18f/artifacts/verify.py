#!/usr/bin/env python3
"""Pure-integer checks for ternary central-binomial residue spectra.

The infinite theorem uses Lucas' theorem and an explicit infinite family
of ternary-digit witnesses. This program verifies the witness mechanism
for a finite range of moduli and offsets; finite tests are not a proof
of statements over unbounded moduli and indices.
"""
from math import comb, gcd


def lucas_central_mod3(k):
    assert k >= 0
    ones = 0
    while k:
        digit = k % 3
        if digit == 2:
            return 0
        ones += digit
        k //= 3
    return (-1) ** ones % 3


def order_three(b):
    assert b > 0 and b % 3
    t = 1
    while pow(3,t,b) != 1 % b:
        t += 1
        assert t < 2*b+1
    return t


def make_witness(b, beta, target):
    assert target in (0,1,2) and gcd(b,3)==1
    period = order_three(b)
    wanted = beta % b
    if target:
        count = next(m for m in range(1,2*b+4)
                     if m % b == wanted and (-1)**m % 3 == target)
        k = sum(pow(3,period*j) for j in range(1,count+1))
    else:
        count = next(m for m in range(1,b+3) if (m+2)%b == wanted)
        k = sum(pow(3,period*j) for j in range(1,count+1))
        k += 2*pow(3,period*(count+1))
    assert k % b == wanted
    # Multiplying by 3^(period*h) for large h preserves the progression
    # and makes the corresponding n positive and arbitrarily large.
    while k <= b + beta:
        k *= pow(3,period)
    assert (k-beta)%b == 0 and (k-beta)//b >= 1
    assert lucas_central_mod3(k) == target, (b,beta,target,k)
    # A second, independent digit check on 2k via Lucas' theorem.
    lower, upper, value = k, 2*k, 1
    while lower or upper:
        lo, hi = lower%3, upper%3
        value = value * (comb(hi,lo) if lo<=hi else 0) % 3
        lower//=3; upper//=3
    assert value == target
    return k


def expected(b,beta):
    if b%2:
        return {0,1,2}
    return {0, 1 if beta%2 == 0 else 2}


if __name__ == '__main__':
    witness_count=0
    for b in range(1,41):
        if b%3 == 0:
            continue
        for beta in range(-b,b+1):
            for val in expected(b,beta):
                make_witness(b,beta,val)
                witness_count+=1
            for n in range(1,60):
                k=b*n+beta
                if k>=0:
                    assert lucas_central_mod3(k) in expected(b,beta)
    for k in range(0,100):
        assert lucas_central_mod3(k) == comb(2*k,k)%3
    print('VERIFY_OK witness_classes='+str(witness_count)+' moduli=1..40_coprime_to_3 offsets=-b..b direct_central=0..99')
