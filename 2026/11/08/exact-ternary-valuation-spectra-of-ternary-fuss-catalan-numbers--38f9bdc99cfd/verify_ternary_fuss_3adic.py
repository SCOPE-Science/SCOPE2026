#!/usr/bin/env python3
"""Computational checks of ternary Fuss--Catalan 3-adic valuation polynomials."""
from collections import Counter
from math import comb
from fractions import Fraction

def digit_sum_3(x):
    s = 0
    while x:
        s += x % 3
        x //= 3
    return s

def val_3(x):
    if x == 0:
        raise ValueError('undefined at zero')
    v=0
    while x % 3 == 0:
        v += 1
        x //= 3
    return v

def v_factorial_3(n):
    v=0
    while n:
        n//=3
        v+=n
    return v

def v_fuss_direct(n):
    return (v_factorial_3(3*n)-v_factorial_3(n)-v_factorial_3(2*n)-val_3(2*n+1))

def v_fuss_digits(n):
    j=val_3(2*n+1)
    a=((2*n+1)//(3**j)-1)//2
    return digit_sum_3(2*a)//2

def recurrence_rows(levels):
    A=[1]
    B=[2,1]
    yield A
    yield B
    for r in range(2,levels+1):
        C=[0]*(r+1)
        for j,b in enumerate(B):
            C[j] += 2*b
            C[j+1] += 2*b
        for j,b in enumerate(A):
            C[j]-=b
            C[j+1]-=b
            C[j+2]-=b
        yield C
        A,B=B,C

if __name__ == '__main__':
    rows=list(recurrence_rows(9))
    total=0
    for r in range(10):
        hist=Counter()
        for n in range(3**r):
            v=v_fuss_direct(n)
            assert v==v_fuss_digits(n),(r,n,v,v_fuss_digits(n))
            hist[v]+=1
            total+=1
        expected=rows[r]
        assert [hist[j] for j in range(r+1)] == expected,(r,expected,hist)
        assert len(hist)==r+1 and min(hist)==0 and max(hist)==r
        assert sum(expected)==3**r and expected[0]==r+1 and expected[-1]==1
        assert sum(j*expected[j] for j in range(r+1))*4 == (2*r-1)*3**r+1
        mean = Fraction(sum(j*expected[j] for j in range(r+1)),3**r)
        second = Fraction(sum(j*j*expected[j] for j in range(r+1)),3**r)
        assert mean == Fraction(r,2)-Fraction(1,4)+Fraction(1,4*3**r)
        assert second - mean**2 == Fraction(r,6)+Fraction(1,16)-Fraction(1,16*3**(2*r))
    for n in range(150):
        c=comb(3*n,n)//(2*n+1)
        assert c*(2*n+1)==comb(3*n,n)
        assert val_3(c)==v_fuss_direct(n)
    print('VERIFY_OK levels=0..9 individual_index_checks=%d direct_large_binomials=150 recurrence=PASS digit_formula=PASS exact_mean_variance=PASS' % total)
    for r in range(7): print('P_%d:'%r, rows[r])
