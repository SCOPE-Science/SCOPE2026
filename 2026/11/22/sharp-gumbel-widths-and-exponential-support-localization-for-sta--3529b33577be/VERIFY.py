#!/usr/bin/env python3
"""Exact checks of the permutation stack-sorting simplex geometry.

Finite checks do not establish the asymptotic point-process theorem, which is
proved analytically in the accompanying result.
"""
from fractions import Fraction
from itertools import permutations
from math import erfc, exp, log, sqrt


def stack_sort(p):
    stack, out = [], []
    for item in p:
        while stack and stack[-1] < item:
            out.append(stack.pop())
        stack.append(item)
    while stack:
        out.append(stack.pop())
    return tuple(out)


def orbit(n):
    p = tuple(range(2, n + 1)) + (1,)
    out = [p]
    while p != tuple(range(1, n + 1)):
        p = stack_sort(p)
        if p in out:
            raise AssertionError('unexpected repeated iterate')
        out.append(p)
    return out


def difference(n, j):
    base = tuple(range(1, n + 1))
    v = tuple(range(2, j + 2)) + (1,) + tuple(range(j + 2, n + 1))
    return tuple(a-b for a,b in zip(v,base))


def exact_checks():
    for n in range(3, 26):
        v = [difference(n,j) for j in range(n)]
        for j in range(n):
            assert v[j] == tuple([1]*j+([-j] if j else [])+[0]*(n-j-1)) if j else v[j] == (0,)*n
        for j in range(1,n):
            for k in range(1,n):
                d = sum(x*y for x,y in zip(v[j],v[k]))
                assert d == (j*(j+1) if j==k else 0), (n,j,k,d)
        observed = orbit(n)
        expected = [tuple(range(2,j+2))+(1,)+tuple(range(j+2,n+1)) for j in range(n)]
        assert observed == list(reversed(expected)), (n, observed)
    print('STACK_SORT_ORTHOGONAL_GRAM_PASS: n=3..25')


def phi_bar(x):
    return erfc(x/sqrt(2.0))/2.0


def finite_joint_cdf(n,u,v):
    p=1.0
    for j in range(1,n):
        a=sqrt(j*(j+1))/n
        p *= 1-phi_bar(u/a)-phi_bar(v/a)
    return p


def tail_sum(n, x=0.0):
    t=sqrt(2*log(n))
    b=t-(1.5*log(2*log(n))+0.5*log(2*3.141592653589793))/t
    u=b+x/t
    return sum(phi_bar(n*u/sqrt(j*(j+1))) for j in range(1,n))


if __name__=='__main__':
    exact_checks()
    for n in [1000,10000,100000]:
        s=tail_sum(n)
        print('finite positive exceedance sum',n,round(s,8),'limit target',round(exp(0),8))
    assert 0 <= finite_joint_cdf(100, 3, 3) <= 1
    print('STACK_WIDTH_CDF_FINITE_PASS')
