#!/usr/bin/env python3
"""Finite exact checks for the resampled record-removal chain.

The asymptotic normal theorem requires the analytic proof in RESULT.md.
This self-contained script only checks finite transition laws, path identities,
and absorbing-time moments; it does not certify any infinite-limit assertion.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def records(seq):
    highest = -1
    count = 0
    for x in seq:
        if x > highest:
            highest = x
            count += 1
    return count


def unsigned_stirling(nmax):
    c = [[0] * (nmax+1) for _ in range(nmax+1)]
    c[0][0] = 1
    for n in range(1, nmax+1):
        for r in range(1,n+1):
            c[n][r] = c[n-1][r-1] + (n-1)*c[n-1][r]
    return c


def check():
    nmax=13
    c = unsigned_stirling(nmax)
    checks=0
    H=[F(0)]
    A=[F(0)]
    for m in range(1,nmax+1):
        H.append(H[-1]+F(1,m))
        A.append(A[-1]+1/H[m])
    mean=[F(0)]*(nmax+1)
    second=[F(0)]*(nmax+1)
    for m in range(1,nmax+1):
        probs=[F(c[m][r],factorial(m)) for r in range(1,m+1)]
        assert sum(probs)==1;checks+=1
        assert sum(probs[r-1]*r for r in range(1,m+1))==H[m];checks+=1
        var=sum(probs[r-1]*(F(r)-H[m])**2 for r in range(1,m+1))
        assert var==H[m]-sum(F(1,j*j) for j in range(1,m+1));checks+=1
        delta_mean=sum(probs[r-1]*(A[m]-A[m-r]-F(r)/H[m]) for r in range(1,m+1))
        assert delta_mean >=0;checks+=1
        # This identity is the exact finite-state compensated-potential relation.
        assert delta_mean==sum(probs[r-1]*(A[m]-A[m-r]) for r in range(1,m+1))-1;checks+=1
        mean[m]=1+sum(probs[r-1]*mean[m-r] for r in range(1,m+1))
        second[m]=1+sum(probs[r-1]*(2*mean[m-r]+second[m-r]) for r in range(1,m+1))
        assert 0<mean[m]<=A[m];checks+=1
        assert second[m]>=mean[m]**2;checks+=1
        if m<=7:
            freq=[0]*(m+1)
            for p in permutations(range(1,m+1)):
                freq[records(p)]+=1
            for r in range(1,m+1):
                assert freq[r]==c[m][r];checks+=1
        if m>1:
            assert mean[m]>mean[m-1];checks+=1
        # An independent recursion verifies potential-minus-mean drift debt.
        if m==1: debt=[F(0)]*(nmax+1)
        debt[m]=delta_mean+sum(probs[r-1]*debt[m-r] for r in range(1,m+1))
        assert A[m]-mean[m]==debt[m];checks+=1
    assert mean[2]==F(3,2);checks+=1
    assert second[2]==F(5,2);checks+=1
    print(f'PASS: {checks} exact rational / permutation assertions, m<= {nmax};')
    print('n, expectation, harmonic-potential, standard_deviation')
    for m in (2,4,8,13):
        print(m,float(mean[m]),float(A[m]),float(second[m]-mean[m]**2)**0.5)

if __name__=='__main__':check()
