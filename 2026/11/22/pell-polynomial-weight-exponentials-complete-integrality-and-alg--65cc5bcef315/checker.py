#!/usr/bin/env python3
"""Exact finite tests for polynomial weights on Pell numbers.

Tests are consistency checks. The infinite claims require the mathematical
proof, including the Dold--Euler criterion and the branch-valuation argument.
"""
from math import comb, gcd


def pell(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,2*b+a
    return a


def companion(n):
    a,b=2,2
    for _ in range(n):
        a,b=b,2*b+a
    return a


def eval_poly(coeffs,z):
    return sum(v*z**j for j,v in enumerate(coeffs))


def dolds(coeffs, bound=180):
    tests=0
    for p in range(2,bound+1):
        if any(p%d==0 for d in range(2,int(p**.5)+1)):
            continue
        z=p
        while z<=bound:
            for m in range(1,bound//z+1):
                if m%p:
                    left=eval_poly(coeffs,pell(m*z))
                    right=eval_poly(coeffs,pell(m*z//p))
                    assert (left-right)%z==0,(coeffs,p,z,m)
                    tests+=1
            z*=p
    return tests


def exp_coeffs(weights):
    a=[1]
    for n in range(1,len(weights)):
        rhs=sum(weights[j]*a[n-j] for j in range(1,n+1))
        assert rhs%n==0,('nonintegral',n,rhs%n)
        a.append(rhs//n)
    return a


def rational_ghost(k,n):
    v=((-1)**k)*comb(2*k,k)*((-1)**k)**n
    for t in range(k):
        v+=((-1)**t)*comb(2*k,t)*((-1)**(t*n))*companion(2*(k-t)*n)
    return v


def main():
    total=0
    # Each polynomial is even in the Pell argument, with equal evaluations
    # at 0 and 1 modulo 2. Coefficients are given from low to high degree.
    good=[(5,), (0,0,2), (0,0,-1,0,1), (7,0,1,0,1),
          (0,0,-1,0,0,0,1), (3,0,-3,0,0,0,1)]
    for c in good:
        total+=dolds(c,120)
    for k in range(1,8):
        c=(0,)*(2*k)+(2,)
        total+=dolds(c,120)
        weights=[0]+[2*pell(n)**(2*k) for n in range(1,37)]
        a=exp_coeffs(weights)
        if k==1:
            assert a[:10]==[1,2,6,26,122,602,3062,15906,83906,447842]
        D=2**(3*k-1)
        for n in range(1,23):
            assert rational_ghost(k,n)==D*weights[n],(k,n)
            total+=1
    # For every positive even power, multiplier 1 fails at n=2.
    for k in range(1,21):
        assert (pell(2)**(2*k)-pell(1)**(2*k))%2==1
        total+=1
    # An odd-weight sample fails the 3-adic first congruence.
    assert (2*pell(3)**3-2*pell(1)**3)%3!=0
    # A polynomial that is even but fails the dyadic parity test.
    assert (pell(2)**4-pell(1)**4)%2!=0
    print('PASS',total,'exact ghost/Dold/multiplier tests; 7 integral Pell-power series through x^36')
    print('degree spectrum for multiplier-two powers:', [(k,2**(3*k-1)) for k in range(1,8)])


if __name__=='__main__':
    main()
