#!/usr/bin/env python3
"""Standalone finite regression for exact Fourier-moment criteria of one-phase cubic sphere designs.
All-dimensional correctness rests on the accompanying analytic proof, not on finite testing.
"""
from itertools import combinations, product
from fractions import Fraction
from math import gcd


def is_sum_free(a):
    s=set(a)
    return len(s)==len(a) and all(x+y not in s for x in s for y in s)

def moment_character(w):
    d=len(w)
    for degree in range(1,4):
        for slots in product(range(2*d),repeat=degree):
            # z_j mapped to frequency +w_j; conjugate to -w_j
            freq=sum((1 if z<d else -1)*w[z%d] for z in slots)
            # balanced only when degree=2, one z_j and its conjugate
            target=Fraction(1,d) if degree==2 and slots[0]%d==slots[1]%d and (slots[0]<d)!=(slots[1]<d) else Fraction(0)
            if freq==0 and target==0:
                return False, (degree,slots,freq)
            if freq!=0 and target!=0:
                return False, (degree,slots,freq)
    return True,None

def test():
    samples=0
    for d in (3,4):
        for w in product(range(-7,8),repeat=d):
            if 0 in w or gcd(*w)!=1: continue
            actual,_=moment_character(w)
            expected=is_sum_free(tuple(abs(q) for q in w))
            assert actual==expected,(w,actual,expected)
            samples+=1
    assert is_sum_free((1,3,5,7,9,11))
    for n in range(1,6):
        for A in combinations(range(1,17),n):
            if is_sum_free(A):
                assert all(x>=2*j-1 for j,x in enumerate(A,1))
                assert sum(x*x for x in A)>=n*(4*n*n-1)//3
    print(f'PASS: {samples} signed primitive winding vectors in d=3,4; all sum-free sets of size 1..5 in [1,16] checked; odd-frequency equality examples.')
if __name__=='__main__':test()
