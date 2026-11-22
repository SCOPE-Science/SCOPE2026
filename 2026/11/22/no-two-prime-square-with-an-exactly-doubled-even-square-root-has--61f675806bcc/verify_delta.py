#!/usr/bin/env python3
"""Exact finite diagnostic for factor-pair differences in the stated family."""
from math import isqrt

def primes_through(n):
    return [a for a in range(2,n+1) if all(a % d for d in range(2,isqrt(a)+1))]

def differences(q,b):
    N=2*q**b
    n=N*N
    
    if q == 2:
        divisors=[2**j for j in range(1,2*b+3)]
    else:
        divisors=[(2**i)*(q**j) for i in range(3) for j in range(2*b+1)]
    return [n//d-d for d in sorted(set(divisors)) if 1<d<N and n%d==0]

def has_delta(q,b):
    vals=sorted(differences(q,b), reverse=True)
    for i, a in enumerate(vals):
        for j in range(i+1,len(vals)):
            v=vals[j]
            if a-v in vals[j:]: return True
    return False

def main():
    test_count=0
    for q in primes_through(37):
        for b in range(1,11):
            assert not has_delta(q,b), (q,b)
            test_count+=1
    for b in range(1,101):
        M=3**(2*b)
        B=2*M-2
        C=M-4
        assert B-C==M+2
        assert B-2*C==6
    print('DELTA_TWO_PRIME_ROOT_EXACT_CHECK_OK',test_count,100)

if __name__=='__main__': main()
