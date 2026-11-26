#!/usr/bin/env python3
"""Elementary reproducibility checks for the stated spectral asymptotic.
No external packages are required; finite examples do not prove the limit.
"""
import math
from fractions import Fraction


def r(m, d, n):
    return math.exp(math.lgamma((n+d+1)/m)-math.lgamma((n+d)/m)-math.log(n+d))


def eigen(m, d, n, j):
    assert n >= 0 and 0 <= j <= n
    return (j+1)*r(m,d,n) - (j*r(m,d,n-1) if j else 0.0)


def model(m, d, n, j):
    q=(m-1)/m
    return m**(-1/m)*n**(-q)*(1-q*j/n)


def run():
    for m,d in [(2.0,2),(1.5,3),(3.0,2)]:
        n=2000
        errs=[]
        for j in (0,n//2,n):
            e=eigen(m,d,n,j)
            assert e>0
            errs.append(abs(e/model(m,d,n,j)-1))
        assert max(errs)<0.003, (m,d,errs)
        print('shell',m,d,'max_relative_error',max(errs))
    avg=sum(Fraction(math.comb(4,k)*(-1)**k, (k+1)*2**k) for k in range(5))
    assert avg==Fraction(31,80)
    C=Fraction(1,8)*avg
    assert C==Fraction(31,640)
    print('exact_C_2_2=',C)

if __name__=='__main__':
    run()
