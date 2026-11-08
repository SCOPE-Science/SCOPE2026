#!/usr/bin/env python3
"""Exact finite checks for a primorial obstruction in primitive Frobenius representations."""
from math import gcd


def primes_leq(limit):
    return [n for n in range(2, limit + 1) if all(n % d for d in range(2, int(n**.5) + 1))]


def primorial_away_from_a(a, K):
    P = 1
    for p in primes_leq(K):
        if gcd(p, a) == 1:
            P *= p
    return P


def construct(a, b, K):
    assert a >= 3 and gcd(a, b) == 1 and K >= a
    P = primorial_away_from_a(a, K)
    assert K * b > a * P
    t = (-b * pow(P, -1, a)) % a
    t += a * ((K * b // P - t) // a)
    N = P * t
    assert 0 < N <= K*b and K*b - N < a * P
    assert N % P == 0 and (N+b) % a == 0
    return P, N


def direct_is_nonprimitive(a, b, N):
    for y in range(N // b + 1):
        remainder = N - b * y
        if remainder % a == 0:
            x = remainder // a
            assert x >= 0
            if gcd(x, y) == 1:
                raise AssertionError((a,b,N,x,y))
    return True


def run():
    count = 0
    for a in range(3, 19):
        for K in range(a, 19):
            P=primorial_away_from_a(a,K)
            for b0 in (a*P+1, a*P+73, a*P+1019):
                b=next(v for v in range(b0, b0+a+1) if gcd(v,a)==1)
                if K*b <= a*P:
                    continue
                _,N=construct(a,b,K)
                assert direct_is_nonprimitive(a,b,N)
                count+=1
    assert count > 200
    print('CRT_EXACT_AND_ALL_REPRESENTATIONS_OK cases=',count)
    for a,K,b in [(3,8,1000),(7,13,100000),(3,17,100000)]:
        P,N=construct(a,b,K)
        assert direct_is_nonprimitive(a,b,N)
        print('EXAMPLE',a,b,K,'P=',P,'N=',N)
    print('VERIFY_OK finite_only=True analytic_asymptotic_not_computationally_certified=True')


if __name__ == '__main__':
    run()
