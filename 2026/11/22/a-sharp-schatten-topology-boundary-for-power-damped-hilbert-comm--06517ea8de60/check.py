#!/usr/bin/env python3
"""Finite diagnostics for the Hilbert commutator's trace-ideal boundary.

The infinite-dimensional statements require the analytical arguments.
This file uses only the Python standard library.
"""
import math


def kernel(m, n, s):
    return (m**(-s)-n**(-s))/(m+n-1)


def predicted_lower(s):
    delta=(5/4)**(-s)-(7/4)**(-s)
    return 2**(-2*s)*delta/(8*(1-2**(-s)))


def run():
    count=0
    for s in (0.02,0.1,0.3,1.0,2.0):
        for k in range(2,8):
            b=2**k
            aa=range(b,5*b//4)
            bb=range(7*b//4,2*b)
            assert len(aa)==len(bb)==b//4
            v=(sum(kernel(m,n,s) for m in aa for n in bb))/(b//4)
            delta=(5/4)**(-s)-(7/4)**(-s)
            assert v >= b**(-s)*delta/16-1e-13
            count+=1
        for m in range(1,38):
            for n in range(1,38):
                assert abs(kernel(m,n,s)+kernel(n,m,s)) < 1e-15
                count+=1
        hsq=sum(kernel(m,n,s)**2 for m in range(1,401) for n in range(1,401))
        upper=23*s*s*math.log(2)**2/(1-2**(-2*s))
        assert hsq <= upper+1e-13
        count+=1
        assert predicted_lower(s)>0
        count+=1
    theoretical=math.log(7/5)/(8*math.log(2))
    for s in (0.0001,0.0003,0.001,0.003):
        assert abs(predicted_lower(s)-theoretical)<0.003
        count+=1
    print('PASS:',count,'finite skewness, block, trace-lower-bound and HS-upper-bound checks')
    print('rigorous nuclear endpoint lower bound',theoretical)


if __name__ == '__main__':
    run()
