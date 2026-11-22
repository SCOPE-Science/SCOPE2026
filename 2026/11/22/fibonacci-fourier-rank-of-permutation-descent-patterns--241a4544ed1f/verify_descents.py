#!/usr/bin/env python3
"""Independent exact-integer verification of descent-pattern Fourier factorization.

Run: python3 verify_descents.py
No nonstandard dependencies. This is finite corroboration, not an infinite proof.
"""
from itertools import permutations
from math import factorial
from fractions import Fraction
from collections import Counter

def descent_mask(p):
    return sum((p[i] > p[i+1]) << i for i in range(len(p)-1))

def tangent_factor(l):
    # Signed Eulerian polynomial at -1, evaluated by exact enumeration.
    r = sum((-1)**descent_mask(p).bit_count() for p in permutations(range(l+1)))
    return Fraction(r,factorial(l+1))

def even_runs(mask,n):
    lengths = []
    j=0
    while j<n-1:
        if mask & (1<<j):
            start=j
            while j<n-1 and mask&(1<<j): j+=1
            lengths.append(j-start)
        else:j+=1
    return lengths

def fwht(v):
    h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                a,b=v[j],v[j+h]
                v[j],v[j+h]=a+b,a-b
        h*=2

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def main():
    factors={l:tangent_factor(l) for l in range(1,9)}
    assert all(factors[l]==0 for l in range(1,9,2))
    assert {l:int(factors[l]*factorial(l+1)) for l in (2,4,6,8)} == {2:-2,4:16,6:-272,8:7936}
    tests=0
    for n in range(2,10):
        f=[0]*(1<<(n-1))
        for p in permutations(range(n)):
            f[descent_mask(p)]+=1
        fwht(f)
        nonzero=0
        for mask,observed in enumerate(f):
            ls=even_runs(mask,n)
            product=Fraction(factorial(n))
            for l in ls:
                product*=factors[l]
            assert product.denominator==1
            assert observed==product.numerator, (n,mask,observed,product)
            assert (observed!=0)==all(l%2==0 for l in ls), (n,mask)
            nonzero+=observed!=0
            tests+=1
        assert nonzero==fib(n), (n,nonzero)
        print('PASS n=%d rank=%d nullity=%d' %(n,nonzero,len(f)-nonzero))
    print('PASS Fourier coefficient comparisons:',tests)

if __name__=='__main__': main()
