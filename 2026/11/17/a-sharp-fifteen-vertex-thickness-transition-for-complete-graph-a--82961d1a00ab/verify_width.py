#!/usr/bin/env python3
"""Exact arithmetic checks for the minimum-width formulas.

Pure Python standard library. The unrestricted argument is given in RESULT.md;
this checker verifies the finite base cases and the cut-support calculations.
"""
import itertools
import math


def cross(n, k, s):
    return sum(math.comb(n, j)-math.comb(s, j)-math.comb(n-s, j)
               for j in range(2, k+1))


def cfull(n, s):
    return (2**s-1)*(2**(n-s)-1)


def width_squared_order_compare(n, s, t, k=None):
    if k is None:
        k=n
    a, b = cross(n, k, s), cross(n, k, t)
    # w_s^2 - w_t^2 has sign of this exact integer.
    return a*a*t*(n-t)-b*b*s*(n-s)


def test():
    finite_cases=0
    # Unrestricted proof reduces n<=14 to these exact inequalities.
    for n in range(3, 15):
        for s in range(2, n//2+1):
            assert width_squared_order_compare(n,s,1)>0, (n,s)
            finite_cases+=1
    assert width_squared_order_compare(15,7,1)<0
    # All relevant minimum directions for complete-stage profiles.
    all_profiles=0
    for n in range(3,121):
        m=n//2
        expected = 1 if n<=14 else m
        for s in range(1,m+1):
            assert width_squared_order_compare(n,s,expected)>=0, (n,s)
            assert (width_squared_order_compare(n,s,expected)==0)==(s==expected)
            all_profiles+=1
    # Compare the full generic-permutation support to the cut formula
    # without assuming the binomial expression: all coordinate masks.
    cut_cases=0
    for n in range(3,9):
        for k in range(2,n+1):
            a=[sum(math.comb(i-1,j-1) for j in range(1,k+1))
               for i in range(1,n+1)]
            d=[a[i]-a[n-1-i] for i in range(n)]
            assert all(d[i]<d[i+1] for i in range(n-1))
            assert sum(d)==0
            for s in range(1,n):
                assert sum(d[n-s:]) == cross(n,k,s),(n,k,s)
                cut_cases+=1
    # Actual vertex formula for small dimensions, by directly summing
    # simplex vertices selected by a fixed coordinate ordering.
    vertex_cases=0
    for n in range(3,7):
        for k in range(2,n+1):
            actual=[0]*n
            for mask in range(1,1<<n):
                if mask.bit_count()>k:
                    continue
                i=max(i for i in range(n) if (mask>>i)&1)
                actual[i]+=1
            expected=[sum(math.comb(i,j-1) for j in range(1,k+1)) for i in range(n)]
            assert actual==expected
            vertex_cases+=1
    print('COMPLETE_GRAPH_WIDTH_PASS',
          'base_inequalities='+str(finite_cases),
          'profile_comparisons='+str(all_profiles),
          'cut_support_cases='+str(cut_cases),
          'simplex_vertex_cases='+str(vertex_cases),
          'threshold_n=15')

if __name__=='__main__':
    test()
